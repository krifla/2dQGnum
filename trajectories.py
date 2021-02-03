# --------------------------------------------------------------------------------
# calculating backward trajectories
# --------------------------------------------------------------------------------

# IMPORTANT: Horizontal (vertical) resolution needs to be 10 km (10 hPa)
assert ((ps-pt)/(nrws-1) == .01 or (ps-pt)/(nrws-1) == .005), 'FIX VERTICAL RESOLUTION'
assert int(round(wl[i_maxunstab[eps1_index,eps2_index]]/.01)) == len(kx)-1, 'FIX HORIZONTAL RESOLUTION'

#def prepare_background_state_and_variables():

cph = sigmar_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1]/k[i_maxunstab[eps1_index,eps2_index]]*10/10**4 # in units of 10 km/s for consistency with 10 km horizontal resolution
utr = u[:nrws]*10/10**4 # in units of 10 km/s for consistency with 10 km horizontal resolution
#kx2 = np.append(np.append(np.append(np.append(kx[:-1],kx+2*np.pi)[:-1],kx+4*np.pi)[:-1],kx+6*np.pi)[:-1],kx+8*np.pi)
kx2 = np.append(np.append(kx[:-1],kx+2*np.pi)[:-1],kx+4*np.pi)
ly2 = np.linspace(1*np.pi,3*np.pi,int(len(kx)*4/np.pi))
l   = k[i_maxunstab[eps1_index,eps2_index]]*np.pi/4

traj2d = True # constant in the meridional directorion?
traj3d = True # sinusoidal in the meridional direction?

xdim = int(len(kx2))
ydim = int(len(ly2))

#vref = .0005 # in 10 km/s (due to horisontal resolution), i.e. vmax is 5 m/s
#wref = .0001 # wmean is 1*10^-3 hPa/s
#if heating1 == True:
#    vref = .0010 # vmax is 10 m/s
#    wref = .0005 # wmean is 5*10^-3 hPa/s

mpl.rc('font',size=12)

# -----------------------------------------------------------------------------

# expanding 2D fields in y direction

def y_expand_fields():

    global psi3d,v3d,w3d,u3d,utr3d

    #sinfac = 2
    
    psiext = np.zeros((nrws,xdim))
    vext = np.zeros((nrws,xdim))    
    wext = np.zeros((nrws,xdim))
    
    for mi in range(nrws): # extend zonally to more wavelengths
        psiext[mi] = np.append(np.append(psi[mi,:-1],psi[mi])[:-1],psi[mi])
        vext[mi] = np.append(np.append(v[mi,:-1],v[mi])[:-1],v[mi])
        wext[mi] = np.append(np.append(w[mi,:-1],w[mi])[:-1],w[mi])
        
    psi3d = nan*np.ones((xdim,ydim,nrws))
    v3d = nan*np.ones((xdim,ydim,nrws))
    w3d = np.zeros((xdim,ydim,nrws))
    u3d = np.zeros((xdim,ydim,nrws))
    utr3d = np.zeros((ydim,nrws))

    if traj2d == True and traj3d == False:
        print ('2D flow field')
        for li in range(ydim):
            for mi in range(nrws):
                psi3d[:,li,mi] = psiext[mi] # multiplication by -1 is to shift the wave with half a wavelength
                v3d[:,li,mi] = vext[mi]
                w3d[:,li,mi] = wext[mi]
    if traj3d == True:
        print ('3D flow field')
        for li in range(int(ydim/2-1/4*len(ly2)),int(ydim/2+1/4*len(ly2))):
            for mi in range(nrws):
                psi3d[:,li,mi] = psiext[mi]*np.sin(ly2[li]-3/2*np.pi)**2
                v3d[:,li,mi] = vext[mi]*np.sin(ly2[li]-3/2*np.pi)**2
                w3d[:,li,mi] = wext[mi]*np.sin(ly2[li]-3/2*np.pi)**2
                u3d[:,li,mi] = -psiext[mi]*l*np.cos(ly2[li]-3/2*np.pi)*2*np.sin(ly2[li]-3/2*np.pi)
                utr3d[li,mi] = utr[mi]*np.sin(ly2[li]-3/2*np.pi)**2
#        for li in range(ydim): #kx
#            for mi in range(nrws):
#                utr3d[li,mi] = utr[mi]*np.sin(ly2[li]-3/2*np.pi)**2
                #if sinfac == 1:
                #    u3d[:,li,mi] = +psiext[mi]*l*np.cos(ly2[li]-3/2*np.pi)#; u3d[int(len(kx))-1:,li,mi] = +psi[mi]*l*np.cos(ly2[li]-3/2*np.pi)
                #if sinfac == 2:


# -----------------------------------------------------------------------------

# defining cyclone area

def define_cyclone_area():

    global cyc_s,cyc_e

    cyc_s = np.zeros(nrws,dtype=int)
    cyc_e = np.zeros(nrws,dtype=int)
    for mi in range(nrws):
        if psi3d[0,int(ydim/2),mi] < 0 and psi3d[-1,int(ydim/2),mi] > 0:
            cyc_s[mi] = 0
        if psi3d[-1,int(ydim/2),mi] < 0 and psi3d[0,int(ydim/2),mi] > 0:
            cyc_e[mi] = int(len(kx)-1)
        for ki in range(1,xdim):
            if psi3d[ki,int(ydim/2),mi] < 0 and psi3d[ki-1,int(ydim/2),mi] > 0 and cyc_s[mi] == 0:
                cyc_s[mi] = ki
            if psi3d[ki-1,int(ydim/2),mi] < 0 and psi3d[ki,int(ydim/2),mi] > 0 and cyc_e[mi] == 0:
                if ki-1 > cyc_s[mi] and cyc_s[mi] != 0:
                    cyc_e[mi] = ki-1
                    

# -----------------------------------------------------------------------------

# defining warm conveyor belt (wcb) and surface flux layer (sfl)

def define_wcb_and_sfl():

    global wcb,sfl # NB: these use a lot of memory!

    wcb = np.zeros((xdim,ydim,nrws))
    sfl = np.zeros((xdim,ydim,nrws))
    Qext = np.append(np.append(Q[:,:-1],Q,axis=1)[:,:-1],Q,axis=1)#-np.append(Q[:,:-1],Q,axis=1)
    
    
    if traj2d == True and traj3d == False:
        for li in range(ydim):
            for mi in range(jtlc,jblc+1):
                for ki in range(cyc_s[jtml],cyc_s[jtml]+len(kx)):#            for ki in range(xdim):
                    if Qext[mi,ki] > 0 and w3d[ki,li,mi] < 0:
                        wcb[ki,li,mi] = 1
            if heating2 == True:
                for mi in range(jtsf+1,nrws):
                    for ki in range(xdim):
                        sfl[ki,li,mi] = Qext[mi,ki]
    
    if traj3d == True:
        for li in range(int(ydim/2-1/4*len(ly2)),int(ydim/2+1/4*len(ly2))):
            for mi in range(jtlc,jblc+1):
                for ki in range(cyc_s[jtml],cyc_s[jtml]+len(kx)):
                    if Qext[mi,ki] > 0 and w3d[ki,li,mi] < 0:
                    #if w3d[ki,li,jtml] < 0:
                        wcb[ki,li,mi] = 1#h1[eps1_index,:nrws]
            if heating2 == True:
                for mi in range(jtsf+1,nrws):
                    for ki in range(xdim):
                        sfl[ki,li,mi] = Qext[mi,ki]*np.sin(ly2[li]-3/2*np.pi)**2
                  
             
# -----------------------------------------------------------------------------             
             
def define_starting_coordinates():

    global plow,ntr,ntrx,ntry,ntrz,k0s,l0s,m0s,k0,l0,m0

    plow = pblc
