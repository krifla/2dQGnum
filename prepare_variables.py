
# --------------------------------------------------------------------------------
# wave solution (see Mak1994, eq. 15)
# --------------------------------------------------------------------------------

#global shift#, psi, w, v, T

#psi_maxunstab = psi_maxunstab*scalefactor
#w_maxunstab = w_maxunstab*scalefactor

psi	= ( psi_maxunstab[eps1_index,eps2_index,:,np.newaxis]*np.exp(kx[np.newaxis,:]*1j) ).real
shift = np.argwhere(psi[-1] == np.max(psi[-1]))[0][0] # phase shift for all wave structures for better comparison
psi	= ( psi_maxunstab[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
w	= ( w_maxunstab[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real

if unstab2 == True:
    psi2 = ( psi_maxunstab2[eps1_index,eps2_index,:,np.newaxis]*np.exp(kx[np.newaxis,:]*1j) ).real
    shift2 = np.argwhere(psi2[-1] == np.max(psi2[-1]))[0][0] # phase shift for all wave structures for better comparison
    psi2 = ( psi_maxunstab2[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift2])*1j) ).real
    w2 = ( w_maxunstab2[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift2])*1j) ).real

if unstab3 == True:
    psi3 = ( psi_maxunstab3[eps1_index,eps2_index,:,np.newaxis]*np.exp(kx[np.newaxis,:]*1j) ).real
    shift3 = np.argwhere(psi3[-1] == np.max(psi3[-1]))[0][0] # phase shift for all wave structures for better comparison
    psi3 = ( psi_maxunstab3[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift3])*1j) ).real
    w3 = ( w_maxunstab3[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift3])*1j) ).real
    
