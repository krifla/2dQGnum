#!/usr/bin/env python
# coding: utf-8

# Vicky stuff:
# pbetween 1 and 2 and jbetween 1 and 2
# klaas?
# stratidilution -> smoothstrat	
# smoothstrato -> smooth_S
# smooth -> smooth_u


# *****************************************************************************
# -----------------------------------------------------------------------------
# MODEL INPUT
# -----------------------------------------------------------------------------
# *****************************************************************************

# -----------------------------------------------------------------------------
# settings for heating, stratification, shear, friction, coriolis
# -----------------------------------------------------------------------------

### what kind of diabatic heating?
heating1	= False		# latent heating			                    Mak1994
heating1_ice= False		# latent heating at ice cloud stage	            Flacké
evap		= False		# latent cooling below heating layer    	    Flacké
heating2	= False		# sensible surface fluxes		                Mak1998

# more realistic heating profiles?
h1pro	= False
h1proa	= True			# Flacké, profile with latent heating only
h1prob	= False			# Flacké
h1proc	= False			# Flacké, profile with latent heating AND cooling
h1prod	= False			# Flacké
h2pro	= False			# Mak1998

# heating parameters
if heating1 == True:
    epsilon1 = np.array([0,1.5,2,2.5])### 3 for tropopause experiments
if heating1 == False:
    epsilon1 = np.array([0])
eps1_index = 0

if heating2 == True:
    epsilon2 = np.array([2.5])#1*(1-1j)/np.sqrt(2)])
if heating2 == False:
    epsilon2 = np.array([0])
eps2_index = 0
wpar = False	# parametrise surface fluxes wrt vertical velocity instead of T' or v'
vpar = False	# parametrise surface fluxes wrt meridional velocity instead of T' or w'
if wpar == True and vpar == True:
    raise AssertionError('wpar or vpar must be false')


### discontinuous stratification?
if heating2 == True:
    disc_strat = False###		# Mak1998
else:
    disc_strat = False		# Mak1994

# second discontinuity in stratification?
if disc_strat == True:
    disc_strat_2 = False	# Flacké
else:
    disc_strat_2 = False
    
# more realistic stratification profile?
Spro = False			# Mak1998
    
    
### add stratosphere?
stratos = False###         # Flacké

# settings at tropopause
smoothstrat     = False # smoothing stratification profile?              Vicky
smoothshear     = False # smoothing shear profile?                       Vicky
smooth_Sinv     = True # smoothing 1/S                                  Flacké
smoothshearstrat = False # smooth lambda/S                              Flacké
smoothfac       = 40
smoothsine      = True
TIL             = False # tropopause inversion layer?                   Vicky


### friction drag on?
drag		= False		# frictional effects			Flacké
alpha		= .5		# friction coefficient			Flacké
                        # ("The timescale of Rayleigh friction is about 5–10 days,
                        # in tropics sometimes 1 day or less" (Wu et al. 1999),
                        # yielding nondim alpha = .1-.2 or >1.0)
if drag == False:
    alpha = 0


### coriolis/latitude (Flacké)

ffac = 1.			        # f is set to 10^-4 corresponding to 43 deg and ffac is the difference factor from this
            			    # ex: ffac = 1.3 (1.4) corresponds to 1.3 (1.4) *10^-4 and 63 (74) deg North
epsilon1 = epsilon1/ffac**2	# epsilon1 is a function of the Coriolis parameter
beta = 0#1.6			    # 1.6*10^-11 at 44 deg, 1.0*10^-11 at 63 deg


# -----------------------------------------------------------------------------
# nondimensionalised constants and variables
# -----------------------------------------------------------------------------

### wavelength and wavenumber
wl	= np.logspace(np.log(1.),np.log(2.),150)
wl	= np.append(wl,np.logspace(np.log(2.05),np.log(4),50))
k	= 2.*np.pi/wl

### pressure levels and resolution

ps	    = 1.		# pressure @ surface/bottom of domain		Mak1994+1998
ptml	= .9		# pressure @ top of moist layer			    Mak1994: 0.9
pblc	= ptml		# pressure @ bottom of liquid cloud layer	Mak1994
ptlc	= .4###		# pressure @ top of liquid cloud layer		Mak1994: 0.4
ptic	= .6		# pressure @ top of ice cloud layer		    Flacké
ptsf	= .9		# pressure @ top of surface flux layer		Mak1998: 0.85	
ptbl	= .85		# pressure @ top of mixed boundary layer/
                    # level of stratification discontinuity		Mak1998: 0.8
ptdl	= .89		# pressure @ top of drag layer			    Flacké
pt	    = .0###		# pressure @ top of domain			        Mak1994: 0.15 or Mak1998: 0
ptrop	= .25 		# pressure @ tropopause				        Flacké

nrws	= 201   			# vertical resolution (number of grid points)
dp	    = (pt-ps)/(nrws-1)	# vertical resolution (constant increment)
					        # NOTE: be careful with derivatives when defining dp negative
p	= np.linspace(pt, ps, nrws)	# pressure vector
p	= np.append(p,p)		    # pressure vector repeated for calculations in model core

jtml	= int((pt-ptml)/dp)		# ptml entry			Mak1994
jblc	= int((pt-pblc)/dp)		# pblc entry			Mak1994
jtlc	= int((pt-ptlc)/dp)		# ptlc entry			Mak1994
jtic	= int((pt-ptic)/dp)		# ptic entry			Flacké
jtsf	= int((pt-ptsf)/dp)		# ptsf entry			Mak1998
jtbl	= int((pt-ptbl)/dp)		# ptbl entry			Mak1998
jtdl	= int((pt-ptdl)/dp)		# ptdl entry			Flacké
jtrop	= int((pt-ptrop)/dp)	# ptrop entry			Flacké

# testing if pressure levels are too close
if disc_strat_2 == True:
    try:
        if jtbl-1 <= jtlc:
            raise ValueTooSmallError
        if jtsf+1 >= jblc:
            raise ValueTooSmallError
    except NameError:
        print ('ptsf too close to pblc and/or ptbl too close to ptlc')
        
# making sure plevels correspond to index
ptml = p[jtml]; pblc = p[jblc]; ptlc = p[jtlc]; ptic = p[jtic];
ptsf = p[jtsf]; ptbl = p[jtbl]; ptdl = p[jtdl]; ptrop = p[jtrop]


# -----------------------------------------------------------------------------

### define stratification S (jump or analytic function)

S1	= 1			# static stability				        Mak1994
#S1	= 2			# static stability at upper levels		Mak1998
if disc_strat == True and heating2 == True:
    S2	= 2#(1-.7*np.tanh(abs(epsilon2[eps2_index])))*S1	# static stability at lower levels, dependent on epsilon
else:
    S2	= S1
    
S = np.zeros((nrws))
dSdp = np.zeros((nrws))
ddpS = np.zeros((nrws))
S0 = .5*(3*S2-S1)		# Mak1998

for j in range(jtbl):
    S[j] = S1
for j in range(jtbl,nrws):
    if Spro == False:
        S[j] = S2
    elif Spro == True:
        S[j] = S1 + (S0-S1)*((p[j]-ptbl)/(1-ptbl))**.5
        dSdp[j] = (S0-S1)/2/((1-ptbl)*(p[j]-ptbl))**.5
if disc_strat_2 == True:
    for j in range(jtsf,nrws):
        S[j] = S1
S[jtbl] = (S1+S2)/2


# inclusion of stratosphere 
   