#    if pblc >= ptsf:
#        plow = ptsf-.05
             
    # number of trajectories
    ntrx = 5
    ntry = 5
    if traj3d == False:
        ntry = 1
    ntrz = 9#int((plow-ptlc)/0.05+1) #int(ntr/ntrx/ntry)
    ntr = ntrx*ntry*ntrz
    if ntrz < 1 or ntrx*ntry*ntrz != ntr:
        sys.exit('ntrz')
                     
    k0s = np.empty((ntr), dtype=int)
    l0s = np.empty((ntr), dtype=int)
    m0s = np.empty((ntr), dtype=int)

    # starting coordinates

    start_in_trough = False
    start_in_wcb = True
        
    for li in range(ntry):
        for j in range(li*ntrx*ntrz,(li+1)*ntrx*ntrz):
            if ntry == 5:
                l0s[j] = int(ydim/2-1/16*len(ly2))+1/32*len(ly2)*li
            if ntry == 3:
                l0s[j] = int(ydim/2-1/16*len(ly2))+1/16*len(ly2)*li
            if ntry == 1:
                l0s[j] = int(ydim/2)
    for mi in range(ntrz):  
        for li in range(ntry):
            for ki in range(ntrx):
                if start_in_trough == True:
                    m0s[ki+li*ntrx*ntrz+mi*ntrx] = int(np.argwhere(p[:nrws] <= (0.95-0.05*mi))[-1,0])
                if start_in_wcb == True:
                    if ntrz == 1:
                        m0s[ki+li*ntrx*ntrz+mi*ntrx] = int(np.argwhere(p[:nrws] >= 0.6)[0][0])
                    else:
                        m0s[ki+li*ntrx*ntrz+mi*ntrx] = int(np.argwhere(p[:nrws] <= (plow-(plow-p[jtlc])/(ntrz-1)*mi))[-1,0])
                        
    wcbs = np.argwhere(wcb[:,int(ydim/2),int(mean([jtlc,jblc]))] == 1)[0][0]#np.argwhere(w3d[int(xdim/3):,int(ydim/2),jtml] < 0)[0][0]
    wcbe = np.zeros(ntrz,dtype=int)
    for mi in range(ntrz):
        wcbe[mi] = (np.argwhere(wcb[:,int(ydim/2),m0s[mi*ntrx]] == 1)[-1][0])#np.argwhere(w3d[int(xdim/3):,int(ydim/2),jtml] < 0)[0][0]
    dx = (np.min(wcbe)-wcbs)/(ntrx-1)
    #print (dx,np.max(wcbe)-np.min(wcbe))
        
        
    if start_in_trough == True:
        for ki in range(ntrx):
            for j in range(ntry*ntrz):
                if ntrx == 3:
                    k0s[ki+j*ntrx] = cyc_s[m0s[ki+j*ntrx]]+(4)/16*(cyc_e[m0s[ki+j*ntrx]]-cyc_s[m0s[ki+j*ntrx]])+(ki*4)/16*(cyc_e[m0s[ki+j*ntrx]]-cyc_s[m0s[ki+j*ntrx]])
                if ntrx == 5:
                    k0s[ki+j*ntrx] = cyc_s[m0s[ki+j*ntrx]]+(ki*4)/16*(cyc_e[m0s[ki+j*ntrx]]-cyc_s[m0s[ki+j*ntrx]])
    if start_in_wcb == True:
        for ki in range(ntrx):
#            for mi in range(m0s):
            for j in range(ntry*ntrz):
                k0s[ki+j*ntrx] = int(wcbs+dx*ki)#(wcbe[j%ntry]-wcbs)*ki/(ntrx-1)
                if ntrx == 1:
                    k0s[ki+j*ntrx] = int((wcbs+dx*ki))#wcbe[j%ntry])/2) #(4)/16*(cyc_e[m0s[ki+j*ntrx]]-cyc_s[m0s[ki+j*ntrx]])+(1*4)/16*(cyc_e[m0s[ki+j*ntrx]]-cyc_s[m0s[ki+j*ntrx]])#int((wcbs+wcbe)/2) #
                #if ntrx == 3:
                 #   k0s[ki+j*ntrx] = (4)/16*(cyc_e[m0s[ki+j*ntrx]]-cyc_s[m0s[ki+j*ntrx]])+(ki*4)/16*(cyc_e[m0s[ki+j*ntrx]]-cyc_s[m0s[ki+j*ntrx]])#wcbs+(int((wcbs+wcbe)/2)-wcbs)*j 
                #if ntrx == 5:
                 #   k0s[ki+j*ntrx] = wcbs+(ki*4)/16*(cyc_e[m0s[ki+j*ntrx]]-cyc_s[m0s[ki+j*ntrx]])
        
    k0 = [k0s.tolist()]; l0 = [l0s.tolist()]; m0 = [m0s.tolist()]


# -----------------------------------------------------------------------------
                
def manual_coord():

    l0s[0] = int(ydim/2-1/8*len(kx));		m0s[0] = np.argwhere(p > 0.95)[0,0]; k0s[0] = cyc_s[m0s[0]]+1/16*(cyc_e[m0s[0]]-cyc_s[m0s[0]])
    if ntr >= 2:
        l0s[1] = int(ydim/2);				m0s[1] = np.argwhere(p > 0.95)[0,0]; k0s[1] = cyc_s[m0s[1]]+1/16*(cyc_e[m0s[1]]-cyc_s[m0s[1]])
    if ntr >= 3:
        l0s[2] = int(ydim/2+1/8*len(kx));	m0s[2] = np.argwhere(p > 0.95)[0,0]; k0s[2] = cyc_s[m0s[2]]+1/16*(cyc_e[m0s[2]]-cyc_s[m0s[2]])
    if ntr >= 4:
        l0s[3] = int(ydim/2-1/8*len(kx));	m0s[3] = np.argwhere(p > 0.85)[0,0]; k0s[3] = cyc_s[m0s[3]]+8/16*(cyc_e[m0s[3]]-cyc_s[m0s[3]])
    if ntr >= 5:
        l0s[4] = int(ydim/2);				m0s[4] = np.argwhere(p > 0.85)[0,0]; k0s[4] = cyc_s[m0s[4]]+8/16*(cyc_e[m0s[4]]-cyc_s[m0s[4]])
    if ntr >= 6:
        l0s[5] = int(ydim/2+1/8*len(kx));	m0s[5] = np.argwhere(p > 0.85)[0,0]; k0s[5] = cyc_s[m0s[5]]+8/16*(cyc_e[m0s[5]]-cyc_s[m0s[5]])
    if ntr >= 7:
        l0s[6] = int(ydim/2-1/8*len(kx));	m0s[6] = np.argwhere(p > 0.75)[0,0]; k0s[6] = cyc_s[m0s[6]]+15/16*(cyc_e[m0s[6]]-cyc_s[m0s[6]])
    if ntr >= 8:
        l0s[7] = int(ydim/2);				m0s[7] = np.argwhere(p > 0.75)[0,0]; k0s[7] = cyc_s[m0s[7]]+15/16*(cyc_e[m0s[7]]-cyc_s[m0s[7]])
    if ntr >= 9:
        l0s[8] = int(ydim/2+1/8*len(kx));	m0s[8] = np.argwhere(p > 0.75)[0,0]; k0s[8] = cyc_s[m0s[8]]+15/16*(cyc_e[m0s[8]]-cyc_s[m0s[8]])
    if ntr >= 10:
        l0s[9] = int(ydim/2-1/8*len(kx));	m0s[9] = np.argwhere(p > 0.95)[0,0]; k0s[9] = cyc_s[m0s[9]]+8/16*(cyc_e[m0s[9]]-cyc_s[m0s[9]])
    if ntr >= 11:
        l0s[10] = int(ydim/2);				m0s[10] = np.argwhere(p > 0.95)[0,0]; k0s[10] = cyc_s[m0s[10]]+8/16*(cyc_e[m0s[10]]-cyc_s[m0s[10]])
    if ntr >= 12:
        l0s[11] = int(ydim/2+1/8*len(kx));	m0s[11] = np.argwhere(p > 0.95)[0,0]; k0s[11] = cyc_s[m0s[11]]+8/16*(cyc_e[m0s[11]]-cyc_s[m0s[11]])
    for n in range(ntr):
        if k0s[n] < cyc_s[m0s[n]] or k0s[n] > cyc_e[m0s[n]]:
            sys.exit('starting point of trajectory #%d (%d,%d,%d) is outside of cyclone area' %(i,k0s[n],l0s[n],m0s[n]))
    k0 = [k0s.tolist()]; l0 = [l0s.tolist()]; m0 = [m0s.tolist()]    
    
    return (k0,l0,m0)
    
# -----------------------------------------------------------------------------
    
# calculating backward coordinates

def calculate_trajectories():

    global k0,l0,m0,cycrel,dt,tfac,ts,te,vfac,gfac

    ts = 0*24*60**2			# starting time
    trun = -1*24*60**2		# run time
    te = ts + trun			# end time
    t = ts; dt = -2*60**2	# time resolution

    cycrel = True			# are trajectories relative to cyclone movement?

    while t > ts+trun:# 0<m0[-1][0]<nrws-1 and 0<m0[-1][1]<nrws-1 and for i in range(ntr):#  and 0 <= l0[-1] <= int(len(kx)):# and cyc_s[m0[-1]] <= k0[-1] <= cyc_e[m0[-1]]
        vfac = vref/np.nanmax(abs(v3d[:,int(ydim/2),jtml:]))
        wfac = vfac*10**(-1) # factor that converts nondimensional omega to omega with units kPa/s = 10 hPa/s