if stab == True:
    psi_s = ( psi_maxstab[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    w_s = ( w_maxstab[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real

if stab2 == True:
    psi_s2 = ( psi_maxstab2[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    w_s2 = ( w_maxstab2[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    
if stab3 == True:
    psi_s3 = ( psi_maxstab3[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    w_s3 = ( w_maxstab3[eps1_index,eps2_index,:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    
# --------------------------------------------------------------------------------
# structure of meridional velocity
# proportional to dpsi/dx = ikpsi
# --------------------------------------------------------------------------------

v = (1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index])
v = (v[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real

if unstab2 == True:
    v2 = (1j*k[i_maxunstab2[eps1_index,eps2_index]]*psi_maxunstab2[eps1_index,eps2_index])
    v2 = (v2[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift2])*1j) ).real

if unstab3 == True:
    v3 = (1j*k[i_maxunstab3[eps1_index,eps2_index]]*psi_maxunstab3[eps1_index,eps2_index])
    v3 = (v3[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift3])*1j) ).real

if stab == True:
    v_s = (1j*k[i_maxstab[eps1_index,eps2_index]]*psi_maxstab[eps1_index,eps2_index])
    v_s = (v_s[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    
if stab2 == True:
    v_s2 = (1j*k[i_maxstab2[eps1_index,eps2_index]]*psi_maxstab2[eps1_index,eps2_index])
    v_s2 = (v_s2[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    
if stab3 == True:
    v_s3 = (1j*k[i_maxstab3[eps1_index,eps2_index]]*psi_maxstab3[eps1_index,eps2_index])
    v_s3 = (v_s3[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    
# --------------------------------------------------------------------------------
# structure of zonal velocity
# proportional to -integral(dw/dp)dx
# --------------------------------------------------------------------------------

def dwdpcalc(arg):
    dwdp = np.zeros((len(w[:,0])), dtype = complex)
    for i in range(1,len(arg)-1):
        dwdp[i] = -(arg[i+1]-arg[i-1])/(2*dp)
    dwdp[0] = -(arg[1]-arg[0])/dp
    dwdp[-1] = -(arg[-1]-arg[-2])/dp

    #uatemp = (uatemp[:,np.newaxis]*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    return dwdp

#dwdp = dwdpcalc(w_maxunstab[eps1_index,eps2_index])
#dwdp = (dwdp[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
#ua = 1j*dwdp/k[i_maxunstab[eps1_index,eps2_index]]
##ua = (ua[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real

#def uacalc(arg):
#    dwdp = np.zeros((len(epsilon1),len(w[:,0])), dtype = complex)
#    for e in range(len(epsilon1)):
#        for i in range(1,len(arg[eps1_index,eps2_index])-1):
#            dwdp[e,i] = -(arg[e,eps2_index,i+1]-arg[e,eps2_index,i-1])/(2*dp)
#        dwdp[e,0] = -(arg[e,eps2_index,1]-arg[e,eps2_index,0])/dp
#        dwdp[e,-1] = -(arg[e,eps2_index,-1]-arg[e,eps2_index,-2])/dp
#
#    uatemp = 1j*dwdp/k[i_maxunstab[e,eps2_index]]
#    #uatemp = (uatemp[:,np.newaxis]*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
#    return uatemp
#
#ua = uacalc(w_maxunstab)
#ua = (ua[:,:,np.newaxis]*exp((kx[np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,shift])*1j) ).real

if unstab2 == True:
    dwdp2 = dwdpcalc(w_maxunstab2[eps1_index,eps2_index])
    ua2 = 1j*dwdp2/k[i_maxunstab2[eps1_index,eps2_index]]
    ua2 = (ua2[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift2])*1j) ).real
    
if unstab3 == True:
    dwdp3 = dwdpcalc(w_maxunstab3[eps1_index,eps2_index])
    ua3 = 1j*dwdp3/k[i_maxunstab3[eps1_index,eps2_index]]
    ua3 = (ua3[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift3])*1j) ).real
    
# --------------------------------------------------------------------------------
# structure of temperature (or more correctly: density) 
# proportional to -dpsi/dp (times pressure)
# --------------------------------------------------------------------------------

def tempcalc(arg):
    Ttemp = np.zeros(np.shape(arg), dtype = complex)
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            for j in range(1,len(arg[e,e2])-1):
                Ttemp[e,e2,j] = (arg[e,e2,j+1]-arg[e,e2,j-1])/(2*dp)
            if heating1 == True and h1pro == False:
                Ttemp[e,e2,jtlc-1] = (arg[e,e2,jtlc-1]-arg[e,e2,jtlc-2])/dp
                Ttemp[e,e2,jtlc] = (arg[e,e2,jtlc+1]-arg[e,e2,jtlc])/dp
                if pblc<1:
                    Ttemp[e,e2,jblc-1] = (arg[e,e2,jblc-1]-arg[e,e2,jblc-2])/dp
                    Ttemp[e,e2,jblc] = (arg[e,e2,jblc+1]-arg[e,e2,jblc])/dp
            if stratos == True and smoothshearstrat == False:
                Ttemp[e,e2,jtrop] = (Ttemp[e,e2,jtrop-1]+Ttemp[e,e2,jtrop+1])/2
            Ttemp[e,e2,0] = (arg[e,e2,1]-arg[e,e2,0])/dp
            Ttemp[e,e2,-1] = (arg[e,e2,-1]-arg[e,e2,-2])/dp
    #Ttemp = ( Ttemp[:,np.newaxis]*exp(kx[np.newaxis,:]*1j) ).real
    return Ttemp


T = tempcalc(psi_maxunstab)
T = ( T[:,:,:,np.newaxis]*np.exp((kx[np.newaxis,np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,np.newaxis,shift])*1j) ).real

if unstab2 == True:
    T2 = tempcalc(psi_maxunstab2)
    T2 = ( T2[:,:,:,np.newaxis]*np.exp((kx[np.newaxis,np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,np.newaxis,shift2])*1j) ).real
    
if unstab3 == True:
    T3 = tempcalc(psi_maxunstab3)
    T3 = ( T3[:,:,:,np.newaxis]*np.exp((kx[np.newaxis,np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,np.newaxis,shift3])*1j) ).real

if stab == True:
    T_s = tempcalc(psi_maxstab)
    T_s = ( T_s[:,:,:,np.newaxis]*np.exp((kx[np.newaxis,np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,np.newaxis,shift])*1j) ).real
    
if stab2 == True:
    T_s2 = tempcalc(psi_maxstab2)
    T_s2 = ( T_s2[:,:,:,np.newaxis]*np.exp((kx[np.newaxis,np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,np.newaxis,shift])*1j) ).real
    
if stab3 == True:
    T_s3 = tempcalc(psi_maxstab3)
    T_s3 = ( T_s3[:,:,:,np.newaxis]*np.exp((kx[np.newaxis,np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,np.newaxis,shift])*1j) ).real
	
    
# --------------------------------------------------------------------------------
# structure of total static stability
# --------------------------------------------------------------------------------

# second derivative of psi
d2psidp2 = -(tempcalc(tempcalc(psi_maxunstab)))
d2psidp2 = ( d2psidp2[:,:,:,np.newaxis]*np.exp((kx[np.newaxis,np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,np.newaxis,shift])*1j) ).real

f = 10**(-4)
p00 = 10**5
L = 10**6
R = 287
cp = 1004

# the three terms of total static stability (turned off to free memory)
#Stot1 = (S[np.newaxis,:nrws,np.newaxis])
#Stot2 = np.insert(-f*(d2psidp2[:,:,1:,:]+1/p[np.newaxis,1:nrws,np.newaxis]*T[:,:,1:,:])*(p00/f/L)**2,0,nan,axis=2) # nan added where there is division by p=0
#Stot3 = np.insert(f/p[np.newaxis,1:nrws,np.newaxis]*T[:,:,1:,:]*(R/cp)*(p00/f/L)**2,0,nan,axis=2) # nan added where there is division by p=0
#Stot = Stot1 + Stot2 + Stot3

# --------------------------------------------------------------------------------
# structure of diabatic heating
# --------------------------------------------------------------------------------

#if heating1 == True or heating2 == True:
    
def Qcalc(arg1,arg2,arg3,arg4):
    if wpar == False and vpar == False:
        Qtemp = -epsilon1[eps1_index]*h1[eps1_index,:nrws]*arg1/2 \
                +epsilon2[eps2_index]*h2[eps2_index,:nrws]*(-arg2)
    if wpar == True:
        Qtemp = -epsilon1[eps1_index]*h1[eps1_index,:nrws]*arg1/2 \
                +epsilon2[eps2_index]*h2[eps2_index,:nrws]*arg1
    if vpar == True:
        Qtemp = -epsilon1[eps1_index]*h1[eps1_index,:nrws]*arg1/2 \
                -1j*k[i_maxunstab[eps1_index,eps2_index]]*epsilon2[eps2_index]*h2[eps2_index,:nrws]*arg3
    Qtemp = (Qtemp[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,arg4])*1j)).real
    return Qtemp

Q = Qcalc(w_maxunstab[eps1_index,eps2_index,jtml],tempcalc(psi_maxunstab)[eps1_index,eps2_index,-1],psi_maxunstab[eps1_index,eps2_index,-1],shift)

if unstab2 == True:
    Q2 = Qcalc(w_maxunstab2[eps1_index,eps2_index,jtml],tempcalc(psi_maxunstab2)[eps1_index,eps2_index,-1],psi_maxunstab2[eps1_index,eps2_index,-1],shift2)

if unstab3 == True:
    Q3 = Qcalc(w_maxunstab3[eps1_index,eps2_index,jtml],tempcalc(psi_maxunstab3)[eps1_index,eps2_index,-1],psi_maxunstab3[eps1_index,eps2_index,-1],shift3)

# --------------------------------------------------------------------------------
# structure of potential vorticity
# proportional to d((dpsi/dp)/S)/dp-k²psi
#                     PV1 + PV2    + PV3
# --------------------------------------------------------------------------------

def PVcalc(arg1,arg2,arg3,arg4):
    PV1temp = np.zeros((len(epsilon1),len(epsilon2),nrws,len(kx)))#, dtype = complex)
    PV2temp = np.zeros((len(epsilon1),len(epsilon2),nrws,len(kx)))#, dtype = complex)
    PV3temp = np.zeros((len(epsilon1),len(epsilon2),nrws), dtype = complex)
    
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            for i in range(len(kx)):
                for j in range(1,nrws-1):
                    PV1temp[e,e2,j,i] = (arg2[e,e2,j+1,i]-arg2[e,e2,j-1,i])/S[j]/(2*dp)
                    PV2temp[e,e2,j,i] = -1/S[j]**2*(S[j+1]-S[j-1])/(2*dp)*arg2[e,e2,j,i]
                if stratos == True and smoothshearstrat == False and smoothstrat == False and smoothshear == False:
                    PV1temp[e,e2,jtrop,i] = (arg2[e,e2,jtrop+1,i]/S[jtrop+1]-arg2[e,e2,jtrop-1,i]/S[jtrop-1])/(2*dp)
                    PV2temp[e,e2,jtrop,i] = 0 # @ discrete tropopause, PV1 and PV2 are merged to one term
                PV1temp[e,e2,0,i] = (arg2[e,e2,0,i])/S[0]/dp###(arg2[e,e2,1,i]-arg2[e,e2,0,i])/S[0]/dp
                PV1temp[e,e2,-1,i] = (-arg2[e,e2,-1,i])/S[-1]/dp###(arg2[e,e2,-1,i]-arg2[e,e2,-2,i])/S[-1]/dp
                PV2temp[e,e2,0,i] = -(S[1]-S[0])/S[0]**2/dp*arg2[e,e2,0,i]
                PV2temp[e,e2,-1,i] = -(S[-1]-S[-2])/S[-1]**2/dp*arg2[e,e2,-1,i]
            PV3temp[e,e2] = -k[arg3[e,e2]]**2*(arg1[e,e2])
        PV3temp = (PV3temp[:,:,:,np.newaxis]*np.exp((kx[np.newaxis,np.newaxis,np.newaxis,:]+kx[np.newaxis,np.newaxis,np.newaxis,arg4])*1j)).real
            
        return PV1temp, PV2temp, PV3temp, PV1temp+PV2temp+PV3temp


PV1_u, PV2_u, PV3_u, PV_u = PVcalc(psi_maxunstab,T,i_maxunstab,shift)

if unstab2 == True:
    PV1_u2, PV2_u2, PV3_u2, PV_u2 = PVcalc(psi_maxunstab2,T2,i_maxunstab2,shift2)
            
if unstab3 == True:
    PV1_u3, PV2_u3, PV3_u3, PV_u3 = PVcalc(psi_maxunstab3,T3,i_maxunstab3,shift3)

if stab == True:
    PV1_s, PV2_s, PV3_s, PV_s = PVcalc(psi_maxstab,T_s,i_maxstab,shift)

if stab2 == True:
    PV1_s2, PV2_s2, PV3_s2, PV_s2 = PVcalc(psi_maxstab2,T_s2,i_maxstab2,shift)
            
if stab3 == True:
    PV1_s3, PV2_s3, PV3_s3, PV_s3 = PVcalc(psi_maxstab3,T_s3,i_maxstab3,shift)    
    
