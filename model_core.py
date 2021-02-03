#!/usr/bin/env python
# coding: utf-8


# **********************************************************************************
# ----------------------------------------------------------------------------------
# MODEL CORE COMPUTATION
# ----------------------------------------------------------------------------------
# **********************************************************************************

# ----------------------------------------------------------------------------------
# linear matrix equation Ax = Bsx, where s is the eigenvalue sigma
#
# representing the numerical versions of the equations in the domain
# x = [w_0, w_1, ... , w_(nrws-1), psi_0, psi_1, ... , psi_(nrws-1)]
# ----------------------------------------------------------------------------------


def define_matrix():

    global A,B

    A = np.zeros((len(epsilon1),len(epsilon2),len(k),2*nrws,2*nrws), dtype = complex)

    ### omega eq. in the interior ------------------------------------------------------

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            for i in range(len(k)):
                for j in range(1,nrws-1):
                    A[e][e2][i][j][j-1]			=  1/dp**2.
                    A[e][e2][i][j][j]			= -2/dp**2.-S[j]*k[i]**2.
                    A[e][e2][i][j][j+1]			=  1/dp**2.
                    A[e][e2][i][j][nrws+j-1]	= +k[i]**2*alpha*h3[j]/(2*dp)-1j*beta*k[i]/(2*dp)
                    A[e][e2][i][j][nrws+j]		= -1j*2*lambda1[j]*k[i]**3.
                    A[e][e2][i][j][nrws+j+1]	= -k[i]**2*alpha*h3[j]/(2*dp)+1j*beta*k[i]/(2*dp)
                    
                    if heating1 == True:
                        A[e][e2][i][j][jtml]	= A[e][e2][i][j][jtml]+epsilon1[e]*k[i]**2./2.*h1[e,j]		# mak1994
                        
                    if heating2 == True:
                        if wpar == False and vpar == False: #(linearly extrapolated derivative)
                            A[e][e2][i][j][-3]	= A[e][e2][i][j][-3]+1/2*epsilon2[e2]*k[i]**2.*h2[e2,j]/dp	# mak1998
                            A[e][e2][i][j][-2]	= A[e][e2][i][j][-2]-  2*epsilon2[e2]*k[i]**2.*h2[e2,j]/dp	# mak1998
                            A[e][e2][i][j][-1]	= A[e][e2][i][j][-1]+3/2*epsilon2[e2]*k[i]**2.*h2[e2,j]/dp	# mak1998
                        if vpar == True and wpar == False:
                            A[e][e2][i][j][-1] = A[e][e2][i][j][-1]+1j*epsilon2[e2]*k[i]**3.*h2[e2,j] # NB! sign
                        if vpar == False and wpar == True:
                            A[e][e2][i][j][jtml] = A[e][e2][i][j][jtml]-epsilon2[e2]*k[i]**2.*h2[e2,j] # removed /2
                    
                if drag == True and alpha != 0: # Aug2017
                    if i == 0:
                        print ('friction')
                    A[e][e2][i][jtdl][:]			= 0.
                    A[e][e2][i][jtdl][jtdl-2]		= 1/2/dp 
                    A[e][e2][i][jtdl][jtdl-1]		=  -2/dp 
                    A[e][e2][i][jtdl][jtdl]			=   3/dp
                    A[e][e2][i][jtdl][jtdl+1]		=  -2/dp
                    A[e][e2][i][jtdl][jtdl+2]		= 1/2/dp
                    A[e][e2][i][jtdl][nrws+jtdl+1]	=  alpha*k[i]**2.*h3[jtdl+1]
                    A[e][e2][i][jtdl][nrws+jtdl-1]	= -alpha*k[i]**2.*h3[jtdl-1]

                    
    ### PV eq. in the interior ----------------------------------------------------------

                for j in range(nrws+1,2*nrws-1):
                    A[e][e2][i][j][j-1]		= (u[j]*k[i])*( 1/S[j]/dp**2. + ddpS[j]/2./dp)
                    A[e][e2][i][j][j]		= (u[j]*k[i])*(-2/S[j]/dp**2. - k[i]**2.) + 1j*alpha*h3[j]*k[i]**2. + k[i]*(dldp[j]/S[j] + lambda1[j]*ddpS[j]) + k[i]*beta # Flacké + Vicky   ###k[i]*(lambda1[j-1]/S[j-1]-lambda1[j+1]/S[j+1])/(2*dp) #WRONG!
                    A[e][e2][i][j][j+1]		= (u[j]*k[i])*( 1/S[j]/dp**2. - ddpS[j]/2./dp)
                    if heating1 == True and (Spro == True or h1pro == True):
                        A[e][e2][i][j][jtml]	= 1j*epsilon1[e]/2.*(h1[e,j]*ddpS[j]+dh1dp[e,j]/S[j])		 				    # mak1994
                    if heating2 == True and (Spro == True or h2pro == True) and wpar == False and vpar == False:
                        A[e][e2][i][j][-3]		= A[e][e2][i][j][-3]+1/2*1j*epsilon2[e2]/dp*(h2[e2,j]*ddpS[j]+dh2dp[e2,j]/S[j])	# mak1998
                        A[e][e2][i][j][-2]		= A[e][e2][i][j][-2]-  2*1j*epsilon2[e2]/dp*(h2[e2,j]*ddpS[j]+dh2dp[e2,j]/S[j])	# mak1998
                        A[e][e2][i][j][-1]		= A[e][e2][i][j][-1]+3/2*1j*epsilon2[e2]/dp*(h2[e2,j]*ddpS[j]+dh2dp[e2,j]/S[j])	# mak1998
                    # NB! careful if looking at continuous profiles for other surface flux formulationsif i = 57:
                
        
    ### boundary conditions for W ------------------------------------------------------

                A[e][e2][i][0][0]			= 1.
                A[e][e2][i][nrws-1][nrws-1]	= 1.

    ### boundary conditions for Psi ----------------------------------------------------

                if stratos == False:
                    A[e][e2][i][nrws][nrws]		= 3/2*((u[nrws])*k[i])/dp + lambda1[nrws]*k[i]
                    A[e][e2][i][nrws][nrws+1]	=  -2*((u[nrws])*k[i])/dp
                    A[e][e2][i][nrws][nrws+2]	= 1/2*((u[nrws])*k[i])/dp
                if stratos == True:
                    #A[e][e2][i][nrws][nrws]		= 1  # if psi is zero at top        Vicky
                    A[e][e2][i][nrws][nrws]		= 1/dp  # if dpsi/dp is zero at top
                    A[e][e2][i][nrws][nrws+1]   = -1/dp  # if dpsi/dp is zero at top
                
                A[e][e2][i][-1][-3]			= 1/2*(-((u[-1])*k[i])/dp)
                A[e][e2][i][-1][-2]			=  -2*(-((u[-1])*k[i])/dp)
                A[e][e2][i][-1][-1]			= 3/2*(-((u[-1])*k[i])/dp) + lambda1[-1]*k[i]
                
                if heating1 == True:
                    A[e][e2][i][nrws][jtml]		= A[e][e2][i][nrws][jtml]+1j*epsilon1[e]*h1[e,0]/2
                    A[e][e2][i][-1][jtml]		= A[e][e2][i][-1][jtml]+1j*epsilon1[e]*h1[e,-1]/2
                if heating2 == True:
                    if wpar == False and vpar == False:
                        A[e][e2][i][-1][-3]			= A[e][e2][i][-1][-3] + 1/2*1j*epsilon2[e2]*(h2[e2,-1])/dp	# mak1998
                        A[e][e2][i][-1][-2]			= A[e][e2][i][-1][-2] -   2*1j*epsilon2[e2]*(h2[e2,-1])/dp	# mak1998
                        A[e][e2][i][-1][-1]			= A[e][e2][i][-1][-1] + 3/2*1j*epsilon2[e2]*(h2[e2,-1])/dp	# mak1998
                        # sign in front of derivatives due to dp<0
                    if wpar == True and vpar == False:
                        #A[e][e2][i][nrws][jtml]= A[e][e2][i][nrws][jtml] - 1j*epsilon2[e2]*h2[e2,0] # removed /2
                        A[e][e2][i][-1][jtml]	= A[e][e2][i][-1][jtml] - 1j*epsilon2[e2]*h2[e2,-1] # removed /2
                    if wpar == False and vpar == True:
                        A[e][e2][i][-1][-1]		= A[e][e2][i][-1][-1] - 1*k[i]*epsilon2[e2]*h2[e2,-1] # NB! sign

    ### conditions at discontinuity levels
        
                if heating1 == True and h1pro == False:
                    if i == 0 and e == 0:
                        print ('latent heating')
                    if ptlc > .15:
    #                    A[e][e2][i][nrws+jtlc][:]			= 0.
                        A[e][e2][i][nrws+jtlc][nrws+jtlc-2]	= -1/2*(u[nrws+jtlc]*k[i])/(dp)*(1/(S[nrws+jtlc-1]))
                        A[e][e2][i][nrws+jtlc][nrws+jtlc-1]	=    2*(u[nrws+jtlc]*k[i])/(dp)*(1/(S[nrws+jtlc-1]))
                        A[e][e2][i][nrws+jtlc][nrws+jtlc]	= -3/2*(u[nrws+jtlc]*k[i])/(dp)*(1/(S[nrws+jtlc+1])+1/(S[nrws+jtlc-1]))-k[i]*lambda1[jtlc]*(1/S[nrws+jtlc+1]-1/S[nrws+jtlc-1])
                        A[e][e2][i][nrws+jtlc][nrws+jtlc+1]	=    2*(u[nrws+jtlc]*k[i])/(dp)*(1/(S[nrws+jtlc+1]))
                        A[e][e2][i][nrws+jtlc][nrws+jtlc+2]	= -1/2*(u[nrws+jtlc]*k[i])/(dp)*(1/(S[nrws+jtlc+1]))
                        A[e][e2][i][nrws+jtlc][jtml]		=  -1j*epsilon1[e]/2.*(h1[e,nrws+jtlc+1]/S[nrws+jtlc+1]-h1[e,nrws+jtlc-1]/S[nrws+jtlc-1])
        
                    if pblc < 1:
    #                    A[e][e2][i][nrws+jblc][:]			= 0.
                        A[e][e2][i][nrws+jblc][nrws+jblc-2]	= -1/2*(u[nrws+jblc]*k[i])/(dp)*(1/(S[nrws+jblc-1]))
                        A[e][e2][i][nrws+jblc][nrws+jblc-1]	=    2*(u[nrws+jblc]*k[i])/(dp)*(1/(S[nrws+jblc-1]))
                        A[e][e2][i][nrws+jblc][nrws+jblc]	= -3/2*(u[nrws+jblc]*k[i])/(dp)*(1/(S[nrws+jblc+1])+1/(S[nrws+jblc-1]))-k[i]*lambda1[jblc]*(1/S[nrws+jblc+1]-1/S[nrws+jblc-1])
                        A[e][e2][i][nrws+jblc][nrws+jblc+1]	=    2*(u[nrws+jblc]*k[i])/(dp)*(1/(S[nrws+jblc+1]))
                        A[e][e2][i][nrws+jblc][nrws+jblc+2]	= -1/2*(u[nrws+jblc]*k[i])/(dp)*(1/(S[nrws+jblc+1]))
                        A[e][e2][i][nrws+jblc][jtml]		=  -1j*epsilon1[e]/2.*(h1[e,nrws+jblc+1]/S[nrws+jblc+1]-h1[e,nrws+jblc-1]/S[nrws+jblc-1])
           
                    if heating1_ice == True:
    #                    A[e][e2][i][nrws+jtic][:]			= 0.
                        A[e][e2][i][nrws+jtic][nrws+jtic-2]	= -1/2*(u[nrws+jtic]*k[i])/(dp)*(1/(S[nrws+jtic-1]))
                        A[e][e2][i][nrws+jtic][nrws+jtic-1]	=    2*(u[nrws+jtic]*k[i])/(dp)*(1/(S[nrws+jtic-1]))
                        A[e][e2][i][nrws+jtic][nrws+jtic]	= -3/2*(u[nrws+jtic]*k[i])/(dp)*(1/(S[nrws+jtic+1])+1/(S[nrws+jtic-1]))-k[i]*lambda1[jtic]*(1/S[nrws+jtic+1]-1/S[nrws+jtic-1])
                        A[e][e2][i][nrws+jtic][nrws+jtic+1]	=    2*(u[nrws+jtic]*k[i])/(dp)*(1/(S[nrws+jtic+1]))
                        A[e][e2][i][nrws+jtic][nrws+jtic+2]	= -1/2*(u[nrws+jtic]*k[i])/(dp)*(1/(S[nrws+jtic+1]))
                        A[e][e2][i][nrws+jtic][jtml]		=  -1j*epsilon1[e]/2.*(h1[e,nrws+jtic+1]/S[nrws+jtic+1]-h1[e,nrws+jtic-1]/S[nrws+jtic-1])
                    
                if heating2 == True:
                    if i == 0 and e == 0:
                        print ('surface fluxes')