#        wfac = wref/np.nanmean(abs(w3d[:,int(ydim/2),:]))
#        vfac = wfac*10**(1)
        tfac = 0#-.25*24*60**2#trun/2 # sets centering of the growth rate factor
        gfac = np.exp(sigmai_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1]/10**5*(t-tfac))
        if gfac != 1 and t == ts:
            print (f'starting growth rate factor is {gfac}')
        if gfac != 1 and t == ts-1*24*60**2-dt:
            print (f'growth rate factor one day back in time is {gfac}')
        if cycrel == True:
            k0.append((np.round(k0[-1]+dt*(utr3d[l0[-1],m0[-1]]+u3d[k0[-1],l0[-1],m0[-1]]*vfac*gfac-cph))).tolist())
        if cycrel == False:
            k0.append((np.round(k0[-1]+dt*(utr3d[l0[-1],m0[-1]]+u3d[list(x+int(round(cph*t)) for x in k0[-1]),l0[-1],m0[-1]]*vfac*gfac))).tolist())
        if cycrel == True:
            l0.append((np.round(l0[-1]+dt*v3d[k0[-2],l0[-1],m0[-1]]*vfac*gfac)).tolist())
        if cycrel == False:
            l0.append((np.round(l0[-1]+dt*v3d[list(x+int(round(cph*t)) for x in k0[-2]),l0[-1],m0[-1]]*vfac*gfac)).tolist())
        if cycrel == True:            
            if nrws == 86:
                m0.append((np.round(m0[-1]+dt*w3d[k0[-2],l0[-2],m0[-1]]*wfac*gfac)).tolist()) # .00001/np.nanmax(w3d[:,:,-1]) instead of fac gives a max w of 1 cm/s. *12 converts km to kPa=10hPa
            if nrws == 2*86-1:
                m0.append((np.round(m0[-1]+dt*w3d[k0[-2],l0[-2],m0[-1]]*wfac*gfac*2)).tolist())
        if cycrel == False:            
            if nrws == 86:
                m0.append((np.round(m0[-1]+dt*w3d[list(x+int(round(cph*t)) for x in k0[-2]),l0[-2],m0[-1]]*wfac*gfac)).tolist()) # .00001/np.nanmax(w3d[:,:,-1]) instead of fac gives a max w of 1 cm/s. *12 converts km to kPa=10hPa
            if nrws == 2*86-1:
                m0.append((np.round(m0[-1]+dt*w3d[list(x+int(round(cph*t)) for x in k0[-2]),l0[-2],m0[-1]]*wfac*gfac*2)).tolist())
        for n in range(ntr):
            if m0[-1][n] >= nrws-2:
                m0[-1][n] = nrws-3
            #    print ('touchdown')
            if m0[-1][n] <= 1:
                m0[-1][n] = 2
            #    print ('touchup')
            while k0[-1][n] < 0:
                k0[-1][n] = k0[-1][n]+xdim
            while k0[-1][n] > len(kx2)-1:
                k0[-1][n] = k0[-1][n]-xdim
            if math.isnan(l0[-1][n]) == True:
                l0[-1][n] = 0
                print ('l0 = nan')
            if traj3d == False:
                while l0[-1][n] < 0:
                    l0[-1][n] = l0[-1][n]+ydim
                while l0[-1][n] > ydim-1:
                    l0[-1][n] = l0[-1][n]-ydim
            k0[-1][n] = int(k0[-1][n])
            l0[-1][n] = int(l0[-1][n])
            m0[-1][n] = int(m0[-1][n])
        t = t+dt
        
    print (f'max surface psi: {np.max(abs(psi3d[:,int(ydim/2),jtml:]*vfac*10**4)):.2f} 10^6 m^2/s; max surface v: {np.max(abs(v3d[:,int(ydim/2),jtml:]*vfac*10**4)):.2f} m/s; mean w: {np.mean(abs(w3d[:,int(ydim/2),:]*wfac*10**4)):.2f} 10^-3 hPa/s')
#    print (np.nanmean(abs(psi3d[:,int(ydim/2),:]))*vfac,np.nanmean(abs(v3d[:,int(ydim/2),:]))*vfac)
    

# -----------------------------------------------------------------------------
    
### plotting preparations

def prepare_trajectory_plot():#,k0ext = np.array(k0)):

    global cph,cycrel,kx2,k0,l0,m0
    global k0ext,cycdist,br,clab
    global xmin, xmax, ymin, ymax

    if cycrel == True:
        cycdist = -cph*60**2*24*10#np.exp(-sigmai_sorted[0,0,i_maxunstab[0,0],-1]/10**5*tfac)*10**5/sigmai_sorted[0,0,i_maxunstab[0,0],-1]*(np.exp(sigmai_sorted[0,0,i_maxunstab[0,0],-1]*te/10**5)-np.exp(sigmai_sorted[0,0,i_maxunstab[0,0],-1]/10**5*ts)) # distance cyclone moves during time span: integral of cph*exp() wrt time
    else:
        cycdist = NaN

    lev = 8

    k0 = np.array(k0)
    l0 = np.array(l0)
    m0 = np.array(m0)

    for ki in range(len(k0)):
        for n in range(ntr):
            if l0[ki,n] == 0:
                m0[ki:,n] = m0[ki-1,n]
                k0[ki:,n] = k0[ki-1,n]
                l0[ki:,n] = l0[ki-1,n]
            
    br = len(k0)*np.ones((ntr),dtype=int)#[[]]*ntr
    for n in range(ntr):
        for ki in range(len(k0)-1):
            if abs(kx2[k0[ki,n]]-kx2[k0[ki+1,n]]) > 3/4*kx2[-1]:
                if br[n] == len(k0):
                    br[n] = ki

    #clab = (['k','g',c_reds[0],'grey',c_blues[0], 'w','y'])
    clab = cm.viridis#Set1_r
    #br, len(k0)
    
    #k0ext=k0ext
    if cycrel == True:
        k0ext = np.array(k0)

        for n in range(ntr):
            for i in range(1,len(k0)):    
                for j in range(1,i+1):
                    k0ext[-j,n] = (k0ext[-j,n]+int(round(cph*dt))) 
    try:
        k0ext
    except:
        k0ext = 0*np.array(k0)          
    
    ymin = int(ydim/2-1.5/4*len(ly2)); ymax = int(ydim/2+1.5/4*len(ly2)-1) 
#    ymin = int(ydim/2-1/4*len(ly2)); ymax = int(ydim/2+1/4*len(ly2)-1)
    xmin = int(len(kx)*1/4-1); xmax = int(len(kx)*6/4-1)#int(len(kx))-2; xmax = int(len(kx)*3-4)  ###0; xmax = 4*np.pi#
    x2min = np.argwhere(wcb[:,int(ydim/2),jtml]>0)[0][0]; x2max = np.argwhere(wcb[:,int(ydim/2),jtml]>0)[-1][0]  
    
    
# -----------------------------------------------------------------------------
    
### counting number of trajectories that enter the warm conveyor belt after being in the surface flux layer 

def trajectories_in_wcb_and_sfl():

    global wcbsfl

    wcbsfl = np.zeros(ntr)
    
    for n in range(ntr):
        twcb = 0; tsfl = 0
        for t in range(br[n]):#int((te-ts)/dt+1)):
            if wcb[k0[t][n],l0[t][n],m0[t][n]] > 0: # does trajectory touch warm conveyor belt?
                twcb = 1
            if sfl[k0[t][n],l0[t][n],m0[t][n]] != 0: # does trajectory touch surface flux layer?
                tsfl = 1
        if twcb == 1 and tsfl == 1:
            wcbsfl[n] = 1
    

# -----------------------------------------------------------------------------
    
### finding and plotting height and width of trajectories relative to starting point