if stratos == True:
    for j in range(jtrop):
        S[j] = 4*S1#3.389830508474576*S1
    S[jtrop] = (S[jtrop-1]+S[jtrop+1])/2
    #S[jtrop-10:jtrop] = 3
    #S[jtrop:jtrop+11] = 1.25
    #S[jtrop] = (S[jtrop-1]+S[jtrop+1])/2
    #S[jtrop-10] = (S[jtrop-11]+S[jtrop-9])/2
    #S[jtrop+10] = (S[jtrop+9]+S[jtrop+11])/2


# design tropopause inversion layer

def assymptotic(j):         # design TIL structure          Vicky
    if j == jtrop:
        j = jtrop + 10000
    S = 4+(6/(jtrop-j))-6/jtrop #7.3, 20
    return S
    
if TIL == True:                 # Vicky and Flacké
    TIL_top = .2#ptrop-.05#.2
    TIL_max = ptrop#.25
    TIL_bot = .3#ptrop+.05#.3
    j_TIL_top = int((pt-TIL_top)/dp)#np.argwhere(p >= TIL_top)[0,0]
    j_TIL_max = int((pt-TIL_max)/dp)#np.argwhere(p >= TIL_max)[0,0]
    j_TIL_bot = int((pt-TIL_bot)/dp)#np.argwhere(p >= TIL_bot)[0,0]
    #for j in range(jtrop):
    #    S[j] = assymptotic(j)
    S_TIL = 6
    TIL_step = True
    if TIL_step == False:
        for j in range(j_TIL_top,j_TIL_max):
            S[j] = S[0]+(S_TIL-S[0])*(p[j]-p[j_TIL_top])/(p[j_TIL_max]-p[j_TIL_top])
        for j in range(j_TIL_max,j_TIL_bot):
            S[j] = (S_TIL)*(1-(S_TIL-1)/S_TIL*(p[j]-p[j_TIL_max])/(p[j_TIL_bot]-p[j_TIL_max]))
    if TIL_step == True:
        for j in range(j_TIL_top,j_TIL_bot):
            S[j] = S_TIL
    #S[j_TIL_top] = (S[j_TIL_top-1]+S[j_TIL_top+1])/2
    #S[j_TIL_max] = (S[j_TIL_max-1]+S[j_TIL_max+1])/2
    #S[jtrop] = (S[jtrop-1]+S[jtrop+1])/2
    #S[j_TIL_bot] = (S[j_TIL_bot-1]+S[j_TIL_bot+1])/2


# -----------------------------------------------------------------------------

### define vertical wind shear lambda and zonal wind u
lambda_steps = False
lamstrat_steps = True
three_steps = False
five_steps = False

lambda1	= np.ones(nrws)*3.5		# zonal wind shear			Mak1994
#lambda1 = np.ones(nrws)*5		# zonal wind shear			Mak1998

u = np.zeros(nrws)
for j in range(nrws):
    u[j] = lambda1[j]*(ps-p[j])			# zonal wind			Mak1994
#    u[j] = .4+lambda1[j]*(ps-p[j])		# zonal wind			Mak1998


# inclusion of stratosphere

if stratos == True:			# wind shear in stratosphere		Flacké
    for j in range(jtrop):
        lambda1[j] = -3.5#2.0762711864406773
    lambda1[jtrop] = (lambda1[jtrop-1]+lambda1[jtrop+1])/2
    
    u[jtrop] = lambda1[jtrop+1]*(ps-ptrop) # to make sure that the averaging of the discontinuous lambda at the tropopause doesn't mess up the zonal wind
    for j in range(jtrop):
        u[j] = u[jtrop]+lambda1[j]*(ptrop-p[j])	# zonal wind in stratosphere	Flacké
       
    
    if smoothshearstrat == False and three_steps == True or five_steps == True:
        delrange = 20 #10
        fac1 = 2/3#1/5 #1/3
        fac2 = 1/3#4/5 #2/3
        fac3 = 3/5
        fac4 = 2/5
        if lambda_steps == True:
            print ('defining lambda as multiple step function')
            for j in range(jtrop-delrange,jtrop):
                lambda1[j] = (lambda1[0]*fac1+lambda1[jtrop]*fac2)
                #lambda1[j] = (lambda1[-1])
                #lambda1[j] = (lambda1[0]-1/3*(-lambda1[0]+lambda1[-1]))
            lambda1[jtrop-delrange] = (lambda1[0]+lambda1[jtrop-delrange+1])/2
            for j in range(jtrop+1,jtrop+delrange):
                lambda1[j] = (lambda1[-1]*fac1+lambda1[jtrop]*fac2)
                #lambda1[j] = (lambda1[0])
                #lambda1[j] = (lambda1[0]+1/3*(-lambda1[0]+lambda1[-1]))
            lambda1[jtrop+delrange] = (lambda1[-1]+lambda1[jtrop+delrange-1])/2
            lambda1[jtrop] = (lambda1[jtrop-1]+lambda1[jtrop+1])/2
            if five_steps == True:
                for j in range(jtrop-2*delrange,jtrop-delrange):
                    lambda1[j] = (lambda1[0]*fac3+lambda1[jtrop]*fac4)
                lambda1[jtrop-2*delrange] = (lambda1[0]+lambda1[jtrop-2*delrange+1])/2
                for j in range(jtrop+delrange+1,jtrop+2*delrange):
                    lambda1[j] = (lambda1[-1]*fac3+lambda1[jtrop]*fac4)
                lambda1[jtrop+2*delrange] = (lambda1[-1]+lambda1[jtrop+2*delrange-1])/2

        if lamstrat_steps == True:
            print ('defining lambda/S as multiple step function')        
            lamstrat = np.array(lambda1/S)
            lamstrat[jtrop] = (lamstrat[0]+lamstrat[-1])/2
            for j in range(jtrop-delrange,jtrop):
                lamstrat[j] = (lamstrat[0]*fac1+lamstrat[jtrop]*fac2)
                #lamstrat[j] = (lamstrat[-1])
                #lamstrat[j] = (lamstrat[0]-1/3*(-lamstrat[0]+lamstrat[-1]))
            lamstrat[jtrop-delrange] = (lamstrat[0]+lamstrat[jtrop-delrange+1])/2
            for j in range(jtrop+1,jtrop+delrange):
                lamstrat[j] = (lamstrat[-1]*fac1+lamstrat[jtrop]*fac2)
                #lamstrat[j] = (lamstrat[0])
                #lamstrat[j] = (lamstrat[0]+1/3*(-lamstrat[0]+lamstrat[-1]))
            lamstrat[jtrop+delrange] = (lamstrat[-1]+lamstrat[jtrop+delrange-1])/2
            lamstrat[jtrop] = (lamstrat[jtrop-1]+lamstrat[jtrop+1])/2
            if five_steps == True:
                for j in range(jtrop-2*delrange,jtrop-delrange):
                    lamstrat[j] = (lamstrat[0]*fac3+lamstrat[jtrop]*fac4)
                lamstrat[jtrop-2*delrange] = (lamstrat[0]+lamstrat[jtrop-2*delrange+1])/2
                for j in range(jtrop+delrange+1,jtrop+2*delrange):
                    lamstrat[j] = (lamstrat[-1]*fac3+lamstrat[jtrop]*fac4)
                lamstrat[jtrop+2*delrange] = (lamstrat[-1]+lamstrat[jtrop+2*delrange-1])/2
            
            # distribute lambda/S relatively equally for S and lambda:
            delS = S_disc[-2]-S_disc[1]
            dellam = lambda1_disc[-2]-lambda1_disc[1]
            fac = -(lambda1_disc[1]-S_disc[1]*lamstrat)/((dellam-delS*lamstrat))
            if lambda1[1] != lambda1[-2] and S[1] != S[-2]:
                S[1:nrws-1] = S_disc[1] + delS*fac[1:nrws-1]
                #S[nrws+1:-1] = S[1:nrws-1]
                lambda1[1:nrws-1] = lambda1_disc[1] + dellam*fac[1:nrws-1]
                #lambda1[nrws+1:-1] = lambda1[1:nrws-1]
            elif lambda1[1] == lambda1[-2] or S[1] == S[-2]:
                if smooth_Sinv == True:
                    S[1:nrws-1] = 1/smooth(1/S_disc[1:nrws-1],smoothfac)
                else:
                    S[1:nrws-1] = smooth(S_disc[1:-1],smoothfac)
                #S[nrws+1:-1] = S[1:nrws-1]
                lambda1[1:nrws-1] = smooth(lambda1_disc[1:-1],smoothfac)
                #lambda1[nrws+1:-1] = lambda1[1:nrws-1]

        for j in range(1,nrws):
            u[j] = u[j-1]+(lambda1[j]+lambda1[j-1])/2*(p[j-1]-p[j])