#                    A[e][e2][i][nrws+jtsf][:]			= 0.
                    A[e][e2][i][nrws+jtsf][nrws+jtsf-2]	= -1/2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf-1]))
                    A[e][e2][i][nrws+jtsf][nrws+jtsf-1]	=    2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf-1]))
                    A[e][e2][i][nrws+jtsf][nrws+jtsf]	= -3/2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf+1])+1/(S[nrws+jtsf-1]))-k[i]*lambda1[jtsf]*(1/S[nrws+jtsf+1]-1/S[nrws+jtsf-1])
                    A[e][e2][i][nrws+jtsf][nrws+jtsf+1]	=   +2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf+1]))
                    A[e][e2][i][nrws+jtsf][nrws+jtsf+2]	= -1/2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf+1]))

                    if wpar == False and vpar == False:
                        A[e][e2][i][nrws+jtsf][-3]			= -1/2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtsf+1]/S[nrws+jtsf+1]-h2[e2,nrws+jtsf-1]/S[nrws+jtsf-1])
                        A[e][e2][i][nrws+jtsf][-2]			=    2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtsf+1]/S[nrws+jtsf+1]-h2[e2,nrws+jtsf-1]/S[nrws+jtsf-1])
                        A[e][e2][i][nrws+jtsf][-1]			= -3/2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtsf+1]/S[nrws+jtsf+1]-h2[e2,nrws+jtsf-1]/S[nrws+jtsf-1])
                    if wpar == True and vpar == False:
                        if ptsf < 1:
                            A[e][e2][i][nrws+jtsf][jtml]	= A[e][e2][i][nrws+jtsf][jtml] + 1j*epsilon2[e2]*(h2[e2,nrws+jtsf+1]/S[nrws+jtsf+1]-h2[e2,nrws+jtsf-1]/S[nrws+jtsf-1]) # removed /2
                    if wpar == False and vpar == True:
                        if ptsf < 1:
                            A[e][e2][i][nrws+jtsf][-1]		= A[e][e2][i][nrws+jtsf][-1] + 1*k[i]*epsilon2[e2]*(h2[e2,nrws+jtsf+1]/S[nrws+jtsf+1]-h2[e2,nrws+jtsf-1]/S[nrws+jtsf-1])


                if disc_strat == True:
                    if i == 0 and e == 0:
                        print ('discontinuous stratification')
                    A[e][e2][i][nrws+jtbl][:]				= 0.
                    A[e][e2][i][nrws+jtbl][nrws+jtbl-2]	= -1/2*(u[nrws+jtbl]*k[i])/(dp)*(1/(S[nrws+jtbl-1]))
                    A[e][e2][i][nrws+jtbl][nrws+jtbl-1]	=   +2*(u[nrws+jtbl]*k[i])/(dp)*(1/(S[nrws+jtbl-1]))
                    A[e][e2][i][nrws+jtbl][nrws+jtbl]	= -3/2*(u[nrws+jtbl]*k[i])/(dp)*(1/(S[nrws+jtbl+1])+1/(S[nrws+jtbl-1]))-k[i]*(lambda1[jtbl+1]/S[nrws+jtbl+1]-lambda1[jtbl-1]/S[nrws+jtbl-1])
                    A[e][e2][i][nrws+jtbl][nrws+jtbl+1]	=   +2*(u[nrws+jtbl]*k[i])/(dp)*(1/(S[nrws+jtbl+1]))
                    A[e][e2][i][nrws+jtbl][nrws+jtbl+2]	= -1/2*(u[nrws+jtbl]*k[i])/(dp)*(1/(S[nrws+jtbl+1]))

                    if heating1 == True and h1pro == False:
                        A[e][e2][i][nrws+jtbl][jtml]	= -1j*epsilon1[e]/2*(h1[e,nrws+jtbl+1]/S[nrws+jtbl+1]-h1[e,nrws+jtbl-1]/S[nrws+jtbl-1])
                    if heating2 == True:
                        if wpar == False and vpar == False:
                            A[e][e2][i][nrws+jtbl][-3]	= -1/2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtbl+1]/S[nrws+jtbl+1]-h2[e2,nrws+jtbl-1]/S[nrws+jtbl-1])
                            A[e][e2][i][nrws+jtbl][-2]	=    2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtbl+1]/S[nrws+jtbl+1]-h2[e2,nrws+jtbl-1]/S[nrws+jtbl-1])
                            A[e][e2][i][nrws+jtbl][-1]	= -3/2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtbl+1]/S[nrws+jtbl+1]-h2[e2,nrws+jtbl-1]/S[nrws+jtbl-1])
                        if wpar == True and vpar == False:
                            A[e][e2][i][nrws+jtbl][jtml]= A[e][e2][i][nrws+jtbl][jtml] + 1j*epsilon2[e2]*(h2[e2,nrws+jtbl+1]/S[nrws+jtbl+1]-h2[e2,nrws+jtbl-1]/S[nrws+jtbl-1]) # removed /2
                        if wpar == False and vpar == True:
                            A[e][e2][i][nrws+jtbl][-1]	= +1*k[i]*epsilon2[e2]*(h2[e2,nrws+jtbl+1]/S[nrws+jtbl+1]-h2[e2,nrws+jtbl-1]/S[nrws+jtbl-1])

                if disc_strat_2 == True:
                    if i == 0 and e == 0:
                        print ('discontinuous stratification')
    #                A[e][e2][i][nrws+jtsf][:]				= 0.
                    A[e][e2][i][nrws+jtsf][nrws+jtsf-2]	= -1/2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf-1]))
                    A[e][e2][i][nrws+jtsf][nrws+jtsf-1]	=   +2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf-1]))
                    A[e][e2][i][nrws+jtsf][nrws+jtsf]	= -3/2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf+1])+1/(S[nrws+jtsf-1]))-k[i]*(lambda1[jtsf+1]/S[nrws+jtsf+1]-lambda1[jtsf-1]/S[nrws+jtsf-1])
                    A[e][e2][i][nrws+jtsf][nrws+jtsf+1]	=   +2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf+1]))
                    A[e][e2][i][nrws+jtsf][nrws+jtsf+2]	= -1/2*(u[nrws+jtsf]*k[i])/(dp)*(1/(S[nrws+jtsf+1]))

                    if heating1 == True and h1pro == False:
                        A[e][e2][i][nrws+jtsf][jtml]	= -1j*epsilon1[e]/2*(h1[e,nrws+jtsf+1]/S[nrws+jtsf+1]-h1[e,nrws+jtsf-1]/S[nrws+jtsf-1])
                    if heating2 == True:
                        A[e][e2][i][nrws+jtsf][-3]		= -1/2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtsf+1]/S[nrws+jtsf+1]-h2[e2,nrws+jtsf-1]/S[nrws+jtsf-1])
                        A[e][e2][i][nrws+jtsf][-2]		=    2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtsf+1]/S[nrws+jtsf+1]-h2[e2,nrws+jtsf-1]/S[nrws+jtsf-1])
                        A[e][e2][i][nrws+jtsf][-1]		= -3/2*1j*epsilon2[e2]/dp*(h2[e2,nrws+jtsf+1]/S[nrws+jtsf+1]-h2[e2,nrws+jtsf-1]/S[nrws+jtsf-1])
                        
                if stratos == True and smoothshearstrat == False and ((smoothshear == False and lambda1[jtrop-1] != lambda1[jtrop+1]) or (smoothstrat == False and S[jtrop-1] != S[jtrop+1])):
                    if i == 0 and e == 0:
                        print ('discontinuous stratosphere')
    #                A[e][e2][i][nrws+jtrop][:]				= 0.
                    A[e][e2][i][nrws+jtrop][nrws+jtrop-2]	= -1/2*(u[nrws+jtrop]*k[i])/(dp)*(1/(S[nrws+jtrop-1]))
                    A[e][e2][i][nrws+jtrop][nrws+jtrop-1]	=   +2*(u[nrws+jtrop]*k[i])/(dp)*(1/(S[nrws+jtrop-1]))
                    A[e][e2][i][nrws+jtrop][nrws+jtrop]		= -3/2*(u[nrws+jtrop]*k[i])/(dp)*(1/(S[nrws+jtrop+1])+1/(S[nrws+jtrop-1]))-k[i]*(lambda1[nrws+jtrop+1]/S[nrws+jtrop+1]-lambda1[nrws+jtrop-1]/S[nrws+jtrop-1])
                    A[e][e2][i][nrws+jtrop][nrws+jtrop+1]	=   +2*(u[nrws+jtrop]*k[i])/(dp)*(1/(S[nrws+jtrop+1]))
                    A[e][e2][i][nrws+jtrop][nrws+jtrop+2]	= -1/2*(u[nrws+jtrop]*k[i])/(dp)*(1/(S[nrws+jtrop+1]))
                    
                    if three_steps == True or five_steps == True:
        #                A[e][e2][i][nrws+jtrop][:]				= 0.
                        A[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange-2]	= -1/2*(u[nrws+jtrop-delrange]*k[i])/(dp)*(1/(S[nrws+jtrop-delrange-1]))
                        A[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange-1]	=   +2*(u[nrws+jtrop-delrange]*k[i])/(dp)*(1/(S[nrws+jtrop-delrange-1]))
                        A[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange]	= -3/2*(u[nrws+jtrop-delrange]*k[i])/(dp)*(1/(S[nrws+jtrop-delrange+1])+1/(S[nrws+jtrop-delrange-1]))-k[i]*(lambda1[nrws+jtrop-delrange+1]/S[nrws+jtrop-delrange+1]-lambda1[nrws+jtrop-delrange-1]/S[nrws+jtrop-delrange-1])
                        A[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange+1]	=   +2*(u[nrws+jtrop-delrange]*k[i])/(dp)*(1/(S[nrws+jtrop-delrange+1]))
                        A[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange+2]	= -1/2*(u[nrws+jtrop-delrange]*k[i])/(dp)*(1/(S[nrws+jtrop-delrange+1]))

        #                A[e][e2][i][nrws+jtrop][:]				= 0.
                        A[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange-2]	= -1/2*(u[nrws+jtrop+delrange]*k[i])/(dp)*(1/(S[nrws+jtrop+delrange-1]))
                        A[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange-1]	=   +2*(u[nrws+jtrop+delrange]*k[i])/(dp)*(1/(S[nrws+jtrop+delrange-1]))
                        A[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange]	= -3/2*(u[nrws+jtrop+delrange]*k[i])/(dp)*(1/(S[nrws+jtrop+delrange+1])+1/(S[nrws+jtrop+delrange-1]))-k[i]*(lambda1[nrws+jtrop+delrange+1]/S[nrws+jtrop+delrange+1]-lambda1[nrws+jtrop+delrange-1]/S[nrws+jtrop+delrange-1])
                        A[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange+1]	=   +2*(u[nrws+jtrop+delrange]*k[i])/(dp)*(1/(S[nrws+jtrop+delrange+1]))
                        A[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange+2]	= -1/2*(u[nrws+jtrop+delrange]*k[i])/(dp)*(1/(S[nrws+jtrop+delrange+1]))
                    
                    # use one-sided finite differences at levels next to discontinuity levels            Flacké
                    #A[e][e2][i][nrws+jtrop-1][:]                = 0.
                    #A[e][e2][i][nrws+jtrop-1][nrws+jtrop-3]		= (u[jtrop-1]*k[i])*( 1/S[jtrop-1]/dp**2.)
                    #A[e][e2][i][nrws+jtrop-1][nrws+jtrop-2]		= (u[jtrop-1]*k[i])*(-2/S[jtrop-1]/dp**2. + ddpS[jtrop-1]/dp)
                    #A[e][e2][i][nrws+jtrop-1][nrws+jtrop-1]		= (u[jtrop-1]*k[i])*( 1/S[jtrop-1]/dp**2. - ddpS[jtrop-1]/dp - k[i]**2.) - k[i]*(lambda1[jtrop-1]/S[jtrop-1]-lambda1[jtrop-2]/S[jtrop-2])/(dp) + 1j*alpha*h3[jtrop-1]*k[i]**2. + k[i]*beta
                    #A[e][e2][i][nrws+jtrop+1][:]                = 0.
                    #A[e][e2][i][nrws+jtrop+1][nrws+jtrop+1]		= (u[jtrop+1]*k[i])*( 1/S[jtrop+1]/dp**2. + ddpS[jtrop+1]/dp - k[i]**2.) - k[i]*(lambda1[jtrop+2]/S[jtrop+2]-lambda1[jtrop+1]/S[jtrop+1])/(dp) + 1j*alpha*h3[jtrop+1]*k[i]**2. + k[i]*beta
                    #A[e][e2][i][nrws+jtrop+1][nrws+jtrop+2]		= (u[jtrop+1]*k[i])*(-2/S[jtrop+1]/dp**2. - ddpS[jtrop+1]/dp)
                    #A[e][e2][i][nrws+jtrop+1][nrws+jtrop+3]		= (u[jtrop+1]*k[i])*( 1/S[jtrop+1]/dp**2.)
                    
                    #A[e][e2][i][jtrop-1][:]         	=  0.
                    #A[e][e2][i][jtrop-1][jtrop-3]		=  1/dp**2.
                    #A[e][e2][i][jtrop-1][jtrop-2]		= -2/dp**2.
                    #A[e][e2][i][jtrop-1][jtrop-1]	    =  1/dp**2.-S[jtrop-1]*k[i]**2.
                    #A[e][e2][i][jtrop-1][nrws+jtrop-2]	=  k[i]**2*alpha*h3[jtrop-2]/(dp)-1j*beta*k[i]/(dp)
                    #A[e][e2][i][jtrop-1][nrws+jtrop-1]	= -k[i]**2*alpha*h3[jtrop-1]/(dp)+1j*beta*k[i]/(dp)-1j*2*lambda1[jtrop-1]*k[i]**3.
                    #A[e][e2][i][jtrop+1][:]         	=  0.
                    #A[e][e2][i][jtrop+1][jtrop+1]	    =  1/dp**2.-S[jtrop+1]*k[i]**2.
                    #A[e][e2][i][jtrop+1][jtrop+2]		= -2/dp**2.
                    #A[e][e2][i][jtrop+1][jtrop+3]		=  1/dp**2.
                    #A[e][e2][i][jtrop+1][nrws+jtrop+2]	= -k[i]**2*alpha*h3[jtrop+2]/(dp)+1j*beta*k[i]/(dp)
                    #A[e][e2][i][jtrop+1][nrws+jtrop+1]	=  k[i]**2*alpha*h3[jtrop+1]/(dp)-1j*beta*k[i]/(dp)-1j*2*lambda1[jtrop+1]*k[i]**3.
                    
                    # add heating terms back again:
                    #if heating1 == True and (Spro == True or h1pro == True):
                    #    A[e][e2][i][jtrop-1][jtml]	    = 1j*epsilon1[e]/2.*(h1[e,jtrop-1]*ddpS[jtrop-1]+dh1dp[e,jtrop-1]/S[jtrop-1])       		 				    # mak1994
                    #if heating2 == True and (Spro == True or h2pro == True) and wpar == False and vpar == False:
                    #    A[e][e2][i][jtrop-1][-3]		= A[e][e2][i][jtrop-1][-3]+1/2*1j*epsilon2[e2]/dp*(h2[e2,jtrop-1]*ddpS[jtrop-1]+dh2dp[e2,jtrop-1]/S[jtrop-1])	# mak1998
                    #    A[e][e2][i][jtrop-1][-2]		= A[e][e2][i][jtrop-1][-2]-  2*1j*epsilon2[e2]/dp*(h2[e2,jtrop-1]*ddpS[jtrop-1]+dh2dp[e2,jtrop-1]/S[jtrop-1])	# mak1998
                    #    A[e][e2][i][jtrop-1][-1]		= A[e][e2][i][jtrop-1][-1]+3/2*1j*epsilon2[e2]/dp*(h2[e2,jtrop-1]*ddpS[jtrop-1]+dh2dp[e2,jtrop-1]/S[jtrop-1])	# mak1998
                    
                    #if heating1 == True:
                    #    A[e][e2][i][jtrop-1][jtml]	= A[e][e2][i][jtrop-1][jtml]+epsilon1[e]*k[i]**2./2.*h1[e,jtrop-1]		# mak1994
                    #    A[e][e2][i][jtrop+1][jtml]	= A[e][e2][i][jtrop+1][jtml]+epsilon1[e]*k[i]**2./2.*h1[e,jtrop+1]		# mak1994
                    #if heating2 == True:
                    #    if wpar == False and vpar == False: #(linearly extrapolated derivative)
                    #        A[e][e2][i][jtrop-1][-3]	= A[e][e2][i][jtrop-1][-3]+1/2*epsilon2[e2]*k[i]**2.*h2[e2,jtrop-1]/dp	# mak1998
                    #        A[e][e2][i][jtrop-1][-2]	= A[e][e2][i][jtrop-1][-2]-  2*epsilon2[e2]*k[i]**2.*h2[e2,jtrop-1]/dp	# mak1998
                    #        A[e][e2][i][jtrop-1][-1]	= A[e][e2][i][jtrop-1][-1]+3/2*epsilon2[e2]*k[i]**2.*h2[e2,jtrop-1]/dp	# mak1998
                    #        A[e][e2][i][jtrop+1][-3]	= A[e][e2][i][jtrop+1][-3]+1/2*epsilon2[e2]*k[i]**2.*h2[e2,jtrop+1]/dp	# mak1998
                    #        A[e][e2][i][jtrop+1][-2]	= A[e][e2][i][jtrop+1][-2]-  2*epsilon2[e2]*k[i]**2.*h2[e2,jtrop+1]/dp	# mak1998
                    #        A[e][e2][i][jtrop+1][-1]	= A[e][e2][i][jtrop+1][-1]+3/2*epsilon2[e2]*k[i]**2.*h2[e2,jtrop+1]/dp	# mak1998
                    #    if vpar == True and wpar == False:
                    #        A[e][e2][i][jtrop-1][-1] = A[e][e2][i][jtrop-1][-1]+1j*epsilon2[e2]*k[i]**3.*h2[e2,jtrop-1] # NB! sign
                    #        A[e][e2][i][jtrop+1][-1] = A[e][e2][i][jtrop+1][-1]+1j*epsilon2[e2]*k[i]**3.*h2[e2,jtrop+1] # NB! sign
                    #    if vpar == False and wpar == True:
                    #        A[e][e2][i][jtrop-1][jtml] = A[e][e2][i][jtrop-1][jtml]-epsilon2[e2]*k[i]**2.*h2[e2,jtrop-1] # removed /2
                    #        A[e][e2][i][jtrop+1][jtml] = A[e][e2][i][jtrop+1][jtml]-epsilon2[e2]*k[i]**2.*h2[e2,jtrop+1] # removed /2
                    