def find_and_plot_trajectory_distance():

    global trdp, trdy, exp, wcbsflexp, wcbsfl_dp

    trdp=([]); trdy=([]); exp=([]); wcbsflexp=([]); wcbsfl_dp=([])

    trdp.append(np.zeros(ntr))
    trdy.append(np.zeros(ntr))
    exp.append(vref)
    wcbsflexp.append(wcbsfl)
    wcbsfl_dp.append(np.zeros(ntr))
    
    oneday = int(-1*24*60**2/dt)
        
    for n in range(ntr):
        trdp[-1][n] = -(p[m0s[n]]-p[np.max(m0[:oneday,n])]) # finding maximum downward displacement during the last day relative to starting coordinate
        if br[n] < oneday:
            trdp[-1][n] = -(p[m0s[n]]-p[np.max(m0[:br[n],n])])
        trdy[-1][n] = ((ly2[l0s[n]]-ly2[np.min(l0[:oneday,n])]))/(2*np.pi)*wl[i_maxunstab[eps1_index,eps2_index]] # finding maximum southward displacement during the last day relative to starting coordinate
        if br[n] < oneday:
            trdy[-1][n] = ((ly2[l0s[n]]-ly2[np.min(l0[:br[n],n])]))/(2*np.pi)*wl[i_maxunstab[eps1_index,eps2_index]]
   
    show_wcbsfl = True
    linreg = ([])
    
    ylow = int((ly2[l0s[0]]-ly2[int(ydim/2)])*wl[i_maxunstab[eps1_index,eps2_index]]/(2*np.pi)*10**3)
                
    fig,ax = plt.subplots(figsize=(10,7))
        
    for i in range(len(trdp)):
        if show_wcbsfl == True:
            markers = (['s','^','o','X'])
            if ntry == 3 and ntrz > 1 and len(trdp) == 1:
                for n in range(ntry):
                    ax.scatter((),(),s=60,marker=markers[n],color='grey',edgecolor='grey',label=int(ylow-ylow*n*(ntry-1)/2))
                leg = ax.legend(loc=4,framealpha=.2,title='y(t$_0$) [km]')
            else:
                ax.scatter((),(),s=60,marker=markers[i],color='grey',edgecolor='grey',label=int(exp[i]*10**4))
                leg = ax.legend(loc=4,framealpha=.2,title='max $v_s$ [m/s]')#bbox_to_anchor=(1,0.5), loc='center left', fancybox=True)
            for n in range(ntr):
                if wcbsflexp[i][n] <= 0:
                    if ntry == 3 and ntrz > 1 and len(trdp) == 1:
                        ax.scatter(trdy[i][n]*1000,trdp[i][n]*1000,s=20,marker=markers[int(round((l0s[n]-l0s[0])*2/(l0s[-1]-l0s[0])))],color='grey',edgecolor='grey',alpha=.5)
                    else:    
                        ax.scatter(trdy[i][n]*1000,trdp[i][n]*1000,s=20,marker=markers[i],color='grey',edgecolor='grey',alpha=.5)#,label=f'max $v_s$ = {exp[i]*10**4} m/s')
                else: # color all scatter points that belong to a trajectory that touches both the warm conveyor belt and the surface flux layer
                    if ntry == 1:
                        ax.scatter(trdy[i][n]*1000,trdp[i][n]*1000,s=60,marker=markers[i],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),edgecolor=None,alpha=.8)
                    if ntrz == 1:
                        ax.scatter(trdy[i][n]*1000,trdp[i][n]*1000,s=60,marker=markers[i],color=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])),edgecolor=None,alpha=.8)
                    if ntry == 3 and ntrz > 1 and len(trdp) == 1:
                        ax.scatter(trdy[i][n]*1000,trdp[i][n]*1000,s=60,marker=markers[int(round((l0s[n]-l0s[0])*2/(l0s[-1]-l0s[0])))],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),edgecolor=None,alpha=.8)
                    else:
                        ax.scatter(trdy[i][n]*1000,trdp[i][n]*1000,s=60,marker=markers[i],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),edgecolor=None,alpha=.8)
        else:
            colors = (['k',(0, 109/255., 136/255.),(209/255., 98/255., 76/255.),'grey'])
            v1 = ax.scatter((),(),s=60,marker='o',color=colors[i],edgecolor=colors[i],alpha=.6,label=f'max $v_s$ = {exp[i]*10**4} m/s')
            linreg.append(np.poly1d(np.polyfit(trdy[i]*1000,trdp[i]*1000,deg=1)))
            ax.plot(trdy[i]*1000,linreg[i](trdy[i]*1000),color=colors[i],alpha=.6)
            for n in range(ntr):
                ax.scatter(trdy[i][n]*1000,trdp[i][n]*1000,s=15,marker='o',color=colors[i],edgecolor=colors[i],alpha=.6)   
    ax.axhline(100,c='k',ls='--',lw=1,alpha=.5,zorder=-1)
    ax.set_xlabel('southward displacement [km]')
    ax.set_ylabel('downward displacement [hPa]')
#    ax.set_xlim(-10,340)
    ax.add_artist(leg)
    if ntry == 1 or (ntry == 3 and ntrz > 1 and len(trdp) == 1):
#        ax.set_ylim(-10,440)
        h = [plt.plot([],[], color=clab((p[m0s[-(n*ntrx+1)]]-ptlc)/(plow-ptlc)), marker='o', ls='')[0] for n in range(ntrz)]
        plt.legend(handles=h, labels=[int(round(p[m0s[-(n*ntrx+1)]]*1000)) for n in range(ntrz)],loc=2, title='$p(t_0)$ [hPa]',framealpha=.2)
    if ntrz == 1:
        #ax.set_ylim(-10,240)
        h = [plt.plot([],[], color=clab(n/(ntry-1)), marker='o', ls='')[0] for n in range(ntry)]
        plt.legend(handles=h, labels=[int(ylow-ylow/2*n) for n in range(ntry)],loc=2, title='y(t$_0$) [km]',framealpha=.2)
    plt.show()
    
    for n in range(ntr):
        if np.squeeze(trdp[-1])[n] > 0 and wcbsfl[n] == 1: # > 0.1
            wcbsfl_dp[-1][n] = 1
    
# -----------------------------------------------------------------------------
    
### finding influence by surface fluxes along trajectories

def integrate_sfl():

    global sflpos,sflneg,sfl_in_range

    sflpos = np.zeros((ntr,len(k0)))
    sflneg = np.zeros((ntr,len(k0)))
    sflpos_acc = np.zeros((ntr,len(k0)))
    sflneg_acc = np.zeros((ntr,len(k0)))
        
    sfl_in_range = np.array(sfl) # defining surface flux layer remotely ahead of cyclone (one half cyclone length ahead of border of cyclone)
    for mi in range(nrws):
        for ki in range(xdim):
            if ki < cyc_e[mi]+np.argwhere(kx2 >= np.pi)[0][0] or ki > cyc_e[mi]+np.argwhere(kx2 >= 3*np.pi)[0][0]:
                sfl_in_range[ki,:,mi] = 0

    for n in range(ntr):
        if wcbsfl_dp[-1][n] == 1:
            for t in range(len(k0)):
                gfac = np.exp(sigmai_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1]/10**5*(t*dt-tfac))
                if sfl[k0[t,n],l0[t,n],m0[t,n]] > 0:
                    if gfac == 1:
                        sflpos[n,t] = sfl[k0[t,n],l0[t,n],m0[t,n]]*vfac*10**3/(4*10**4)*-dt  # dimensionalising diabatic heating (10**3 to convert vfac to m instead of km, factor 4 comes from assuming a gas constant of 400 J/(K*kg), where 461 is for water vapour) 
                    else:
                        sflpos[n,t] = sfl[k0[t,n],l0[t,n],m0[t,n]]*vfac*10**3/(4*10**4)*-dt*gfac  # dimensionalising diabatic heating (10**3 to convert vfac to m instead of km, factor 4 comes from assuming a gas constant of 400 J/(K*kg), where 461 is for water vapour) 
                sflpos_acc[n,t] = sflpos_acc[n,t-1] + sflpos[n,t]
                if sfl[k0[t,n],l0[t,n],m0[t,n]] < 0:
                    if gfac == 1:
                        sflneg[n,t] = sfl[k0[t,n],l0[t,n],m0[t,n]]*vfac*10**3/(4*10**4)*-dt #_in_range #sflneg[n]
                    else:
                        sflneg[n,t] = sfl[k0[t,n],l0[t,n],m0[t,n]]*vfac*10**3/(4*10**4)*-dt*gfac #_in_range #sflneg[n]
                sflneg_acc[n,t] = sflneg_acc[n,t-1] + sflneg[n,t]
    taupos = int(sum(sflpos))
    tauneg = int(sum(sflneg))
    gam = 1004/(2.3*10**6)#(2.5*10**6) # c_p/L_c
    ratio = (wcbsfl_dp[-1].tolist()).count(1.)/len([1 for i in trdp[-1] if i > .1])
    Qsum = np.sum(sflpos_acc[:,-1]+sflneg_acc[:,-1])/(-te)
    print (f'Average dQ: {ratio*Qsum:.3}, which is {ratio*Qsum/(Q[Q > 0].mean()*vfac*10**3/(4*10**4))*100:.3} % of total heating, and means a change from epsilon {epsilon1[eps1_index]} to {epsilon1[eps1_index]*(1+ratio*Qsum/(Q[Q > 0].mean()*vfac*10**3/(4*10**4))):.3}')
            
    time_restr = np.linspace(0*60**2*24,-te,5*10)
    dist_restr = np.linspace(-0.5,1.5,5*10)
    Qsum_restr = np.zeros((ntr, len(time_restr),len(dist_restr)))
    Qsum_restr_avg = np.zeros((len(time_restr),len(dist_restr)))
    
    def linint(arg1):
        arg2 = np.zeros(2*len(arg1)-1)
        for i in range(len(arg2)):
            if i % 2 == 0:
                arg2[i] = arg1[int(i/2)]
            else:
                arg2[i] = (arg1[int((i-1)/2)]+arg1[int((i+1)/2)])/2
        return arg2
                
                
    fig,(ax1,ax3) = plt.subplots(2,figsize=(9,7), gridspec_kw={'height_ratios': [1, 1.7]})
#    ax2 = ax1.twinx()
#    ax4 = ax3.twinx()
    if np.max(wcbsfl_dp) > 0:
        for n in range(ntr):
            if np.max(sflpos[n]) != 0 or np.min(sflneg[n]) != 0:
                distance = (kx2[k0[:br[n],n]]-kx2[cyc_e[m0[:br[n],n]]])/(2*np.pi)#*wl[i_maxunstab[eps1_index,eps2_index]]#-kx2[np.min(k0)])
                ax1.scatter(distance,sflpos[n,:br[n]],color='w',edgecolor=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.8)
                #ax2.plot(distance,sflpos_acc[n,:br[n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.6)
                
                func_acc = interp1d(distance,sflpos_acc[n]+sflneg_acc[n])
                func_inst = interp1d(distance,sflpos[n]+sflneg[n])
                distance_new = linint(linint(distance))