#        u[:nrws] = u[:nrws] - ((u-u_disc)[nrws-1]/2)


#lamstrat = np.array(lambda1/S)
#lamstrat[:jtrop] = -0.6124999999999999
#lamstrat[jtrop] = (lamstrat[0]+lamstrat[-1])/2
#lambda1 = lamstrat
#for j in range(1,nrws):
#    u[j] = u[j-1]+(lambda1[j]+lambda1[j-1])/2*(p[j-1]-p[j])
      
# -----------------------------------------------------------------------------

### smoothing

# save discontinuous profiles before smoothing
S_disc = np.array(S[:nrws])
u_disc = np.array(u[:nrws])
lambda1_disc = np.array(lambda1[:nrws])
lamstrat_disc = np.array(lambda1[:nrws]/S[:nrws])

def smooth(S, N):         # smooth tropopause N times     Vicky
    for iteration in range(N):
        s_new = S.copy()
        s_new[1:-1] += 0.25*(S[:-2] - 2*S[1:-1] + S[2:])
        S = s_new 
    return S

def smooth_sine(lamstrat):
    global ptrop_range, sm_scale, noncons
    ptrop_range = 10 #default 10, *15* or 20 depending on vertical resolution
    amp = lambda1[-1]/S[-1]
    noncons = False
    if noncons == False:
        sm_scale = 1.*(lambda1[0]/S[0])/(lambda1[-1]/S[-1])
    else:
        sm_scale = .7*(lambda1[0]/S[0])/(lambda1[-1]/S[-1])
        
    for i in range(jtrop-ptrop_range):
        lamstrat[i] = sm_scale*amp
    for i in range(2*ptrop_range+1):
        lamstrat[jtrop-ptrop_range+i] = (1+sm_scale)/2*amp+(1-sm_scale)/2*amp*np.sin(np.linspace(-np.pi/2,np.pi/2,2*ptrop_range+1)[i])#-np.pi/2,np.pi/2,50)
    lamstrat_old = np.array(lamstrat)
    if TIL == True:
        lamstrat[:jtrop] = np.array([np.mean(x) for x in zip(lamstrat[:jtrop],np.ones(jtrop)*sm_scale*amp)]) # ensures that nonconservative step function is used
        lamstrat[jtrop:] = np.array([np.mean(x) for x in zip(lamstrat[jtrop:],lamstrat_disc[jtrop:])])
#    lamstrat[:jtrop] = lamstrat[:jtrop] + lamstrat_disc[:jtrop] - lamstrat_disc[0]
#    lamstrat[jtrop:] = lamstrat[jtrop:] + lamstrat_disc[jtrop:] - lamstrat_disc[-1]
    if lamstrat[jtrop] > 0:
        lamstrat_new = np.array(lamstrat)
        if lambda1[0] <= -10000:
            while lamstrat_new[jtrop] < -10000:
                for i in range(nrws-1):
                    lamstrat_new[i+1] = lamstrat[i]
                lamstrat = np.array(lamstrat_new)    
    return lamstrat_old, lamstrat

# smooth S only

if stratos == True and TIL == False and smoothstrat == True and smoothshearstrat == False:         # Vicky
    if smooth_Sinv == False:
        S = smooth(S, smoothfac)
    if smooth_Sinv == True:
        S = 1/smooth(1/S, smoothfac)
          
# analytic expression for smooth S
Sinv_ana = np.array(1/S)
if smoothstrat == True:
    delta = 0.17
    c1 = -1/4*(1/S[-1]-1/S[0])/(int(delta/dp)*dp)**3
    c2 =  3/4*(1/S[-1]-1/S[0])/(int(delta/dp)*dp)**2
    for n in range(jtrop+int(delta/dp),jtrop-int(delta/dp)):
        Sinv_ana[n] = 1/S[0] + c1*(p[n]-(ptrop-delta))**3. + c2*(p[n]-(ptrop-delta))**2.

          
# smooth lambda only
     
if stratos == True and smoothshear == True and smoothshearstrat == False:     # Vicky
    lambda1 = smooth(lambda1,smoothfac)

# analytic expression for smooth lambda
lambda1_ana = np.array(lambda1)

if smoothshear == True:
    delta = 0.17
    c1 = -1/4*(lambda1[-2]-lambda1[1])/(int(delta/dp)*dp)**3
    c2 =  3/4*(lambda1[-2]-lambda1[1])/(int(delta/dp)*dp)**2
    for n in range(jtrop+int(delta/dp),jtrop-int(delta/dp)):
        lambda1_ana[n] = lambda1[0] + c1*(p[n]-(ptrop-delta))**3. + c2*(p[n]-(ptrop-delta))**2.

          
# smooth lambda/S
lamstrat = np.array(lamstrat_disc[:nrws])