# ----------------------------------------------------------------------------------


    B = np.zeros((len(epsilon1),len(epsilon2),len(k),2*nrws,2*nrws), dtype = complex)

    ### PV eq. in the interior --------------------------------------------------------

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            for i in range(len(k)):
                for j in range(nrws+1,2*nrws-1):
                    B[e][e2][i][j][j-1]		= (1/S[j]/dp**2.) + ddpS[j]/2./dp
                    B[e][e2][i][j][j]		= (-2/S[j]/dp**2. - k[i]**2.)
                    B[e][e2][i][j][j+1]		= (1/S[j]/dp**2.) - ddpS[j]/2./dp

    ### boundary conditions for Psi

                if stratos == False:
                    B[e][e2][i][nrws][nrws]		= 3/2/dp
                    B[e][e2][i][nrws][nrws+1]	= -2/dp
                    B[e][e2][i][nrws][nrws+2]	= 1/2/dp
                B[e][e2][i][-1][-3]			= -1/2/dp
                B[e][e2][i][-1][-2]			= 2/dp
                B[e][e2][i][-1][-1]			= -3/2/dp
                
    ### conditions at discontinuity levels

                if heating1 == True and h1pro == False:
                    if ptlc > .15:
                        B[e][e2][i][nrws+jtlc][:]			= 0.
                        B[e][e2][i][nrws+jtlc][nrws+jtlc-2]	= -1/2/(dp)*(1/(S[nrws+jtlc-1]))
                        B[e][e2][i][nrws+jtlc][nrws+jtlc-1]	=    2/(dp)*(1/(S[nrws+jtlc-1]))
                        B[e][e2][i][nrws+jtlc][nrws+jtlc]	= -3/2/(dp)*(1/(S[nrws+jtlc+1])+1/(S[nrws+jtlc-1]))
                        B[e][e2][i][nrws+jtlc][nrws+jtlc+1]	=    2/(dp)*(1/(S[nrws+jtlc+1]))
                        B[e][e2][i][nrws+jtlc][nrws+jtlc+2]	= -1/2/(dp)*(1/(S[nrws+jtlc+1]))
                    
                    if pblc < 1:
                        B[e][e2][i][nrws+jblc][:]			= 0.
                        B[e][e2][i][nrws+jblc][nrws+jblc-2]	= -1/2/(dp)*(1/(S[nrws+jblc-1]))
                        B[e][e2][i][nrws+jblc][nrws+jblc-1]	=    2/(dp)*(1/(S[nrws+jblc-1]))
                        B[e][e2][i][nrws+jblc][nrws+jblc]	= -3/2/(dp)*(1/(S[nrws+jblc+1])+1/(S[nrws+jblc-1]))
                        B[e][e2][i][nrws+jblc][nrws+jblc+1]	=    2/(dp)*(1/(S[nrws+jblc+1]))
                        B[e][e2][i][nrws+jblc][nrws+jblc+2]	= -1/2/(dp)*(1/(S[nrws+jblc+1]))

                    if heating1_ice == True:
                        B[e][e2][i][nrws+jtic][:]			= 0.
                        B[e][e2][i][nrws+jtic][nrws+jtic-2]	= -1/2/(dp)*(1/(S[nrws+jtic-1]))
                        B[e][e2][i][nrws+jtic][nrws+jtic-1]	=    2/(dp)*(1/(S[nrws+jtic-1]))
                        B[e][e2][i][nrws+jtic][nrws+jtic]	= -3/2/(dp)*(1/(S[nrws+jtic+1])+1/(S[nrws+jtic-1]))
                        B[e][e2][i][nrws+jtic][nrws+jtic+1]	=    2/(dp)*(1/(S[nrws+jtic+1]))
                        B[e][e2][i][nrws+jtic][nrws+jtic+2]	= -1/2/(dp)*(1/(S[nrws+jtic+1]))
                    
                if heating2 == True:
                    B[e][e2][i][nrws+jtsf][:]			= 0.
                    B[e][e2][i][nrws+jtsf][nrws+jtsf-2]	= -1/2/(dp)*(1/(S[nrws+jtsf-1]))
                    B[e][e2][i][nrws+jtsf][nrws+jtsf-1]	=    2/(dp)*(1/(S[nrws+jtsf-1]))
                    B[e][e2][i][nrws+jtsf][nrws+jtsf]	= -3/2/(dp)*(1/(S[nrws+jtsf+1])+1/(S[nrws+jtsf-1]))
                    B[e][e2][i][nrws+jtsf][nrws+jtsf+1]	=    2/(dp)*(1/(S[nrws+jtsf-1]))
                    B[e][e2][i][nrws+jtsf][nrws+jtsf+2]	= -1/2/(dp)*(1/(S[nrws+jtsf+1]))
                        
                if disc_strat == True:
                    B[e][e2][i][nrws+jtbl][:]			= 0.
                    B[e][e2][i][nrws+jtbl][nrws+jtbl-2]	= -1/2/(dp)*(1/(S[nrws+jtbl-1]))
                    B[e][e2][i][nrws+jtbl][nrws+jtbl-1]	=    2/(dp)*(1/(S[nrws+jtbl-1]))
                    B[e][e2][i][nrws+jtbl][nrws+jtbl]	= -3/2/(dp)*(1/(S[nrws+jtbl+1])+1/(S[nrws+jtbl-1]))
                    B[e][e2][i][nrws+jtbl][nrws+jtbl+1]	=    2/(dp)*(1/(S[nrws+jtbl+1]))
                    B[e][e2][i][nrws+jtbl][nrws+jtbl+2]	= -1/2/(dp)*(1/(S[nrws+jtbl+1]))
                    
                if disc_strat_2 == True:
                    B[e][e2][i][nrws+jtsf][:]			= 0.
                    B[e][e2][i][nrws+jtsf][nrws+jtsf-2]	= -1/2/(dp)*(1/(S[nrws+jtsf-1]))
                    B[e][e2][i][nrws+jtsf][nrws+jtsf-1]	=    2/(dp)*(1/(S[nrws+jtsf-1]))
                    B[e][e2][i][nrws+jtsf][nrws+jtsf]	= -3/2/(dp)*(1/(S[nrws+jtsf+1])+1/(S[nrws+jtsf-1]))
                    B[e][e2][i][nrws+jtsf][nrws+jtsf+1]	=    2/(dp)*(1/(S[nrws+jtsf+1]))
                    B[e][e2][i][nrws+jtsf][nrws+jtsf+2]	= -1/2/(dp)*(1/(S[nrws+jtsf+1]))

                if stratos == True and smoothshearstrat == False and ((smoothshear == False and lambda1[jtrop-1] != lambda1[jtrop+1]) or (smoothstrat == False and S[jtrop-1] != S[jtrop+1])):
                    B[e][e2][i][nrws+jtrop][:]			    = 0.
                    B[e][e2][i][nrws+jtrop][nrws+jtrop-2]	= -1/2/(dp)*(1/(S[nrws+jtrop-1]))
                    B[e][e2][i][nrws+jtrop][nrws+jtrop-1]	=    2/(dp)*(1/(S[nrws+jtrop-1]))
                    B[e][e2][i][nrws+jtrop][nrws+jtrop]     = -3/2/(dp)*(1/(S[nrws+jtrop+1])+1/(S[nrws+jtrop-1]))
                    B[e][e2][i][nrws+jtrop][nrws+jtrop+1]	=    2/(dp)*(1/(S[nrws+jtrop+1]))
                    B[e][e2][i][nrws+jtrop][nrws+jtrop+2]	= -1/2/(dp)*(1/(S[nrws+jtrop+1]))
                    
                    if three_steps == True or five_steps == True:
                        B[e][e2][i][nrws+jtrop-delrange][:]			    = 0.
                        B[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange-2]	= -1/2/(dp)*(1/(S[nrws+jtrop-delrange-1]))
                        B[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange-1]	=    2/(dp)*(1/(S[nrws+jtrop-delrange-1]))
                        B[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange]   = -3/2/(dp)*(1/(S[nrws+jtrop-delrange+1])+1/(S[nrws+jtrop-delrange-1]))
                        B[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange+1]	=    2/(dp)*(1/(S[nrws+jtrop-delrange+1]))
                        B[e][e2][i][nrws+jtrop-delrange][nrws+jtrop-delrange+2]	= -1/2/(dp)*(1/(S[nrws+jtrop-delrange+1]))
                        
                        B[e][e2][i][nrws+jtrop+delrange][:]			    = 0.
                        B[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange-2]	= -1/2/(dp)*(1/(S[nrws+jtrop+delrange-1]))
                        B[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange-1]	=    2/(dp)*(1/(S[nrws+jtrop+delrange-1]))
                        B[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange]   = -3/2/(dp)*(1/(S[nrws+jtrop+delrange+1])+1/(S[nrws+jtrop+delrange-1]))
                        B[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange+1]	=    2/(dp)*(1/(S[nrws+jtrop+delrange+1]))
                        B[e][e2][i][nrws+jtrop+delrange][nrws+jtrop+delrange+2]	= -1/2/(dp)*(1/(S[nrws+jtrop+delrange+1]))
                    
                    # use one-sided finite differences at levels next to discontinuity levels            Flacké
                    #B[e][e2][i][nrws+jtrop-1][:]                = 0.
                    #B[e][e2][i][nrws+jtrop-1][nrws+jtrop-3]		= ( 1/S[jtrop-1]/dp**2.)
                    #B[e][e2][i][nrws+jtrop-1][nrws+jtrop-2]		= (-2/S[jtrop-1]/dp**2. - (1/S[jtrop-1]-1/S[jtrop-2])/dp**2)
                    #B[e][e2][i][nrws+jtrop-1][nrws+jtrop-1]		= ( 1/S[jtrop-1]/dp**2. + (1/S[jtrop-1]-1/S[jtrop-2])/dp**2 - k[i]**2.)
                    #B[e][e2][i][nrws+jtrop+1][:]                = 0.
                    #B[e][e2][i][nrws+jtrop+1][nrws+jtrop+1]		= ( 1/S[jtrop+1]/dp**2. - (1/S[jtrop+2]-1/S[jtrop+1])/dp**2 - k[i]**2.)
                    #B[e][e2][i][nrws+jtrop+1][nrws+jtrop+2]		= (-2/S[jtrop+1]/dp**2. + (1/S[jtrop+2]-1/S[jtrop+1])/dp**2)
                    #B[e][e2][i][nrws+jtrop+1][nrws+jtrop+3]		= ( 1/S[jtrop+1]/dp**2.)
                    
                if drag == True and alpha != 0:
                    B[e][e2][i][jtdl][:]				= 0.
                        
    # scaling of W with respect to coriolis parameter:
    if ffac != 1:
        for j in range(nrws):
            A[:,:,:,:,j] = A[:,:,:,:,j]*ffac
        B[:,:,:,:,j] = B[:,:,:,:,j]*ffac

    