#                print (len(k0), len(distance), len(distance_new))
                sfl_acc_new = func_acc(distance_new)
                sfl_inst_new = func_inst(distance_new)
                for t in range(len(distance_new)-1):
                    if abs(sfl_inst_new[t])/np.max(abs(sfl_inst_new))<.1:
                        ax3.plot(distance_new[t:t+2],sfl_acc_new[t:t+2],color=cm_bgr(((sfl_inst_new[t])/np.max(abs(sfl_inst_new))+1)/2))
                        #ax3.plot(distance[t:t+2],sflpos_acc[n,t:t+2]+sflneg_acc[n,t:t+2],color=cm_bgr(((sflpos[n,t]+sflneg[n,t])/np.max(abs(sflpos+sflneg))+1)/2))
                    else:
                        ax3.plot(distance_new[t:t+2],sfl_acc_new[t:t+2],color=cm_bgr(((sfl_inst_new[t])/np.max(abs(sfl_inst_new))+1)/2),zorder=1000)                        
                        #ax3.plot(distance[t:t+2],sflpos_acc[n,t:t+2]+sflneg_acc[n,t:t+2],color=cm_bgr(((sflpos[n,t]+sflneg[n,t])/np.max(abs(sflpos+sflneg))+1)/2),zorder=1000)                        
    #                    ax3.plot(distance[:-int(60**2*24/dt)+1],sflpos_acc[n,:-int(60**2*24/dt)+1]+sflneg_acc[n,:-int(60**2*24/dt)+1],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.8)
                
                ax3.plot(distance[-int(60**2*24/dt):br[n]],sflpos_acc[n,-int(60**2*24/dt):br[n]]+sflneg_acc[n,-int(60**2*24/dt):br[n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),ls='--',alpha=.8)
                #ax3.plot(distance,sflpos_acc[n,:br[n]]+sflneg_acc[n,:br[n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.8)
                ax1.scatter(distance,sflneg[n,:br[n]],color='w',edgecolor=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.8)
                #ax2.plot(distance,sflneg_acc[n,:br[n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.6)
                
                for t in range(len(time_restr)):
                    for d in range(len(dist_restr)):
                        if distance[-1] < dist_restr[d]:
                            Qsum_restr[n,t,d] = 0
                        else:
                            start = np.argwhere(distance >= dist_restr[d])[0][0]
                            end = -int((time_restr[t])/dt)
                            if start >= end:
                                Qsum_restr[n,t,d] = NaN
                            else:
                                Qsum_restr[n,t,d] = (sflpos_acc[n,end]+sflneg_acc[n,end]-sflpos_acc[n,start]-sflneg_acc[n,start])/(-dt*(end-start))

#        ax3.plot(distance                
#        plt.plot(distance,sum(sflpos,axis=0),'k')
        ax3.set_xlabel('# of wavelengths away from eastern cyclone edge')
        ax3.set_ylabel('accumulated heating (K) \nby surface fluxes')
        #ax2.set_ylabel('accumulated heating or cooling (K) \nby surface fluxes')
#        ax2.set_ylabel('change in \nsaturation mixing ratio')
        ax1.set_ylabel('heating/cooling (K) \nby surface fluxes')#,fontsize=16)
        ax1.set_ylim(1.1*np.min(sflneg),1.1*np.max(sflpos))
        ax3.set_ylim(-4,1)
        ax3.set_xticks([0,.5,1,1.5,2.0,2.5])
#        ax2.set_ylim(1.1*np.min(sflneg)*gam,1.1*np.max(sflpos)*gam)
#        ax3.set_ylim(.85*np.min(sflpos_acc+sflneg_acc),.85*np.max(sflpos_acc+sflneg_acc))
#        ax4.set_ylim(.95*np.min(sflpos_acc+sflneg_acc)*gam,.95*np.max(sflpos_acc+sflneg_acc)*gam)
#        ax4.set_ylabel('accumulated change in \nsaturation mixing ratio')
#        ax2.set_ylim(1.1*np.min(sflneg_acc),1.1*np.max(sflpos_acc))
#        plt.ylim(-.1*maxval,1.1*maxval)
#        plt.text(0,.9*maxval,f'$\\tau^+$: {taupos} \n$\\tau^-$: {tauneg}')# int(sum(sflpos)))
        plt.show()
        
    for t in range(len(time_restr)):
        for d in range(len(dist_restr)):
            Qsum_restr_avg[t,d] = np.sum(Qsum_restr[:,t,d])*ratio
            
    fig,ax = plt.subplots(figsize=(8,5))
    
    vmin = -np.nanmax(abs(Qsum_restr_avg/(Q[Q > 0].mean()*vfac*10**3/(4*10**4))*epsilon1[eps1_index]))
    vmax = np.nanmax(abs(Qsum_restr_avg/(Q[Q > 0].mean()*vfac*10**3/(4*10**4))*epsilon1[eps1_index]))
    
    norm = MidpointNormalize(midpoint=0)
    cs = ax.contourf(dist_restr,time_restr/(24*60**2),Qsum_restr_avg/(Q[Q > 0].mean()*vfac*10**3/(4*10**4))*epsilon1[eps1_index],10,norm=norm,vmin=vmin,vmax=vmax,cmap=cm_br)
    cs2 = ax.contour(dist_restr,time_restr/(24*60**2),Qsum_restr_avg/(Q[Q > 0].mean()*vfac*10**3/(4*10**4))*epsilon1[eps1_index],10,colors='k',linestyles='-',linewidths=.5)
    cbar = fig.colorbar(cs)
    cbar.add_lines(cs2)
    cbar.set_label('$\Delta \\varepsilon$', rotation=270, labelpad=15)#$\Delta$Q / $\overline{Q}$ (%)
#    ax.add_patch(patches.Rectangle((.5,0),1,1.5,linewidth=1.5,linestyle='--',edgecolor='k',facecolor='none'))
    ax.set_xlabel('starting point of integration \n(# of wavelengths from eastern cyclone edge)')
    ax.set_xticks([-.5,0,.5,1])#,1.5])
    ax.set_xlim(-.5,1)
    ax.set_ylabel('integration time (days)')
    ax.set_yticks([0,.5,1,1.5,2])
    plt.show()
    
    print (np.nanmax(Qsum_restr_avg[:int(len(time_restr)*3/4),int(len(dist_restr)/2):]/(Q[Q > 0].mean()*vfac*10**3/(4*10**4))*epsilon1[eps1_index]))

        
# -----------------------------------------------------------------------------
    
# 3D plot

def plot_trajectories_3D():

#    print (f'shape: {np.shape(psi3d)}')    
#    print (np.shape(kx2_3d),np.shape(ly2_3d),np.shape(kx2_2dy))

    kx2_2dy,ly2_2dx = np.meshgrid(kx2,ly2)########################
    kx2_2dp,p_2dx = np.meshgrid(kx2,p[:nrws])
    ly2_2dp,p_2dy = np.meshgrid(ly2,p[:nrws])
    kx2_3d,ly2_3d,p_3d = np.meshgrid(kx2,ly2,p[:nrws])
 
    vmin = np.nanmin(psi3d); vmax = np.nanmax(psi3d)

#    mpl.rc('font',size=18)

    fig = plt.figure(figsize=(7,7), dpi=300)#
    ax = fig.add_subplot(111, projection='3d')
    lw=2
    ms=15
    markers = (['s','^','o','X'])
#    mpl.rc('font',size=10)
    
    colorsList = [(1,1,1),(.5,.5,.5)]
    binarymap = mpl.colors.ListedColormap(colorsList)
    
    trajectories = True
    box = False # plot wcb as a box?
    
    
    # streamfunction sections plotted in shading:
    
    #ax.contourf(kx2_2dp, psi3d[:,int(ydim/2),:].T, p_2dx, zdir='y', offset=kx2[int(ydim/2+2/4*len(kx)-1)], vmin=vmin, vmax=vmax, alpha=.6, cmap=cm_br, zorder=1)
    ax.contourf(np.min(psi3d[:,ymin:ymax,:],0).T, ly2_2dp[:,ymin:ymax], p_2dy[:,ymin:ymax], zdir='x', offset=kx2[xmax-1], vmin=vmin, vmax=vmax, alpha=.7, cmap=cm_br)#, zorder=-1)    #ax.contour(np.nanmin(psi3d[:,int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1),:],0).T, kx2_2dp[:,int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1)], p_2dy[:,int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1)], zdir='x', offset=kx2[-1], colors='k', zorder=1)
    ax.contourf(kx2_2dy[ymin:ymax,xmin:xmax], ly2_2dx[ymin:ymax,xmin:xmax], psi3d[xmin:xmax,ymin:ymax,0].T, zdir='z', offset=0.15, vmin=vmin, vmax=vmax, alpha=.7, cmap=cm_br)#, zorder=1000)
    #ax.contour(kx2_2dy[int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1),:], kx2_2dx[int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1),:], np.nan_to_num(psi3d)[:,int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1),0].T, zdir='z', offset=0.15, colors='k', zorder=1000)
    ax.contourf(kx2_2dy[ymin:ymax,xmin:xmax], ly2_2dx[ymin:ymax,xmin:xmax], psi3d[xmin:xmax,ymin:ymax,-1].T, zdir='z', offset=1, vmin=vmin, vmax=vmax, alpha=.7, cmap=cm_br, zorder=-1)
    #ax.contour(kx2_2dy[int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1),:], kx2_2dx[int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1),:], np.nan_to_num(psi3d)[:,int(ydim/2-2/4*len(kx)-1):int(ydim/2+2/4*len(kx)-1),-1].T, zdir='z', offset=1, colors='k', zorder=1)

    # wcb and sfl plotted in shading and/or contours:

    norm = MidpointNormalize(midpoint=.1)
    if heating1 == True or heating2 == True:
        ax.contourf(kx2_2dp, wcb[:,int(ydim/2),:].T, p_2dx, zdir='y', offset=ly2[ymax], vmin=0,vmax=1,alpha=.05, cmap=binarymap) # wcb projected onto back wall
        #ax.contourf(kx2_2dp[jtsf:,xmin:xmax], sfl[xmin:xmax,int(ydim/2),jtsf:].T, p_2dx[jtsf:,xmin:xmax], zdir='y', offset=ly2[ymax],alpha=.1, cmap=cm_br) # sfl projected onto back wall
        if box == True:
            ax.contourf(kx2_2dp[jtlc:jblc,x2min:x2max], wcb[x2min:x2max,int(ydim/2),jtlc:jblc].T, p_2dx[jtlc:jblc,x2min:x2max], zdir='y', offset=ly2[int(ydim/2-1/8*len(ly2)-1)],norm=norm,vmin=-1,vmax=1,alpha=.2, cmap=cm_br, zorder=100000)
            ax.contourf(kx2_2dp[jtlc:jblc,x2min:x2max], wcb[x2min:x2max,int(ydim/2),jtlc:jblc].T, p_2dx[jtlc:jblc,x2min:x2max], zdir='y', offset=ly2[int(ydim/2+1/8*len(ly2)-1)], norm=norm,vmin=-1,vmax=1,alpha=.2, cmap=cm_br, zorder=10)
            ax.contourf(wcb[np.argwhere(wcb[:,int(ydim/2),jtml]>0)[0][0],ymin:ymax,jtlc:jblc].T, ly2_2dp[jtlc:jblc,ymin:ymax], p_2dy[jtlc:jblc,ymin:ymax], zdir='x', offset=kx2[x2min], norm=norm,vmin=-1,vmax=1,alpha=.2, cmap=cm_br, zorder=100000)
            ax.contourf(wcb[np.argwhere(wcb[:,int(ydim/2),jtml]>0)[0][0],ymin:ymax,jtlc:jblc].T, ly2_2dp[jtlc:jblc,ymin:ymax], p_2dy[jtlc:jblc,ymin:ymax], zdir='x', offset=kx2[x2max], norm=norm,vmin=-1,vmax=1,alpha=.2, cmap=cm_br, zorder=10)
            ax.contourf(kx2_2dy[ymin:ymax,x2min:x2max], ly2_2dx[ymin:ymax,x2min:x2max], wcb[x2min:x2max,ymin:ymax,jtlc].T, zdir='z', offset=p[jtlc], norm=norm,vmin=-1,vmax=1,alpha=.2, cmap=cm_br, zorder=100000)
            ax.contourf(kx2_2dy[ymin:ymax,x2min:x2max], ly2_2dx[ymin:ymax,x2min:x2max], wcb[x2min:x2max,ymin:ymax,jblc].T, zdir='z', offset=p[jblc], norm=norm,vmin=-1,vmax=1,alpha=.2, cmap=cm_br, zorder=10)
    #        ax.voxels(ly2_3d, kx2_3d, p_3d, np.swapaxes(wcb[:-1,:-1,:-1],0,1), alpha=.1, cmap=binarymap)#, vmin=-1,vmax=1

    # trajectories plotted in grey and colored lines:

    norm = MidpointNormalize(midpoint=0)
    if trajectories == True:
        for n in range(ntr):
            if np.squeeze(trdp[-1])[n] > 0: # shows only trajectories that ascend minimum 0*1000 hPa the last day (or while being inside domain)
                if wcbsfl[n] == 0 and (heating1 == True or heating2 == True):#(i not in set(np.arange(2,int(ntr),3)))==True:#
                    ax.plot(kx2[k0[:-int(60**2*24/dt)+1,n]],ly2[l0[:-int(60**2*24/dt)+1,n]],p[m0[:-int(60**2*24/dt)+1,n]],color='grey',ls='--',alpha=.2,lw=lw-.5,zorder=10000)
                    ax.plot(kx2[k0[-int(60**2*24/dt):br[n],n]],ly2[l0[-int(60**2*24/dt):br[n],n]],p[m0[-int(60**2*24/dt):br[n],n]],color='grey',ls='--',alpha=.2,lw=lw-.5,zorder=10000)
                    #ax.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],p[m0[:br[n],n]],color='grey',alpha=.2,lw=lw,zorder=10000)
                    #ax.plot(kx2[k0ext[:br[n],n]],ly2[l0[:br[n],n]],p[m0[:br[n],n]],color='k',ls=':',alpha=1,zorder=10000)
                    if ntry == 3 and ntrz > 1 and len(trdp) == 1:
                        ax.scatter(kx2[k0s[n]],ly2[l0s[n]],p[m0s[n]],marker=markers[int(round((l0s[n]-l0s[0])*2/(l0s[-1]-l0s[0])))],s=ms,color='grey',edgecolor='grey',zorder=10000)#,label=int(p[m0s[m]]*1000)
                    else:
                        ax.scatter(kx2[k0s[n]],ly2[l0s[n]],p[m0s[n]],s=ms,color='grey',edgecolor='grey',alpha=.2,zorder=10000)
                else: # if trajectories touch sfl before ascending into the wcb
                    if ntry == 1:
                        ax.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],p[m0[:br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),lw=lw,zorder=10000)
                        ax.scatter(kx2[k0s[n]],ly2[l0s[n]],p[m0s[n]],s=ms,color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),edgecolor=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),zorder=10000)
                    elif ntrz == 1:
                        ax.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],p[m0[:br[n],n]],color=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])),lw=lw,zorder=10000)
                        ax.scatter(kx2[k0s[n]],ly2[l0s[n]],p[m0s[n]],s=ms,color=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])),edgecolor=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])),zorder=10000)
                    elif ntry == 3 and ntrz > 1 and len(trdp) == 1:
                        ax.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],p[m0[:br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),lw=lw,zorder=10000)
                        ax.scatter(kx2[k0s[n]],ly2[l0s[n]],p[m0s[n]],marker=markers[int(round((l0s[n]-l0s[0])*2/(l0s[-1]-l0s[0])))],s=ms,color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),edgecolor=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),zorder=10000)#,label=int(p[m0s[m]]*1000)
                    else:
                        for t in range(len(k0)-1):
                            if abs(sflpos[n,t]+sflneg[n,t])/np.max(abs(sflpos+sflneg))<.1:
                                ax.plot(kx2[k0[t:t+2,n]],ly2[l0[t:t+2,n]],p[m0[t:t+2,n]],color=cm_bgr(((sflpos[n,t]+sflneg[n,t])/np.max(abs(sflpos+sflneg))+1)/2),lw=lw-.5,solid_capstyle='projecting',zorder=10000)#(p[m0s[n]]-ptlc)/(plow-ptlc) #clab((p[m0s[n]]-ptlc)/(plow-ptlc))
                            else:
                                ax.plot(kx2[k0[t:t+2,n]],ly2[l0[t:t+2,n]],p[m0[t:t+2,n]],color=cm_bgr(((sflpos[n,t]+sflneg[n,t])/np.max(abs(sflpos+sflneg))+1)/2),lw=lw-.5,solid_capstyle='projecting',zorder=10000000)#(p[m0s[n]]-ptlc)/(plow-ptlc) #clab((p[m0s[n]]-ptlc)/(plow-ptlc))
                        #ax.plot(kx2[k0[:-int(60**2*24/dt)+1,n]],ly2[l0[:-int(60**2*24/dt)+1,n]],p[m0[:-int(60**2*24/dt)+1,n]],color='k',alpha=.4,lw=lw,zorder=10000)#(p[m0s[n]]-ptlc)/(plow-ptlc) #clab((p[m0s[n]]-ptlc)/(plow-ptlc))
                        #ax.plot(kx2[k0[-int(60**2*24/dt):br[n],n]],ly2[l0[-int(60**2*24/dt):br[n],n]],p[m0[-int(60**2*24/dt):br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),ls='--', alpha=.4,lw=lw,zorder=10000)#(p[m0s[n]]-ptlc)/(plow-ptlc)
                        #ax.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],p[m0[:br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.4,lw=lw,zorder=10000)#(p[m0s[n]]-ptlc)/(plow-ptlc)
                        ax.scatter(kx2[k0s[n]],ly2[l0s[n]],p[m0s[n]],s=ms,color=cm_bgr(.5),edgecolor=cm_bgr(.5),zorder=1000000)#,label=int(p[m0s[m]]*1000) #clab((p[m0s[n]]-ptlc)/(plow-ptlc))
                if dt > 0:
                    for ki in range(br[n])[::8]:
                        ax.scatter(kx2[k0[ki,n]],ly2[l0[ki,n]],p[m0[ki,n]],s=ms,color='grey')
        for m in range(ntrz):
            ax.scatter((),(),(),s=ms,color=clab((p[m0s[-(m*ntrx+1)]]-ptlc)/(plow-ptlc)),label=(int(p[m0s[-(m*ntrx+1)]]*1000)))