if smoothshearstrat == True:# and smoothshear == False and smoothstrat == False:
    if smoothsine == False:
        lamstrat[1:-1] = smooth(lamstrat_disc[1:-1],smoothfac)
        
        # distribute lambda/S relatively equally for S and lambda:
        delS = S_disc[-2]-S_disc[1]
        dellam = lambda1_disc[-2]-lambda1_disc[1]
        fac = -(lambda1_disc[1]-S_disc[1]*lamstrat)/((dellam-delS*lamstrat))
        if lambda1[1] != lambda1[-2] and S[1] != S[-2]:
            S[1:nrws-1] = S_disc[1] + delS*fac[1:nrws-1]
            #S[nrws+1:-1] = S[1:nrws-1]
            lambda1[1:nrws-1] = lambda1_disc[1] + dellam*fac[1:nrws-1]
            #lambda1[nrws+1:-1] = lambda1[1:nrws-1]
        elif lambda1[1] == lambda1[-2] or S[1] == S[-2]:
            if smooth_Sinv == True:
                S[1:nrws-1] = 1/smooth(1/S_disc[1:nrws-1],smoothfac)
            else:
                S[1:nrws-1] = smooth(S_disc[1:-1],smoothfac)
            #S[nrws+1:-1] = S[1:nrws-1]
            lambda1[1:nrws-1] = smooth(lambda1_disc[1:-1],smoothfac)
            #lambda1[nrws+1:-1] = lambda1[1:nrws-1]

    if smoothsine == True:
        lamstrat_old, lamstrat = smooth_sine(lamstrat)
        
        # distribute lambda/S relatively equally for S and lambda:
        delS = S_disc[-2]-S_disc[1]
        dellam = lambda1_disc[-2]-lambda1_disc[1]
        fac = -(lambda1_disc[1]-S_disc[1]*lamstrat)/((dellam-delS*lamstrat))
        fac_old = -(lambda1_disc[1]-S_disc[1]*lamstrat_old)/((dellam-delS*lamstrat_old))
        # or distributing lambda/S relatively equally for 1/S and lambda (where Sinv = 1/S_disc[1] + (1/S_disc[-2]-1/S_disc[1])*facinv)
        #delSinv = 1/S_disc[-2]-1/S_disc[1] 
        #a = 1
        #b = (dellam*1/S_disc[1]+lambda1[1]*delSinv)/(dellam*delSinv)
        #c = (lambda1[1]/S[1]-lamstrat)/(dellam*delSinv)
        #c_old = (lambda1[1]/S[1]-lamstrat_old)/(dellam*delSinv)
        #facinv_p = (-b+np.sqrt(b**2-4*a*c))/(2*a)
        #facinv_n = (-b-np.sqrt(b**2-4*a*c))/(2*a)
        #facinv = np.zeros(nrws)
        #facinv_p_old = (-b+np.sqrt(b**2-4*a*c_old))/(2*a)
        #facinv_n_old = (-b-np.sqrt(b**2-4*a*c_old))/(2*a)
        #facinv_old = np.zeros(nrws)
        #for i in range(nrws):
        #    if facinv_p[i] != 0 and facinv_n[i] != 0:
        #        facinv[i] = np.max([facinv_p[i], facinv_n[i]])
        #        facinv_old[i] = np.max([facinv_p_old[i], facinv_n_old[i]])
        S_old = np.array(S_disc)
        lambda1_old = np.array(lambda1_disc)

        if lambda1[1] != lambda1[-2] and S[1] != S[-2]:
            S = S_disc[1] + delS*fac
            S_old = S_disc[1] + delS*fac_old
            #Sinv = 1/S_disc[1] + delSinv*facinv
            #Sinv_old = 1/S_disc[1] + delSinv*facinv_old
            #S = 1/Sinv
            #S_old = 1/Sinv_old
            lambda1 = lambda1_disc[1] + dellam*fac
            #lambda1 = lambda1_disc[1] + dellam*facinv
            lambda1_old = lambda1_disc[1] + dellam*fac_old
            #lambda1_old = lambda1_disc[1] + dellam*facinv_old
        elif lambda1[1] == lambda1[-2] and S[1] != S[-2]:
            S[:nrws] = lambda1/lamstrat
            S_old = lambda1/lamstrat_old
        elif lambda1[1] != lambda1[-2] and S[1] == S[-2]:
            lambda1 = lamstrat/S
            lambda1_old = lamstrat_old/S

        
        
# -----------------------------------------------------------------------------

# recalculate zonal wind based on smooth lambda profile
if stratos == True and smoothshear == True or smoothshearstrat == True:
    for j in range(1,nrws):
        u[-j-1] = u[-j]-(lambda1[nrws-j]+lambda1[nrws-j-1])/2*(p[-j-1]-p[-j])
#        u[j] = u[j-1]+(lambda1[j]+lambda1[j-1])/2*(p[j-1]-p[j])
#    u[:nrws] = u[:nrws] - ((u-u_disc)[nrws-1]/2)
    #u[nrws:] = u[:nrws]    
    if smoothsine == True:
        u_old = np.zeros(nrws)
        for j in range(1,nrws):
            u_old[-j-1] = u_old[-j]-(lambda1_old[-j]+lambda1_old[-j-1])/2*(p[-j-1]-p[-j])


# -----------------------------------------------------------------------------

# design schafler profiles (Fig. 9a in Schafler et al. 2020) from skewed normal distribution
schafler = False

if smoothshearstrat == True and schafler == True:
    skew = -2 #3])
    loc = ptrop #ptrop-.1
    scale = .1 #.2
    weight = .05 #.05
    u = u[:nrws]-weight*skewnorm.pdf(p[:nrws], skew, loc, scale)
    
    lambda1[1:nrws-1] = -(u[:nrws-2]-u[2:nrws])/(2*dp)
    lambda1[0] = -(u[0]-u[1])/(dp)
    lambda1[nrws-1] = -(u[nrws-2]-u[nrws-1])/(dp)


# -----------------------------------------------------------------------------

# find derivatives: dldp, dSdp, ddpS based on profiles of lambda and S

# calculate derivative of wind shear throughout domain          
dldp = np.zeros(nrws)     # Vicky
dldp[2:-2] = (lambda1[1:nrws-3]-lambda1[3:nrws-1])/(2*dp)
dldp[0] = -lambda1[0]/dp
dldp[-1] = lambda1[nrws-1]/dp
if stratos == True and smoothshearstrat == False and smoothshear == False:
    dldp[jtrop-1] = 0
    dldp[jtrop+1] = 0
    
# calculate derivative of stratification throughout domain          
dSdp[1:nrws-1] = ((S[:nrws-2] - S[2:nrws])/(2*dp))
if smoothshearstrat == False and smoothstrat == False:
    dSdp[jtrop-1] = 0
    dSdp[jtrop+1] = 0
ddpS[1:nrws-1] = (1/S[:nrws-2] - 1/S[2:nrws])/(2*dp)
if smoothshearstrat == False and smoothstrat == False:
    ddpS[jtrop-1] = 0
    ddpS[jtrop+1] = 0


# scaling with respect to coriolis parameter
S = S/ffac**2
dSdp = dSdp/ffac**2
ddpS = ddpS/ffac**2


# extend profiles for calculations in model core
u       = np.append(u,u)
lambda1 = np.append(lambda1,lambda1)
dldp    = np.append(dldp,dldp)
S       = np.append(S,S)
dSdp    = np.append(dSdp,dSdp)
ddpS    = np.append(ddpS,ddpS)

# -----------------------------------------------------------------------------

### calculating meridional gradient of basic-state PV
     
def calc_dqdy(S,lambda1):
    dqdy = np.zeros(nrws)
    dqdy[1:-1] = (lambda1[:nrws-2]/S[:nrws-2] - lambda1[2:nrws]/S[2:nrws])/(2*dp)
#    dqdy[2:-2] = (lamstrat[1:nrws-3] - lamstrat[3:nrws-1])/(2*dp)
#    if smoothstrat == False and smoothshear == False and smoothshearstrat == False:
#        dqdy[jtrop-1] = 0
#        dqdy[jtrop+1] = 0
    dqdy[0] = dldp[0]/S[0]/2
    dqdy[-1] = dldp[nrws-1]/S[nrws-1]/2
    return dqdy
    
dqdy = calc_dqdy(S,lambda1)
dqdy_disc = calc_dqdy(S_disc, lambda1_disc)


# -----------------------------------------------------------------------------
# definition of heating and drag profiles
# -----------------------------------------------------------------------------

### latent heating profile (Mak1994) ------------------------------------------

h = np.zeros((len(epsilon1),nrws))
h1 = np.zeros((len(epsilon1),2*nrws))
dhdp = np.zeros((len(epsilon1),nrws))
dh1dp = np.zeros((len(epsilon1),2*nrws))