# ----------------------------------------------------------------------------------
    
def check_matrix():
        
    # checking matrices A and B by plotting them -----------------------------------

    if nrws < 51:
        kind=int(np.argwhere(k==np.max(k))[0][0])
        s=2000/nrws
        vec = np.linspace(0,2*nrws,2*nrws)
        
        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8)) = plt.subplots(4,2,figsize=(15,12))
        ax = ([ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8])
        
        norm = MidpointNormalize(midpoint=0)
        pl1=ax[0].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=(np.real(A[e,0,kind,nrws:,:])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        #pl1=ax[0].scatter(np.tile(vec,2*nrws),np.repeat(vec,2*nrws),s=s,c=(np.real(A[0,0,kind])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')    
        norm = MidpointNormalize(midpoint=0)
        pl2=ax[1].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=(np.imag(A[e,0,kind,nrws:,:])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl3=ax[2].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=(np.real(A[e,0,kind,:nrws,:])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')    
        norm = MidpointNormalize(midpoint=0)
        pl4=ax[3].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=(np.imag(A[e,0,kind,:nrws,:])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl5=ax[4].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=(np.real(B[e,0,kind,nrws:,:])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl6=ax[5].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=(np.imag(B[e,0,kind,nrws:,:])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl7=ax[6].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=(np.real(B[e,0,kind,:nrws,:])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl8=ax[7].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=(np.imag(B[e,0,kind,:nrws,:])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        pl = ([pl1,pl2,pl3,pl4,pl5,pl6,pl7,pl8])
        #ax4.contour(vec,vec,imag(B[0,0,50]))
        for i in range(8):
            fig.colorbar(pl[i], ax=ax[i])
        for i in [0,1,4,5]:
            ax[i].set_ylabel('nrws:2*nrws')
            ax[i].set_xlim(-1,2*nrws+1)
            ax[i].set_ylim(nrws,2*nrws+1)#-1,nrws+1)
            ax[i].set_xticks([jblc,jtlc,jtsf,jtbl,nrws,nrws+jblc,nrws+jtlc,nrws+jtsf,nrws+jtbl])
            ax[i].set_yticks([nrws,nrws+jblc,nrws+jtlc,nrws+jtsf,nrws+jtbl])
            ax[i].set_xticklabels(('','','','','','','','',''))
            ax[i].set_yticklabels(('','','','',''))
            ax[i].axhline(nrws,c='k',ls='--',alpha=.1)
            ax[i].axvline(nrws,c='k',ls='--',alpha=.1)
        for i in [2,3,6,7]:
            ax[i].set_ylabel('0:nrws')
            ax[i].set_xlim(-1,2*nrws+1)
            ax[i].set_ylim(-1,nrws)
            ax[i].set_xticks([jblc,jtlc,jtsf,jtbl,nrws,nrws+jblc,nrws+jtlc,nrws+jtsf,nrws+jtbl])
            ax[i].set_yticks([jblc,jtlc,jtsf,jtbl,nrws])
            ax[i].set_xticklabels(('','','','','','','','',''))
            ax[i].set_yticklabels(('','','','',''))
            ax[i].axhline(nrws,c='k',ls='--',alpha=.1)
            ax[i].axvline(nrws,c='k',ls='--',alpha=.1)
        ax[0].set_title('Real A')
        ax[1].set_title('Imaginary A')
        ax[4].set_title('Real B')
        ax[5].set_title('Imaginary B')
        plt.show()
    
# ----------------------------------------------------------------------------------    
    
def solve_matrix():

    global sigmai_sorted, sigmar_sorted, eigvecs_sorted
        
    # ----------------------------------------------------------------------------------
    # finding eigenvalues and eigenfunctions of Ax = cBx
    # ----------------------------------------------------------------------------------

    eigvals = np.zeros((len(epsilon1),len(epsilon2),len(k),2*nrws),dtype=complex)			# sigma
    eigvecs = np.zeros((len(epsilon1),len(epsilon2),len(k),2*nrws,2*nrws),dtype=complex)	# omega (first part) and psi (last part)

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            for i in range(len(k)):
                eigvals[e,e2,i], eigvecs[e,e2,i] = eig(A[e,e2,i]/np.max(A[e,e2,:]),B[e,e2,i]/np.max(A[e,e2,:]))
                # this is where the solution is calculated and typically where the code slows down
                
        
    ### finding the most unstable and stable solutions -----------------------------------

    sigmai = imag(eigvals)
    sigmar = real(eigvals)

    # careful! this MAY mess up solutions! 
    sigmai[np.abs(sigmai) == inf] = nan		# converts inf values to nan values
    sigmar[np.abs(sigmar) == inf] = nan		# converts inf values to nan values

    # finding nans in eigenvalues and preparing to eliminate corresponding eigenvectors
    nvalvec = np.zeros((len(epsilon1),len(k)), dtype=int)
    for e in range(len(epsilon1)):
        for i in range(len(k)):
            nvalvec[e,i] = len(sigmai[e,eps2_index,i][np.logical_not(np.isnan(sigmai[e,eps2_index,i]))])
    nval = (np.max(nvalvec))

    sorter				= np.zeros((len(epsilon1),len(epsilon2),len(k),nval), dtype = int)
    sigmar_temp			= np.zeros((len(epsilon1),len(epsilon2),len(k),nval))
    sigmai_temp			= np.zeros((len(epsilon1),len(epsilon2),len(k),nval))
    eigvecs_temp		= np.zeros((len(epsilon1),len(epsilon2),len(k),2*nrws,nval), dtype = complex)
    sigmar_sorted		= np.zeros((len(epsilon1),len(epsilon2),len(k),nval))
    sigmai_sorted		= np.zeros((len(epsilon1),len(epsilon2),len(k),nval))
    eigvecs_sorted		= np.zeros((len(epsilon1),len(epsilon2),len(k),2*nrws,nval), dtype = complex)

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            for i in range(len(k)):
                sigmai_temp[e,e2,i,:nvalvec[e,i]]		= sigmai[e,e2,i][np.logical_not(np.isnan(sigmai[e,e2,i]))]
                sigmar_temp[e,e2,i,:nvalvec[e,i]]		= sigmar[e,e2,i][np.logical_not(np.isnan(sigmai[e,e2,i]))]

                sorter[e,e2,i]			= sigmai_temp[e,e2,i].argsort()
                sigmai_sorted[e,e2,i]	= sigmai_temp[e,e2,i][sorter[e,e2,i]]
                sigmar_sorted[e,e2,i]	= sigmar_temp[e,e2,i][sorter[e,e2,i]]
                
                for j in range(2*nrws):
                    eigvecs_temp[e,e2,i,j,:nvalvec[e,i]]	= eigvecs[e,e2,i,j][np.logical_not(np.isnan(sigmai[e,e2,i]))]
                    eigvecs_sorted[e,e2,i,j]	            = eigvecs_temp[e,e2,i,j][sorter[e,e2,i]]
        
# ----------------------------------------------------------------------------------        
        
def check_solution():        
                    
    ### checking if solutions fulfill model equations (residual should be around zero) -----------------------------------

    mpl.rc('font',size=12)

    if nrws < 51:
        kind = int(len(k)/2) #int(np.argwhere(sigmai_sorted[e,e2,:,-1]==np.max(sigmai_sorted[e,e2,:,-1]))[0][0])
        s = 2000/nrws
        vec = np.linspace(0,2*nrws,2*nrws)
        
        fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9),(ax10,ax11,ax12)) = plt.subplots(4,3,figsize=(20,12))
        ax = ([ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10,ax11,ax12])
        
        eq1A = ((A[0,0,kind,nrws:,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()#-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.real(B[0,0,kind,nrws:,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()
        eq1Areal = np.real(eq1A)
        eq1Aimag = np.imag(eq1A)
        
        eq1B = (-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*(B[0,0,kind,nrws:,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()
        eq1Breal = np.real(eq1B)
        eq1Bimag = np.imag(eq1B)    
        
        eq1real  = eq1Areal+eq1Breal
        eq1realSUM = np.real(((A[0,0,kind,nrws:,:]) @ eigvecs_sorted[0,0,kind,:,-1])-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.real(B[0,0,kind,nrws:,:]) @ eigvecs_sorted[0,0,kind,:,-1])
        eq1imag  = eq1Aimag+eq1Bimag
        eq1imagSUM = np.imag(((A[0,0,kind,nrws:,:]) @ eigvecs_sorted[0,0,kind,:,-1])-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.real(B[0,0,kind,nrws:,:]) @ eigvecs_sorted[0,0,kind,:,-1])
        
        eq2A = ((A[0,0,kind,:nrws,:])*eigvecs_sorted[0,0,kind,:,-1])
        eq2Areal = np.real(eq2A)
        eq2Aimag = np.imag(eq2A)
        
        eq2B = (-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*(B[0,0,kind,:nrws,:])*eigvecs_sorted[0,0,kind,:,-1])
        eq2Breal = np.real(eq2B)
        eq2Bimag = np.imag(eq2B)
                           
        eq2real  = eq2Areal+eq2Breal
        eq2realSUM = np.real(((A[0,0,kind,:nrws,:]) @ eigvecs_sorted[0,0,kind,:,-1])-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.real(B[0,0,kind,:nrws,:]) @ eigvecs_sorted[0,0,kind,:,-1])
        eq2imag  = eq2Aimag+eq2Bimag
        eq2imagSUM = np.imag(((A[0,0,kind,:nrws,:]) @ eigvecs_sorted[0,0,kind,:,-1])-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.real(B[0,0,kind,:nrws,:]) @ eigvecs_sorted[0,0,kind,:,-1])

    #    eq2Areal = (np.real(A[0,0,kind,:nrws,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()#-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.real(B[0,0,kind,nrws:,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()
    #    eq2Breal = (-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.real(B[0,0,kind,:nrws,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()
    #    eq2real  = eq2Areal+eq2Breal
        
    #    eq2Aimag = (np.imag(A[0,0,kind,:nrws,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()#-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.real(B[0,0,kind,nrws:,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()
    #    eq2Bimag = (-(sigmar_sorted[0,0,kind,-1]+1j*sigmai_sorted[0,0,kind,-1])*np.imag(B[0,0,kind,:nrws,:])*eigvecs_sorted[0,0,kind,:,-1]).ravel()
    #    eq2imag  = eq2Aimag+eq2Bimag
        
        norm = MidpointNormalize(midpoint=0)
        pl1=ax[0].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=eq1Areal,edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        #pl1=ax[0].scatter(np.tile(vec,2*nrws),np.repeat(vec,2*nrws),s=s,c=(np.real(A[0,0,kind])).ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')    
        norm = MidpointNormalize(midpoint=0)
        pl2=ax[1].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=eq1Breal,edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl3=ax[2].plot(eq1realSUM, vec[:nrws])
        #pl3=ax[2].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=eq1real,edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')    
        
        norm = MidpointNormalize(midpoint=0)
        pl4=ax[3].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=eq1Aimag,edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl5=ax[4].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=eq1Bimag,edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        #pl6=ax[5].scatter(np.tile(vec,nrws),np.repeat(vec[nrws:],2*nrws),s=s,c=eq1imag,edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        pl6=ax[5].plot(eq1imagSUM, vec[:nrws])
       
        norm = MidpointNormalize(midpoint=0)
        pl7=ax[6].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=eq2Areal.ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl8=ax[7].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=eq2Breal.ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl9=ax[8].plot(eq2realSUM, vec[:nrws])
        #pl9=ax[8].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=eq2real.ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')

        norm = MidpointNormalize(midpoint=0)
        pl10=ax[9].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=eq2Aimag.ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        pl11=ax[10].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=eq2Bimag.ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        norm = MidpointNormalize(midpoint=0)
        #pl12=ax[11].scatter(np.tile(vec,nrws),np.repeat(vec[:nrws],2*nrws),s=s,c=eq2imag.ravel(),edgecolor = 'grey', marker='s',cmap=plt.cm.bwr,norm=norm)#,origin='lower')
        pl12=ax[11].plot(eq2imagSUM, vec[:nrws])

        pl = ([pl1,pl2,pl3,pl4,pl5,pl6,pl7,pl8,pl9,pl10,pl11,pl12])
        #ax4.contour(vec,vec,imag(B[0,0,50]))
        for i in [0,1,3,4,6,7,9,10]:
            fig.colorbar(pl[i], ax=ax[i])
        for i in [0,1,3,4]:
            ax[i].set_ylabel('nrws:2*nrws')
            ax[i].set_xlim(-1,2*nrws+1)
            ax[i].set_ylim(nrws,2*nrws+1)#-1,nrws+1)
            ax[i].set_xticks([jblc,jtlc,jtsf,jtbl,nrws,nrws+jblc,nrws+jtlc,nrws+jtsf,nrws+jtbl])
            ax[i].set_yticks([nrws,nrws+jblc,nrws+jtlc,nrws+jtsf,nrws+jtbl])
            ax[i].set_xticklabels(('','','','','','','','',''))
            ax[i].set_yticklabels(('','','','',''))
            ax[i].axhline(nrws,c='k',ls='--',alpha=.1)
            ax[i].axvline(nrws,c='k',ls='--',alpha=.1)
        for i in [6,7,9,10]:
            ax[i].set_ylabel('0:nrws')
            ax[i].set_xlim(-1,2*nrws+1)
            ax[i].set_ylim(-1,nrws)
            ax[i].set_xticks([jblc,jtlc,jtsf,jtbl,nrws,nrws+jblc,nrws+jtlc,nrws+jtsf,nrws+jtbl])
            ax[i].set_yticks([jblc,jtlc,jtsf,jtbl,nrws])
            ax[i].set_xticklabels(('','','','','','','','',''))
            ax[i].set_yticklabels(('','','','',''))
            ax[i].axhline(nrws,c='k',ls='--',alpha=.1)
            ax[i].axvline(nrws,c='k',ls='--',alpha=.1)
        for i in [2,5]:
            ax[i].set_ylabel('nrws:2*nrws')
            ax[i].set_ylim(-1,nrws)
            ax[i].set_yticks([jblc,jtlc,jtsf,jtbl,nrws])
            ax[i].set_yticklabels(('','','','',''))
        for i in [8,11]:
            ax[i].set_ylabel('0:nrws')
            ax[i].set_ylim(-1,nrws)
            ax[i].set_yticks([jblc,jtlc,jtsf,jtbl,nrws])
            ax[i].set_yticklabels(('','','','',''))
        ax[0].set_title('Eq. 1, real part of Ax*')
        ax[1].set_title('Eq. 1, real part of cBx*')
        ax[2].set_title('Eq. 1, real part of (A+cB)x')
        ax[3].set_title('Eq. 1, imaginary part of Ax*')
        ax[4].set_title('Eq. 1, imaginary part of cBx*')
        ax[5].set_title('Eq. 1, imaginary part of (A+cB)x')
        ax[6].set_title('Eq. 2, real part of Ax*')
        ax[7].set_title('Eq. 2, real part of cBx*')
        ax[8].set_title('Eq. 2, real part of (A+cB)x')
        ax[9].set_title('Eq. 2, imaginary part of Ax*')
        ax[10].set_title('Eq. 2, imaginary part of cBx*')
        ax[11].set_title('Eq. 2, imaginary part of (A+cB)x')
        plt.tight_layout()
        plt.show()
        