#        plt.legend(fontsize='large',loc='best',title='p(t$_0$) [hPa]:')
    
    ax.set_xlabel('x [km]', labelpad=1)
    ax.set_xticks([np.pi/2,np.pi*2/2,np.pi*3/2,np.pi*4/2,np.pi*5/2,np.pi*6/2])#,6*np.pi])
    ax.set_xticklabels([0,'%d' %(np.pi*1/2/k[i_maxunstab[eps1_index,eps2_index]]*10**3),'%d' %(np.pi*2/2/k[i_maxunstab[eps1_index,eps2_index]]*10**3), '%d' %(np.pi*3/2/k[i_maxunstab[eps1_index,eps2_index]]*10**3), '%d' %(np.pi*4/2/k[i_maxunstab[eps1_index,eps2_index]]*10**3), '%d' %(np.pi*5/2/k[i_maxunstab[eps1_index,eps2_index]]*10**3)])#,'%d' %(6*np.pi/k[i_maxunstab[eps1_index,eps2_index]]*10**3)],fontsize=16)#'%d' %(-2*np.pi/k[i_maxunstab[eps1_index,eps2_index]]*10**3),
    ax.set_xlim(kx2[xmin],kx2[xmax])
#    if cycrel == True:
#        ax.set_xlim(np.pi,9*np.pi)#kx2[-1])
    
    ax.set_ylabel('y [km]')
    ax.set_yticks(([ly2[int(ydim/2-1/8*len(kx2))],ly2[int(ydim/2+1/8*len(kx2))]]),minor=True)
    ax.set_yticks([ly2[int(ydim/2-1/4*len(ly2))],ly2[int(ydim/2)],ly2[int(ydim/2+1/4*len(ly2))]])
    ax.set_yticklabels(['%d' %(-1/4*2*np.pi/l*10**3),0,'%d' %(1/4*2*np.pi/l*10**3)])#,fontsize=16)#    ax.set_ylim(kx2[int(ydim/2-1/4*len(ly2))],kx2[int(ydim/2+1/4*len(ly2)-1)])
    ax.minorticks_on()
    ax.tick_params(axis='y',which='minor', length=3, width=1)
    ax.tick_params(axis='y',which='major', length=6, width=1)
    ax.set_ylim(ly2[ymin],ly2[ymax])#ly2[int(ydim/2-1/4*len(ly2))],ly2[int(ydim/2+1/4*len(ly2)-1)])
    
    ax.set_zticks([pt,ptlc,ptml,ptsf,ps])
    ax.set_zticklabels([int(pt*1000),int(ptlc*1000),int(ptml*1000),int(ptsf*1000),int(ps*1000)])#,fontsize=16)#'150     ','1000        '])
    ax.set_zlim(.15,1)
    ax.zaxis.set_rotate_label(False)  # disable automatic rotation
    ax.set_zlabel('p [hPa]', rotation=92)#pressure (hPa)
    ax.invert_zaxis()
    
    #ax.plot((kx[cyc_s[-1]],kx[cyc_s[-1]]+1/2*kx[-1]),(ly2[int(ydim/2)],ly2[int(ydim/2)]),(p[-1],p[-1]),color='grey',ls='-',zorder=10000)
    #ax.plot((kx[cyc_s[-1]]+1/4*kx[-1],kx[cyc_s[-1]]+1/4*kx[-1]),(ly2[int(ydim/2)]-1/8*ly2[-1]*len(kx2)/len(ly2),ly2[int(ydim/2)]+1/8*ly2[-1]*len(kx2)/len(ly2)),(p[-1],p[-1]),color='grey',ls='-',zorder=10000)
    #ax.plot((kx[cyc_s[-1]]+1/4*kx[-1],kx[cyc_s[-1]]+1/4*kx[-1]),(ly2[int(ydim/2)]-1/8*ly2[-1],ly2[int(ydim/2)]+1/8*ly2[-1]),(p[-1],p[-1]),color='grey',ls='--',zorder=10000)
    
    ax.azim = -115
    ax.elev = 25
    ax.grid(False)
    ax.xaxis.labelpad=25
    ax.yaxis.labelpad=20
    ax.zaxis.labelpad=5
    ax.patch.set_alpha(0)
    ax.w_xaxis.set_pane_color((1,1,1,1))
    ax.w_yaxis.set_pane_color((1,1,1,1))
    ax.w_zaxis.set_pane_color((1,1,1,1))
    ax.xaxis.pane.set_edgecolor((.95, .95, .95, .95))
    ax.yaxis.pane.set_edgecolor((.95, .95, .95, .95))
    ax.zaxis.pane.set_edgecolor((.95, .95, .95, .95))

    #ax.text2D(0.15, 0.88, 'wavelength:\n  %1d km' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000), transform=ax.transAxes)
    fig.tight_layout()

    plt.show()
    plt.savefig('test.png', transparent=True)
    
    if heating1 == True or heating2 == True:
        print (f'{(wcbsfl_dp[-1].tolist()).count(1.)} out of {len([1 for i in trdp[-1] if i > .1])} trajectories touch surface flux layer before warm conveyor belt')
   
    