hblcstep = 0
if heating1 == True:
    htlcstep = 1
    hblcstep = 1
    if evap == True:
        hblcstep = 1.1#+1/12.5
    htic = 4
    if h1pro == False:
        for e in range(len(epsilon1)):            
            for j in range(jtlc+1,jblc+1):
                h[e,j] = htlcstep
            if jtlc != 0:
                h[e,jtlc] = htlcstep/2
            if jblc != nrws-1:
                h[e,jblc] = htlcstep/2
                if (evap == True and hblcstep != 1):
                    h[e,jblc] = htlcstep-hblcstep/2
                #if (wpar == True and ptsf == pblc) and evap == False:
                 #   h[e,jblc] = htlcstep-(htlcstep+epsilon2[eps2_index]/epsilon1[eps1_index]*1)/2
            for j in range(jblc+1,nrws):
                h[e,j] = htlcstep-hblcstep
            if heating1_ice == True:
                for j in range(jtlc,jtic):
                    h[e,j] = htic
            h[e,jtlc] = (h[e,jtlc-1]+h[e,jtlc+1])/2
    if h1pro == True:		# definition of different smooth, modified heating profiles
        pd  = .1		# delta p, describes sharpness of curve
        jd = int(-pd/dp)
        pd = -jd*dp
        pd2 = pd*2.5		# delta p, describes sharpness of curve at lower levels
        jd2 = int(-pd2/dp)
        pd2 = -jd2*dp
        cblift = True		# uses a different level for the bottom of the heating layer
        if cblift == True:
            pblc2 = ps-pd2
            jblc2 = np.argwhere(p >= pblc2)[0][0]
            pblc2 = p[jblc2]
        fac = 1.8#(ps-pb)/(pb-pm)*1.5		# amplitude of the heating profile
        if h1proa == True and h1prob == False:
            for e in range(len(epsilon1)):
                for j in range(jtlc-jd,jtlc+jd):
                    h[e,j] = fac*(np.sin(np.pi*(p[j]-(p[jtlc]-pd))/(2*((p[jtlc]+pd)-(p[jtlc]-pd)))))**2.
                    dhdp[e,j] = fac*2*np.pi/(2*(p[jtlc]+pd)-(p[jtlc]-pd))*np.sin(np.pi*(p[j]-(p[jtlc]-pd))/(2*((p[jtlc]+pd)-(p[jtlc]-pd))))*np.cos(np.pi*(p[j]-(p[jtlc]-pd))/(2*((p[jtlc]+pd)-(p[jtlc]-pd))))
                for j in range(jtlc+jd,jblc-jd2):
                    h[e,j] = fac
                if cblift == False:
                    for j in range(jblc-jd2,jbd+1):
                        h[e,j] = (np.sin(np.pi*((p[jblc]+pd2-p[j])/(2*((p[jblc]+pd2)-(p[jblc]-pd2))))))**2.
                        dhdp[e,j] = -2*np.pi/(2*((p[jblc]+pd2)-(p[jblc]-pd2)))*np.sin(np.pi*((p[jblc]+pd2-p[j])/(2*((p[jblc]+pd2)-(p[jblc]-pd2)))))*np.cos(np.pi*((p[jblc]+pd2-p[j])/(2*((p[jblc]+pd2)-(p[jblc]-pd2)))))
                if cblift == True:
                    for j in range(jblc2-jd2,jblc2+jd2+1):
                        h[e,j] = fac*(np.sin(np.pi*((p[j]-(p[jblc2]+pd2))/(2*((p[jblc2]+pd2)-(p[jblc2]-pd2))))))**2.
                        dhdp[e,j] = -fac*2*np.pi/(2*((p[jblc2]+pd2)-(p[jblc2]-pd2)))*np.sin(np.pi*((p[jblc2]+pd2-p[j])/(2*((p[jblc2]+pd2)-(p[jblc2]-pd2)))))*np.cos(np.pi*((p[jblc2]+pd2-p[j])/(2*((p[jblc2]+pd2)-(p[jblc2]-pd2)))))
        if h1prob == True or h1proc == True or h1prod == True and h1proa == False:
            if h1prob == True:
                for e in range(len(epsilon1)):      
                    for i in range(jtu,jtd):
                        h[e,i]=1/fac*(np.sin(np.pi/(2*(ptd-ptu))*(p[i]-ptu)))**2
                        dhdp[e,i]=1/fac*np.pi/(ptd-ptu)*np.sin(np.pi/(2*(ptd-ptu))*(p[i]-ptu))*np.cos(np.pi/(2*(ptd-ptu))*(p[i]-ptu))
                    for i in range(jtd,jbu):
                        h[e,i] = 1/fac
                        dhdp[e,i] = 0
                    for i in range(jbu,jbd):
                        h[e,i]=1/fac*(np.sin(np.pi/(2*(pbd-pbu))*(pbd-p[i])))**2
                        dhdp[e,i]=-1/fac*np.pi/(2*(pbd-pbu))*np.cos(np.pi/(2*(pbd-pbu))*(pbd-p[i]))*2*np.sin(np.pi/(2*(pbd-pbu))*(pbd-p[i]))
            if h1proc == True:
                for e in range(len(epsilon1)):      
                    for i in range(jtlc-jd,jtlc+jd):
                        h[e,i]=fac*(np.sin(np.pi*(p[i]-(ptlc-pd))/(2*((ptlc+pd)-(ptlc-pd)))))**2
                        dhdp[e,i]=fac*2*np.pi/(2*(p[jtlc]+pd)-(p[jtlc]-pd))*np.sin(np.pi*(p[i]-(p[jtlc]-pd))/(2*((p[jtlc]+pd)-(p[jtlc]-pd))))*np.cos(np.pi*(p[i]-(p[jtlc]-pd))/(2*((p[jtlc]+pd)-(p[jtlc]-pd))))
                    for i in range(jtlc+jd,jblc-jd2):
                        h[e,i] = fac
                        dhdp[e,i] = 0
                    for i in range(nrws-2*jd2,nrws):
                        h[e,i]=fac*np.sin(np.pi*(p[i]-p[jblc])/(2*(p[nrws-2*jd2]-p[jblc])))
                        dhdp[e,i]=fac*np.cos(np.pi*(p[jblc]-ps)*(p[i]-p[jblc])/(2*(p[nrws-2*jd2]-p[jblc])*(p[jblc]-ps)))*np.pi*(p[jblc]-ps)/(2*(p[nrws-2*jd2]-p[jblc])*(p[jblc]-ps))                       
            if h1prod == True:
                pbuu = .9
                pbdd = (pbd+pb)/2
                jbuu = np.argwhere(p >= pbuu)[0][0]
                jbdd = np.argwhere(p >= pbdd)[0][0]
                fac2 = (ps-pbd)/(pbd-pbu)
                for e in range(len(epsilon1)):      
                    for i in range(jtu,jtd):
                        h[e,i]=1/fac*(np.sin(np.pi/(2*(ptd-ptu))*(p[i]-ptu)))**2
                        dhdp[e,i]=1/fac*np.pi/(ptd-ptu)*np.sin(np.pi/(2*(ptd-ptu))*(p[i]-ptu))*np.cos(np.pi/(2*(ptd-ptu))*(p[i]-ptu))
                    for i in range(jtd,jbu):
                        h[e,i] = 1/fac
                        dhdp[e,i] = 0
                    for i in range(jbu,jbuu):
                        h[e,i]=1/fac*(np.sin(np.pi/(2*(pbuu-pbu))*(pbuu-p[i])))**2
                        dhdp[e,i]=-1/fac*np.pi/(2*(pbuu-pbu))*np.cos(np.pi/(2*(pbuu-pbu))*(pbuu-p[i]))*2*np.sin(np.pi/(2*(pbuu-pbu))*(pbd-p[i]))
                    for i in range(jbuu,jbdd):
                        h[e,i]=0
                        dhdp[e,i]=0
                    for i in range(jbdd,nrws):
                        h[e,i]=-fac2/fac*(np.sin(np.pi/(2*(p[-1]-pbdd))*(pbdd-p[i])))**2
                        dhdp[e,i]=fac2/fac*np.pi/(2*(ps-pbdd))*np.cos(np.pi/(2*(p[-1]-pbdd))*(pbdd-p[i]))*2*np.sin(np.pi/(2*(p[-1]-pbdd))*(pbdd-p[i]))
    for e in range(len(epsilon1)):
        h1[e] = np.append(h[e],h[e])
        dh1dp[e] = np.append(dhdp[e],dhdp[e])

            
### heating profile for surface fluxes (Mak1998) -------------------------------------

h = np.zeros((len(epsilon2),nrws))
h2 = np.zeros((len(epsilon2),2*nrws))
dhdp = np.zeros((len(epsilon2),nrws))
dh2dp = np.zeros((len(epsilon2),2*nrws))

delta = .05
H = (1-ptsf)/(delta*(2-np.exp((ptbl-ptsf)/delta)-np.exp((ptsf-1)/delta)))

if heating2 == True:
    for e in range(len(epsilon2)):
        if h2pro == False:
            h2step = 1.
            for j in range(jtsf, nrws):
                h[e,j] = h2step
            h[e,jtsf] = h2step/2
        if h2pro == True:
            for j in range(jtbl,jtsf):
                h[e,j] = H*np.exp((p[j]-ptsf)/delta)
                dhdp[e,j] = H/delta*np.exp((p[j]-ptsf)/delta)
            for j in range(jtsf, nrws):
                h[e,j] = H*np.exp((ptsf-p[j])/delta)         
                dhdp[e,j] = -H/delta*np.exp((ptsf-p[j])/delta) 
            h[e,jtsf] = H#NaN#h[e,jtsf-1]
            dhdp[e,jtsf] = NaN
        h2[e]=np.append(h[e],h[e])
        dh2dp[e]=np.append(dhdp[e],dhdp[e])
        

### inclusion of drag/rayleigh friction (Flacké) ------------------------------------

h3 = np.zeros((nrws))
#dh3dp = np.zeros((2*nrws))
        
if drag == True:
    for j in range(jtdl):
        h3[j] = 0
    for j in range(jtdl,nrws):
        h3[j] = 1
h3[jtdl] = (h3[jtdl+1]+h3[jtdl-1])/2
h3 = np.append(h3,h3)


### saving different heating profiles for comparison ------------------------------------

if heating1 == True and h1pro == False and evap == False:
    htemp1 = h1
if heating1 == True and h1pro == False and evap == True and hblcstep == 1.3:
    htemp2 = h1
if heating1 == True and h1pro == False and evap == True and hblcstep == 1.5:
    htemp3 = h1
if heating1 == True and h1pro == True and h1proc == True:
    htemp4 = h1
if heating1 == True and h1pro == True and h1prod == True:
    htemp5 = h1
if heating1 == True and h1pro == True and h1proa == True:
    htemp6 = h1

# -----------------------------------------------------------------------------

def check_wind_and_heating():

    global S_ref
    
    ymin = 0#.1 #0
    ymax = 1#.4 #1

    # -----------------------------------------------------------------------------
    # checking if different profiles are defined correctly
    # -----------------------------------------------------------------------------

    mpl.rc('font',size=12)
    fig, (ax0,ax1,ax2,ax3) = plt.subplots(1,4, figsize=(10,5))

    ### plot zonal wind -----------------------------------------------------------
        
    ax0b = ax0.twiny()
    ax0.axhline(ptrop,c='y')
#    ax0c = ax0.twiny()
    ax0.plot(u[:nrws],p[:nrws], c=c[1])
    ax0b.plot(lambda1[:nrws],p[:nrws], c=c[1],ls='--')
#    ax0b.plot((1/S[:nrws]-.6)*3.5/.4,p[:nrws],c='y',alpha=.7)
#    ax0b.plot(lambda1_ana[:nrws],p[nrws:], c='y', lw=3, alpha=.5)
#    ax0c = ax0.twiny()
#    ax0c.plot(dldp[1:nrws-1],p[1:nrws-1], c=c[1],ls=':')
    try:
        u_disc
    except:
        pass
    else:
        if smoothshear == True and lambda1[jtrop+1]!=lambda1[jtrop-1] or smoothshearstrat == True:
            ax0.plot(u_disc[:nrws],p[:nrws], c=c[1], alpha=.5)
            ax0b.plot(lambda1_disc[:nrws],p[:nrws], c=c[1], alpha=.5, ls='--')
    try:
        u_old
    except:
        pass
    else:
        if smoothshear == True and lambda1[jtrop+1]!=lambda1[jtrop-1] or smoothshearstrat == True:
            ax0.plot(u_old[:nrws],p[:nrws], c=c[1], alpha=.2)
            ax0b.plot(lambda1_old[:nrws],p[:nrws], c=c[1], alpha=.2, ls='--')
#    ax0c.plot(dldp[:nrws],p[:nrws], c=c[1],ls=':')
#    ax0c.spines["top"].set_position(("axes", 1.2))
    ax0b.set_ylim(ymin,ymax)
    ax0b.invert_yaxis()
    ax0b.set_ylabel('pressure')
    ax0.set_xlabel('- u -')
#    ax0c.set_xlabel('$d\lambda/dp$')
    ax0b.set_xlabel('- - $\mathregular{\lambda}$ - -')
    
    print (f'max dldp @ p = {p[np.argwhere(dldp == np.max(dldp[1:-1]))[0][0]]:.4f}')
    
    ### plot dq/dy ----------------------------------------------------------------
    
    ax1b = ax1.twiny()
    ax1.axhline(ptrop,c='y')
#    ax1b.plot(dqdy[1:nrws-1],p[1:nrws-1], c=c[5], ls='--')
    ax1b.plot(lamstrat[:nrws],p[:nrws], c=c[5], ls='--')#lambda1[:nrws]/S[:nrws],p[:nrws], c=c[5], ls='--')
    ax1b.plot(lamstrat_disc[:nrws],p[:nrws], c=c[5], alpha=.5,ls='--')
#    ax1b.plot(lambda1_ana[:nrws]*Sinv_ana[:nrws],p[nrws:], c='y', lw=3, alpha=.5)
    ax1.plot(dqdy[:nrws],p[:nrws], c=c[5])
    ax1.set_ylim(ymin,ymax)
    ax1.set_xlim(-np.max(np.abs(dqdy)),np.max(np.abs(dqdy)))
    if stratos == True or pt == .25:
        if smoothstrat == False:
            ax1.text(0, ptrop, f'{dqdy[jtrop]:1.0f} --> ', verticalalignment='center', horizontalalignment='right')
        else:
            ax1.text(0, p[np.argwhere(dqdy[1:-1]==np.max(dqdy[1:-1]))[0][0]], f'{dqdy[np.argwhere(dqdy[1:-1]==np.max(dqdy[1:-1]))[0][0]]:1.0f} --> ', verticalalignment='center', horizontalalignment='right')
    try:
        dqdy_disc
    except:
        pass
    else:
        if stratos == True and smoothshear == True or smoothstrat == True or smoothshearstrat == True:
            ax1.plot(dqdy_disc[:nrws],p[:nrws], c=c[5], alpha=.5)
            ax1.text(np.max(np.abs(dqdy)), ptrop, f'{dqdy_disc[jtrop]:1.0f}', verticalalignment='center', horizontalalignment='right', alpha=.5)
    if pt == 0:
        ax1.text(0, .05, f'{dqdy[0]:1.0f} ', verticalalignment='center', horizontalalignment='right')    
    ax1.text(0, .95, f'{dqdy[-1]:1.0f} ', verticalalignment='center', horizontalalignment='right')    
    ax1.invert_yaxis()
    ax1.set_ylabel('pressure')
    ax1.set_xlabel('- dq/dy -')
    ax1b.set_xlabel('- - $\mathregular{\lambda}$/S - -')
    ax1b.set_xlim(-1.1*np.max(lamstrat),1.1*np.max(lamstrat))
    
    print (f'max dqdy @ p = {p[np.argwhere(dqdy == np.max(dqdy[1:-1]))[0][0]]:.4f}')

    ### plot stratification -------------------------------------------------------

    if TIL == True and smoothstrat == False:
        S_ref = S

    ax2b = ax2.twiny()
    ax2.axhline(ptrop,c='y')
    ax2.plot(S[:nrws],p[nrws:], c='k')