# -----------------------------------------------------------------------------

### plotting streamfunction cross sections with trajectories ------------------

def plot_trajectories_2D():

    compare_frameworks = False

#    colorsList = [(1,1,1),(.5,.5,.5)]
#    binarymap = mpl.colors.ListedColormap(colorsList)

#    mpl.rc('font',size=12)

    fig, (ax0,ax1) = plt.subplots((2), figsize=(6.6,8), dpi=300)#3.6,3))
    #fig = plt.figure(figsize=(5,7))
    #gs = gridspec.GridSpec(2, 1, height_ratios=[6, 3]) 
    #ax0 = plt.subplot(gs[0])
    #ax1 = plt.subplot(gs[1])
        
    psiplot = ax0.contourf(kx2, p[:nrws], psi3d[:,int(ydim/2),:].T, lev, alpha=.4, cmap=cm_br)
    ax0.contour(kx2, p[jtsf:nrws], sfl[:,int(ydim/2),jtsf:].T, 4, colors='k',alpha=.3)#_in_range
#    ax0.contourf(kx2, p[:nrws], wcb[:,int(ydim/2),:].T, alpha=.2, cmap=binarymap)
    #ax0.scatter(kx2[cyc_s.tolist()],p[:nrws],c='k',marker='.',s=1)
    #ax0.scatter(kx2[cyc_e.tolist()],p[:nrws],c='k',marker='.',s=1)
    ax0.set_title('psi @ y = 0')
    for n in range(ntr):
        if np.squeeze(trdp[-1])[n] > 0:
            if wcbsfl[n] == 0 and (heating1 == True or heating2 == True):#(i not in set(np.arange(2,int(ntr),3)))==True: #
                if compare_frameworks == True:
                    ax0.scatter(kx2[k0[:br[n],n]],p[m0[:br[n],n]],s=10,color='grey',alpha=1, zorder=1)
                    ax0.plot(kx2[k0[:br[n],n]],p[m0[:br[n],n]],color='grey',alpha=1, zorder=1)
                    ax0.scatter(kx2[k0ext[:br[n],n]],p[m0[:br[n],n]],s=10,color='k',alpha=1, zorder=1)#,ls=':'
                    ax0.plot(kx2[k0ext[:br[n],n]],p[m0[:br[n],n]],ls=':',color='k',alpha=1, zorder=1)
                    ax0.scatter(kx2[k0s[n]],p[m0s[n]],s=10,color='grey',alpha=1,zorder=1)
                else:
                    ax0.plot(kx2[k0[:-int(60**2*24/dt)+1,n]],p[m0[:-int(60**2*24/dt)+1,n]],color='grey',alpha=.3, zorder=1)
                    ax0.plot(kx2[k0[-int(60**2*24/dt):br[n],n]],p[m0[-int(60**2*24/dt):br[n],n]],color='grey',ls='--',alpha=.3, zorder=1)
                    #ax0.plot(kx2[k0[:br[n],n]],p[m0[:br[n],n]],color='grey',alpha=.3, zorder=1)
                    ax0.scatter(kx2[k0s[n]],p[m0s[n]],s=10,color='grey',alpha=1,zorder=1)
            else:
                if ntry == 1:
                    ax0.plot(kx2[k0[:br[n],n]],p[m0[:br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.6, zorder=3)
                    ax0.scatter(kx2[k0s[n]],p[m0s[n]],s=10,color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),edgecolor=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),zorder=3)
                if ntrz == 1:
                    ax0.plot(kx2[k0[:br[n],n]],p[m0[:br[n],n]],color=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])), zorder=3)
                    ax0.scatter(kx2[k0s[n]],p[m0s[n]],s=10,color=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])),edgecolor=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])),zorder=3)
                else:
                    ax0.plot(kx2[k0[:-int(60**2*24/dt)+1,n]],p[m0[:-int(60**2*24/dt)+1,n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.6, zorder=3)
                    ax0.plot(kx2[k0[-int(60**2*24/dt):br[n],n]],p[m0[-int(60**2*24/dt):br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),ls='--',alpha=.6, zorder=3)
                    #ax0.plot(kx2[k0[:br[n],n]],p[m0[:br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.6, zorder=3)
                    ax0.scatter(kx2[k0s[n]],p[m0s[n]],s=10,color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),edgecolor=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),zorder=3)
            if dt > 0:
                for ki in range(br[n]):#[::8]:
                    ax0.scatter(kx2[k0[ki,n]],p[m0[ki,n]],s=3,color='grey',zorder=2)
#    for i in range(ntr):
#        ax0.scatter(kx2[k0s[n]],p[m0s[n]],s=5,color=clab(n/ntr),edgecolor=clab(n/ntr),zorder=3)
    #    if ts == 0:
    #        ax0.scatter(kx2[k0s[n]],p[m0s[n]],s=15,c=clab(n/ntr), zorder=3)
    #    if ts > 0:
    #        ax0.scatter(kx2[k0[br[n]-1,n]],p[m0[br[n]-1,n]],s=15,c=clab(n/ntr), zorder=3)
    ax0.set_xlabel('')
    ax0.set_xticks([])
    ax0.set_xlim(kx2[xmin],kx2[xmax])#*3/4
    if cycrel == True:
        ax0.set_xlim(kx2[xmin],kx2[xmax])#np.pi,8*np.pi)#kx2[-1])
    ax0.set_ylabel('p')
    #ax0.set_yticks([.15,1])
    if cycrel == True:
        ax0.hlines(y=0.25,xmin=kx2[np.argwhere(wcb==1)[0][0]],xmax=kx2[np.argwhere(wcb==1)[0][0]]-cycdist/wl[i_maxunstab[eps1_index,eps2_index]]/1000*kx[-1],lw=1)
        ax0.vlines(x=kx2[np.argwhere(wcb==1)[0][0]],ymin=.24,ymax=.26,lw=1)
        ax0.vlines(x=kx2[np.argwhere(wcb==1)[0][0]]-cycdist/wl[i_maxunstab[eps1_index,eps2_index]]/1000*kx[-1],ymin=.24,ymax=.26,lw=1)
#        ax0.hlines(y=0.25,xmin=kx2[-1]*15/16+cycdist/wl[i_maxunstab[eps1_index,eps2_index]]/1000*kx[-1],xmax=kx2[-1]*15/16,lw=1)
#        ax0.vlines(x=kx2[-1]*15/16+cycdist/wl[i_maxunstab[eps1_index,eps2_index]]/1000*kx[-1],ymin=.24,ymax=.26,lw=1)
#        ax0.vlines(x=kx2[-1]*15/16,ymin=.24,ymax=.26,lw=1)
    ax0.invert_yaxis()
#    ax0.grid('on')
    
    psiplot = ax1.contourf(kx2, ly2, (psi3d[:,:,m0s[0]]).T,lev,alpha=.4,cmap=cm_br)
#    ax1.contourf(kx2, ly2, (wcb[:,:,jtml]).T, alpha=.2, cmap=binarymap)
    #ax1.contour(kx, kx[:int(len(kx)/2)], (u3d[:,:,m0s]).T, 3, colors='k')
    ax1.set_title('psi @ p = %1.2f' %(p[m0s[0]]))
    for n in range(ntr):
        if np.squeeze(trdp[-1])[n] > 0:
            if wcbsfl[n] == 0 and (heating1 == True or heating2 == True):#
                if compare_frameworks == True:
                    ax1.scatter(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],s=10,color='grey',alpha=1,zorder=1)
                    ax1.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],color='grey',alpha=1,zorder=1)
                    ax1.scatter(kx2[k0ext[:br[n],n]],ly2[l0[:br[n],n]],s=10,color='k',alpha=1,zorder=1)
                    ax1.plot(kx2[k0ext[:br[n],n]],ly2[l0[:br[n],n]],color='k',ls=':',alpha=1,zorder=1)
                    ax1.scatter(kx2[k0s[n]],ly2[l0s[n]],s=10,color='grey',alpha=1,zorder=1)
                else:
                    ax1.plot(kx2[k0[:-int(60**2*24/dt)+1,n]],ly2[l0[:-int(60**2*24/dt)+1,n]],color='grey',alpha=.3,zorder=1)            
                    ax1.plot(kx2[k0[-int(60**2*24/dt):br[n],n]],ly2[l0[-int(60**2*24/dt):br[n],n]],color='grey',ls='--',alpha=.3,zorder=1)            
                    #ax1.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],color='grey',alpha=.3,zorder=1)            
                    ax1.scatter(kx2[k0s[n]],ly2[l0s[n]],s=10,color='grey',alpha=1,zorder=1)
            else:
                if ntry == 1:
                    ax1.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.6,zorder=3)            
                    ax1.scatter(kx2[k0s[n]],ly2[l0s[n]],s=10,color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),zorder=3)
                if ntrz == 1:
                    ax1.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],color=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])),zorder=3)            
                    ax1.scatter(kx2[k0s[n]],ly2[l0s[n]],s=10,color=clab((l0s[n]-l0s[0])/(l0s[-1]-l0s[0])),zorder=3)
                else:
                    ax1.plot(kx2[k0[:-int(60**2*24/dt)+1,n]],ly2[l0[:-int(60**2*24/dt)+1,n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.6,zorder=3)            
                    ax1.plot(kx2[k0[-int(60**2*24/dt):br[n],n]],ly2[l0[-int(60**2*24/dt):br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),ls='--',alpha=.6,zorder=3)            
                    #ax1.plot(kx2[k0[:br[n],n]],ly2[l0[:br[n],n]],color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),alpha=.6,zorder=3)            
                    ax1.scatter(kx2[k0s[n]],ly2[l0s[n]],s=10,color=clab((p[m0s[n]]-ptlc)/(plow-ptlc)),zorder=3)
            if dt > 0:
                for ki in range(br[n]):#[::8]:
                    ax1.scatter(kx2[k0[ki,n]],ly2[l0[ki,n]],s=3,color='grey',zorder=2)
#    for i in range(ntr):
    #    if ts == 0:
    #        ax1.scatter(kx2[k0s[n]],kx2[l0s[n]],s=30,c=clab(n/ntr), zorder=3)
    #    if ts > 0:
    #        ax1.scatter(kx2[k0[br[n]-1,n]],kx2[l0[br[n]-1,n]],s=15,c=clab(n/ntr), zorder=3)
    ax1.set_xlabel('x\nwavelength = %1d km' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000))
    ax1.set_xticks([])
    ax1.set_xlim(kx2[xmin],kx2[xmax])#*3/4
    if cycrel == True:
        ax1.set_xlim(kx2[xmin],kx2[xmax])#np.pi,8*np.pi)#kx2[-1])
    ax1.set_ylabel('y')
    ax1.set_yticks([ly2[int(ydim/2-1/4*len(ly2))],ly2[int(ydim/2-1/8*len(kx2))],ly2[int(ydim/2)],ly2[int(ydim/2+1/8*len(kx2))],ly2[int(ydim/2+1/4*len(ly2))]])
    #ax1.set_yticks([ly2[int(ydim/2-1/4*len(kx))],ly2[int(ydim/2)],ly2[int(ydim/2+1/4*len(kx))]])
    ax1.set_yticklabels(['0','','$\mathregular{\pi/2}$','','$\mathregular{\pi}$'])
#    ax1.set_ylim(ly2[int(ydim/2-1/4*len(ly2))],ly2[int(ydim/2+1/4*len(ly2)-1)])
    ax1.set_ylim(ly2[ymin],ly2[ymax])
    
    plt.tight_layout()
    plt.show()
    
# -----------------------------------------------------------------------------

### plotting basic state u field ------------------

def plot_ubar():

    i = 120 # x index

    fig,ax = plt.subplots()
    
    cs2 = ax.contourf(ly2,p[:nrws],utr3d.T,vmin=-np.max(utr3d),cmap=cm_br)
    ax.contour(ly2,p[:nrws],u3d[i].T,vmin=-np.max(u3d[i]),colors='k')#cmap=cm_br, alpha=.7)
    #plt.colorbar(cs)
    plt.colorbar(cs2)
    ax.set_xlabel('y [km]')
    ax.set_xticks([ly2[int(ydim/2-1/4*len(ly2))],ly2[int(ydim/2)],ly2[int(ydim/2+1/4*len(ly2))]])
    ax.set_xticklabels(['%d' %(-1/4*2*np.pi/l*10**3),0,'%d' %(1/4*2*np.pi/l*10**3)])
    ax.set_ylabel('z [hPa]')
    ax.set_ylim(.15,1)
    ax.set_yticks([pt,ptlc,ptml,ptsf,ps])
    ax.set_yticklabels([int(pt*1000),int(ptlc*1000),int(ptml*1000),int(ptsf*1000),int(ps*1000)])
    ax.set_title(f'@ x = {kx2[i]:.2}')
    ax.invert_yaxis()
    plt.show()