#    ax2b.plot(Sinv_ana[:nrws],p[nrws:], c='y', lw=3, alpha=.5)
#    ax2c = ax2.twiny()
#    ax2.plot(ddpS[1:nrws-1],p[1:nrws-1], c='k', ls=':')
    try:
        S_ref1
    except:
        pass
    else:
        ax2.plot(S_ref[:nrws],p[nrws:], c='k',ls=':')
    ax2b.plot(1/S[:nrws],p[nrws:], c='k',ls='--')
    try:
        S_disc
    except:
        pass
    else:
        if smoothstrat == True or smoothshearstrat == True:
            ax2.plot(S_disc[:nrws],p[nrws:], c='k', alpha=.5)
            ax2b.plot(1/S_disc[:nrws],p[nrws:], c='k',alpha=.5,ls='--')
    try:
        S_old
    except:
        pass
    else:
        if smoothstrat == True or smoothshearstrat == True:
            ax2.plot(S_old,p[nrws:], c='k', alpha=.2)
            ax2b.plot(1/S_old,p[nrws:], c='k',alpha=.2,ls='--')
    #ax2.plot(dSdp[:nrws],p[nrws:], 'b.', markersize=4)
    ax2.set_ylim(ymin,ymax)
    ax2.invert_yaxis()
    ax2.set_ylabel('pressure')
    ax2.set_xlabel('- S -')
    ax2b.set_xlabel('- - 1/S - -')

    print (f' max ddpS @ p = {p[np.argwhere(ddpS == np.max(ddpS[1:-1]))[0][0]]:.4f}')

    ### plot heating- and drag profiles ------------------------------

    ax3.plot(h1[eps1_index,2:nrws],p[2:nrws], c=c[2], linewidth=ms-1.5,label='original heating profile, no lc')
    if heating1 == True or evap == True:
        try:
            htemp11
        except NameError:
            print ('htemp1 not defined')
        else:
            ax3.plot(htemp1[eps1_index,2:nrws],p[2:nrws], c=c_blues[0], linewidth=ms-1.5,label='original heating profile, no evap')
        try:
            htemp61
        except NameError:
            pass
        else:
            ax3.plot(htemp6[eps1_index,2:nrws]*p[2:nrws],p[2:nrws], c=c[2],dashes=(ms+8,ms+8), linewidth=ms-1.5,label='modified profile I')
        #ax3.plot(h1[eps1_index,nrws:]*p[:nrws],p[:nrws], 'b', label='heating profile (real)')
        #ax3.plot(dh1dp[eps1_index,:nrws],p[:nrws], 'g--', markersize=4, label='derivative of diabatic heating profile')
    if heating2 == True:
        ax3.plot(h2[eps2_index,nrws:],p[:nrws], c=c[2], label='surface fluxes')
    if drag == True:
        ax3.plot(h3[nrws:],p[:nrws], 'y', label='drag')
#    ax3.plot(lambda1[:nrws]-(1/S[:nrws]-.6)*3.5/.4, p[:nrws])
    ax3.set_ylim(ymin,ymax)
    ax3.invert_yaxis()
    ax3.set_ylabel('pressure')
    ax3.set_xlabel('heating')

    plt.tight_layout()
    
    
    ### profiles shown together ----------------------------------------------

    combined_profiles = False

    if combined_profiles == True:
        mpl.rc('font',size=22)  

        fig = plt.subplots(figsize=(8,8))
        lw=3
        gca().axvline(0,color='k',linewidth=lw/2)
        gca().axhline(ptrop,color='k',linewidth=lw/2)
        plt.plot(lamstrat[:nrws],p[:nrws],c='k',ls='--',lw=lw)
        plt.plot(lambda1[:nrws],p[:nrws],c=c_greys[0],ls='--',lw=lw)
        plt.plot(S[:nrws],p[:nrws],c=(111/255,145/255,111/255),ls='--',lw=lw)
        plt.plot(lamstrat_disc[:nrws],p[:nrws],c='k',lw=lw,label='$\lambda/N^2$')
        plt.plot(lambda1_disc[:nrws],p[:nrws],c=c_greys[0],lw=lw,label='$\lambda$')
        plt.plot(S_disc[:nrws],p[:nrws],c=(111/255,145/255,111/255),lw=lw,label='$N^2$')
        plt.ylabel('pressure (hPa)')
        plt.xlabel('nondimensional profiles')
        plt.ylim(0,1)
        plt.xlim(-4.1,4.1)
        plt.yticks([0,.25,1])
        gca().set_yticklabels(['0','250','1000'])
        gca().invert_yaxis()
        plt.legend()

    ### profiles shown in z-coordinates ----------------------------------------------
    # for comparison to heating distributions in case studies

    zprof = False

    if zprof == True:

        fig = plt.subplots(figsize=(7,5))
    
        R = 287
        Tref = 273
        g = 10

        if heating1 == True:
            try:
                htemp1
            except NameError:
                print ('htemp1 not defined')
            else:
                plt.plot(htemp1[eps1_index,2:nrws]*p[2:nrws],-R*Tref/g*np.log(p[2:nrws]), c=c_blues[0], linewidth=ms-1.5, label='original heating profile, no evap')
            try:
                htemp6
            except NameError:
                pass
            else:
                plt.plot(htemp6[eps1_index,2:nrws]*p[2:nrws],-R*Tref/g*np.log(p[2:nrws]), c=c[2],dashes=(ms+8,ms+8), linewidth=ms-1.5, label='modified profile I')
            #plt.plot(h1[eps1_index,nrws:]*p[:nrws],p[:nrws], 'b', label='diabatic heating profile (real)')
        if heating2 == True:
            plt.plot(h2[eps2_index,nrws:]*p[:nrws],-R*Tref/g*np.log(p[:nrws]), c=c[2], label='surface fluxes')
        #plt.plot(S[:nrws],p[nrws:], c=c[3], label='stratification')
        if drag == True:
            plt.plot(h3[nrws:],p[:nrws], 'y', label='drag')
        #plt.plot(h[eps1_index,:nrws]/S[:nrws],p[nrws:], 'g')
        #plt.plot(u_test[:nrws],-R*Tref/g*np.log(p[:nrws]), c=c_blues[0], alpha=.5)
        plt.plot(u[:nrws],-R*Tref/g*np.log(p[:nrws]), c=c_blues[0], label='zonal wind')
        plt.ylabel('z')
        plt.axhline(-R*Tref/g*np.log(ptrop), c='y')
        plt.xticks([0,1,2,3])
        gca().set_xticklabels(['0','10','20','30'])
        #plt.ylim(0,25000)
        plt.ylim(-R*Tref/g*np.log(ptrop)-2750,-R*Tref/g*np.log(ptrop)+2250)
        plt.xlim(2.,2.8)
        plt.grid()

    plt.show()

# -----------------------------------------------------------------------------

def show_vertical_profiles():

    global lamstrat_vec, dqdy_vec, lambda_vec, S_vec
    
    try:
        lamstrat_vec
    except:
        lamstrat_vec = np.zeros((5,nrws))
        dqdy_vec = np.zeros((5,nrws))
        lambda_vec = np.zeros((5,nrws))
        S_vec = np.zeros((5,nrws))

    if stratos == True and smoothshearstrat == False:
        lamstrat_vec[0]=lamstrat[:nrws]
        dqdy_vec[0]=dqdy
        lambda_vec[0]=lambda1_disc[:nrws]
        S_vec[0]=S_disc[:nrws]
    if stratos == True and smoothshearstrat == True and ptrop_range == 15 and ptrop < .26 and noncons == False:
        lamstrat_vec[1]=lamstrat
        dqdy_vec[1]=dqdy
        lambda_vec[1]=lambda1[:nrws]
        S_vec[1]=S[:nrws]
    if stratos == True and smoothshearstrat == True and ptrop_range == 10 and ptrop < .26 and noncons == False:
        lamstrat_vec[2]=lamstrat
        dqdy_vec[2]=dqdy
        lambda_vec[2]=lambda1[:nrws]
        S_vec[2]=S[:nrws]
    if stratos == True and smoothshearstrat == True and ptrop_range == 15 and ptrop > .29 and noncons == False:
        lamstrat_vec[3]=lamstrat
        dqdy_vec[3]=dqdy
        lambda_vec[3]=lambda1[:nrws]
        S_vec[3]=S[:nrws]
    if stratos == True and smoothshearstrat == True and ptrop_range == 15 and ptrop < .26 and noncons == True:
        lamstrat_vec[4]=lamstrat
        dqdy_vec[4]=dqdy
        lambda_vec[4]=lambda1[:nrws]
        S_vec[4]=S[:nrws]


    mpl.rc('font',size=18)
    fig, (ax3,ax4,ax1,ax2) = plt.subplots(1,4,figsize=(16,5),dpi=300)
    plt.subplots_adjust(wspace=.05)
    #ax1 = ax.twiny()

    #ax1.axvline(0,c='k',ls='--',lw=1)
    ax1.plot(lamstrat_vec[0,:nrws],p[:nrws],c=c_greys[0],ls='-',lw=2)
    ax2.plot(-dqdy_vec[0,1:nrws-1]/dqdy_disc[-1],p[1:nrws-1],c=c_greys[0],ls='-',lw=2) 
    ax3.plot(lambda_vec[0],p[:nrws],c=c_greys[0],ls='-',lw=2)
    ax4.plot(S_vec[0],p[:nrws],c=c_greys[0],ls='-',lw=2) 
    ax1.plot(lamstrat_vec[1,:nrws],p[:nrws],c='k',ls='-',lw=2)
    ax2.plot(-dqdy_vec[1,1:nrws-1]/dqdy_disc[-1],p[1:nrws-1],c='k',lw=2)
    ax3.plot(lambda_vec[1],p[:nrws],c='k',ls='-',lw=2)
    ax4.plot(S_vec[1],p[:nrws],c='k',ls='-',lw=2)  
    ax1.plot(lamstrat_vec[2,:nrws],p[:nrws],c=c_reds[1],ls='-',lw=2)
    ax2.plot(-dqdy_vec[2,1:nrws-1]/dqdy_disc[-1],p[1:nrws-1],c=c_reds[1],lw=2) 
    ax3.plot(lambda_vec[2],p[:nrws],c=c_reds[1],ls='-',lw=2)
    ax4.plot(S_vec[2],p[:nrws],c=c_reds[1],ls='-',lw=2)
    ax1.plot(lamstrat_vec[3,:nrws],p[:nrws],c=c_blues[1],ls='-',lw=2)
    ax2.plot(-dqdy_vec[3,1:nrws-1]/dqdy_disc[-1],p[1:nrws-1],c=c_blues[1],lw=2) 
    ax3.plot(lambda_vec[3],p[:nrws],c=c_blues[1],ls='-',lw=2)
    ax4.plot(S_vec[3],p[:nrws],c=c_blues[1],ls='-',lw=2) 
    ax1.plot(lamstrat_vec[4,:nrws],p[:nrws],c='y',ls='--',lw=2)
    ax2.plot(-dqdy_vec[4,1:nrws-1]/dqdy_disc[-1],p[1:nrws-1],c='y',ls='--',lw=2)
    ax3.plot(lambda_vec[4],p[:nrws],c='y',ls='--',lw=2)
    ax4.plot(S_vec[4],p[:nrws],c='y',ls='--',lw=2)  

    ax4.plot((),(),c=c_greys[0],lw=2,label='sharp CTL')
    ax4.plot((),(),c='k',lw=2,label='smooth CTL')
    ax4.plot((),(),c=c_reds[1],lw=2,label='smooth shallow')
    ax4.plot((),(),c=c_blues[1],lw=2,label='smooth low')
    ax4.plot((),(),c='y',lw=2,ls='--',label='smooth NCONS-70')

    ax1.set_xlabel('$\\regular{\lambda/S}$ \n$\\regular{(s \; hPa \; m^{-1})}$')
    #ax1.set_xlim(-1.1*np.max(lamstrat),1.1*np.max(lamstrat))
    ax2.set_xlabel('$\\regular{-[d\overline{q}/dy] \; / \; [d\overline{q}/dy]_{surf}}$')#'$\\regular{d\overline{q}/dy}$')
    ax2.set_xlim(-.1,1.3)#np.max(np.abs(dqdy_weaksmooth)),np.max(np.abs(dqdy_weaksmooth)))
    ax2.set_xticks([0,.5,1])
    ax3.set_xlabel('$\\regular{\lambda}$ \n$\\regular{(\\times 10^{-2} \; m \; s^{-1} \; hPa^{-1})}$')
    ax4.set_xlabel('$\\regular{S}$ \n$\\regular{(\\times 10^{-2} \; m^2 \; s^{-2} \; hPa^{-2})}$')
    ax1.set_yticks([0,.2,.25,.3,.5,1])
    ax1.set_yticklabels([])
    ax1.set_ylim(0,.5)#1)
    ax1.invert_yaxis()
    ax2.set_yticks([0,.2,.25,.3,.5,1])
    ax2.set_yticklabels([])
    ax2.set_ylim(0,.5)#1)
    ax2.invert_yaxis()
    ax3.set_yticks([0,.2,.25,.3,.5,1])
    ax3.set_yticklabels([0,200,250,300,500,1000])
    ax3.set_ylim(0,.5)#1)
    ax3.invert_yaxis()
    ax3.set_ylabel('pressure (hPa)')
    ax4.set_yticks([0,.2,.25,.3,.5,1])
    ax4.set_yticklabels([])
    ax4.set_ylim(0,.5)#1)
    ax4.invert_yaxis()
    ax3.text(lambda_vec[0,jtrop],-0.01,'(a)',horizontalalignment='center',verticalalignment='bottom',fontsize=20)
    ax4.text(S_vec[0,jtrop],-0.01,'(b)',horizontalalignment='center',verticalalignment='bottom',fontsize=20)
    ax1.text(lamstrat_vec[1,jtrop],-0.01,'(c)',horizontalalignment='center',verticalalignment='bottom',fontsize=20)
    ax2.text(1.2/2,-0.01,'(d)',horizontalalignment='center',verticalalignment='bottom',fontsize=20)

    ax4.legend(ncol=5,bbox_to_anchor=(1.02, -.4),loc='center',fontsize=17.5, handletextpad=.5, columnspacing=1)

    plt.savefig(f'/home/kfl078/Downloads/smoothprofiles.pdf', transparent=True, bbox_inches='tight', pad_inches=0.1)


