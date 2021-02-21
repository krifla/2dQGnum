# *****************************************************************************
# -----------------------------------------------------------------------------
# MODEL OUTPUT
# -----------------------------------------------------------------------------
# *****************************************************************************

mpl.rc('font',size=22)  

def check_growthrates():

    global sigmai_sorted_1, sigmai_sorted_2, sigmai_sorted_3, sigmai_sorted_4
    global sigmai_sorted_5, sigmai_sorted_6, sigmai_sorted_7, sigmai_sorted_8
    global sigmai_sorted_9, sigmai_sorted_10, sigmai_sorted_11, sigmai_sorted_12, sigmai_sorted_13
    global lw, labels, colors, alphas, linestyles

### plotting the growth rate (and phase speed) ----------------------------

#    sigmai_sorted_1 = sigmai_sorted
#    sigmai_sorted_2 = sigmai_sorted
#    sigmai_sorted_3 = sigmai_sorted
#    sigmai_sorted_4 = sigmai_sorted
#    sigmai_sorted_5 = sigmai_sorted
#    sigmai_sorted_6 = sigmai_sorted
#    sigmai_sorted_7 = sigmai_sorted
#    sigmai_sorted_8 = sigmai_sorted
#    sigmai_sorted_9 = sigmai_sorted
#    sigmai_sorted_10 = sigmai_sorted
#    sigmai_sorted_11 = sigmai_sorted
#    sigmai_sorted_12 = sigmai_sorted
#    sigmai_sorted_13 = sigmai_sorted


    phase_speed = False
    
    lw = 3
    lwfac = 1.5

    labels = (['sharp CTL','sharp CTL-$\\regular{\lambda}$','sharp CTL-$\\regular{S}$', '$\lambda_{st}/\lambda_{tr}= \hspace{1.2} 1$, $S_{st}/S_{tr}=4$','$\lambda_{st}/\lambda_{tr}=-1$, $S_{st}/S_{tr}=1$','$\lambda_{st}/\lambda_{tr}=-1$, $S_{st}/S_{tr}=4$','$\lambda_{st}/\lambda_{tr}=-2$, $S_{st}/S_{tr}=1$','$\lambda_{st}/\lambda_{tr}=-2$, $S_{st}/S_{tr}=4$','narrow range','narrow range noncons','wide range','wide range noncons','low trop','low trop noncons','high trop','high trop noncons','narrow high res','wide high res'])        
    #labels = (['sharp CTL','sharp NCONS-70','smooth CTL','smooth NCONS-70','shallow (100 hPa)','shallow (100 hPa) NCONS-70','deep (200 hPa)','deep (200 hPa) NCONS-70','low (300 hPa)','low (300 hPa) NCONS-70','high (200 hPa)','high (200 hPa) NCONS-70','narrow high res','wide high res'])#$\\regular{p_{trop}}$ = 
#    labels = (['sharp CTL','sharp NCONS-70','smooth CTL','smooth NCONS-70','smooth shallow ($\\regular{\delta=0.1}$) CONS','smooth shallow ($\\regular{\delta=0.1}$) NCONS-70','smooth deep ($\\regular{\delta=0.2}$) CONS','smooth deep ($\\regular{\delta=0.2}$) NCONS-70','smooth low ($\\regular{p_*=0.3}$) CONS','smooth low ($\\regular{p_*=0.3}$) NCONS-70','smooth high ($\\regular{p_*=0.2}$) CONS','smooth high ($\\regular{p_*=0.2}$) NCONS-70','narrow high res','wide high res'])#$\\regular{p_{trop}}$ = 
    #labels = (['$\\varepsilon=2.0$, sharp','$\\varepsilon=2.5$, sharp','$\\varepsilon=1.5$, sharp','narrow range','narrow range noncons','wide range','wide range noncons','$\\varepsilon=2.5$, high trop','$\\varepsilon=2.5$, high trop, noncons','$\\varepsilon=2.0$, high trop','$\\varepsilon=2.0$, high trop, noncons','$\\varepsilon=1.5$, high trop','$\\varepsilon=1.5$, high trop, noncons','narrow high res','wide high res'])        
    #labels = (['no TIL','deep TIL: a7, 200-300','deep TIL: a5, 200-300','deep TIL: a8, 200-300','shallow TIL: a7, 225-275','low deep TIL: a7, 250-350','low shallow TIL: a7, 250-300','high deep TIL: a7, 150-250','high shallow TIL: a7, 200-250','linear TIL','smooth TIL','G&W1 TIL','G&W2 TIL','G&W3 TIL','G&W4 TIL','smooth (default)','smooth noncons','narrow range','narrow range noncons','wide range','wide range noncons','low trop','low trop noncons','high trop','high trop noncons','narrow high res','wide high res'])    
    #labels = (['default','even steps','uneven steps','narrow range','wide range','low trop','high trop','$\lambda_s/\lambda_t=0$','$\lambda_s/\lambda_t=-2$','one step','one center step','12'])
    colors = (['k',c_greys[0],c_blues[1],c_greys[0],'k',c_reds[1],c_reds[1],c_reds[1],c_reds[1],c_blues[1],c_blues[1],c_blues[1],c_blues[1],'y',c_reds[1]])
#    colors = (['k','k','k','k',c_reds[1],c_reds[1],c_reds[1],c_reds[1],c_blues[1],c_blues[1],c_blues[1],c_blues[1],c_blues[1],c_blues[1],'y',c_reds[1]])
    #colors = (['k',c_greys[0],c_greys[0],c_reds[1],c_reds[1],c_blues[1],c_blues[1],c_blues[1],c_blues[1],c_reds[1],c_reds[1],c_reds[1],c_blues[1],c_blues[1],c_blues[1],c_blues[1],'y',c_reds[1]])
    #colors = (['k',c_greys[0],c_greys[0],c_reds[1],c_reds[1],c_blues[1],c_blues[1],'y','y',c_greys[0],c_reds[1],c_blues[1]])
#    alphas = ([1,.3,1,.3,1,.5,1,.5,1,.5,1,.5,1,.5,1,.5,1,1])
    alphas = ([1,1,1,.3,1,1,1,1,1,1,1,1,1,1])
#    linestyles = ([':',':','-.','-.','-','-','--','--','-','-','--','--',':',':'])
    linestyles = (['-','-','-','-','-','--',':','-.','-','--','--','-','-','--','--','-',':'])
    #linestyles = (['-','-','--','-','--','-','--','-','--',':',':',':'])

    two_subplots = False
    
    if two_subplots == True:
        fig, (ax1,ax2) = plt.subplots(2,1,figsize=(20,14), dpi=300)
    else:
        fig, (ax1) = plt.subplots(figsize=(10,5), dpi=300)

    for e in range(1):#len(epsilon1)):
        for e2 in range(len(epsilon2)):
            try:
                sigmai_sorted_1
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_1 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_1[e,e2,:,-1],c=colors[1-1],alpha=alphas[1-1],ls=linestyles[1-1], lw=lw, label=labels[1-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_1[e,e2,:,-1],c=colors[1-1],alpha=alphas[1-1],ls=linestyles[1-1], lw=lw, label=labels[1-1])
            try:
                sigmai_sorted_2
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_2 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_2[e,e2,:,-1],c=colors[2-1],alpha=alphas[2-1], ls=linestyles[2-1], lw=lw, label=labels[2-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_2[e,e2,:,-1],c=colors[2-1],alpha=alphas[2-1], ls=linestyles[2-1], lw=lw, label=labels[2-1])
            try:
                sigmai_sorted_3
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_3 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_3[e,e2,:,-1],c=colors[3-1],alpha=alphas[3-1], ls=linestyles[3-1], lw=lw, label=labels[3-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_3[e,e2,:,-1],c=colors[3-1],alpha=alphas[3-1], ls=linestyles[3-1], lw=lw, label=labels[3-1])
            try:
                sigmai_sorted_4
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_4 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_4[e,e2,:,-1],c=colors[4-1],alpha=alphas[4-1], ls=linestyles[4-1], lw=lw, label=labels[4-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_4[e,e2,:,-1],c=colors[4-1],alpha=alphas[4-1], ls=linestyles[4-1], lw=lw, label=labels[4-1])
            try:
                sigmai_sorted_5
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_5 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_5[e,e2,:,-1],c=colors[5-1],alpha=alphas[5-1], ls=linestyles[5-1], lw=lw, label=labels[5-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_5[e,e2,:,-1],c=colors[5-1],alpha=alphas[5-1], ls=linestyles[5-1], lw=lw, label=labels[5-1])
            try:
                sigmai_sorted_6
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_6 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_6[e,e2,:,-1],c=colors[6-1],alpha=alphas[6-1], ls=linestyles[6-1], lw=lw, label=labels[6-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_6[e,e2,:,-1],c=colors[6-1],alpha=alphas[6-1], ls=linestyles[6-1], lw=lw, label=labels[6-1])
            try:
                sigmai_sorted_7
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_7 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_7[e,e2,:,-1],c=colors[7-1],alpha=alphas[7-1], ls=linestyles[7-1], lw=lw, label=labels[7-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_7[e,e2,:,-1],c=colors[7-1],alpha=alphas[7-1], ls=linestyles[7-1], lw=lw, label=labels[7-1])
            try:
                sigmai_sorted_8
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_8 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_8[e,e2,:,-1],c=colors[8-1],alpha=alphas[8-1], ls=linestyles[8-1], lw=lw, label=labels[8-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_8[e,e2,:,-1],c=colors[8-1],alpha=alphas[8-1], ls=linestyles[8-1], lw=lw, label=labels[8-1])
            try:
                sigmai_sorted_9
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_9 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_9[e,e2,:,-1],c=colors[9-1],alpha=alphas[9-1], ls=linestyles[9-1], lw=lw, label=labels[9-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_9[e,e2,:,-1],c=colors[9-1],alpha=alphas[9-1], ls=linestyles[9-1], lw=lw, label=labels[9-1])
            try:
                sigmai_sorted_10
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_10 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_10[e,e2,:,-1],c=colors[10-1],alpha=alphas[10-1], ls=linestyles[10-1], lw=lw, label=labels[10-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_10[e,e2,:,-1],c=colors[10-1],alpha=alphas[10-1], ls=linestyles[10-1], lw=lw, label=labels[10-1])
            try:
                sigmai_sorted_11
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_11 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_11[e,e2,:,-1],c=colors[11-1],alpha=alphas[11-1], ls=linestyles[11-1], lw=lw, label=labels[11-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_11[e,e2,:,-1],c=colors[11-1],alpha=alphas[11-1], ls=linestyles[11-1], lw=lw, label=labels[11-1])
            try:
                sigmai_sorted_12
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_12 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_12[e,e2,:,-1],c=colors[12-1],alpha=alphas[12-1], ls=linestyles[12-1], lw=lw, label=labels[12-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_12[e,e2,:,-1],c=colors[12-1],alpha=alphas[12-1], ls=linestyles[12-1], lw=lw, label=labels[12-1])
            try:
                sigmai_sorted_131
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_13 not defined')
            else:
                ax1.semilogx(wl,sigmai_sorted_13[e,e2,:,-1],c=colors[13-1],alpha=alphas[13-1], ls=linestyles[13-1], lw=lw, label=labels[13-1])
                if two_subplots == True:
                    ax2.semilogx(wl,sigmai_sorted_13[e,e2,:,-1],c=colors[13-1],alpha=alphas[13-1], ls=linestyles[13-1], lw=lw, label=labels[13-1])

    if two_subplots == True:
        ax1.text(1.423,1.1,'(a)',horizontalalignment='left',verticalalignment='top',fontsize=20) #1.423,1.1 #1.08,1.45
        ax2.text(2.465,0.975,'(b)',horizontalalignment='left',verticalalignment='top',fontsize=20) #2.465,0.975 #1.775,1.345
                
    #ax1.semilogx(wl,sigmai_sorted[e,e2,:,-1],c='y', lw=2*lw, alpha=.3)
    ax1.axhline(0,color='dimgrey',linewidth=1.5)
    if two_subplots == True:
        ax2.axhline(0,color='dimgrey',linewidth=1.5)
    #ax1.axvline(2.5)

#    sigmaplotcustom(ax1)
    ax1.set_ylabel('growth rate (days$^{-1}$)')#,labelpad=18)
#    ax1.set_yticks([0,1,2,3,4,5])
#    ax1.set_yticklabels([0,1,2,3,4,5], fontsize=25)
    ax1.tick_params(axis="y")
    ax1.set_ylim(bottom=0, top=1.35)#bottom=0, top=1.1)#bottom=0, top=1.45)#
    if two_subplots == True:
        ax2.set_ylabel('growth rate (days$^{-1}$)')
        ax2.tick_params(axis="y")
        ax2.set_ylim(bottom=0.925, top=0.975)#bottom=1.305, top=1.345)
        
    ax1.set_xlabel('wavelength (1000 km)')
    ax1.set_xticks(np.arange(2,20,2))
    ax1.set_xticklabels(np.arange(2,20,2))
    ax1.set_xlim(left=1.6,right=15.9)#left=1.75,right=20)#left=1.4,right=20)#
    ax1.xaxis.set_minor_formatter(NullFormatter())
    if two_subplots == True:
        ax2.set_xlabel('wavelength (1000 km)')
        ax2.set_xticklabels(np.arange(2,20,1))
        ax2.set_xticks(np.arange(2,20,1))
        ax2.set_xlim(left=2.6,right=4.6)#left=1.9,right=3.8)
#        ax2.set_xlim(2.8,5)
        ax2.xaxis.set_minor_formatter(NullFormatter())
            
    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    leg = ax1.legend(handlelength=2.1, loc='upper right', fontsize=15)
    leg.get_frame().set_alpha(1)
    if two_subplots == True:
        box = ax2.get_position()
        ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        leg = ax2.legend(handlelength=2.1, loc='upper right', fontsize=15)
        leg.get_frame().set_alpha(1)

    #plt.grid()
    fig.savefig(f'/home/kfl078/Downloads/growthrates_tropsens.pdf', transparent=True, bbox_inches='tight', pad_inches=0.1)

    if phase_speed == True:

        global sigmar_sorted_1, sigmar_sorted_1b, sigmar_sorted_2, sigmar_sorted_3, sigmar_sorted_4
        global sigmar_sorted_5, sigmar_sorted_6, sigmar_sorted_7
        global sigmar_sorted_8, sigmar_sorted_9, sigmar_sorted_10, sigmar_sorted_11

        ### plotting the growth rate (and phase speed) ----------------------------

        
        fig, (ax1) = plt.subplots(figsize=(15,7.5), dpi=300)

        if lambda1[-1]*(1-p[jtrop]) < 4:
            ax1.axhline(lambda1[-1]*(1-p[jtrop]),color='dimgrey',ls='--',linewidth=1.5)
            ax1.text(40,lambda1[-1]*(1-p[jtrop]),'u @ tropopause',fontsize=14,horizontalalignment='right',verticalalignment='bottom')
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                try:
                    sigmai_sorted_1
                except:
                    pass
                else:
                    if (sigmai_sorted_1 == sigmai_sorted).all() == True:
                        sigmar_sorted_1 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_1[e,e2,i,-1] > 0.01 and sigmai_sorted_1[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_1[e,e2,i2,-1] < 0.01 and sigmai_sorted_1[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_1[e,e2,i:i2,-1]/k[i:i2],c=colors[1-1],alpha=alphas[1-1], ls=linestyles[1-1], lw=lw)
                                    break
                                if (sigmai_sorted_1[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_1[e,e2,i:,-1]/k[i:],c=colors[1-1],alpha=alphas[1-1], ls=linestyles[1-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_1[e,e2,:,-1] == np.max(sigmai_sorted_1[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_1[e,e2,index,-1]/k[index],c=colors[1-1],alpha=alphas[1-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[1-1],alpha=alphas[1-1], ls=linestyles[1-1], lw=lw, label=labels[1-1])
                try:
                    sigmai_sorted_2
                except:
                    pass
                else:
                    if (sigmai_sorted_2 == sigmai_sorted).all() == True:
                        sigmar_sorted_2 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_2[e,e2,i,-1] > 0.01 and sigmai_sorted_2[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_2[e,e2,i2,-1] < 0.01 and sigmai_sorted_2[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_2[e,e2,i:i2,-1]/k[i:i2],c=colors[2-1],alpha=alphas[2-1], ls=linestyles[2-1], lw=lw)
                                    break
                                if (sigmai_sorted_2[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_2[e,e2,i:,-1]/k[i:],c=colors[2-1],alpha=alphas[2-1], ls=linestyles[2-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_2[e,e2,:,-1] == np.max(sigmai_sorted_2[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_2[e,e2,index,-1]/k[index],c=colors[2-1],alpha=alphas[2-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[2-1],alpha=alphas[2-1], ls=linestyles[2-1], lw=lw, label=labels[2-1])
                try:
                    sigmai_sorted_3
                except:
                    pass
                else:
                    if (sigmai_sorted_3 == sigmai_sorted).all() == True:
                        sigmar_sorted_3 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_3[e,e2,i,-1] > 0.01 and sigmai_sorted_3[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_3[e,e2,i2,-1] < 0.01 and sigmai_sorted_3[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_3[e,e2,i:i2,-1]/k[i:i2],c=colors[3-1],alpha=alphas[3-1], ls=linestyles[3-1], lw=lw)
                                    break
                                if (sigmai_sorted_3[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_3[e,e2,i:,-1]/k[i:],c=colors[3-1],alpha=alphas[3-1], ls=linestyles[3-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_3[e,e2,:,-1] == np.max(sigmai_sorted_3[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_3[e,e2,index,-1]/k[index],c=colors[3-1],alpha=alphas[3-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[3-1],alpha=alphas[3-1], ls=linestyles[3-1], lw=lw, label=labels[3-1])
                try:
                    sigmai_sorted_4
                except:
                    pass
                else:
                    if (sigmai_sorted_4 == sigmai_sorted).all() == True:
                        sigmar_sorted_4 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_4[e,e2,i,-1] > 0.01 and sigmai_sorted_4[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_4[e,e2,i2,-1] < 0.01 and sigmai_sorted_4[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_4[e,e2,i:i2,-1]/k[i:i2],c=colors[4-1],alpha=alphas[4-1], ls=linestyles[4-1], lw=lw)
                                    break
                                if (sigmai_sorted_4[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_4[e,e2,i:,-1]/k[i:],c=colors[4-1],alpha=alphas[4-1], ls=linestyles[4-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_4[e,e2,:,-1] == np.max(sigmai_sorted_4[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_4[e,e2,index,-1]/k[index],c=colors[4-1],alpha=alphas[4-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[4-1],alpha=alphas[4-1], ls=linestyles[4-1], lw=lw, label=labels[4-1])
                try:
                    sigmai_sorted_5
                except:
                    pass
                else:
                    if (sigmai_sorted_5 == sigmai_sorted).all() == True:
                        sigmar_sorted_5 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_5[e,e2,i,-1] > 0.01 and sigmai_sorted_5[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_5[e,e2,i2,-1] < 0.01 and sigmai_sorted_5[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_5[e,e2,i:i2,-1]/k[i:i2],c=colors[5-1],alpha=alphas[5-1], ls=linestyles[5-1], lw=lw)
                                    break
                                if (sigmai_sorted_5[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_5[e,e2,i:,-1]/k[i:],c=colors[5-1],alpha=alphas[5-1], ls=linestyles[5-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_5[e,e2,:,-1] == np.max(sigmai_sorted_5[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_5[e,e2,index,-1]/k[index],c=colors[5-1],alpha=alphas[5-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[5-1], ls=linestyles[5-1],alpha=alphas[5-1], lw=lw, label=labels[5-1])
                try:
                    sigmai_sorted_6
                except:
                    pass
                else:
                    if (sigmai_sorted_6 == sigmai_sorted).all() == True:
                        sigmar_sorted_6 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_6[e,e2,i,-1] > 0.01 and sigmai_sorted_6[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_6[e,e2,i2,-1] < 0.01 and sigmai_sorted_6[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_6[e,e2,i:i2,-1]/k[i:i2],c=colors[6-1],alpha=alphas[6-1], ls=linestyles[6-1], lw=lw)
                                    break
                                if (sigmai_sorted_6[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_6[e,e2,i:,-1]/k[i:],c=colors[6-1],alpha=alphas[6-1], ls=linestyles[6-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_6[e,e2,:,-1] == np.max(sigmai_sorted_6[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_6[e,e2,index,-1]/k[index],c=colors[6-1],alpha=alphas[6-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[6-1],alpha=alphas[6-1], ls=linestyles[6-1], lw=lw, label=labels[6-1]) 
                try:
                    sigmai_sorted_7
                except:
                    pass
                else:
                    if (sigmai_sorted_7 == sigmai_sorted).all() == True:
                        sigmar_sorted_7 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_7[e,e2,i,-1] > 0.01 and sigmai_sorted_7[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_7[e,e2,i2,-1] < 0.01 and sigmai_sorted_7[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_7[e,e2,i:i2,-1]/k[i:i2],c=colors[7-1],alpha=alphas[7-1], ls=linestyles[7-1], lw=lw)
                                    break
                                if (sigmai_sorted_7[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_7[e,e2,i:,-1]/k[i:],c=colors[7-1],alpha=alphas[7-1], ls=linestyles[7-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_7[e,e2,:,-1] == np.max(sigmai_sorted_7[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_7[e,e2,index,-1]/k[index],c=colors[7-1],alpha=alphas[7-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[7-1],alpha=alphas[7-1], ls=linestyles[7-1], lw=lw, label=labels[7-1])
                try:
                    sigmai_sorted_8
                except:
                    pass
                else:
                    if (sigmai_sorted_8 == sigmai_sorted).all() == True:
                        sigmar_sorted_8 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_8[e,e2,i,-1] > 0.01 and sigmai_sorted_8[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_8[e,e2,i2,-1] < 0.01 and sigmai_sorted_8[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_8[e,e2,i:i2,-1]/k[i:i2],c=colors[8-1],alpha=alphas[8-1], ls=linestyles[8-1], lw=lw)
                                    break
                                if (sigmai_sorted_8[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_8[e,e2,i:,-1]/k[i:],c=colors[8-1],alpha=alphas[8-1], ls=linestyles[8-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_8[e,e2,:,-1] == np.max(sigmai_sorted_8[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_8[e,e2,index,-1]/k[index],c=colors[8-1],alpha=alphas[8-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[8-1],alpha=alphas[8-1], ls=linestyles[8-1], lw=lw, label=labels[8-1])
                try:
                    sigmai_sorted_9
                except:
                    pass
                else:
                    if (sigmai_sorted_9 == sigmai_sorted).all() == True:
                        sigmar_sorted_9 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_9[e,e2,i,-1] > 0.01 and sigmai_sorted_9[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_9[e,e2,i2,-1] < 0.01 and sigmai_sorted_9[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_9[e,e2,i:i2,-1]/k[i:i2],c=colors[9-1],alpha=alphas[9-1], ls=linestyles[9-1], lw=lw)
                                    break
                                if (sigmai_sorted_9[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_9[e,e2,i:,-1]/k[i:],c=colors[9-1],alpha=alphas[9-1], ls=linestyles[9-1], lw=lw)
                    index = np.argwhere(sigmai_sorted_9[e,e2,:,-1] == np.max(sigmai_sorted_9[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_9[e,e2,index,-1]/k[index],c=colors[9-1],alpha=alphas[9-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[9-1],alpha=alphas[9-1], ls=linestyles[9-1], lw=lw, label=labels[9-1])
                try:
                    sigmai_sorted_10
                except:
                    pass
                else:
                    if (sigmai_sorted_10 == sigmai_sorted).all() == True:
                        sigmar_sorted_10 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_10[e,e2,i,-1] > 0.01 and sigmai_sorted_10[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_10[e,e2,i2,-1] < 0.01 and sigmai_sorted_10[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_10[e,e2,i:i2,-1]/k[i:i2],c=colors[10-1],alpha=alphas[10-1], ls=linestyles[10-1], lw=lw)
                                    break
                                if (sigmai_sorted_10[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_10[e,e2,i:,-1]/k[i:],c=colors[10-1],alpha=alphas[10-1], ls=linestyles[10-1], lw=lw, label=labels[10-1])
                    index = np.argwhere(sigmai_sorted_10[e,e2,:,-1] == np.max(sigmai_sorted_10[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_10[e,e2,index,-1]/k[index],c=colors[10-1],alpha=alphas[10-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[10-1],alpha=alphas[10-1], ls=linestyles[10-1], lw=lw, label=labels[10-1])
                try:
                    sigmai_sorted_11
                except:
                    pass
                else:
                    if (sigmai_sorted_11 == sigmai_sorted).all() == True:
                        sigmar_sorted_11 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_11[e,e2,i,-1] > 0.01 and sigmai_sorted_11[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_11[e,e2,i2,-1] < 0.01 and sigmai_sorted_11[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_11[e,e2,i:i2,-1]/k[i:i2],c=colors[11-1],alpha=alphas[11-1], ls=linestyles[11-1], lw=lw)
                                    break
                                if (sigmai_sorted_11[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_11[e,e2,i:,-1]/k[i:],c=colors[11-1],alpha=alphas[11-1], ls=linestyles[11-1], lw=lw, label=labels[11-1])
                    index = np.argwhere(sigmai_sorted_11[e,e2,:,-1] == np.max(sigmai_sorted_11[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_11[e,e2,index,-1]/k[index],c=colors[11-1],alpha=alphas[11-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[11-1],alpha=alphas[11-1], ls=linestyles[11-1], lw=lw, label=labels[11-1])
                try:
                    sigmai_sorted_12
                except:
                    pass
                else:
                    if (sigmai_sorted_12 == sigmai_sorted).all() == True:
                        sigmar_sorted_12 = sigmar_sorted
                    for i in range(len(wl)):
                        if (sigmai_sorted_12[e,e2,i,-1] > 0.01 and sigmai_sorted_12[e,e2,i-1,-1] < 0.01):
                            for i2 in range(i,len(wl)):
                                if (sigmai_sorted_12[e,e2,i2,-1] < 0.01 and sigmai_sorted_12[e,e2,i2-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:i2],sigmar_sorted_12[e,e2,i:i2,-1]/k[i:i2],c=colors[12-1],alpha=alphas[12-1], ls=linestyles[12-1], lw=lw)
                                    break
                                if (sigmai_sorted_12[e,e2,-1,-1] > 0.01):
                                    ax1.semilogx(wl[i:],sigmar_sorted_12[e,e2,i:,-1]/k[i:],c=colors[12-1],alpha=alphas[12-1], ls=linestyles[12-1], lw=lw, label=labels[12-1])
                    index = np.argwhere(sigmai_sorted_12[e,e2,:,-1] == np.max(sigmai_sorted_12[e,e2,:,-1]))
                    ax1.plot(wl[index],sigmar_sorted_12[e,e2,index,-1]/k[index],c=colors[12-1],alpha=alphas[12-1],marker='.',markersize=15)
                    ax1.semilogx((),(),c=colors[12-1],alpha=alphas[12-1], ls=linestyles[12-1], lw=lw, label=labels[12-1])
                          
        #ax1.semilogx(wl,sigmar_sorted[e,e2,:,-1]/k,c='y', lw=2*lw, alpha=.3)
        ax1.axhline(0,color='dimgrey',linewidth=1.5)

    #    sigmaplotcustom(ax1)
        ax1.set_ylabel('phase speed (m/s)')# (m/s)')
    #    ax1.set_yticks([0,1,2,3,4,5])
    #    ax1.set_yticklabels([0,1,2,3,4,5], fontsize=25)
        ax1.tick_params(axis="y")
        ax1.set_ylim(bottom=.5, top=3)
        ticks_y = ticker.FuncFormatter(lambda wl, pos: '{0:g}'.format(wl*10))
        ax1.yaxis.set_major_formatter(ticks_y)
        
#        ax2 = ax1.twinx()
#        ax2.invert_yaxis()
#        y1,y2 = ax1.get_ylim()
#        ax2.set_ylim(1000*p[np.argwhere(u<=y1)[0][0]],p[np.argwhere(u<=y2)[0][0]])
#        ax2.set_ylabel('pressure (hPa)', rotation=270, labelpad=30)
            
        ax1.set_xlabel('wavelength (1000 km)')
        ax1.set_xticks(np.arange(2,20,2))
        ax1.set_xticklabels(np.arange(2,20,2))
    #    ax1.set_xticks(np.arange(3,6,.5))
    #    ax1.set_xticklabels(np.arange(3,6,.5), fontsize=25)
        ax1.set_xlim(left=.9, right=40)#,20)#1.8
        ax1.xaxis.set_minor_formatter(NullFormatter())
                
        box = ax1.get_position()
        ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        leg = ax1.legend(handlelength=2.1, loc=2, fontsize=15)
        leg.get_frame().set_alpha(.5)
        
# -----------------------------------------------------------------------------
        
def save_growthrates(data,i):

    data = data; i=i # what data do you want to save?

    with open(f'model_output/sigmai_sorted__sharp_CTL/sigmai_sorted_{i}.csv', 'w') as outfile:
        # We write this header for readable, the pound symbol
        # will cause numpy to ignore it
        outfile.write('# Array shape: {0}\n'.format(data.shape))

        # Iterating through a ndimensional array produces slices along
        # the last axis. This is equivalent to data[i,:,:] in this case.
        # Because we are dealing with 4D data instead of 3D data,
        # we need to add another for loop that's nested inside of the
        # previous one.
        for threeD_data_slice in data:
            for twoD_data_slice in threeD_data_slice:
                # The formatting string indicates that I'm writing out
                # the values in left-justified columns 7 characters in width
                # with 2 decimal places. 
                np.savetxt(outfile, twoD_data_slice)#, fmt='%-7.2f')
                # Writing out a break to indicate different slices...
                outfile.write('# New slice\n')
                
    
# -----------------------------------------------------------------------------
        
def load_growthrates(data,i):
    
    data = data; i=i # what data do you want to load?
    
    print (i)
    
    new_data = np.loadtxt(f'model_output/sigmai_sorted__no_latent_heating/sigmai_sorted_{i}.csv')
    # Note that this returned a 2D array!
    print(new_data.shape)

    # However, going back to 3D is easy if we know the 
    # original shape of the array
    new_data = new_data.reshape(np.shape(sigmai_sorted))

    # Just to check that they're the same...
    #assert np.all(new_data == data)
    
    return new_data
    
    
# -----------------------------------------------------------------------------

### checking sensitivity to stability parameter for dry vs moist cases

def stability_sensitivity_check():
    
    if heating1 == True and heating2 == False and S1 == 8:#lambda1[0] == 3.5:#
        wl_lhws = wl
        sigmai_sorted_lhws = sigmai_sorted
    if heating1 == True and heating2 == False and S1 == 4:#lambda1[0] == 7:
        wl_lhss = wl
        sigmai_sorted_lhss = sigmai_sorted
    if heating1 == False and heating2 == False and S1 == 8:#lambda1[0] == 3.5:
        wl_nhws = wl
        sigmai_sorted_nhws = sigmai_sorted
    if heating1 == False and heating2 == False and S1 == 4:#lambda1[0] == 7:
        wl_nhss = wl
        sigmai_sorted_nhss = sigmai_sorted
   
    fig, (ax1) = plt.subplots(figsize=(14,5))

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
        
            try:
                sigmai_sorted_lhws
            except NameError:
                print ('sigmai_sorted_lhws not defined')
            else:#, dashes=(ms,ms)
                #arg = np.argwhere(sigmai_sorted_surf1[e,e2,:,-1]>0.01)[0][0]
                #ax1.semilogx(wl_nosurf[arg:],sigmai_sorted_nosurf[e,e2,arg:,0]/sigmai_sorted_surf1[e,e2,arg:,0],c=csurf[0],dashes=(12,12),linewidth=ms, label='Latent heating/no heating, weak shear')#No surface fluxes
                for i in range(1,2):
                    #ax1.semilogx(wl_nosurf[arg:],sigmai_sorted_nosurf[e,e2,arg:,i]/sigmai_sorted_surf1[e,e2,arg:,i],c=csurf[0],dashes=(12,12), linewidth=ms)
                    ax1.semilogx(wl_lhws[:],sigmai_sorted_lhws[e,e2,:,-1],color=c[1],dashes=(12,12), linewidth=ms, label='Latent heating, weak shear')#strong stratification')#
            #plot(wl[np.argwhere(sigmai_sorted_nosurf[e,e2]==np.max(sigmai_sorted_nosurf))[0][0]],np.max(sigmai_sorted_nosurf),'*',markersize=10,color=csurf[0])
        
            try:
                sigmai_sorted_lhss
            except NameError:
                print ('sigmai_sorted_lhss not defined')
            else:#, dashes=(ms,ms)
                #arg = np.argwhere(sigmai_sorted_surf2[e,e2,:,-1]>0.01)[0][0]
                #ax1.semilogx(wl_surf05[arg:],sigmai_sorted_surf05[e,e2,arg:,0]/sigmai_sorted_surf2[e,e2,arg:,0],c=csurf[0], linewidth=ms, label='Latent heating/no heating, strong shear')
                for i in range(1,2):
                    #ax1.semilogx(wl_surf05[arg:],sigmai_sorted_surf05[e,e2,arg:,i]/sigmai_sorted_surf2[e,e2,arg:,i],c=csurf[0], linewidth=ms)
                    ax1.semilogx(wl_lhss[:],sigmai_sorted_lhss[e,e2,:,-1],color=c[1], linewidth=ms, label='Latent heating, strong shear')
            #plot(wl[np.argwhere(sigmai_sorted_surf05[e,e2]==np.max(sigmai_sorted_surf05))[0][0]],np.max(sigmai_sorted_surf05),'*',markersize=10,color=csurf[0])
            
            try:
                sigmai_sorted_nhws
            except NameError:
                print ('sigmai_sorted_nhws not defined')
            else:
                #ax1.semilogx(wl_nhws,sigmai_sorted_nhws[e,e2,:,0],c='grey',dashes=(12,12),linewidth=ms, label='No heating, weak shear')#,dashes=(ms+8,ms+4)
                for i in range(1,2):
                    #ax1.semilogx(wl_nhws,sigmai_sorted_nhws[e,e2,:,i],c='grey',dashes=(12,12),linewidth=ms)
                    ax1.semilogx(wl_nhws,sigmai_sorted_nhws[e,e2,:,-i],c='grey',dashes=(12,12),linewidth=ms, label='No heating, weak shear')
                #plot(wl[np.argwhere(sigmai_sorted_surf1[e,e2]==np.max(sigmai_sorted_surf1))[0][0]],np.max(sigmai_sorted_surf1),'*',markersize=10,color='grey')
            
            try:
                sigmai_sorted_nhss
            except NameError:
                print ('sigmai_sorted_nhss not defined')
            else:
                #ax1.semilogx(wl_surf2,sigmai_sorted_surf2[e,e2,:,0],c='grey', linewidth=ms, label='No heating, strong shear')#,dashes=(ms+4,ms+2,ms,ms+2)
                for i in range(1,2):
                    #ax1.semilogx(wl_surf2,sigmai_sorted_surf2[e,e2,:,i],c='grey',linewidth=ms)
                    ax1.semilogx(wl_nhss,sigmai_sorted_nhss[e,e2,:,-i],c='grey',linewidth=ms, label='No heating, strong shear')
                #plot(wl[np.argwhere(sigmai_sorted_surf2[e,e2]==np.max(sigmai_sorted_surf2))[0][0]],np.max(sigmai_sorted_surf2),'*',markersize=10,color='grey')

    ax1.axhline(0,color='dimgrey',linewidth=ms+1)
    ax1.set_xticks([.1,.5,1,5,10,50])
    ax1.set_xticklabels([100,500,1000,5000,10000,50000])
    ax1.set_xlim((.2, 60))
    ax1.set_xlabel('Wavelength (km)',fontsize=24)
    ax1.set_ylabel('Growth rate (day$\mathregular{^{-1}}$)',fontsize=24)
    #ax1.set_yticks([0,1,2,3,4])#.5,1,1.5,2,2.5,3])
    ax1.set_ylim(0,4)
    ax1.tick_params(axis='both', labelsize=20)
    plt.legend(loc=1, handlelength=3.75, prop={'size': 16})

    plt.show()
    
# -----------------------------------------------------------------------------    
    
### comparing sensitivity to stability parameter for dry vs moist cases

def stability_sensitivity_compare():
    
    try:
        stab_vec
    except:
        ratio = ([])
        stab_vec = ([])
    if S1 == 2:
        if heating1 == False:
            maxEady_2 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_2 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_2 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_2[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_2 and maxLH_2
        except:
            print ('growth rates for stability = 2 not defined')
        else:
            ratio.extend([maxLH_2/maxEady_2])
            stab_vec.extend([S1])
    if S1 == 3:
        if heating1 == False:
            maxEady_3 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_3 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_3 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_3[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_3 and maxLH_3
        except:
            print ('growth rates for stability = 3 not defined')
        else:
            ratio.extend([maxLH_3/maxEady_3])
            stab_vec.extend([S1])
    if S1 == 3.5:
        if heating1 == False:
            maxEady_35 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_35 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_35 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_35[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_35 and maxLH_35
        except:
            print ('growth rates for stability = 3.5 not defined')
        else:
            ratio.extend([maxLH_35/maxEady_35])
            stab_vec.extend([S1])
    if S1 == 4:
        if heating1 == False:
            maxEady_4 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_4 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_4 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_4[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_4 and maxLH_4
        except:
            print ('growth rates for stability = 4 not defined')
        else:
            ratio.extend([maxLH_4/maxEady_4])
            stab_vec.extend([S1])
    if S1 == 4.5:
        if heating1 == False:
            maxEady_45 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_45 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_45 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_45[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_45 and maxLH_45
        except:
            print ('growth rates for stability = 4.5 not defined')
        else:
            ratio.extend([maxLH_45/maxEady_45])
            stab_vec.extend([S1])
    if S1 == 5:
        if heating1 == False:
            maxEady_5 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_5 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_5 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_5[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_5 and maxLH_5
        except:
            print ('growth rates for stability = 5 not defined')
        else:
            ratio.extend([maxLH_5/maxEady_5])
            stab_vec.extend([S1])
    if S1 == 5.5:
        if heating1 == False:
            maxEady_55 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_55 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_55 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_55[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_55 and maxLH_55
        except:
            print ('growth rates for stability = 5.5 not defined')
        else:
            ratio.extend([maxLH_55/maxEady_55])
            stab_vec.extend([S1])
    if S1 == 6:
        if heating1 == False:
            maxEady_6 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_6 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_6 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_6[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_6 and maxLH_6
        except:
            print ('growth rates for stability = 6 not defined')
        else:
            ratio.extend([maxLH_6/maxEady_6])
            stab_vec.extend([S1])
    if S1 == 6.5:
        if heating1 == False:
            maxEady_65 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_65 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_65 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_65[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_65 and maxLH_65
        except:
            print ('growth rates for stability = 6.5 not defined')
        else:
            ratio.extend([maxLH_65/maxEady_65])
            stab_vec.extend([S1])
    if S1 == 7:
        if heating1 == False:
            maxEady_7 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_7 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_7 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_7[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_7 and maxLH_7
        except:
            print ('growth rates for stability = 7 not defined')
        else:
            ratio.extend([maxLH_7/maxEady_7])
            stab_vec.extend([S1])
    if S1 == 8:
        if heating1 == False:
            maxEady_8 = np.max(sigmai_sorted[eps1_index,eps2_index,:,-1])
        if heating1 == True and epsilon1[0] == 0:
            maxEady_8 = np.max(sigmai_sorted[0,eps2_index,:,-1])
            maxLH_8 = np.zeros(len(epsilon1)-1)
            for e in range(1,len(epsilon1)):
                maxLH_8[e-1] = np.max(sigmai_sorted[e,eps2_index,:,-1])
        try:
            maxEady_8 and maxLH_8
        except:
            print ('growth rates for stability = 8 not defined')
        else:
            ratio.extend([maxLH_8/maxEady_8])
            stab_vec.extend([S1])
            
            
    stab_vec_temp = np.array(stab_vec)
    ratio_temp = np.array(ratio)
    stab_vec_sort = stab_vec_temp[stab_vec_temp.argsort()]
    ratio_sort = ratio_temp[stab_vec_temp.argsort()]
    
    if len(stab_vec_sort) > 0:
        arg = np.argwhere(stab_vec_sort == 2)[0][0]
        vgrad = np.gradient(ratio_sort[arg:])
        fulgrad = np.sqrt(vgrad[0]**2 + vgrad[1]**2)

        fig, (ax) = plt.subplots(figsize=(7,4))
    
        ax = plt.contourf(stab_vec_sort[arg:],epsilon1[1:],np.transpose(ratio_sort[arg:]),16,cmap=cm_br)
        plt.colorbar()
        levels = np.arange(-3,0,.2)
        #CS = plt.contour(stab_vec_sort[arg:],epsilon1[1:],np.transpose(abs(fulgrad)),colors='k')
        CS = plt.contour(stab_vec_sort[arg:],epsilon1[1:],np.transpose((vgrad[0])),colors='k')
#        plt.contour(stab_vec_sort[arg:],epsilon1[1:],np.transpose(abs(vgrad[1])),colors='b')
        plt.clabel(CS, fontsize=9, inline=1, fmt='%1.1f')
        #plt.title('ratio between most unstable solutions for latent heating vs dry Eady')
        plt.ylabel('heating intensity parameter $\mathregular{\\varepsilon}$')
        plt.xlabel('stability parameter')
        #plt.xlim(4,8)
        plt.yticks([5,7,9,11,13,15])
        plt.show()
        
# -----------------------------------------------------------------------------
        
### checking sensitivity to heating parameter for surface fluxes

def surface_flux_sensitivity():

    if heating1 == True and heating2 == False:
        wl_nosurf = wl
        sigmai_sorted_nosurf = sigmai_sorted
    if heating1 == True and heating2 == True and epsilon2[eps2_index] == .5:
        wl_surf05 = wl
        sigmai_sorted_surf05 = sigmai_sorted
    if heating1 == True and heating2 == True and epsilon2[eps2_index] == 1:
        wl_surf1 = wl
        sigmai_sorted_surf1 = sigmai_sorted
    if heating1 == True and heating2 == True and epsilon2[eps2_index] == 2:
        wl_surf2 = wl
        sigmai_sorted_surf2 = sigmai_sorted
    if heating1 == True and heating2 == True and epsilon2[eps2_index] == 5:
        wl_surf5 = wl
        sigmai_sorted_surf5 = sigmai_sorted
        
    fig, (ax1) = plt.subplots(figsize=(14,5))

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
        
            try:
                sigmai_sorted_nosurf
            except NameError:
                print ('sigmai_sorted_nosurf not defined')
            else:#, dashes=(ms,ms)
                ax1.semilogx(wl_nosurf,sigmai_sorted_nosurf[e,e2,:,0],color=c[1],dashes=(12,12),linewidth=ms, label='$\mathregular{\\varepsilon_{SF}}$ = 0')#No surface fluxes
                for i in range(1,2):
                    ax1.semilogx(wl_nosurf,sigmai_sorted_nosurf[e,e2,:,i],color=c[1],dashes=(12,12), linewidth=ms)
                    ax1.semilogx(wl_nosurf,sigmai_sorted_nosurf[e,e2,:,-i],color=c[1],dashes=(12,12), linewidth=ms)
        
            try:
                sigmai_sorted_surf05
            except NameError:
                print ('sigmai_sorted_surf05 not defined')
            else:#, dashes=(ms,ms)
                ax1.semilogx(wl_surf05,sigmai_sorted_surf05[e,e2,:,0],c=c_greys[0], linewidth=ms, label='$\mathregular{\\varepsilon_{SF}}$ = 0.5')
                for i in range(1,3):
                    ax1.semilogx(wl_surf05,sigmai_sorted_surf05[e,e2,:,i],c=c_greys[0], linewidth=ms)
                    ax1.semilogx(wl_surf05,sigmai_sorted_surf05[e,e2,:,-i],c=c_greys[0], linewidth=ms)
            
            try:
                sigmai_sorted_surf1
            except NameError:
                print ('sigmai_sorted_surf1 not defined')
            else:
                ax1.semilogx(wl_surf1,sigmai_sorted_surf1[e,e2,:,0],c=c_greys[1],linewidth=ms, label='$\mathregular{\\varepsilon_{SF}}$ = 1.0')#,dashes=(ms+8,ms+4)
                for i in range(1,5):
                    ax1.semilogx(wl_surf1,sigmai_sorted_surf1[e,e2,:,i],c=c_greys[1],linewidth=ms)
                    ax1.semilogx(wl_surf1,sigmai_sorted_surf1[e,e2,:,-i],c=c_greys[1],linewidth=ms)
            
            try:
                sigmai_sorted_surf2
            except NameError:
                print ('sigmai_sorted_surf2 not defined')
            else:
                ax1.semilogx(wl_surf2,sigmai_sorted_surf2[e,e2,:,0],c=c_greys[2], linewidth=ms, label='$\mathregular{\\varepsilon_{SF}}$ = 2.0')#,dashes=(ms+4,ms+2,ms,ms+2)
                for i in range(1,5):
                    ax1.semilogx(wl_surf2,sigmai_sorted_surf2[e,e2,:,i],c=c_greys[2],linewidth=ms)
                    ax1.semilogx(wl_surf2,sigmai_sorted_surf2[e,e2,:,-i],c=c_greys[2],linewidth=ms)
            
            try:
                sigmai_sorted_surf511
            except NameError:
                print ('sigmai_sorted_surf5 not defined')
            else:
                ax1.semilogx(wl_surf5,sigmai_sorted_surf5[e,e2,:,0],c=c_greys[3],linestyle='-', linewidth=ms, label='$\mathregular{\\varepsilon_{SF}}$ = 5.0')
                for i in range(1,5):
                    ax1.semilogx(wl_surf5,sigmai_sorted_surf5[e,e2,:,i],c=c_greys[3],linestyle='-',linewidth=ms)
                    ax1.semilogx(wl_surf5,sigmai_sorted_surf5[e,e2,:,-i],c_greys[3],linestyle='-',linewidth=ms)#, alpha=.9)

    ax1.axhline(0,color='dimgrey',linewidth=ms+1)
    ax1.set_xticks([.1,.5,1,5,10,50])
    ax1.set_xticklabels([100,500,1000,5000,10000,50000])
    ax1.set_xlim((.2, 60))
    ax1.set_xlabel('Wavelength (km)',fontsize=24)
    ax1.set_ylabel('Growth rate (day$\mathregular{^{-1}}$)',fontsize=24)
    ax1.set_yticks([0,1,2,3,4])#.5,1,1.5,2,2.5,3])
    ax1.set_ylim(0,4.5)
    ax1.tick_params(axis='both', labelsize=20)
    plt.legend(loc=1, handlelength=3.75, prop={'size': 17})

    plt.show()
    
    
# -----------------------------------------------------------------------------

### checking sensitivity to top of heating layer

def ptlc_sensitivity():

    ptlc_num = 17
    try:
        ptlc_vec
    except:
        ptlc_vec = np.zeros(ptlc_num)
        sigmai3D_ptlc = np.zeros((ptlc_num,len(k)))
    
    if heating1 == True and h1pro == False and heating2 == False and .89 < pblc <.91:
        i=0
        if .19 < ptlc < .21:
            ptlc_vec[i] = .15#ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .24 < ptlc < .26:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .29 < ptlc < .31:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .34 < ptlc < .36:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .39 < ptlc < .41:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .44 < ptlc < .46:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .49 < ptlc < .51:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .54 < ptlc < .59:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .59 < ptlc < .61:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .64 < ptlc < .66:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .69 < ptlc < .71:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .72 < ptlc < .73:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .74 < ptlc < .76:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .77 < ptlc < .78:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .79 < ptlc < .81:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .82 < ptlc < .83:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .84 < ptlc < .86:
            ptlc_vec[i] = ptlc
            sigmai3D_ptlc[i,:] = sigmai_sorted[e,e2,:,-1]
        
    norm = MidpointNormalize(midpoint=0)
        
    fig, (ax1) = plt.subplots(figsize=(12,3.7))

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):        
            sig = ax1.contourf(wl,ptlc_vec,sigmai3D_ptlc,60,norm=norm,cmap=cm_br)
    fig.colorbar(sig)
    ax1.set_title('growth rate (day$\mathregular{^{-1}}$)',fontsize=18)
    ax1.set_xscale('log')
    ax1.set_xlim((.085, 60))
    ax1.set_xticks([.1,.5,1,5,10,50])
    ax1.set_xticklabels([100,500,1000,5000,10000,50000])
    ax1.set_yticks([.2,.4,.6,.8])
    ax1.set_yticklabels([200,400,600,800])
    ax1.set_xlabel('wavelength (km)',fontsize=16)
    ax1.set_ylabel('pressure at top of heating layer (hPa)',fontsize=16)
    #ax1.set_yticks([0,1,2,3])
    ax1.set_ylim(.15,.85)
    ax1.invert_yaxis()
    #ax1.tick_params(axis='both', labelsize=18)
    #plt.legend(loc=2, handlelength=3.75, prop={'size': 14})
    ax1.tick_params(axis='both', labelsize=14)

    plt.show()
    
# -----------------------------------------------------------------------------

### checking sensitivity to bottom of heating layer

def pblc_sensitivity():

    pblc_num = 11
    try:
        pblc_vec
    except:
        pblc_vec = np.zeros(pblc_num)
        sigmai3D_pblc = np.zeros((pblc_num,len(k)))
    
    if heating1 == True and h1pro == False and heating2 == False and .39 < ptlc <.41:
        i=0
        if .59 < pblc < .61:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .64 < pblc < .66:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .69 < pblc < .71:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .74 < pblc < .76:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .79 < pblc < .81:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .84 < pblc < .86:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .89 < pblc < .91:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .92 < pblc < .93:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .94 < pblc < .96:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .97 < pblc < .98:
            pblc_vec[i] = pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        i=i+1
        if .99 < pblc < 1.:
            pblc_vec[i] = 1#pblc
            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
#        i=i+1
#        if .974 < pblc < .976:
#            pblc_vec[i] = 1#pblc
#            sigmai3D_pblc[i,:] = sigmai_sorted[e,e2,:,-1]
        
    norm = MidpointNormalize(midpoint=0)
        
    fig, (ax1) = plt.subplots(figsize=(12,3.7))

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):        
            sig = ax1.contourf(wl,pblc_vec,sigmai3D_pblc,15,norm=norm,cmap=cm_br)
    fig.colorbar(sig)
    ax1.set_title('growth rate (day$\mathregular{^{-1}}$)',fontsize=18)
    ax1.set_xscale('log')
    ax1.set_xlim((.085, 60))
    ax1.set_xticks([.1,.5,1,5,10,50])
    ax1.set_xticklabels([100,500,1000,5000,10000,50000])
    ax1.set_yticks([.4,.6,.7,.8,.9,1])
    ax1.set_yticklabels([400,600,700,800,900,1000])
    ax1.set_xlabel('wavelength (km)',fontsize=16)
    ax1.set_ylabel('pressure at bottom of heating layer (hPa)',fontsize=16)
    #ax1.set_yticks([0,1,2,3])
    ax1.set_ylim(.6,1.)
    ax1.invert_yaxis()
    #ax1.tick_params(axis='both', labelsize=18)
    #plt.legend(loc=2, handlelength=3.75, prop={'size': 14})
        
    ax1.tick_params(axis='both', labelsize=14)
        
    plt.show()
    
# -----------------------------------------------------------------------------

# -------------------------------------------------------------------------
# defining modes for later evaluation
# -------------------------------------------------------------------------

#def define_and_plot_modes():

# how many unstable and stable modes should be investigated?

unstab2	= False
unstab3	= False
stab	= False
stab2	= False
stab3	= False

# which solutions should be investigated?
# sigmai is sorted from most stable to most unstable: first order (0) = most stable; last order (-1) = most unstable

mu2order = -1
mu3order = -1
ms2order = 0
ms3order = 0

# -------------------------------------------------------------------------

# scaling of solution

scale       = np.zeros((len(epsilon1),len(epsilon2))) # scale factor for most unstable mode
scale_add   = np.zeros((len(epsilon1),len(epsilon2))) # scale factor for additional modes

# defining modes

sigmai_unstab		= np.zeros((len(epsilon1),len(epsilon2),len(k)))
i_maxunstab			= np.zeros((len(epsilon1),len(epsilon2)), dtype=int)
psi_maxunstab		= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
w_maxunstab			= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)

for e in range(len(epsilon1)):
    for e2 in range(len(epsilon2)):
        for i in range(np.argwhere(wl >= 1)[0][0], np.argwhere(wl >= 10)[0][0]-1):#range(len(wl)):#
                sigmai_unstab[e,e2,i] = sigmai_sorted[e,e2,i,-1]
        i_maxunstab[e,e2]		= np.squeeze(np.argwhere(sigmai_unstab[e,e2] == np.max(sigmai_unstab[e,e2]))[0][0]) # wavenumber index of the most unstable solution

try:
    eigvecs_sorted
except:
    print ('w and psi are not redefined')
else:
    eigvecs_sorted_scaled = np.zeros(np.shape(eigvecs_sorted),dtype=complex)   
    
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
        
#            eigvecs_sorted[e,e2]    = eigvecs_sorted[e,e2]#*scale[e,e2]
   
            w_maxunstab[e,e2]		= (eigvecs_sorted[e,e2,i_maxunstab[e,e2],:nrws,-1]) # omega corresponding to the most unstable solution
            #w_maxunstab[e,e2]		= w_maxunstab[e,e2]/np.max(abs(w_maxunstab[e,e2]))
            psi_maxunstab[e,e2]		= (eigvecs_sorted[e,e2,i_maxunstab[e,e2],nrws:,-1]) # psi corresponding to the most unstable solution
            #psi_maxunstab[e,e2]	= psi_maxunstab[e,e2]/np.max(abs(psi_maxunstab[e,e2]))

            scale[e,e2]             = 1#/k[i_maxunstab[e,e2]]/np.max(abs(psi_maxunstab[e,e2,jtml:])) # 1 corresponds to max "surface" velocity of 10 m/s
#            scale[e,e2]             = 1/np.mean(abs(w_maxunstab[e,e2,jtml])) # 1 corresponds to mean omega of 10^-3 hPa/s at cloud base

            w_maxunstab[e,e2]       = w_maxunstab[e,e2]*scale[e,e2]
            psi_maxunstab[e,e2]     = psi_maxunstab[e,e2]*scale[e,e2]

            eigvecs_sorted_scaled[e,e2] = eigvecs_sorted[e,e2]*scale[e,e2]
    del(eigvecs_sorted)
    
# the most unstable/stable sigmas at additional peaks (partly manually found)
# less manual method: find local maxima, i.e. where sigma_i[i] > sigma_i[i-1] and sigma_i[i] > sigma_i[i+1]
        
if unstab2 == True:
    sigmai_unstab2		= np.zeros((len(epsilon1),len(epsilon2),len(k)))
    i_maxunstab2		= np.zeros((len(epsilon1),len(epsilon2)), dtype=int)
    psi_maxunstab2		= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
    w_maxunstab2		= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
    
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):            
            for i in range(np.argwhere(wl>=10)[0][0], np.argwhere(wl>=20)[0][0]): #sigmai_sorted[e,e2,:,mu2order] >= .5*np.max(sigmai_sorted))[0][0])
                sigmai_unstab2[e,e2,i]	= sigmai_sorted[e,e2,i,mu2order]
            i_maxunstab2[e,e2]			= np.squeeze(np.argwhere(sigmai_unstab2[e,e2] == np.max(sigmai_unstab2[e,e2]))[0][0])
            w_maxunstab2[e,e2]			= (eigvecs_sorted[e,e2,i_maxunstab2[e,e2],:nrws,mu2order])
            #w_maxunstab2[e,e2]			= w_maxunstab2[e,e2]/np.max(abs(w_maxunstab2[e,e2]))
            psi_maxunstab2[e,e2]		= (eigvecs_sorted[e,e2,i_maxunstab2[e,e2],nrws:,mu2order])
            #psi_maxunstab2[e,e2]		= psi_maxunstab2[e,e2]/np.max(abs(psi_maxunstab2[e,e2]))

            scale_add[e,e2]             = 1#/k[i_maxunstab2[e,e2]]/np.max(abs(psi_maxunstab2[e,e2,jtml:])) # 1 corresponds to max "surface" velocity of 10 m/s
            w_maxunstab2[e,e2]          = w_maxunstab2[e,e2]*scale_add[e,e2]
            psi_maxunstab2[e,e2]        = psi_maxunstab2[e,e2]*scale_add[e,e2]
                        
if unstab3 == True:
    sigmai_unstab3		= np.zeros((len(epsilon1),len(epsilon2),len(k)))
    i_maxunstab3		= np.zeros((len(epsilon1),len(epsilon2)), dtype=int)
    psi_maxunstab3		= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
    w_maxunstab3		= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
    
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)): 
            for i in range(np.argwhere(wl >= 1)[0][0], np.argwhere(wl >= 2)[0][0]):#np.argwhere(sigmai_sorted[e,e2,:,mu3order] >= .4*np.max(sigmai_sorted))[-1][0],len(wl)):
                sigmai_unstab3[e,e2,i]	= sigmai_sorted[e,e2,i,mu3order]
            i_maxunstab3[e,e2]			= np.squeeze(np.argwhere(sigmai_unstab3[e,e2] == np.max(sigmai_unstab3[e,e2]))[0][0]) #np.argwhere(wl>=6)#
            w_maxunstab3[e,e2]			= (eigvecs_sorted[e,e2,i_maxunstab3[e,e2],:nrws,mu3order])
            #w_maxunstab3[e,e2]			= w_maxunstab3[e,e2]/np.max(abs(w_maxunstab3[e,e2]))
            psi_maxunstab3[e,e2]		= (eigvecs_sorted[e,e2,i_maxunstab3[e,e2],nrws:,mu3order])
            #psi_maxunstab3[e,e2]		= psi_maxunstab3[e,e2]/np.max(abs(psi_maxunstab3[e,e2]))

            scale_add[e,e2]             = 1#/k[i_maxunstab3[e,e2]]/np.max(abs(psi_maxunstab3[e,e2,jtml:])) # 1 corresponds to max "surface" velocity of 10 m/s
            w_maxunstab3[e,e2]          = w_maxunstab3[e,e2]*scale_add[e,e2]
            psi_maxunstab3[e,e2]        = psi_maxunstab3[e,e2]*scale_add[e,e2]
        
if stab == True:
    sigmai_stab			= np.zeros((len(epsilon1),len(epsilon2),len(k)))
    i_maxstab			= np.zeros((len(epsilon1),len(epsilon2)), dtype=int)
    psi_maxstab			= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
    w_maxstab			= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
    
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):             
            for i in range(np.argwhere(wl >= 1)[0][0], np.argwhere(wl >= 6.4)[0][0]):
                sigmai_stab[e,e2,i] = sigmai_sorted[e,e2,i,0]
            i_maxstab[e,e2]		= np.squeeze(np.argwhere(sigmai_stab[e,e2] == np.min(sigmai_stab[e,e2]))[0][0])
            w_maxstab[e,e2]		= (eigvecs_sorted[e,e2,i_maxstab[e,e2],:nrws,0])
            #w_maxstab[e,e2]	= w_maxstab[e,e2]/np.max(abs(w_maxstab[e,e2]))
            psi_maxstab[e,e2]	= (eigvecs_sorted[e,e2,i_maxstab[e,e2],nrws:,0])
            #psi_maxstab[e,e2]	= psi_maxstab[e,e2]/np.max(abs(psi_maxstab[e,e2]))

            scale_add[e,e2]             = 1#/k[i_maxstab[e,e2]]/np.max(abs(psi_maxstab[e,e2,jtml:])) # 1 corresponds to max "surface" velocity of 10 m/s
            w_maxstab[e,e2]            = w_maxstab[e,e2]*scale_add[e,e2]
            psi_maxstab[e,e2]          = psi_maxstab[e,e2]*scale_add[e,e2]
            
if stab2 == True:
    sigmai_stab2		= np.zeros((len(epsilon1),len(epsilon2),len(k)))
    i_maxstab2			= np.zeros((len(epsilon1),len(epsilon2)), dtype=int)
    psi_maxstab2		= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
    w_maxstab2			= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):  
            for i in range(np.argwhere(wl >= 3.)[0][0], np.argwhere(wl >= 3.5)[0][0]):
                sigmai_stab2[e,e2,i]	= sigmai_sorted[e,e2,i,ms2order]
            i_maxstab2[e,e2]			= np.squeeze(np.argwhere(sigmai_stab2[e,e2] == np.min(sigmai_stab2[e,e2]))[0][0]) #np.argwhere(wl>=6)#
            w_maxstab2[e,e2]			= (eigvecs_sorted[e,e2,i_maxstab2[e,e2],:nrws,ms2order])
            #w_maxstab2[e,e2]			= w_maxstab2[e,e2]/np.max(abs(w_maxstab2[e,e2]))
            psi_maxstab2[e,e2]			= (eigvecs_sorted[e,e2,i_maxstab2[e,e2],nrws:,ms2order])
            #psi_maxstab2[e,e2]			= psi_maxstab2[e,e2]/np.max(abs(psi_maxstab2[e,e2]))

            scale_add[e,e2]             = 1#/k[i_maxstab2[e,e2]]/np.max(abs(psi_maxstab2[e,e2,jtml:])) # 1 corresponds to max "surface" velocity of 10 m/s
            w_maxstab2[e,e2]            = w_maxstab2[e,e2]*scale_add[e,e2]
            psi_maxstab2[e,e2]          = psi_maxstab2[e,e2]*scale_add[e,e2]
            
if stab3 == True:
    sigmai_stab3		= np.zeros((len(epsilon1),len(epsilon2),len(k)))
    i_maxstab3			= np.zeros((len(epsilon1),len(epsilon2)), dtype=int)
    psi_maxstab3		= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)
    w_maxstab3			= np.zeros((len(epsilon1),len(epsilon2),nrws), dtype=complex)

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):      
            for i in range(np.argwhere(wl >= 8)[0][0], np.argwhere(wl >= 13)[0][0]):
                sigmai_stab3[e,e2,i]	= sigmai_sorted[e,e2,i,ms3order]
            i_maxstab3[e,e2]			= np.squeeze(np.argwhere(sigmai_stab3[e,e2] == np.min(sigmai_stab3[e,e2]))[0][0]) #np.argwhere(wl>=6)#
            w_maxstab3[e,e2]			= (eigvecs_sorted[e,e2,i_maxstab3[e,e2],:nrws,ms3order])
            #w_maxstab3[e,e2]			= w_maxstab2[e,e2]/np.max(abs(w_maxstab3[e,e2]))
            psi_maxstab3[e,e2]			= (eigvecs_sorted[e,e2,i_maxstab3[e,e2],nrws:,ms3order])
            #psi_maxstab3[e,e2]			= psi_maxstab3[e,e2]/np.max(abs(psi_maxstab3[e,e2]))
            
            scale_add[e,e2]             = 1#/k[i_maxstab3[e,e2]]/np.max(abs(psi_maxstab3[e,e2,jtml:])) # 1 corresponds to max "surface" velocity of 10 m/s
            w_maxstab3[e,e2]            = w_maxstab3[e,e2]*scale_add[e,e2]
            psi_maxstab3[e,e2]          = psi_maxstab3[e,e2]*scale_add[e,e2]


### plotting the growth rate and testing if modes are correctly defined ----------------

def plot_most_unstable_modes():

    if beta > 0:
        sigmai_beta = sigmai_sorted
        
    fig, (ax1) = plt.subplots(figsize=(13,5))

    try:
        sigmai_beta
    except NameError:
        pass #print ('beta not nonzero')
    else:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                ax1.semilogx(wl,sigmai_beta[e,e2,:,0],c='k',linewidth=ms-2, label='beta')
                for i in range(1,5):
                    ax1.semilogx(wl,sigmai_beta[e,e2,:,i],c='k',linewidth=ms-2)
                    ax1.semilogx(wl,sigmai_beta[e,e2,:,-i],c='k',linewidth=ms-2)
            ax1.plot(wl[i_maxunstab[e,eps2_index]],sigmai_unstab[e,eps2_index,i_maxunstab[e,eps2_index]],'*',color='k')
        if unstab2 == True:
            ax1.plot(wl[i_maxunstab2[eps1_index,eps2_index]],sigmai_unstab2[eps1_index,eps2_index,i_maxunstab2[eps1_index,eps2_index]],'*',color='k')
        if unstab3 == True:
            ax1.plot(wl[i_maxunstab3[eps1_index,eps2_index]],sigmai_unstab3[eps1_index,eps2_index,i_maxunstab3[eps1_index,eps2_index]],'*',color='k')

    if beta == 0:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                ax1.semilogx(wl,sigmai_sorted[e,e2,:,0],color=c[1],linestyle=ls, linewidth=ms-2)#, label='no beta')
                for i in range(1,2):
                    ax1.semilogx(wl,sigmai_sorted[e,e2,:,i],color=c[1],linestyle=ls,linewidth=ms-2)
                    ax1.semilogx(wl,sigmai_sorted[e,e2,:,-i],color=c[1],linestyle=ls)#,linewidth=ms-2)                   
#                    ax1.semilogx(wl,sigmai_sorted_noevap[e,e2,:,-i],c=c[2],linestyle=ls)#,linewidth=ms-2)
            ax1.plot(wl[i_maxunstab[e,eps2_index]],sigmai_unstab[e,eps2_index,i_maxunstab[e,eps2_index]],'*',color=c[1])
        if unstab2 == True:
            ax1.plot(wl[i_maxunstab2[eps1_index,eps2_index]],sigmai_unstab2[eps1_index,eps2_index,i_maxunstab2[eps1_index,eps2_index]],'*',color=c[1])
        if unstab3 == True:
            ax1.plot(wl[i_maxunstab3[eps1_index,eps2_index]],sigmai_unstab3[eps1_index,eps2_index,i_maxunstab3[eps1_index,eps2_index]],'*',color=c[1])
        if stab == True:
            ax1.plot(wl[i_maxstab[eps1_index,eps2_index]],sigmai_stab[eps1_index,eps2_index,i_maxstab[eps1_index,eps2_index]],'*',color=c[1])
        if stab2 == True:
            ax1.plot(wl[i_maxstab2[eps1_index,eps2_index]],sigmai_stab2[eps1_index,eps2_index,i_maxstab2[eps1_index,eps2_index]],'*',color=c[1])
        if stab3 == True:
            ax1.plot(wl[i_maxstab3[eps1_index,eps2_index]],sigmai_stab3[eps1_index,eps2_index,i_maxstab3[eps1_index,eps2_index]],'*',color=c[1])
    ax1.axhline(0,color='dimgrey',linewidth=1.5)

    sigmaplotcustom(ax1)
    #ax1.set_xlim(.01,50)
    ax1.set_xlim(.1,30)
#    ax1.set_ylim(0,2)

    box = ax1.get_position()
    ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    #ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()

    # checking wavelength of most unstable solution for different heating intensities (regime shift)

    if len(epsilon1) > 30:
        plt.scatter(wl[i_maxunstab[:,e2]],epsilon1[:],color=c[1],linewidth=0.5,s=40)
        plt.xlabel('Wavelength of most unstable solution (km)')
        plt.ylabel('Latent heating intensity $\mathregular{\\varepsilon}$')
        plt.ylim(-2,62)
        plt.axhline(16,c='k',ls='--')
        plt.annotate('$\mathregular{\\varepsilon}$ = 16',xy=(6,17))
        plt.show()

# -----------------------------------------------------------------------------

def define_tropopause_sensitivity():
    
    global lambda_strat, ptrop_smooth # what are we investigating the sensitivity of?

    # variables for sharp experiments
    global l2l1, S2S1, gr_ls, wl_ls, dq_ls, pdq_ls, cph_ls      # physical values
    global psitrop, psitropeps, psisurf, psiphase               # terms related to psi
    global Ttropeps, Tsurf, Tphase, Tphaseeps                   # terms related to T
    global PVdztrop, PVdzsurf, PVphase                          # terms related to PV
    global wphase                                               # term related to omega
    global Tvtrop, Tvsurf, Twtrop, Twsurf                       # phase relation terms
    global ca, ca_trop, vTlevind, vTpos                         # energetic terms related to v'T'
    global ce, ce_trop, wTpos, wTpos_trop                       # energetic terms related to w'T'
    global norm_energy_ls, norm_psis_ls                         # norm terms
    global vterm_Tmax_tropdown, wterm_Tmax_tropdown, uterm_T90_tropdown, vterm_T90_tropdown, wterm_T90_tropdown  # terms in thermodyn. eq. just below tropopause
    global vterm_Tmax_tropup, wterm_Tmax_tropup, uterm_T90_tropup, vterm_T90_tropup, wterm_T90_tropup            # terms in thermodyn. eq. just above tropopause
    
    # variables for smooth experiments
    global l2l1_sm, S2S1_sm, gr_ls_sm, wl_ls_sm, dq_ls_sm, dq_int_ls_sm, pdq_ls_sm, cph_ls_sm   # physical values
    global psmoothrangemin, psmoothrangemax                                                     # range where dq/dy > 1% of max dq/dy
    global psitrop_sm, psisurf_sm, psiphase_sm                                                  # terms related to psi
    global Ttropeps_sm, Ttroprange_sm, Tsurf_sm, Tphase_sm                                      # terms related to T
    global PVtrop_sm, PVsurf_sm, PVphase_sm, wphase_sm                                          # terms related to PV and omega
    global Tvtrop_sm, Tvsurf_sm, Twtrop_sm, Twsurf_sm                                           # phase relation terms
    global ca_sm, ca_trop_sm, vTlevind_sm, vTpos_sm                                             # energetic terms related to v'T'
    global ce_trop_sm, ce_sm, wTpos_sm, wTpos_trop_sm                                           # energetic terms related to w'T'
    global norm_energy_ls_sm, norm_psis_ls_sm                                                   # norm terms
    global vterm_Tmax_tropeps_sm, wterm_Tmax_tropeps_sm                                         # terms in thermodyn. eq. just below tropopause, at Tmax
    global uterm_T90_tropeps_sm, vterm_T90_tropeps_sm, wterm_T90_tropeps_sm                     # terms in thermodyn. eq. just below tropopause, 90 deg away from Tmax
    global original_smoothfac
    
    # variables for variable height experiments    
    global ptrop_sm, smfac_sm, gr_ps_sm, wl_ps_sm, dq_ps_sm, pdq_ps_sm
    global original_strat
    
    lambda_strat = True
    ptrop_smooth = False
    
    if smoothstrat == False and smoothshear == False and smoothshearstrat == False and lambda_strat == True:
        try:
            l2l1
        except:
            l2l1 = ([])
            S2S1 = ([])
            gr_ls = ([])
            wl_ls = ([])
            dq_ls = ([])
            pdq_ls = ([])
            cph_ls = ([])
            
            psitrop = ([])
            psitropeps = ([])
            psisurf = ([])
            psiphase = ([])
            Ttropeps = ([])
            Tsurf = ([])
            Tphase = ([])
            Tphaseeps = ([])
            PVdztrop = ([])
            PVdzsurf = ([])
            PVphase = ([])
            wphase = ([])
            
            Tvtrop = ([])
            Tvsurf = ([])
            Twtrop = ([])
            Twsurf = ([])
            ca = ([])
            ca_trop = ([])
            vTlevind = ([])
            vTpos = ([])
            ce = ([])
            ce_trop = ([])
            wTpos = ([])
            wTpos_trop = ([])
            
            norm_energy_ls = ([])
            norm_psis_ls = ([])
            
            vterm_Tmax_tropdown = ([])
            wterm_Tmax_tropdown = ([])
            uterm_T90_tropdown = ([])
            vterm_T90_tropdown = ([])
            wterm_T90_tropdown = ([])
            vterm_Tmax_tropup = ([])
            wterm_Tmax_tropup = ([])
            uterm_T90_tropup = ([])
            vterm_T90_tropup = ([])
            wterm_T90_tropup = ([])
            
        if stratos == True and len(l2l1) == 0 or lambda1[1]/lambda1[-2] != l2l1[-1] or S[1]/S[-2] != S2S1[-1]:
            print ('defining terms for new experiment')
            
            l2l1.extend([lambda1[1]/lambda1[-2]])
            S2S1.extend([S[1]/S[-2]])
            gr_ls.extend([np.max(sigmai_sorted[0,0,:,-1])])
            wl_ls.extend([wl[np.argwhere(sigmai_sorted[0,0,:,-1] == np.max(sigmai_sorted[0,0,:,-1]))[0][0]]])
            if wl_ls[-1] > 10:
                wl_ls[-1] = nan
            dq_ls.extend([np.max(dqdy[1:-1])])
            if dq_ls[-1] == 0:
                dq_ls[-1] = nan
            pdq_ls.extend([p[np.argwhere(dqdy == np.max(dqdy[1:-1]))[-1][0]]])
            if pdq_ls[-1] <= p[1]:
                pdq_ls[-1] = nan
            cph_ls.extend([sigmar_sorted[0,0,np.argwhere(sigmai_sorted[0,0,:,-1]==np.max(sigmai_sorted[0,0,:,-1]))[-1][0],-1]/(2*np.pi)*wl_ls[-1]])

            tot_index = np.argwhere(kx == 2*np.pi)[0][0]
            psitrop.extend([np.max(psi[jtrop])])
            psitropeps.extend([np.max(psi[jtrop+1])])
            psisurf.extend([np.max(psi[-1])])
            psitrop_index = np.argwhere(psi[jtrop] == np.min(psi[jtrop]))[0][0]
            psisurf_index = np.argwhere(psi[-1] == np.min(psi[-1]))[0][0]
            psiphase.extend([(psisurf_index-psitrop_index)*360/tot_index])
            Ttropeps.extend([np.max(T[eps1_index,eps2_index,jtrop+1])])
            Tsurf.extend([np.max(T[eps1_index,eps2_index,-1])])
            Ttrop_index = np.argwhere(T[eps1_index,eps2_index,jtrop] == np.max(T[eps1_index,eps2_index,jtrop]))[0][0]
            Ttropeps_index = np.argwhere(T[eps1_index,eps2_index,jtrop+1] == np.max(T[eps1_index,eps2_index,jtrop+1]))[0][0]
            Ttropepsup_index = np.argwhere(T[eps1_index,eps2_index,jtrop-1] == np.max(T[eps1_index,eps2_index,jtrop-1]))[0][0]
            Tsurf_index = np.argwhere(T[eps1_index,eps2_index,-1] == np.max(T[eps1_index,eps2_index,-1]))[0][0]
            Tsurfeps_index = np.argwhere(T[eps1_index,eps2_index,-2] == np.max(T[eps1_index,eps2_index,-2]))[0][0]
            Tphase.extend([(Tsurf_index-Ttrop_index)*360/tot_index])
            Tphaseeps.extend([(Tsurf_index-Ttropeps_index)*360/tot_index])
            PVdztrop.extend([np.max(T[eps1_index,eps2_index,jtrop-1]/S[jtrop-1]-T[eps1_index,eps2_index,jtrop+1]/S[jtrop+1])])
            PVdzsurf.extend([np.max(T[eps1_index,eps2_index,-1])/S[-1]])
            PVtrop_index = np.argwhere(T[eps1_index,eps2_index,jtrop-1]/S[jtrop-1]-T[eps1_index,eps2_index,jtrop+1]/S[jtrop+1] == np.max(T[eps1_index,eps2_index,jtrop-1]/S[jtrop-1]-T[eps1_index,eps2_index,jtrop+1]/S[jtrop+1]))[0][0]
            PVsurf_index = np.argwhere(T[eps1_index,eps2_index,-1]/S[-1] == np.max(T[eps1_index,eps2_index,-1]/S[-1]))[0][0]
            PVphase.extend([(PVsurf_index-PVtrop_index)*360/tot_index])
            wtrop_index = np.argwhere(w[jtrop] == np.min(w[jtrop]))[0][0]
            wtropeps_index = np.argwhere(w[jtrop+1] == np.min(w[jtrop+1]))[0][0]
            wsurfeps_index = np.argwhere(w[-2] == np.min(w[-2]))[0][0]
            wphase.extend([(wsurfeps_index-wtrop_index)*360/tot_index])
            
            vtrop_index = np.argwhere(v[jtrop] == np.max(v[jtrop]))[0][0]
            vtropeps_index = np.argwhere(v[jtrop+1] == np.max(v[jtrop+1]))[0][0]
            vsurf_index = np.argwhere(v[-1] == np.max(v[-1]))[0][0]
            Tvtrop.extend([(Ttropeps_index-vtropeps_index)*360/tot_index])
            Tvsurf.extend([(Tsurf_index-vsurf_index)*360/tot_index])
            Twtrop.extend([(Ttropeps_index-wtropeps_index)*360/tot_index])
            Twsurf.extend([(Tsurfeps_index-wsurfeps_index)*360/tot_index])
            ca.extend([vT[-1]])
            ca_trop.extend([vT_trop[-1]])
            vTlevind.extend([np.argwhere(v*T[eps1_index,eps2_index]==np.max(np.min(v[jtrop+1:]*T[eps1_index,eps2_index,jtrop+1:],axis=1)))[0][0]])
            vTpos.extend([100*(v*T >= 0).sum()/(v*T < inf).sum()])
            ce.extend([wT[-1]])
            ce_trop.extend([wT_trop[-1]])
            wTpos.extend([100*(w*T <= 0).sum()/(w*T < inf).sum()])  
            wTpos_trop.extend([100*(w[jtrop:]*T[eps1_index,eps2_index,jtrop:] <= 0).sum()/(w[jtrop:]*T[eps1_index,eps2_index,jtrop:] < inf).sum()])
            
            t_ls = tempcalc(psi_maxunstab)[eps1_index,eps2_index]
            v_ls = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            norm_energy_ls.extend([simps(abs(v_ls**2+t_ls**2/S[:nrws]),p[:nrws])])
            norm_psis_ls.extend([(np.max(psi[:,-1]))])
            
            vterm_Tmax_tropdown.extend([v[jtrop+1,Ttropeps_index]*lambda1[jtrop+1]])
            wterm_Tmax_tropdown.extend([w[jtrop+1,Ttropeps_index]*S[jtrop+1]])
            uterm_T90_tropdown.extend([u[jtrop+1]*k[i_maxunstab[eps1_index,eps2_index]]*T[eps1_index,eps2_index,jtrop+1,Ttropeps_index]])
            vterm_T90_tropdown.extend([v[jtrop+1,Ttropeps_index+int((tot_index-1)*1/4)]*lambda1[jtrop+1]])
            wterm_T90_tropdown.extend([w[jtrop+1,Ttropeps_index+int((tot_index-1)*1/4)]*S[jtrop+1]])
            vterm_Tmax_tropup.extend([v[jtrop-1,Ttropepsup_index]*lambda1[jtrop-1]])
            wterm_Tmax_tropup.extend([w[jtrop-1,Ttropepsup_index]*S[jtrop-1]])
            uterm_T90_tropup.extend([u[jtrop-1]*k[i_maxunstab[eps1_index,eps2_index]]*T[eps1_index,eps2_index,jtrop-1,Ttropepsup_index]])
            vterm_T90_tropup.extend([v[jtrop-1,Ttropepsup_index+int((tot_index-1)*1/4)]*lambda1[jtrop-1]])
            wterm_T90_tropup.extend([w[jtrop-1,Ttropepsup_index+int((tot_index-1)*1/4)]*S[jtrop-1]])
    
    elif smoothshearstrat == True or smoothstrat == True and smoothshear == True:
        if lambda_strat == True:
            try:
                l2l1_sm
            except:
                l2l1_sm = ([])
                S2S1_sm = ([])
                gr_ls_sm = ([])
                wl_ls_sm = ([])
                dq_ls_sm = ([])
                dq_int_ls_sm = ([])
                pdq_ls_sm = ([])
                cph_ls_sm = ([])
                psmoothrangemin = ([])
                psmoothrangemax = ([])
                
                psitrop_sm = ([])
                psisurf_sm = ([])
                psiphase_sm = ([])
                Ttropeps_sm = ([])
                Ttroprange_sm = ([])
                Tsurf_sm = ([])
                Tphase_sm = ([])
                PVtrop_sm = ([])
                PVsurf_sm = ([])
                PVphase_sm = ([])
                wphase_sm = ([])
                
                Tvtrop_sm = ([])
                Tvsurf_sm = ([])
                Twtrop_sm = ([])
                Twsurf_sm = ([])
                
                ca_sm = ([])
                ca_trop_sm = ([])
                vTlevind_sm = ([])
                vTpos_sm = ([])
                ce_sm = ([])
                ce_trop_sm = ([])
                wTpos_sm = ([])
                wTpos_trop_sm = ([])
                
                norm_energy_ls_sm = ([])
                norm_psis_ls_sm = ([])
                original_smoothfac = smoothfac
            
                vterm_Tmax_tropeps_sm = ([])
                wterm_Tmax_tropeps_sm = ([])
                uterm_T90_tropeps_sm = ([])
                vterm_T90_tropeps_sm = ([])
                wterm_T90_tropeps_sm = ([])
                
            if smoothfac == original_smoothfac: # making sure that the smoothing factor remains the same
                if len(l2l1_sm) == 0 or lambda1[1]/lambda1[-2] != l2l1_sm[-1] or S[1]/S[-2] != S2S1_sm[-1]:
                    l2l1_sm.extend([lambda1[1]/lambda1[-2]])
                    S2S1_sm.extend([S[1]/S[-2]])
                    gr_ls_sm.extend([np.max(sigmai_sorted[0,0,:,-1])])
                    wl_ls_sm.extend([wl[np.argwhere(sigmai_sorted[0,0,:,-1] == np.max(sigmai_sorted[0,0,:,-1]))[0][0]]])
                    if wl_ls_sm[-1] > 10:
                        wl_ls_sm[-1] = nan
                    dq_ls_sm.extend([np.max(dqdy[1:-1])])
                    if dq_ls_sm[-1] == 0:
                        dq_ls_sm[-1] = nan
                    dq_int_ls_sm.extend([np.sum(dqdy[1:-1])])
                    pdq_ls_sm.extend([p[np.argwhere(dqdy == np.nanmax(dqdy[1:-1]))[0][0]]])
                    if pdq_ls_sm[-1] <= p[1]:
                        pdq_ls_sm[-1] = nan
                    tropindex = np.argwhere(p[:nrws]==pdq_ls_sm[-1])[0][0] # index of new tropopause
                    cph_ls_sm.extend([sigmar_sorted[0,0,np.argwhere(sigmai_sorted[0,0,:,-1]==np.max(sigmai_sorted[0,0,:,-1]))[-1][0],-1]/(2*np.pi)*wl_ls_sm[-1]])
                    smoothrangemin = np.argwhere(100*dqdy[1:-2]/np.max(dqdy[1:-2])>=1)[0][0]+1
                    smoothrangemax = np.argwhere(100*dqdy[1:-2]/np.max(dqdy[1:-2])>=1)[-1][0]+1
                    psmoothrangemin.extend([p[smoothrangemin]])
                    psmoothrangemax.extend([p[smoothrangemax]])
                    
                    tot_index = np.argwhere(kx == 2*np.pi)[0][0]
                    psitrop_sm.extend([np.max(psi[tropindex])])
                    psisurf_sm.extend([np.max(psi[-1])])
                    psitrop_index = np.argwhere(psi[tropindex] == np.max(psi[tropindex]))[0][0]
                    psisurf_index = np.argwhere(psi[-1] == np.max(psi[-1]))[0][0]
                    psiphase_sm.extend([(psisurf_index-psitrop_index)*360/tot_index])
                    Ttropeps_sm.extend([np.max(T[eps1_index,eps2_index,tropindex+1])])
                    Ttroprange_sm.extend([np.max(T[eps1_index,eps2_index,tropindex:smoothrangemax])])
                    Tsurf_sm.extend([np.max(T[eps1_index,eps2_index,-1])])
                    Ttropeps_index = np.argwhere(T[eps1_index,eps2_index,tropindex+1] == np.max(T[eps1_index,eps2_index,tropindex+1]))[0][0]
                    Tsurf_index = np.argwhere(T[eps1_index,eps2_index,-1] == np.max(T[eps1_index,eps2_index,-1]))[0][0]
                    Tsurfeps_index = np.argwhere(T[eps1_index,eps2_index,-2] == np.max(T[eps1_index,eps2_index,-2]))[0][0]
                    Tphase_sm.extend([(Tsurf_index-Ttropeps_index)*360/tot_index])
                    PVtrop_sm.extend([np.max(PV_u[eps1_index, eps2_index,tropindex])])
                    PVsurf_sm.extend([np.max(PV_u[eps1_index, eps2_index,-1])])
                    #PVtrop_index = np.argwhere(T[eps1_index,eps2_index,tropindex-1]/S[tropindex-1]-T[eps1_index,eps2_index,tropindex+1]/S[tropindex+1] == np.max(T[eps1_index,eps2_index,tropindex-1]/S[tropindex-1]-T[eps1_index,eps2_index,tropindex+1]/S[tropindex+1]))[0][0]
                    #PVsurf_index = np.argwhere(T[eps1_index,eps2_index,-1]/S[-1] == np.max(T[eps1_index,eps2_index,-1]/S[-1]))[0][0]
                    PVtrop_index = np.argwhere(PV_u[eps1_index, eps2_index,tropindex] == np.max(PV_u[eps1_index, eps2_index,tropindex]))[0][0]
                    PVsurf_index = np.argwhere(PV_u[eps1_index, eps2_index,-1] == np.max(PV_u[eps1_index, eps2_index,-1]))[0][0]
                    PVphase_sm.extend([(PVsurf_index-PVtrop_index)*360/tot_index])
                    wtropeps_index = np.argwhere(w[tropindex+1] == np.min(w[tropindex+1]))[0][0]
                    wsurf_index = np.argwhere(w[-1] == np.min(w[-1]))[0][0]
                    wsurfeps_index = np.argwhere(w[-2] == np.min(w[-2]))[0][0]
                    wphase_sm.extend([(wsurf_index-wtropeps_index)*360/tot_index])
            
                    vtropeps_index = np.argwhere(v[tropindex+1] == np.max(v[tropindex+1]))[0][0]
                    vsurf_index = np.argwhere(v[-1] == np.max(v[-1]))[0][0]
                    Tvtrop_sm.extend([(Ttropeps_index-vtropeps_index)*360/tot_index])
                    Tvsurf_sm.extend([(Tsurf_index-vsurf_index)*360/tot_index])
                    Twtrop_sm.extend([(Ttropeps_index-wtropeps_index)*360/tot_index])
                    Twsurf_sm.extend([(Tsurfeps_index-wsurfeps_index)*360/tot_index])
            
                    ca_sm.extend([vT[-1]])
                    ca_trop_sm.extend([vT_trop[-1]])
                    vTlevind_sm.extend([np.argwhere(v*T[eps1_index,eps2_index]==np.max(np.min(v[tropindex+1:]*T[eps1_index,eps2_index,tropindex+1:],axis=1)))[0][0]])
                    vTpos_sm.extend([100*(v*T >= 0).sum()/(v*T < inf).sum()])
                    ce_sm.extend([wT[-1]])
                    ce_trop_sm.extend([wT_trop[-1]])
                    wTpos_sm.extend([100*(w*T <= 0).sum()/(w*T < inf).sum()])
                    wTpos_trop_sm.extend([100*(w[tropindex+1:]*T[eps1_index,eps2_index,tropindex+1:] <= 0).sum()/(w[tropindex+1:]*T[eps1_index,eps2_index,tropindex+1:] < inf).sum()])

                    t_sm = tempcalc(psi_maxunstab)[eps1_index,eps2_index]
                    v_sm = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
                    norm_energy_ls_sm.extend([simps(abs(v_sm**2+t_sm**2/S[:nrws]),p[:nrws])])
                    norm_psis_ls_sm.extend([(np.max(psi[:,-1]))])
                            
                    vterm_Tmax_tropeps_sm.extend([v[tropindex+1,Ttropeps_index]*lambda1[tropindex+1]])
                    wterm_Tmax_tropeps_sm.extend([w[tropindex+1,Ttropeps_index]*S[tropindex+1]])
                    uterm_T90_tropeps_sm.extend([u[tropindex+1]*k[i_maxunstab[eps1_index,eps2_index]]*T[eps1_index,eps2_index,tropindex+1,Ttropeps_index]])
                    vterm_T90_tropeps_sm.extend([v[tropindex+1,Ttropeps_index+int((tot_index-1)*1/4)]*lambda1[tropindex+1]])
                    wterm_T90_tropeps_sm.extend([w[tropindex+1,Ttropeps_index+int((tot_index-1)*1/4)]*S[tropindex+1]])
            
        if ptrop_smooth == True:    
            try:
                ptrop_sm
            except:
                ptrop_sm = ([])
                smfac_sm = ([])
                gr_ps_sm = ([])
                wl_ps_sm = ([])
                dq_ps_sm = ([])
                pdq_ps_sm = ([])
                original_strat = S1
            if S1 == original_strat: # making sure that stratification remains the same
                if len(ptrop_sm) == 0 or ptrop != ptrop_sm[-1] or smoothfac != smfac_sm[-1]:
                    ptrop_sm.extend([ptrop])
                    smfac_sm.extend([smoothfac])
                    gr_ps_sm.extend([np.max(sigmai_sorted[0,0,:,-1])])
                    wl_ps_sm.extend([wl[np.argwhere(sigmai_sorted[0,0,:,-1] == np.max(sigmai_sorted[0,0,:,-1]))[0][0]]])
                    if wl_ps_sm[-1] > 10:
                        wl_ps_sm[-1] = nan
                    dq_ps_sm.extend([np.max(dqdy[1:-1])])
                    if dq_ps_sm[-1] == 0:
                        dq_ps_sm[-1] = nan
                    pdq_ps_sm.extend([p[np.argwhere(dqdy == np.max(dqdy[1:-1]))[0][0]]])
                    if pdq_ps_sm[-1] <= p[1]:
                        pdq_ps_sm[-1] = nan
                        
# -----------------------------------------------------------------------------
    
def save_sharp_tropopause_sensitivity():

    # save the most important variables from sharp experiments for lambda-S diagram
                        
    np.savetxt('model_output/lambda-S_diagram/l2l1_sort.txt',l2l1_sort)
    np.savetxt('model_output/lambda-S_diagram/S2S1_sort.txt',S2S1_sort)
    np.savetxt('model_output/lambda-S_diagram/gr_sort.txt',gr_sort)
    np.savetxt('model_output/lambda-S_diagram/wl_sort.txt',wl_sort)
    np.savetxt('model_output/lambda-S_diagram/dq_sort.txt',dq_sort)
    np.savetxt('model_output/lambda-S_diagram/cph_sort.txt',cph_sort)
    np.savetxt('model_output/lambda-S_diagram/Ttropeps_sort.txt',Ttropeps_sort)
    np.savetxt('model_output/lambda-S_diagram/Tsurf_sort.txt',Tsurf_sort)
    np.savetxt('model_output/lambda-S_diagram/psitropeps_sort.txt',psitropeps_sort)
    np.savetxt('model_output/lambda-S_diagram/psisurf_sort.txt',psisurf_sort)
    np.savetxt('model_output/lambda-S_diagram/Tvsurf_sort.txt',Tvsurf_sort)
    np.savetxt('model_output/lambda-S_diagram/Tvtrop_sort.txt',Tvtrop_sort)
                        
# -----------------------------------------------------------------------------
    
def load_sharp_tropopause_sensitivity():

    l2l1_sort = np.loadtxt('model_output/lambda-S_diagram/l2l1_sort.txt')
    S2S1_sort = np.loadtxt('model_output/lambda-S_diagram/S2S1_sort.txt')
    gr_sort = np.loadtxt('model_output/lambda-S_diagram/gr_sort.txt')
    wl_sort = np.loadtxt('model_output/lambda-S_diagram/wl_sort.txt')
    dq_sort = np.loadtxt('model_output/lambda-S_diagram/dq_sort.txt')
    cph_sort = np.loadtxt('model_output/lambda-S_diagram/cph_sort.txt')
    Ttropeps_sort = np.loadtxt('model_output/lambda-S_diagram/Ttropeps_sort.txt')
    Tsurf_sort = np.loadtxt('model_output/lambda-S_diagram/Tsurf_sort.txt')
    psitropeps_sort = np.loadtxt('model_output/lambda-S_diagram/psitropeps_sort.txt')
    psisurf_sort = np.loadtxt('model_output/lambda-S_diagram/psisurf_sort.txt')
    Tvsurf_sort = np.loadtxt('model_output/lambda-S_diagram/Tvsurf_sort.txt')
    Tvtrop_sort = np.loadtxt('model_output/lambda-S_diagram/Tvtrop_sort.txt')
    dqdy = np.loadtxt('model_output/lambda-S_diagram/dqdy.txt')
                    
# -----------------------------------------------------------------------------
    
def save_smooth_tropopause_sensitivity():

    # save the most important variables from smooth experiments for lambda-S diagram
                            
    np.savetxt('model_output/lambda-S_diagram/l2l1_sm_sort.txt',l2l1_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/S2S1_sm_sort.txt',S2S1_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/gr_sm_sort.txt',gr_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/wl_sm_sort.txt',wl_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/dq_sm_sort.txt',dq_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/cph_sm_sort.txt',cph_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/Ttroprange_sm_sort.txt',Ttroprange_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/Tsurf_sm_sort.txt',Tsurf_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/psitrop_sm_sort.txt',psitrop_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/psisurf_sm_sort.txt',psisurf_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/Tvsurf_sm_sort.txt',Tvsurf_sm_sort)
    np.savetxt('model_output/lambda-S_diagram/Tvtrop_sm_sort.txt',Tvtrop_sm_sort)
                    
# -----------------------------------------------------------------------------
    
def load_smooth_tropopause_sensitivity():
    
    l2l1_sm_sort = np.loadtxt('model_output/lambda-S_diagram/l2l1_sm_sort.txt')
    S2S1_sm_sort = np.loadtxt('model_output/lambda-S_diagram/S2S1_sm_sort.txt')
    gr_sm_sort = np.loadtxt('model_output/lambda-S_diagram/gr_sm_sort.txt')
    wl_sm_sort = np.loadtxt('model_output/lambda-S_diagram/wl_sm_sort.txt')
    dq_sm_sort = np.loadtxt('model_output/lambda-S_diagram/dq_sm_sort.txt')
    cph_sm_sort = np.loadtxt('model_output/lambda-S_diagram/cph_sm_sort.txt')
    Ttroprange_sm_sort = np.loadtxt('model_output/lambda-S_diagram/Ttroprange_sm_sort.txt')
    Tsurf_sm_sort = np.loadtxt('model_output/lambda-S_diagram/Tsurf_sm_sort.txt')
    psitrop_sm_sort = np.loadtxt('model_output/lambda-S_diagram/psitrop_sm_sort.txt')
    psisurf_sm_sort = np.loadtxt('model_output/lambda-S_diagram/psisurf_sm_sort.txt')
    Tvsurf_sm_sort = np.loadtxt('model_output/lambda-S_diagram/Tvsurf_sm_sort.txt')
    Tvtrop_sm_sort = np.loadtxt('model_output/lambda-S_diagram/Tvtrop_sm_sort.txt')
    
# -----------------------------------------------------------------------------
    
def plot_tropopause_sensitivity():

    global l2l1_sort, S2S1_sort, gr_sort, wl_sort, dq_sort, cph_sort #, pdq_sort
    global Ttropeps_sort,Tsurf_sort,psitropeps_sort,psisurf_sort
    global Tvsurf_sort,Tvtrop_sort
    global l2l1_sm_sort, S2S1_sm_sort, gr_sm_sort, wl_sm_sort, dq_sm_sort, cph_sm_sort #, pdq_sm_sort
#    global vterm_T90_tropeps_sm_sort, wterm_T90_tropeps_sm_sort, wterm_T90_tropeps_sm_sort, Twtrop_sm_sort, Twtrop_sm_sort_pos, vterm_T90_tropdown_sort, wterm_T90_tropdown_sort, Twtrop_sort
    global Ttroprange_sm_sort,Tsurf_sm_sort,psitrop_sm_sort,psisurf_sm_sort
    global Tvsurf_sm_sort,Tvtrop_sm_sort

    lambda_strat = True
    ptrop_smooth = False
    
    if lambda_strat == True:
        try:
            l2l1
        except:
            pass
        else:
            l2l1_sort = sort(list(set(l2l1)))
            S2S1_sort = sort(list(set(S2S1)))

            gr_sort  = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            wl_sort  = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            dq_sort  = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            pdq_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            cph_sort  = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            
            psitrop_sort  = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            psitropeps_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            psisurf_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            psiphase_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            Ttropeps_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            Tsurf_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            Tphase_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            Tphaseeps_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            PVdztrop_sort  = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            PVdzsurf_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            PVphase_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            wphase_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            
            Tvtrop_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            Tvsurf_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            Twtrop_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            Twsurf_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            ca_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            ca_trop_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            vTlevind_sort  = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            u_vTlevind_sort  = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            vTpos_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            ce_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            ce_trop_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            wTpos_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            wTpos_trop_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            
            norm_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*0.001#nan
            
            vterm_Tmax_tropdown_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            wterm_Tmax_tropdown_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            uterm_T90_tropdown_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            vterm_T90_tropdown_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            wterm_T90_tropdown_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            vterm_Tmax_tropup_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            wterm_Tmax_tropup_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            uterm_T90_tropup_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            vterm_T90_tropup_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan
            wterm_T90_tropup_sort = np.ones((len(l2l1_sort),len(S2S1_sort)))*nan


            for l in range(len(l2l1_sort)):
                for s in range(len(S2S1_sort)):
                    try:
                        ([x for x in np.argwhere(l2l1 == l2l1_sort[l]) if x in np.argwhere(S2S1 == S2S1_sort[s])][0][0])
                    except:
                        pass
                    else:
                        index = [x for x in np.argwhere(l2l1 == l2l1_sort[l]) if x in np.argwhere(S2S1 == S2S1_sort[s])][0][0]
                        gr_sort[l,s]  = gr_ls [index]
                        wl_sort[l,s]  = wl_ls [index]
                        dq_sort[l,s]  = dq_ls [index]
                        pdq_sort[l,s] = pdq_ls[index]
                        cph_sort[l,s] = cph_ls [index]
                        
                        psitrop_sort[l,s] = psitrop [index]
                        psitropeps_sort[l,s] = psitropeps [index]
                        psisurf_sort[l,s] = psisurf [index]
                        psiphase_sort[l,s] = psiphase[index]
                        Ttropeps_sort[l,s] = Ttropeps[index]
                        Tsurf_sort[l,s] = Tsurf[index]
                        Tphase_sort[l,s] = Tphase[index]
                        Tphaseeps_sort[l,s] = Tphaseeps[index]
                        PVdztrop_sort[l,s] = PVdztrop [index]
                        PVdzsurf_sort[l,s] = PVdzsurf [index]
                        PVphase_sort[l,s] = PVphase[index]
                        wphase_sort[l,s] = wphase[index]
                        
                        Tvtrop_sort[l,s] = Tvtrop[index]
                        Tvsurf_sort[l,s] = Tvsurf[index]
                        Twtrop_sort[l,s] = Twtrop[index]
                        Twsurf_sort[l,s] = Twsurf[index]
                        
                        ca_sort[l,s] = ca[index]
                        ca_trop_sort[l,s] = ca_trop[index]
                        vTlevind_sort[l,s] = vTlevind [index]
                        if math.isnan(vTlevind[index]) == False:
                            u_vTlevind_sort[l,s] = u[vTlevind[index]]
                        vTpos_sort[l,s] = vTpos[index]
                        ce_sort[l,s] = ce[index]
                        ce_trop_sort[l,s] = ce_trop[index]
                        wTpos_sort[l,s] = wTpos[index]
                        wTpos_trop_sort[l,s] = wTpos_trop[index]
                        
                        norm_sort[l,s] = PVdzsurf_sort[l,s]#norm_energy_ls[index] # normalise with respect to energy or psis?
                        
                        vterm_Tmax_tropdown_sort[l,s] = vterm_Tmax_tropdown[index]
                        wterm_Tmax_tropdown_sort[l,s] = wterm_Tmax_tropdown[index]
                        uterm_T90_tropdown_sort[l,s] = uterm_T90_tropdown[index]
                        vterm_T90_tropdown_sort[l,s] = vterm_T90_tropdown[index]
                        #if abs(wterm_T90_tropdown[index]) > 0.005:
                        wterm_T90_tropdown_sort[l,s] = wterm_T90_tropdown[index]
                        #if (vterm_Tmax_tropup[index]) < -0.0003:# and (vterm_Tmax_tropup[index]) >  0:
                        vterm_Tmax_tropup_sort[l,s] = vterm_Tmax_tropup[index]
                        wterm_Tmax_tropup_sort[l,s] = wterm_Tmax_tropup[index]
                        uterm_T90_tropup_sort[l,s] = uterm_T90_tropup[index]
                        vterm_T90_tropup_sort[l,s] = vterm_T90_tropup[index]
                        wterm_T90_tropup_sort[l,s] = wterm_T90_tropup[index]

        try:
            l2l1_sm
        except:
            pass
        else:
            l2l1_sm_sort = sort(list(set(l2l1_sm)))
            S2S1_sm_sort = sort(list(set(S2S1_sm)))

            gr_sm_sort  = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            wl_sm_sort  = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            dq_sm_sort  = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            pdq_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            cph_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            psmoothrangemax_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            psmoothrangemin_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            
            psitrop_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            psisurf_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            psiphase_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            Ttropeps_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            Ttroprange_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            Tsurf_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            Tphase_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            PVtrop_sm_sort  = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            PVsurf_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            PVphase_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            
            Tvtrop_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            Tvsurf_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            Twtrop_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            Twtrop_sm_sort_pos = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            Twsurf_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            
            ca_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            ca_trop_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            vTlevind_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            u_vTlevind_sm_sort  = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            vTpos_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            ce_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            ce_trop_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            wTpos_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            wTpos_trop_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            
            norm_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            
            vterm_Tmax_tropeps_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            wterm_Tmax_tropeps_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            uterm_T90_tropeps_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            vterm_T90_tropeps_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            wterm_T90_tropeps_sm_sort = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan
            wterm_T90_tropeps_sm_sort_pos = np.ones((len(l2l1_sm_sort),len(S2S1_sm_sort)))*nan

            for l in range(len(l2l1_sm_sort)):
                for s in range(len(S2S1_sm_sort)):
                    try:
                        ([x for x in np.argwhere(l2l1_sm == l2l1_sm_sort[l]) if x in np.argwhere(S2S1_sm == S2S1_sm_sort[s])][0][0])
                    except:
                        pass
                    else:
                        index = [x for x in np.argwhere(l2l1_sm == l2l1_sm_sort[l]) if x in np.argwhere(S2S1_sm == S2S1_sm_sort[s])][0][0]
                        gr_sm_sort[l,s]  = gr_ls_sm [index]
                        wl_sm_sort[l,s]  = wl_ls_sm [index]
                        dq_sm_sort[l,s]  = dq_ls_sm [index]
                        pdq_sm_sort[l,s] = pdq_ls_sm[index]
                        cph_sm_sort[l,s] = cph_ls_sm[index]
                        psmoothrangemax_sort[l,s] = psmoothrangemax[index]
                        psmoothrangemin_sort[l,s] = psmoothrangemin[index]
                        
                        psitrop_sm_sort[l,s] = psitrop_sm[index]
                        psisurf_sm_sort[l,s] = psisurf_sm[index]
                        psiphase_sm_sort[l,s] = psiphase_sm[index]
                        Ttropeps_sm_sort[l,s] = Ttropeps_sm[index]
                        Ttroprange_sm_sort[l,s] = Ttroprange_sm[index]
                        Tsurf_sm_sort[l,s] = Tsurf_sm[index]
                        Tphase_sm_sort[l,s] = Tphase_sm[index]
                        PVtrop_sm_sort[l,s] = PVtrop_sm[index]
                        PVsurf_sm_sort[l,s] = PVsurf_sm[index]
                        PVphase_sm_sort[l,s] = PVphase_sm[index]
                        
                        Tvtrop_sm_sort[l,s] = Tvtrop_sm[index]
                        Tvsurf_sm_sort[l,s] = Tvsurf_sm[index]
                        Twtrop_sm_sort[l,s] = Twtrop_sm[index]
                        Twtrop_sm_sort_pos[l,s] = Twtrop_sm_sort[l,s]
                        if Twtrop_sm_sort[l,s] < 0:
                            Twtrop_sm_sort_pos[l,s] = nan
                        Twsurf_sm_sort[l,s] = Twsurf_sm[index]
                        
                        ca_sm_sort[l,s] = ca_sm[index]
                        ca_trop_sm_sort[l,s] = ca_trop_sm[index]
                        vTlevind_sm_sort[l,s] = vTlevind_sm[index]
                        if math.isnan(vTlevind_sm[index]) == False:
                            u_vTlevind_sm_sort[l,s] = u[vTlevind_sm[index]]
                        vTpos_sm_sort[l,s] = vTpos_sm[index]
                        ce_sm_sort[l,s] = ce_sm[index]
                        ce_trop_sm_sort[l,s] = ce_trop_sm[index]
                        wTpos_sm_sort[l,s] = wTpos_sm[index]
                        wTpos_trop_sm_sort[l,s] = wTpos_trop_sm[index]
                        norm_sm_sort[l,s] = norm_energy_ls_sm[index]
                        
                        vterm_Tmax_tropeps_sm_sort[l,s] = vterm_Tmax_tropeps_sm[index]
                        wterm_Tmax_tropeps_sm_sort[l,s] = wterm_Tmax_tropeps_sm[index]
                        uterm_T90_tropeps_sm_sort[l,s] = uterm_T90_tropeps_sm[index]
                        vterm_T90_tropeps_sm_sort[l,s] = vterm_T90_tropeps_sm[index]
                        wterm_T90_tropeps_sm_sort[l,s] = wterm_T90_tropeps_sm[index]
                        wterm_T90_tropeps_sm_sort_pos[l,s] = wterm_T90_tropeps_sm_sort[l,s]
                        if wterm_T90_tropeps_sm_sort[l,s] < 0:
                            wterm_T90_tropeps_sm_sort_pos[l,s] = nan

        nrows = 2
        add_axes = True
        
        fig1, axs = plt.subplots(nrows,2,figsize=(16,nrows*7))
        fig2, axs_add = plt.subplots(nrows,2,figsize=(16,nrows*7))
        fig1.subplots_adjust(wspace=.3, hspace=.3)
        fig2.subplots_adjust(wspace=.3, hspace=.3)
                    
        try:
            l2l1
        except:
            pass
        else:
            im1 = axs[0,0].contour(S2S1_sort, l2l1_sort, gr_sort, 15, colors='k')
            axs[0,0].clabel(im1, im1.levels[::1], inline=1, fmt='%1.2f')
            im1b = axs[0,0].contour(S2S1_sort, l2l1_sort, gr_sort, levels = [1.0840181256117791], colors='k', linewidths=5)
#            axs[0,0].clabel(im1b, inline=1, fmt='%1.f')
            im2 = axs[0,1].contour(S2S1_sort, l2l1_sort, 1000*wl_sort, 15, colors='k')
            axs[0,1].clabel(im2, im2.levels[::2], inline=1, fmt='%1.0f')
            im2b = axs[0,1].contour(S2S1_sort, l2l1_sort, 1000*wl_sort, levels = [2897.9982599649047], colors='k', linewidths=5)
#            axs[0,1].clabel(im2b, inline=1, fmt='%1.f')
            im3 = axs[1,0].contour(S2S1_sort, l2l1_sort, 10*(cph_sort), 15, colors='k')
            axs[1,0].clabel(im3, im3.levels[::2], inline=1, fmt='%1.1f')
            im3b = axs[1,0].contour(S2S1_sort, l2l1_sort, 10*cph_sort, levels=[10*u[jtrop]/2], colors='k', linewidths=5)
            #axs[1,0].clabel(im3b, inline=1, fmt='%1.f')
            im4 = axs[1,1].contour(S2S1_sort, l2l1_sort, (dq_sort)/[-dqdy[-1]], 10, colors='k')
            axs[1,1].clabel(im4, inline=1, fmt='%1.1f')
            im4b = axs[1,1].contour(S2S1_sort, l2l1_sort, (dq_sort)/[-dqdy[-1]], levels = [1], colors='k', linewidths=5)
            axs[1,1].clabel(im4b, inline=1, fmt='%1.1f')
#            im4 = axs[1,1].contour(S2S1_sort, l2l1_sort, pdq_sm_sort, 10, colors='k') # NB! pressure does not change if tropopause is discontinuous, i.e. this is only nonzero when smoothing is on
#            axs[1,1].clabel(im4, im4.levels[::2], inline=1, fmt='%1.2f')
            axs[0,0].text(.01,1.05,'(a)',fontsize=24)
            axs[0,1].text(.01,1.05,'(b)',fontsize=24)
            axs[1,0].text(.01,1.05,'(c)',fontsize=24)
            axs[1,1].text(.01,1.05,'(d)',fontsize=24)
            im5 = axs_add[0,0].contour(S2S1_sort, l2l1_sort, Ttropeps_sort/Tsurf_sort, 15, colors='k')
            axs_add[0,0].clabel(im5, im5.levels[::2], inline=1, fmt='%1.2f')
#            im5b = axs[2,0].contour(S2S1_sort, l2l1_sort, Tphase, levels = [-48], colors='k', linestyles='-', linewidths=5)
#            axs[2,0].clabel(im5b, inline=1, fmt='%1.f')
            im6 = axs_add[0,1].contour(S2S1_sort, l2l1_sort, psitropeps_sort/psisurf_sort, 15, colors='k')
            axs_add[0,1].clabel(im6, im6.levels[::2], inline=1, fmt='%1.2f')
#            im6b = axs[2,1].contour(S2S1_sort, l2l1_sort, psiphase_sort, levels = [90], colors='k', linewidths=5)
#            axs[2,1].clabel(im6b, im6b.levels[::2], inline=1, fmt='%1.0f')
            if nrows >= 4:
                im7 = axs[3,0].contour(S2S1_sort, l2l1_sort, ca_sort/norm_sort, 15, colors='k')
                axs[3,0].clabel(im7, im7.levels[::2], inline=1)#, fmt='%1.f')
#                im7b = axs[3,0].contour(S2S1_sort, l2l1_sort, ca_sort/norm_sort, levels=[], colors='k', linewidths=5)
#                axs[3,0].clabel(im7b, inline=1, fmt='%1.f')
                im8 = axs[3,1].contour(S2S1_sort, l2l1_sort, vTpos_sort, 15, colors='k')
                axs[3,1].clabel(im8, im8.levels[::2], inline=1, fmt='%1.f')
#                im8b = axs[3,1].contour(S2S1_sort, l2l1_sort, vTpos_sort, levels=[77.27126288659794], colors='k', linewidths=5)
#                axs[3,1].clabel(im8b, im8b.levels[::2], inline=1, fmt='%1.f')
            if add_axes == True:  
                #im7 = axs_add[0,0].contour(S2S1_sort, l2l1_sort, wterm_Tmax_tropdown_sort/vterm_Tmax_tropdown_sort, 15, colors='k')#ca
                #axs_add[0,0].clabel(im7, im7.levels[::2], inline=1, fmt='%1.2f')
    #            im7b = axs[3,0].contour(S2S1_sort, l2l1_sort, ca_sort/norm_sort, levels=[], colors='k', linewidths=5)
    #            axs[3,0].clabel(im7b, inline=1, fmt='%1.f')
                #im8 = axs_add[0,1].contour(S2S1_sort, l2l1_sort, wterm_T90_tropdown_sort/vterm_T90_tropdown_sort, 15, colors='k')#vTpos_sort
                #axs_add[0,1].clabel(im8, im8.levels[::2], inline=1, fmt='%1.2f')
    #            im8b = axs_add[0,1].contour(S2S1_sort, l2l1_sort, vTpos_sort, levels=[77.27126288659794], colors='k', linewidths=5)
    #            axs_add[0,1].clabel(im8b, im8b.levels[::2], inline=1, fmt='%1.f')
                #im9 = axs_add[1,0].contour(S2S1_sort, l2l1_sort, Twsurf_sort, 15, colors='k')
                #axs_add[1,0].clabel(im9, im9.levels[::2], inline=1, fmt='%1.1f')
                #im10 = axs_add[1,1].contour(S2S1_sort, l2l1_sort, Twtrop_sort, 15, colors='k')
                #axs_add[1,1].clabel(im10, im10.levels[::2], inline=1, fmt='%1.f')
                im11 = axs_add[1,0].contour(S2S1_sort, l2l1_sort, Tvsurf_sort, levels=[-69.51724137931035], colors='k', linestyles='-', linewidths=5)
                im11 = axs_add[1,0].contour(S2S1_sort, l2l1_sort, Tvsurf_sort, 15, colors='k')
                axs_add[1,0].clabel(im11, im11.levels[::2], inline=1, fmt='%1.1f')
                im12 = axs_add[1,1].contour(S2S1_sort, l2l1_sort, Tvtrop_sort, levels=[69.51724137931035], colors='k', linewidths=5)
                im12 = axs_add[1,1].contour(S2S1_sort, l2l1_sort, Tvtrop_sort, 15, colors='k')
                axs_add[1,1].clabel(im12, im12.levels[::2], inline=1, fmt='%1.f')
                axs_add[0,0].text(.01,1.05,'(a)',fontsize=24)
                axs_add[0,1].text(.01,1.05,'(b)',fontsize=24)
                axs_add[1,0].text(.01,1.05,'(c)',fontsize=24)
                axs_add[1,1].text(.01,1.05,'(d)',fontsize=24)
        try:
            l2l1_sm
        except:
            print ('plotting sharp experiments only')
            norm = MidpointNormalize(midpoint=0)
            axs[0,0].contourf(S2S1_sort, l2l1_sort, gr_sort, cmap=cm_br)
            axs[0,1].contourf(S2S1_sort, l2l1_sort, 1000*wl_sort, cmap=cm_br)
            axs[1,0].contourf(S2S1_sort, l2l1_sort, 10*(cph_sort), cmap=cm_br)
            axs[1,1].contourf(S2S1_sort, l2l1_sort, (dq_sort)/[-dqdy[-1]], cmap=cm_br)
            axs_add[0,0].contourf(S2S1_sort, l2l1_sort, Ttropeps_sort/Tsurf_sort, cmap=cm_br)#Tphaseeps_sort
            axs_add[0,1].contourf(S2S1_sort, l2l1_sort, psitropeps_sort/psisurf_sort, cmap=cm_br)#-wphase_sort
            if nrows >= 4:
                axs[3,0].contourf(S2S1_sort, l2l1_sort, ca_trop_sort/norm_sort, cmap=cm_br)
                axs[3,1].contourf(S2S1_sort, l2l1_sort, vTpos_sort, cmap=cm_br)
            if add_axes == True:
                #axs_add[0,0].contourf(S2S1_sort, l2l1_sort, wterm_Tmax_tropdown_sort/vterm_Tmax_tropdown_sort, cmap=cm_br)
                #axs_add[0,1].contourf(S2S1_sort, l2l1_sort, wterm_T90_tropdown_sort/vterm_T90_tropdown_sort, cmap=cm_br)
                #axs_add[1,0].contourf(S2S1_sort, l2l1_sort, Twsurf_sort, cmap=cm_br)
                #axs_add[1,1].contourf(S2S1_sort, l2l1_sort, Twtrop_sort, cmap=cm_br)
                axs_add[1,0].contourf(S2S1_sort, l2l1_sort, Tvsurf_sort, cmap=cm_br)
                axs_add[1,1].contourf(S2S1_sort, l2l1_sort, Tvtrop_sort, cmap=cm_br)
        else:
            if np.array_equal(l2l1_sort, np.round(l2l1_sm_sort,1)) == True and np.array_equal(S2S1_sort, np.round(S2S1_sm_sort,1)) == True:
                print ('plotting relative difference between sharp and smooth experiments')
                norm = MidpointNormalize(midpoint=0)
                im1 = axs[0,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(gr_sm_sort-gr_sort)/gr_sort, norm=norm, cmap=cm_br)#-2*np.nanmax(100*(gr_sm_sort-gr_sort)/gr_sort))
                fig1.colorbar(im1,ax=axs[0,0])
                norm = MidpointNormalize(midpoint=0)
                im2 = axs[0,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(wl_sm_sort-wl_sort)/wl_sort, norm=norm, cmap=cm_br)
                fig1.colorbar(im2,ax=axs[0,1])
                norm = MidpointNormalize(midpoint=0)
                im3 = axs[1,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(cph_sm_sort-cph_sort)/cph_sort, norm=norm, cmap=cm_br)
                fig1.colorbar(im3,ax=axs[1,0])
                norm = MidpointNormalize(midpoint=.5*np.nanmax(100*(dq_sm_sort-dq_sort)/dq_sort))            
                im4 = axs[1,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(dq_sm_sort-dq_sort)/dq_sort, norm=norm, cmap=cm_br, vmin=2*np.nanmax(100*(dq_sm_sort-dq_sort)/dq_sort))         
                cbar = fig1.colorbar(im4,ax=axs[1,1],ticks=None)
                cbar.set_ticks([np.nanmax(100*(dq_sm_sort-dq_sort)/dq_sort)])
                cbar.ax.set_yticklabels(['{:.0f}'.format(np.nanmax(100*(dq_sm_sort-dq_sort)/dq_sort))])# for x in np.arange(cbar_min, cbar_max+cbar_step, cbar_step)])
#                norm = MidpointNormalize(midpoint=.99*np.nanmin(100*(pdq_sm_sort-pdq_sort)/pdq_sort))   
#                im4 = axs[1,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(pdq_sm_sort-pdq_sort)/pdq_sort, norm=norm, cmap=cm_br)
#                axs[1,1].set_title('pressure @ max interior dq/dy')
                norm = MidpointNormalize(midpoint=.9*np.nanmax(100*(Ttroprange_sm_sort/Tsurf_sm_sort-Ttropeps_sort/Tsurf_sort)/(Ttropeps_sort/Tsurf_sort)))   
                im5 = axs_add[0,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(Ttroprange_sm_sort/Tsurf_sm_sort-Ttropeps_sort/Tsurf_sort)/(Ttropeps_sort/Tsurf_sort), norm=norm, cmap=cm_br)
                fig2.colorbar(im5,ax=axs_add[0,0])
                norm = MidpointNormalize(midpoint=.9*np.nanmax(100*(psitrop_sm_sort/psisurf_sm_sort-psitropeps_sort/psisurf_sort)/(psitropeps_sort/psisurf_sort)))  
                im6 = axs_add[0,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(psitrop_sm_sort/psisurf_sm_sort-psitropeps_sort/psisurf_sort)/(psitropeps_sort/psisurf_sort), norm=norm, cmap=cm_br)
                fig2.colorbar(im6,ax=axs_add[0,1])
                if nrows >= 4:
                    im7 = axs[3,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(ca_sort-ca_sort)/ca_sort, cmap=cm_br)
                    fig1.colorbar(im7,ax=axs[3,0])
                    im8 = axs[3,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(vTpos_sm_sort-vTpos_sort)/vTpos_sort, cmap=cm_br)
                    fig1.colorbar(im8,ax=axs[3,1])
                    if nrows >= 5:
                        im9 = axs[4,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(Tvsurf_sm_sort-Tvsurf_sort)/Tvsurf_sort, cmap=cm_br)
                        fig1.colorbar(im9,ax=axs[4,0])
                        im10 = axs[4,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(Tvtrop_sm_sort-Tvtrop_sort)/Tvtrop_sort, cmap=cm_br)
                        fig1.colorbar(im10,ax=axs[4,1])
                if add_axes == True:
                    #norm = MidpointNormalize(midpoint=0)
                    #im7 = axs_add[0,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(wterm_Tmax_tropeps_sm_sort/vterm_Tmax_tropeps_sm_sort-wterm_Tmax_tropdown_sort/vterm_Tmax_tropdown_sort)/(wterm_Tmax_tropdown_sort/vterm_Tmax_tropdown_sort), norm=norm, cmap=cm_br)
                    #fig2.colorbar(im7,ax=axs_add[0,0])
                    #norm = MidpointNormalize(midpoint=0)
                    #im8 = axs_add[0,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(wterm_T90_tropeps_sm_sort_pos/vterm_T90_tropeps_sm_sort-wterm_T90_tropdown_sort/vterm_T90_tropdown_sort)/(wterm_T90_tropdown_sort/vterm_T90_tropdown_sort), norm=norm, cmap=cm_br)
                    #fig2.colorbar(im8,ax=axs_add[0,1])
                    #norm = MidpointNormalize(midpoint=0)
                    #im9 = axs_add[1,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(Twsurf_sm_sort-Twsurf_sort)/(Twsurf_sort), norm=norm, cmap=cm_br)
                    #fig2.colorbar(im9,ax=axs_add[1,0])
                    #norm = MidpointNormalize(midpoint=.8*np.nanmax(100*(Twtrop_sm_sort_pos-Twtrop_sort)/(Twtrop_sort)))
                    #im10 = axs_add[1,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(Twtrop_sm_sort_pos-Twtrop_sort)/(Twtrop_sort), norm=norm, cmap=cm_br)
                    #fig2.colorbar(im10,ax=axs_add[1,1])
                    norm = MidpointNormalize(midpoint=0)
                    im11 = axs_add[1,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(Tvsurf_sm_sort-Tvsurf_sort)/(Tvsurf_sort), norm=norm, cmap=cm_br)
                    fig2.colorbar(im11,ax=axs_add[1,0])
                    norm = MidpointNormalize(midpoint=.9*np.nanmax(100*(Tvtrop_sm_sort-Tvtrop_sort)/(Tvtrop_sort)))
                    im12 = axs_add[1,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 100*(Tvtrop_sm_sort-Tvtrop_sort)/(Tvtrop_sort), norm=norm, cmap=cm_br)
                    fig2.colorbar(im12,ax=axs_add[1,1])
                # plotting sharp experiments in yellow contours:
                norm = MidpointNormalize(midpoint=0)
                im1 = axs[0,0].contour(S2S1_sm_sort, l2l1_sm_sort, gr_sm_sort, 15, colors='y')
                #axs[0,0].clabel(im1, im1.levels[::2], inline=1, fmt='%1.2f')
                im2 = axs[0,1].contour(S2S1_sm_sort, l2l1_sm_sort, 1000*wl_sm_sort, colors='y')
                im3 = axs[1,0].contour(S2S1_sm_sort, l2l1_sm_sort, 10*cph_sm_sort, colors='y')
                im4 = axs[1,1].contour(S2S1_sm_sort, l2l1_sm_sort, dq_sm_sort/[-dqdy[-1]], colors='y')           
                im5 = axs_add[0,0].contour(S2S1_sm_sort, l2l1_sm_sort, Ttroprange_sm_sort/Tsurf_sm_sort, colors='y')
                im6 = axs_add[0,1].contour(S2S1_sm_sort, l2l1_sm_sort, psitrop_sm_sort/psisurf_sm_sort, colors='y')
                if nrows >= 4:
                    im7 = axs[3,0].contourf(S2S1_sm_sort, l2l1_sm_sort, ceca_sm_sort, cmap=cm_br)
                    fig1.colorbar(im7,ax=axs[3,0])
                    im8 = axs[3,1].contourf(S2S1_sm_sort, l2l1_sm_sort, vTpos_sort, cmap=cm_br)
                    fig1.colorbar(im8,ax=axs[3,1])
                if add_axes == True:
                    #im7 = axs_add[0,0].contourf(S2S1_sm_sort, l2l1_sm_sort, (wterm_Tmax_tropeps_sm_sort/vterm_Tmax_tropeps_sm_sort), cmap=cm_br)
                    #fig2.colorbar(im7,ax=axs_add[0,0])
                    #im8 = axs_add[0,1].contourf(S2S1_sm_sort, l2l1_sm_sort, (wterm_T90_tropeps_sm_sort/vterm_T90_tropeps_sm_sort), cmap=cm_br)
                    #fig2.colorbar(im8,ax=axs_add[0,1])
                    #im9 = axs_add[1,0].contourf(S2S1_sm_sort, l2l1_sm_sort, (Twsurf_sm_sort), cmap=cm_br)
                    #fig2.colorbar(im9,ax=axs_add[1,0])
                    #norm = MidpointNormalize(midpoint=0)
                    #im10 = axs_add[1,1].contourf(S2S1_sm_sort, l2l1_sm_sort, (Twtrop_sm_sort), norm=norm, cmap=cm_br)
                    #fig2.colorbar(im10,ax=axs_add[1,1])
                    im11 = axs_add[1,0].contour(S2S1_sm_sort, l2l1_sm_sort, (Tvsurf_sm_sort), colors='y')
                    im12 = axs_add[1,1].contour(S2S1_sm_sort, l2l1_sm_sort, (Tvtrop_sm_sort), colors='y')
            elif np.shape(gr_sm_sort)[0]>1 and np.shape(gr_sm_sort)[1]>1:
                print ('plotting solutions for sharp and smooth experiments')
                norm = MidpointNormalize(midpoint=0)
                im1 = axs[0,0].contourf(S2S1_sm_sort, l2l1_sm_sort, gr_sm_sort, cmap=cm_br)
                fig1.colorbar(im1,ax=axs[0,0])
                im2 = axs[0,1].contourf(S2S1_sm_sort, l2l1_sm_sort, 1000*wl_sm_sort, cmap=cm_br)
                fig1.colorbar(im2,ax=axs[0,1])       
#                norm = MidpointNormalize(midpoint=1.1*np.nanmax(dq_sm_sort))#midpoint=-dqdy[-1])
                im3 = axs[1,0].contourf(S2S1_sm_sort, l2l1_sm_sort, 10*cph_sm_sort, cmap=cm_br)
                fig1.colorbar(im3,ax=axs[1,0])
                im4 = axs[1,1].contourf(S2S1_sm_sort, l2l1_sm_sort, dq_sm_sort/[-dqdy[-1]], cmap=cm_br)           
                fig1.colorbar(im4,ax=axs[1,1])
#                norm = MidpointNormalize(midpoint=130)
                im5 = axs_add[0,0].contourf(S2S1_sm_sort, l2l1_sm_sort, Ttroprange_sm_sort/Tsurf_sm_sort, cmap=cm_br)
                fig2.colorbar(im5,ax=axs_add[0,0])
#                norm = MidpointNormalize(midpoint=90)
                im6 = axs_add[0,1].contourf(S2S1_sm_sort, l2l1_sm_sort, psitrop_sm_sort/psisurf_sm_sort, cmap=cm_br)
                fig2.colorbar(im6,ax=axs_add[0,1])
                #norm = MidpointNormalize(midpoint=ptrop)
                #im6 = axs[2,1].contourf(S2S1_sm_sort, l2l1_sm_sort, pdq_sm_sort, norm=norm, cmap=cm_br)
                #fig1.colorbar(im6,ax=axs[2,1])
                if nrows >= 4:
                    im7 = axs[3,0].contourf(S2S1_sm_sort, l2l1_sm_sort, ceca_sm_sort, cmap=cm_br)
                    fig1.colorbar(im7,ax=axs[3,0])
                    im8 = axs[3,1].contourf(S2S1_sm_sort, l2l1_sm_sort, vTpos_sort, cmap=cm_br)
                    fig1.colorbar(im8,ax=axs[3,1])
                if add_axes == True:
                    #im7 = axs_add[0,0].contourf(S2S1_sm_sort, l2l1_sm_sort, (wterm_Tmax_tropeps_sm_sort/vterm_Tmax_tropeps_sm_sort), cmap=cm_br)
                    #fig2.colorbar(im7,ax=axs_add[0,0])
                    #im8 = axs_add[0,1].contourf(S2S1_sm_sort, l2l1_sm_sort, (wterm_T90_tropeps_sm_sort/vterm_T90_tropeps_sm_sort), cmap=cm_br)
                    #fig2.colorbar(im8,ax=axs_add[0,1])
                    #im9 = axs_add[1,0].contourf(S2S1_sm_sort, l2l1_sm_sort, (Twsurf_sm_sort), cmap=cm_br)
                    #fig2.colorbar(im9,ax=axs_add[1,0])
                    #norm = MidpointNormalize(midpoint=0)
                    #im10 = axs_add[1,1].contourf(S2S1_sm_sort, l2l1_sm_sort, (Twtrop_sm_sort), norm=norm, cmap=cm_br)
                    #fig2.colorbar(im10,ax=axs_add[1,1])
                    im11 = axs_add[1,0].contourf(S2S1_sm_sort, l2l1_sm_sort, (Tvsurf_sm_sort), cmap=cm_br)
                    fig2.colorbar(im11,ax=axs_add[1,0])
                    im12 = axs_add[1,1].contourf(S2S1_sm_sort, l2l1_sm_sort, (Tvtrop_sm_sort), cmap=cm_br)
                    fig2.colorbar(im12,ax=axs_add[1,1])
        for i in range(nrows):
            for j in range(2):
                axs[i,j].plot(4, 1-.05,'o',c=c_blues[1],ms=15,mec='k')
                axs[i,j].plot(4,-1+.05,'o',c='k',ms=15,mec='k')
                axs[i,j].plot(1+.1,-1+.05,'o',c=c_greys[0],ms=15,mec='k')
            axs[i,0].set_ylabel('$\\regular{\lambda_{st}/\lambda_{tr}}$')
        axs[nrows-1,0].set_xlabel('$\\regular{S_{st}/S_{tr}}$')
        axs[nrows-1,1].set_xlabel('$\\regular{S_{st}/S_{tr}}$')
        axs[0,0].set_title('max growth rate (1/day)')
        axs[0,1].set_title('wavelength (km)')
        axs[1,0].set_title('c$\\regular{_{ph}}$ (m/s)')#u$_{v\'T\'}$ -
        axs[1,1].set_title('$\\regular{-[d\overline{q}/dy]_{trop} / [d\overline{q}/dy]_{surf}}$')
        axs_add[0,0].set_title('$\\regular{T_{trop}/T_{surf}}$')
        axs_add[0,1].set_title('$\\regular{\psi_{trop}/\psi_{surf}}$')#pressure of new tropopause')#
        if nrows >= 4:
            axs[3,0].set_title('$\\regular{C_a}$ normalized by energy')
            axs[3,1].set_title('area where $\\regular{C_a}$(x,p)>0 (%)')
        if add_axes == True:
            #axs_add[0,0].set_title('wterm/vterm @ trop-,Tmax')#$T_{surf}/T_{trop}$')#$\mathregular{C_a}$ not normalized')# by PVdz_surf')# by energy')
            #axs_add[0,1].set_title('wterm/vterm @ trop-,T90')#$\psi_{surf}/\psi_{trop}$')#area where $\mathregular{C_a}$(x,p)>0 (%)')
            #axs_add[1,0].set_title('T-w phase shift @ surf (deg)')#vterm/wterm @ trop+,Tmax')#$T_{surf}/\psi_{surf}$')#\psi_{trop}/\psi_{surf}$')#psi_trop/psi_surf')#$\mathregular{C_e}$ normalized by energy')
            #axs_add[1,1].set_title('T-w phase shift @ trop (deg)')#vterm/wterm @ trop+,T90')#$T_{trop}/\psi_{trop}$')#PVdz_trop/PVdz_surf')#area where $\mathregular{C_e}$(x,p)>0 (%)')
            axs_add[1,0].set_title('T-v phase @ surf (deg)')
            axs_add[1,1].set_title('T-v phase @ trop (deg)')
            for i in range(nrows):
                for j in range(2):
                    axs_add[i,j].plot(4, 1-.05,'o',c=c_blues[1],ms=15,mec='k')
                    axs_add[i,j].plot(4,-1,'o',c='k',ms=15,mec='k')
                    axs_add[i,j].plot(1+.1,-1,'o',c=c_greys[0],ms=15,mec='k')
                axs_add[i,0].set_ylabel('$\\regular{\lambda_{st}/\lambda_{tr}}$')
            axs_add[nrows-1,0].set_xlabel('$\\regular{S_{st}/S_{tr}}$')
            axs_add[nrows-1,1].set_xlabel('$\\regular{S_{st}/S_{tr}}$')
            plt.setp(axs_add,xticks=S2S1_sort,yticks=l2l1_sort,xlim=[1,5],ylim=[-2,1])
        plt.setp(axs,xticks=S2S1_sort,yticks=l2l1_sort,xlim=[1,5],ylim=[-2,1])

        for i in range(nrows):
            for j in range(2):
                xmin, xmax = axs[i,j].get_xlim()
                ymin, ymax = axs[i,j].get_ylim()
                axs[i,j].add_patch(patches.Rectangle((xmin,ymin), xmax-xmin, ymax-ymin, hatch='.', fill=None, zorder=-10))
        for i in range(nrows):
            for j in range(2):
                xmin, xmax = axs_add[i,j].get_xlim()
                ymin, ymax = axs_add[i,j].get_ylim()
                axs_add[i,j].add_patch(patches.Rectangle((xmin,ymin), xmax-xmin, ymax-ymin, hatch='.', fill=None, zorder=-10))

        fig1.subplots_adjust(wspace=.3, hspace=.3)
        fig2.subplots_adjust(wspace=.3, hspace=.3)
        fig1.tight_layout()
        fig2.tight_layout()
        fig1.savefig(f'/home/kfl078/Downloads/S-vs-lambda_trop250_lambda35_original_sharp-smoothsine15.pdf', transparent=True)
        fig2.savefig(f'/home/kfl078/Downloads/S-vs-lambda_trop250_lambda35_extra_sharp-smoothsine15.pdf', transparent=True)
        plt.show()

    if ptrop_smooth == True:
        try:
            ptrop_sm
        except:
            pass
        else:
            ptrop_sm_sort = sort(list(set(ptrop_sm)))
            smfac_sm_sort = sort(list(set(smfac_sm)))

            gr_ps_sm_sort  = np.ones((len(ptrop_sm_sort),len(smfac_sm_sort)))*nan
            wl_ps_sm_sort  = np.ones((len(ptrop_sm_sort),len(smfac_sm_sort)))*nan
            dq_ps_sm_sort  = np.ones((len(ptrop_sm_sort),len(smfac_sm_sort)))*nan
            pdq_ps_sm_sort = np.ones((len(ptrop_sm_sort),len(smfac_sm_sort)))*nan

            for l in range(len(ptrop_sm_sort)):
                for s in range(len(smfac_sm_sort)):
                    try:
                        ([x for x in np.argwhere(ptrop_sm == ptrop_sm_sort[l]) if x in np.argwhere(smfac_sm == smfac_sm_sort[s])][0][0])
                    except:
                        pass
                    else:
                        index = [x for x in np.argwhere(ptrop_sm == ptrop_sm_sort[l]) if x in np.argwhere(smfac_sm == smfac_sm_sort[s])][0][0]
                        gr_ps_sm_sort[l,s]  = gr_ps_sm [index]
                        wl_ps_sm_sort[l,s]  = wl_ps_sm [index]
                        dq_ps_sm_sort[l,s]  = dq_ps_sm [index]
                        pdq_ps_sm_sort[l,s] = pdq_ps_sm[index]

            ptrop_sm_sort = 1000*ptrop_sm_sort

            fig, axs = plt.subplots(2,2,figsize=(14,12))

#            if np.array_equal(ptrop_sort, np.round(ptrop_sm_sort,1)) == True and np.array_equal(smfac_sort, np.round(smfac_sm_sort,1)) == True:
            norm = MidpointNormalize(midpoint=0)
            im1 = axs[0,0].contourf(smfac_sm_sort, ptrop_sm_sort, gr_ps_sm_sort, cmap=cm_br)
            fig.colorbar(im1,ax=axs[0,0])
            im2 = axs[0,1].contourf(smfac_sm_sort, ptrop_sm_sort, wl_ps_sm_sort, cmap=cm_br)
            fig.colorbar(im2,ax=axs[0,1])
#                norm = MidpointNormalize(midpoint=.99*np.nanmax(dq_ps_sm_sort))            
            im3 = axs[1,0].contourf(smfac_sm_sort, ptrop_sm_sort, dq_ps_sm_sort, cmap=cm_br)
#                norm = MidpointNormalize(midpoint=.99*np.nanmin(pdq_ps_sm_sort))            
            fig.colorbar(im3,ax=axs[1,0])
            im4 = axs[1,1].contourf(smfac_sm_sort, ptrop_sm_sort, pdq_ps_sm_sort, cmap=cm_br)
            fig.colorbar(im4,ax=axs[1,1])
            axs[0,0].set_ylabel('pressure @ tropopause (hPa)')
            axs[1,0].set_ylabel('pressure @ tropopause (hPa)')
            axs[1,0].set_xlabel('smooth factor')
            axs[1,1].set_xlabel('smooth factor')
            axs[0,0].set_title('max growth rate')
            axs[0,1].set_title('wavelength @ max growth rate')
            axs[1,0].set_title('max interior dq/dy')
            axs[1,1].set_title('pressure @ max interior dq/dy')
            plt.setp(axs,xticks=smfac_sm_sort,yticks=np.round(ptrop_sm_sort))
            for i in range(2):
                for j in range(2):
                    axs[i,j].invert_yaxis()

            plt.tight_layout()
            plt.show()

# -----------------------------------------------------------------------------
### defining variables for testing the growth rate sensitivity to various tropopause levels and smoothing ranges

def define_tropopause_smoothing_sensitivity():
    
    global ptrop_vec, range_vec, ptrop_noncons_vec, range_noncons_vec
    global gr_vec, gr_noncons_vec, gr_sharp
    
    if smoothshearstrat == False:
        gr_sharp = np.max(sigmai_sorted[0,0,:,-1])
    
    if smoothshearstrat == True and smoothsine == True:
        
        if noncons == False:
            try:
                ptrop_vec
            except:
                ptrop_vec = ([])
                range_vec = ([])
                gr_vec = ([])

            if len(ptrop_vec) == 0 or ptrop != ptrop_vec[-1] or -(2*ptrop_range+1)*dp != range_vec[-1]:
                print ('defining growth rate for conserved experiments')

                ptrop_vec.extend([ptrop])
                range_vec.extend([-(2*ptrop_range+1)*dp])
                gr_vec.extend([np.max(sigmai_sorted[0,0,:,-1])])

        if noncons == True:
            try:
                ptrop_noncons_vec
            except:
                ptrop_noncons_vec = ([])
                range_noncons_vec = ([])
                gr_noncons_vec = ([])

            if len(ptrop_noncons_vec) == 0 or ptrop != ptrop_noncons_vec[-1] or -(2*ptrop_range+1)*dp != range_noncons_vec[-1]:
                print ('defining growth rate for nonconserved experiments')

                ptrop_noncons_vec.extend([ptrop])
                range_noncons_vec.extend([-(2*ptrop_range+1)*dp])
                gr_noncons_vec.extend([np.max(sigmai_sorted[0,0,:,-1])])

# -----------------------------------------------------------------------------
### plotting growth rate differences for various tropopause levels and smoothing ranges

def plot_tropopause_smoothing_sensitivity():

    global gr_cons_sort, gr_noncons_sort
    
    try:
        ptrop_vec
    except:
        pass
    else:
        ptrop_sort = sort(list(set(ptrop_vec)))
        range_sort = sort(list(set(range_vec)))
        gr_cons_sort  = np.ones((len(ptrop_sort),len(range_sort)))*nan

        for i in range(len(ptrop_sort)):
            for j in range(len(range_sort)):
                try:
                    ([x for x in np.argwhere(ptrop_vec == ptrop_sort[i]) if x in np.argwhere(range_vec == range_sort[j])][0][0])
                except:
                    pass
                else:
                    index = [x for x in np.argwhere(ptrop_vec == ptrop_sort[i]) if x in np.argwhere(range_vec == range_sort[j])][0][0]
                    gr_cons_sort[i,j]  = gr_vec[index]

    try:
        ptrop_noncons_vec
    except:
        pass
    else:
        ptrop_noncons_sort = sort(list(set(ptrop_noncons_vec)))
        range_noncons_sort = sort(list(set(range_noncons_vec)))
        gr_noncons_sort  = np.ones((len(ptrop_noncons_sort),len(range_noncons_sort)))*nan

        for i in range(len(ptrop_noncons_sort)):
            for j in range(len(range_noncons_sort)):
                try:
                    ([x for x in np.argwhere(ptrop_noncons_vec == ptrop_noncons_sort[i]) if x in np.argwhere(range_noncons_vec == range_noncons_sort[j])][0][0])
                except:
                    pass
                else:
                    index = [x for x in np.argwhere(ptrop_noncons_vec == ptrop_noncons_sort[i]) if x in np.argwhere(range_noncons_vec == range_noncons_sort[j])][0][0]
                    gr_noncons_sort[i,j]  = gr_noncons_vec[index]

    ptrop_sort = 1000*np.array(ptrop_sort)
    range_sort = 1000*np.array(range_sort)
    ptrop_noncons_sort = 1000*np.array(ptrop_noncons_sort)
    range_noncons_sort = 1000*np.array(range_noncons_sort)
                    
    fig, ax = plt.subplots(figsize=(12,10))

    try:
        ptrop_vec
    except:
        pass
    else:
        print ('plotting conserved experiments in contours')
        im1 = ax.contour(range_sort, ptrop_sort, 100*(np.array(gr_cons_sort)-gr_sharp)/gr_sharp, colors='k')
        ax.clabel(im1, im1.levels[::1], inline=1, fmt='%1.1f')
    try:
        ptrop_vec
    except:
        pass
    else:
        print ('plotting nonconserved experiments in contours')
        im2 = ax.contourf(range_noncons_sort, ptrop_noncons_sort, 100*(np.array(gr_noncons_sort)-gr_sharp)/gr_sharp,cmap=cm_br)
        fig.colorbar(im2,ax=ax)
    ax.set_title('difference in growth rate relative to sharp experiment (%) \ncontours/shading: conserved/nonconserved experiments')
    ax.set_ylabel('tropopause level (hPa)')
    ax.set_yticks([200,250,300])
    ax.invert_yaxis()
    ax.set_xlabel('vertical range of smoothing (hPa)')
#    ax.set_yticks([])

#    plt.tight_layout()
    plt.show()
    
    
# -----------------------------------------------------------------------------

### plotting the error growth over a medium-range forecast comparing two different growth rates

def error_growth():

    global gr_sh_lamS, gr_sm_lamS, gr_sm_low_lamS, gr_sm_high_lamS
    global gr_sm_noncons_lamS, gr_sm_noncons_low_lamS, gr_sm_noncons_high_lamS
#    global gr_sm_S, gr_sh_S, gr_sm_lam, gr_sh_lam
#    global gr_schafler_lam, gr_schafler_lamS

    time = np.linspace(0,10*24*60**2,100)

    gr_sm_narrow_lamS = np.max(sigmai_sorted_4)*10**(-5)
    gr_sm_noncons_narrow_lamS = np.max(sigmai_sorted_5)*10**(-5)
    gr_sm_wide_lamS = np.max(sigmai_sorted_6)*10**(-5)
    gr_sm_noncons_wide_lamS = np.max(sigmai_sorted_7)*10**(-5)
    
#    if smoothshearstrat == True and schafler == True:
#        if S[0] == 4*S[-1]:
#            gr_schafler_lamS = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
#        if S[0] == S[-1]:
#            gr_schafler_lam = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
    if lambda1_disc[0] == -lambda1_disc[-1] and S_disc[0] == 4*S_disc[-1]:
        if smoothshearstrat == True:
            if noncons == False and ptrop_range == 15 and 0.24 < ptrop < 0.26:
                print ('default experiment')
                gr_sm_lamS = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
            if noncons == False and ptrop_range == 15 and 0.19 < ptrop < 0.21:
                print ('high trop experiment')
                gr_sm_high_lamS = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
            if noncons == False and ptrop_range == 15 and 0.29 < ptrop < 0.31:
                print ('low trop experiment')
                gr_sm_low_lamS = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
            if noncons == True and ptrop_range == 15 and 0.24 < ptrop < 0.26:
                print ('default noncons experiment')
                gr_sm_noncons_lamS = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
            if noncons == True and ptrop_range == 15 and 0.19 < ptrop < 0.21:
                print ('high trop noncons experiment')
                gr_sm_noncons_high_lamS = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
            if noncons == True and ptrop_range == 15 and 0.29 < ptrop < 0.31:
                print ('low trop noncons experiment')
                gr_sm_noncons_low_lamS = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
        if smoothshearstrat == False:
            gr_sh_lamS = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
#    if lambda1[0] == lambda1[-1] and S[0] == 4*S[-1]:
#        if smoothshearstrat == True:
#            gr_sm_S = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
#        if smoothshearstrat == False:
#            gr_sh_S = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
#    if lambda1[0] == -lambda1[-1] and S[0] == S[-1]:
#        if smoothshearstrat == True:
#            gr_sm_lam = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
#        if smoothshearstrat == False:
#            gr_sh_lam = np.max(sigmai_sorted[0,0,:,-1])*10**(-5)
            
    fig = plt.subplots(figsize=(8,8))
    
    plt.axhline(0,c='k',ls='-')
    try:
        gr_sh_lamS
    except:
        pass
    else:
        try:
            gr_sm_lamS
        except:
            pass
        else:
            plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_lamS-gr_sh_lamS)*time)-1),c=colors[2-1],alpha=alphas[2-1],ls=linestyles[2-1],lw=lw,label=labels[2-1])
        try:
            gr_sm_noncons_lamS
        except:
            pass
        else:
            plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_noncons_lamS-gr_sh_lamS)*time)-1),c=colors[3-1],alpha=alphas[3-1],ls=linestyles[3-1],lw=lw,label=labels[3-1])
        plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_narrow_lamS-gr_sh_lamS)*time)-1),c=colors[4-1],alpha=alphas[4-1],ls=linestyles[4-1],lw=lw,label=labels[4-1])
        plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_noncons_narrow_lamS-gr_sh_lamS)*time)-1),c=colors[5-1],alpha=alphas[5-1],ls=linestyles[5-1],lw=lw,label=labels[5-1])
        plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_wide_lamS-gr_sh_lamS)*time)-1),c=colors[6-1],alpha=alphas[6-1],ls=linestyles[6-1],lw=lw,label=labels[6-1])
        plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_noncons_wide_lamS-gr_sh_lamS)*time)-1),c=colors[7-1],alpha=alphas[7-1],ls=linestyles[7-1],lw=lw,label=labels[7-1])
        try:
            gr_sm_low_lamS
        except:
            pass
        else:
            plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_low_lamS-gr_sh_lamS)*time)-1),c=colors[8-1],alpha=alphas[8-1],ls=linestyles[8-1],lw=lw,label=labels[8-1])
        try:
            gr_sm_noncons_low_lamS
        except:
            pass
        else:
            plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_noncons_low_lamS-gr_sh_lamS)*time)-1),c=colors[9-1],alpha=alphas[9-1],ls=linestyles[9-1],lw=lw,label=labels[9-1])
        try:
            gr_sm_high_lamS
        except:
            pass
        else:
            plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_high_lamS-gr_sh_lamS)*time)-1),c=colors[10-1],alpha=alphas[10-1],ls=linestyles[10-1],lw=lw,label=labels[10-1])
        try:
            gr_sm_noncons_high_lamS
        except:
            pass
        else:
            plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_noncons_high_lamS-gr_sh_lamS)*time)-1),c=colors[11-1],alpha=alphas[11-1],ls=linestyles[11-1],lw=lw,label=labels[11-1])
#    try:
#        gr_schafler_lamS and gr_sh_lamS
#    except:
#        pass
#    else:
#        plt.plot(time/(24*60**2), 100*(np.exp((gr_schafler_lamS-gr_sh_lamS)*time)-1),'blue',ls='--',label='S-lam, Schäfler')
#    try:
#        gr_sm_lam and gr_sh_lam
#    except:
#        pass
#    else:
#        plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_lam-gr_sh_lam)*time)-1), 'green', label='lam')
#    try:
#        gr_schafler_lam and gr_sh_lam
#    except:
#        pass
#    else:
#        plt.plot(time/(24*60**2), 100*(np.exp((gr_schafler_lam-gr_sh_lam)*time)-1),'green',ls='--',label='lam, Schäfler')
#    try:
#        gr_sm_S and gr_sh_S
#    except:
#        pass
#    else:
#        plt.plot(time/(24*60**2), 100*(np.exp((gr_sm_S-gr_sh_S)*time)-1), 'red', label='S')
    plt.xlabel('time (days)')
    plt.ylabel('error relative to sharp experiment (%)')
    plt.legend(fontsize=14)
    plt.show()

# -----------------------------------------------------------------------------

### defining the error as a 4D matrix

def define_error_growth_4D_matrix():

    global gr_sh, gr_matrix
    global ran_ticks, alt_ticks, cons_ticks, eps_ticks
    global ndran, ndalt, ndcons, ndeps
    
    # define dimensions of 4D matrix
    ran_ticks = np.array([50,100,150,200]) # vertical range of smoothing/tropopause
    ndran = len(ran_ticks)
    alt_ticks = np.array([200,250,300]) # altitude of tropopause
    ndalt = len(alt_ticks)
    cons_ticks = np.array([100,85,70]) # conservativity - how much of dq/dy should be conserved above smoothing region?
    ndcons = len(cons_ticks)
    eps_ticks = epsilon1#np.array([0,1.5,2,2.5]) # latent heating intensity
    ndeps = len(epsilon1)#4

    # define growth rate for comparison, typically sharp or weakly smoothed experiment
    try:
        gr_sh
    except:
        gr_sh = np.zeros((ndeps))
    else:
        pass
    if stratos == True and smoothshearstrat == False and smoothshear == False and smoothstrat == False:
        for e in range(ndeps):
            print ('saving max growth rate for sharp experiment')
            gr_sh[e] = np.max(sigmai_sorted[e,0,:,-1])*10**(-5)
            
    # define max growth rate for various smooth experiments and put them in the correct entry of the matrix
    try:
        gr_matrix
    except:
        gr_matrix = np.zeros((ndran*ndcons,ndalt*ndeps))
    else:
        pass
    if stratos == True and smoothshearstrat == True:
        print ('saving max growth rate for smooth experiment')
        if noncons == False:
            i = 0*ndran + np.argwhere(-dp*(ptrop_range*2)*1000==ran_ticks)[0,0]
        if noncons == True and sm_scale == .85*(lambda1_disc[0]/S_disc[0])/(lambda1_disc[-1]/S_disc[-1]):
            i = 1*ndran + np.argwhere(-dp*(ptrop_range*2)*1000==ran_ticks)[0,0]
        if noncons == True and sm_scale == .7*(lambda1_disc[0]/S_disc[0])/(lambda1_disc[-1]/S_disc[-1]):
            i = 2*ndran + np.argwhere(-dp*(ptrop_range*2)*1000==ran_ticks)[0,0]
        for e in range(ndeps):
            j = e*ndalt + np.argwhere(ptrop*1000==alt_ticks)[0,0]
            if np.max(sigmai_sorted[e,0,:,-1]) > 10:
                raise AssertionError('unrealistic maximum of growth rate - remove spikes')    
            gr_matrix[i,j] = np.max(sigmai_sorted[e,0,:,-1])*10**(-5)
        

# -----------------------------------------------------------------------------

### plotting the error as a 4D matrix

def plot_error_growth_4D_matrix():  

    global error_matrix_noheating, error_matrix_heating  

    # define error matrix relative to sharp(?) experiment after %day days
    error_matrix_noheating = np.zeros((ndran*ndcons,ndalt*1))
    error_matrix_heating = np.zeros((ndran*ndcons,ndalt*(ndeps-1)))
    #time = np.linspace(0,10*24*60**2,100)
    day=5
    for i in range(ndran*ndcons):
        for j in range(ndalt*1):
            error_matrix_noheating[i,j] = 100*(np.exp((gr_matrix[i,j]-gr_sh[0])*day*24*60**2)-1)#gr_matrix[0,1]
        for j in range(ndalt*(ndeps-1)):
            error_matrix_heating[i,j] = 100*(np.exp((gr_matrix[i,j+ndalt*1]-gr_sh[2])*day*24*60**2)-1) ### consider comparing to sharp experiment for given epsilon: use int(j/3)+1 instead of epsilon=2
    error_matrix_heating = np.concatenate((error_matrix_heating[:,:ndalt],error_matrix_heating[:,ndalt:2*ndalt],error_matrix_heating[:,2*ndalt:3*ndalt]))

    # show change in growth rate instead?
    plot_gr = True
    if plot_gr == True:
        error_matrix_noheating = np.zeros((ndran*ndcons,ndalt*1))
        error_matrix_heating = np.zeros((ndran*ndcons,ndalt*(ndeps-1)))
        for i in range(ndran*ndcons):
            for j in range(ndalt*1):
                error_matrix_noheating[i,j] = 100*((gr_matrix[i,j]-gr_sh[0])/gr_sh[0])
            for j in range(ndalt*(ndeps-1)):
                error_matrix_heating[i,j] = 100*((gr_matrix[i,j+ndalt*1]-gr_sh[2])/gr_sh[2]) ### consider comparing to sharp experiment for given epsilon: use int(j/3)+1 instead of epsilon=2
        error_matrix_heating = np.concatenate((error_matrix_heating[:,:ndalt],error_matrix_heating[:,ndalt:2*ndalt],error_matrix_heating[:,2*ndalt:3*ndalt]))
            
    # prepare custom colorbar for scatter plot 
    common_colorbar = True
    cb_v1 = False
    cb_v2 = True
    cb_v3 = False
    if common_colorbar == False:
        if plot_gr == True:
            inc = 5*round(math.ceil((np.max(error_matrix_noheating))/8)/5)
            vmin = inc*math.floor(np.min(error_matrix_noheating)/inc)
            vmax = inc*math.ceil(np.max(error_matrix_noheating)/inc)
            lev = 2*int(vmax/inc)
            levmin = int(-vmin/vmax*lev/2)    
        else:
            inc = 2#5*round(math.ceil((np.max(error_matrix_noheating))/8)/5)
            vmin = inc*math.floor(np.min(error_matrix_noheating)/inc)
            vmax = inc*math.ceil(np.max(error_matrix_noheating)/inc)
            lev = 2*int(vmax/inc)
            levmin = int(-vmin/vmax*lev/2)
        cm_colors = [(0, 109/255., 136/255.), (1, 1, 1), (209/255., 98/255., 76/255.)]
        cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=lev)
        cm_colors = []
        for i in range(int(lev/2-levmin),lev):
            cm_colors.append(cm_br_scat(i))
        cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=len(cm_colors))
        ticks = np.arange(vmin,vmax,inc)
    else:
        if cb_v1 == True:
            vmin = -11
            vmax = 15
            cm_colors = [(0, 109/255., 136/255.), (1, 1, 1), (209/255., 98/255., 76/255.)]
            cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=13)
            cm_colors = [cm_br_scat(1),cm_br_scat(1),cm_br_scat(2),cm_br_scat(2),cm_br_scat(5),cm_br_scat(6),cm_br_scat(7),cm_br_scat(10),cm_br_scat(10),cm_br_scat(11),cm_br_scat(11),cm_br_scat(12),cm_br_scat(12)]
            cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=len(cm_colors))
            ticks = np.array([-11, -7, -3, -1, 1, 3, 7, 11, 15])
        elif cb_v2 == True:
            vmin = -16
            vmax = 16
            cm_colors = [(0, 109/255., 136/255.), (1, 1, 1), (209/255., 98/255., 76/255.)]
            cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=17)
            cm_colors = [cm_br_scat(0),cm_br_scat(0),cm_br_scat(0),cm_br_scat(0),cm_br_scat(1),cm_br_scat(1),cm_br_scat(1),cm_br_scat(1),cm_br_scat(2),cm_br_scat(2),cm_br_scat(2),cm_br_scat(2),cm_br_scat(5),cm_br_scat(6),cm_br_scat(7),cm_br_scat(8),cm_br_scat(8),cm_br_scat(9),cm_br_scat(10),cm_br_scat(11),cm_br_scat(14),cm_br_scat(14),cm_br_scat(14),cm_br_scat(14),cm_br_scat(15),cm_br_scat(15),cm_br_scat(15),cm_br_scat(15),cm_br_scat(16),cm_br_scat(16),cm_br_scat(16),cm_br_scat(16)]
            cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=len(cm_colors))
            ticks = np.array([-16,-12, -8, -4, -1, 1, 4, 8, 12, 16]) ### consider to remove +/- 2 and 3 for the second plot
        elif cb_v3 == True:
            vmin = -12
            vmax = 16
            cm_colors = [(0, 109/255., 136/255.), (1, 1, 1), (209/255., 98/255., 76/255.)]
            cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=13)
            cm_colors = [cm_br_scat(1),cm_br_scat(1),cm_br_scat(1),cm_br_scat(1),cm_br_scat(2),cm_br_scat(2),cm_br_scat(2),cm_br_scat(2),cm_br_scat(4),cm_br_scat(4),cm_br_scat(4),cm_br_scat(6),cm_br_scat(6),cm_br_scat(8),cm_br_scat(8),cm_br_scat(8),cm_br_scat(10),cm_br_scat(10),cm_br_scat(10),cm_br_scat(10),cm_br_scat(11),cm_br_scat(11),cm_br_scat(11),cm_br_scat(11),cm_br_scat(12),cm_br_scat(12),cm_br_scat(12),cm_br_scat(12)]
            cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=len(cm_colors))
            ticks = np.array([-12, -8, -4, -1, 1, 4, 8, 12, 16])

    # plot error growth after %day days
    fig,axes = plt.subplots(nrows=1,ncols=ndcons,figsize=(13,5), dpi=300)#3.2
    plt.subplots_adjust(wspace=.05)

    #norm = MidpointNormalize(midpoint=0)#np.min(error_matrix_noheating),vmax=np.max(error_matrix_noheating))

    for i,ax in enumerate(axes.flat):
        im = ax.scatter(np.tile(ran_ticks,ndalt),np.repeat(alt_ticks,ndran),
                        s=2800,c=((error_matrix_noheating)[i*ndran:(i+1)*ndran,:]).T.ravel(),
                        edgecolor = 'grey', marker='s',cmap=cm_br_scat,
                        vmin=vmin,vmax=vmax)
        ax.set_xticks(ran_ticks)
        for tick in ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        ax.set_xlim(20,230)
        ax.set_yticks(alt_ticks)
        for tick in ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        if i!=0 and i!=3 and i!=6:
            ax.set_yticklabels([])
        ax.set_ylim(170,330)
        ax.invert_yaxis()
        for j in range(len(np.tile(ran_ticks,ndalt))):
            ax.text(np.tile(ran_ticks,ndalt)[j],np.repeat(alt_ticks,ndran)[j],'{:1.1f}'.format(((error_matrix_noheating)[i*ndran:(i+1)*ndran,:]).T.ravel()[j]),horizontalalignment='center',verticalalignment='center',fontsize=18)
    axes.flat[0].set_title('CONS', fontsize=20)
    axes.flat[1].set_title('NCONS-85', fontsize=20)
    axes.flat[2].set_title('NCONS-70', fontsize=20)
    axes.flat[0].set_xlabel('$\\regular{vertical \; extent \; (hPa)}$', fontsize=20)
    axes.flat[1].set_xlabel('$\\regular{vertical \; extent \; (hPa)}$', fontsize=20)
    axes.flat[2].set_xlabel('$\\regular{vertical \; extent \; (hPa)}$', fontsize=20)
    axes.flat[0].set_ylabel('$\\regular{\\varepsilon=0}$ \n\n$\\regular{altitude \; (hPa)}$', fontsize=20)
    #axes.flat[0].text(-85,160,'a)')
    
    cb = fig.colorbar(im, ax=axes, orientation='horizontal', fraction=.2, shrink=1., anchor=(0.5, -1), boundaries=np.arange(-4,5,1),ticks=ticks)
    if plot_gr == False:
        cb.set_label(label=f'error after {day} days (%) relative to sharp experiment', size=18)
    else:
        cb.set_label(label=f'change in growth rate (%) relative to sharp experiment', size=18)
    cb.ax.tick_params(labelsize=18)

    plt.savefig(f'/home/kfl078/Downloads/4Dmatrix_noheating_growthrate_common-colorbar.pdf', transparent=True, bbox_inches='tight', pad_inches=.1)

    #fig.tight_layout()
    plt.show()


    # prepare custom colorbar for scatter plot with latent heating
    if common_colorbar == False:    
        inc = 10#20*round(math.ceil((np.max(error_matrix_heating))/10)/20)
        vmin = inc*math.floor(np.min(error_matrix_heating)/inc)
        vmax = inc*math.ceil(np.max(error_matrix_heating)/inc)
        lev = 2*int(vmax/inc)
        levmin = int(-vmin/vmax*lev/2)
        cm_colors = [(0, 109/255., 136/255.), (1, 1, 1), (209/255., 98/255., 76/255.)]
        cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=lev)
        cm_colors = []
        for i in range(int(lev/2-levmin),lev):
            cm_colors.append(cm_br_scat(i))
        cm_br_scat = LinearSegmentedColormap.from_list('my_list', cm_colors, N=len(cm_colors))
        ticks = np.arange(vmin,vmax,inc)

    # plot error growth after %day days
    fig,axes = plt.subplots(nrows=ndeps-1,ncols=ndcons,figsize=(13,16), dpi=300)
    plt.subplots_adjust(wspace=.05,hspace=0.05)

    for i,ax in enumerate(axes.flat):
        #ax.set_axis_off()
        im = ax.scatter(np.tile(ran_ticks,ndalt),np.repeat(alt_ticks,ndran),
                        s=2800,c=(error_matrix_heating[i*ndran:(i+1)*ndran,:]).T.ravel(),
                        edgecolor = 'grey', marker='s',cmap=cm_br_scat,
                        vmin=vmin,vmax=vmax)
        ax.set_xticks(ran_ticks)
        for tick in ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(20) 
        if i < ndcons*(ndeps-2):
            ax.set_xticklabels([])
        ax.set_xlim(20,230)
        ax.set_yticks(alt_ticks)
        for tick in ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        if i!=0 and i!=3 and i!=6:
            ax.set_yticklabels([])
        ax.set_ylim(170,330)
        ax.invert_yaxis()
        for j in range(len(np.tile(ran_ticks,ndalt))):
            ax.text(np.tile(ran_ticks,ndalt)[j],np.repeat(alt_ticks,ndran)[j],'{:1.1f}'.format(((error_matrix_heating)[i*ndran:(i+1)*ndran,:]).T.ravel()[j]),horizontalalignment='center',verticalalignment='center',fontsize=18)
    axes.flat[0].set_title('CONS', fontsize=20)
    axes.flat[1].set_title('NCONS-85', fontsize=20)
    axes.flat[2].set_title('NCONS-70', fontsize=20)
    axes.flat[ndcons*(ndeps-1)-3].set_xlabel('$\\regular{vertical \; extent \; (hPa)}$', fontsize=20)
    axes.flat[ndcons*(ndeps-1)-2].set_xlabel('$\\regular{vertical \; extent \; (hPa)}$', fontsize=20)
    axes.flat[ndcons*(ndeps-1)-1].set_xlabel('$\\regular{vertical \; extent \; (hPa)}$', fontsize=20)
    #axes.flat[0].set_ylabel('$\\regular{\\varepsilon=0}$ \n$\\regular_{altitude}$', fontsize=35)
    axes.flat[0].set_ylabel('$\\regular{\\varepsilon=1.5}$ \n\n$\\regular{altitude \; (hPa)}$', fontsize=20)
    axes.flat[3].set_ylabel('$\\regular{\\varepsilon=2.0}$ \n\n$\\regular{altitude \; (hPa)}$', fontsize=20)
    axes.flat[6].set_ylabel('$\\regular{\\varepsilon=2.5}$ \n\n$\\regular{altitude \; (hPa)}$', fontsize=20)
    #axes.flat[0].text(-85,160,'b)')

    cb = fig.colorbar(im, ax=axes, orientation='horizontal', fraction=.2, shrink=1., anchor=(0.5, 1.37), boundaries=np.arange(-16,17,1), ticks=ticks)
    if plot_gr == False:
        cb.set_label(label=f'error after {day} days (%) relative to sharp experiment for $\\varepsilon=2$', size=18)
    else:
        cb.set_label(label=f'change in growth rate (%) relative to sharp experiment', size=18)
    cb.ax.tick_params(labelsize=18)

    plt.savefig(f'/home/kfl078/Downloads/4Dmatrix_heating_growthrate_common-colorbar.pdf', transparent=True, bbox_inches='tight', pad_inches=0.1)

    #fig.tight_layout()
    plt.show()


# -----------------------------------------------------------------------------

### checking growth rate and wavelength for various latent heating and cooling intensities

def check_growthrate_and_wavelength_vs_epsilon_and_gamma():
    
    global evap_vec, sigmai3D_evapcond, WLmax
    
    if len(epsilon1) > 1:
        if sigmai3D_evapcond is None:
            evap_vec = ([])
            sigmai3D_evapcond = ([])
            WLmax = ([])

        if heating1 == True and heating2 == False and evap == False:
            evap_vec.extend([1])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.05:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.1:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.2:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.3:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.4:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.5:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))

        evap_vec_temp = np.array(evap_vec)
        sigmai3D_evapcond_temp = np.array(sigmai3D_evapcond)
        WLmax_temp = np.array(WLmax)
        evap_vec_sort = evap_vec_temp[evap_vec_temp.argsort()]
        sigmai3D_evapcond_sort = sigmai3D_evapcond_temp[evap_vec_temp.argsort()]
        WLmax_sort = WLmax_temp[evap_vec_temp.argsort()]
        
        
        if len(evap_vec) > 1:
            
            fig = plt.subplots(figsize=(6,9))

            norm = MidpointNormalize(midpoint=np.min(sigmai3D_evapcond_sort))
            ax = plt.contourf(evap_vec_sort,epsilon1,np.transpose(sigmai3D_evapcond_sort),9,norm=norm,cmap=cm_gwrr)
            CS = plt.contour(evap_vec_sort,epsilon1,np.transpose(WLmax_sort)*1000,12,colors='k',linewidths=.5)
            #ax2 = plt.contour(evap_vec_sort,epsilon1,np.transpose(sigmai3D_evapcond_sort),16,colors='k',lw=.5)
            cbar = plt.colorbar(ax, orientation="horizontal", pad=0.15)
            #cbar.add_lines(ax2)
            cbar.set_label('10$\mathregular{^{-5}s^{-1}}$')#, rotation=270, labelpad=18)
        #    cbar.set_label('growth rate (day$\mathregular{^{-1}}$)')#, rotation=270, labelpad=25)
            plt.ylabel('heating intensity parameter $\mathregular{\\varepsilon}$')
            plt.xlabel('relative cooling parameter $\mathregular{\gamma}$')
            plt.xticks([1,1.1,1.2,1.3,1.4,1.5])
            #plt.yticks([0,5,10,15])
            gca().set_xticklabels(['0.0','0.1','0.2','0.3','0.4','0.5'])
            #plt.tick_params(axis='both', labelsize=14)
            #cbar.ax.tick_params(labelsize=14)
#            manual_locations = [(1.25,10.5),(1.25,11.2),(1.25,12.),(1.25,13),(1.25,13.5),(1.25,14),(1.25,14.5)]#,(1.3, 14.5)]
            manual_locations = [(1.25,10.5),(1.25,12),(1.25,13.5),(1.25,14.5),(1.25,15.5),(1.25,16.5),(1.25,17.5)]#,(1.3, 14.5)]
            CLS = plt.clabel(CS, CS.levels[2::3],fmt='%d', fontsize=12)#,manual=manual_locations)#,inline=True)
            #new_labels = []
            #for label in CLS:
            #    lx,ly = label.get_position()
            #    new_labels.append((1.25,ly))
            #for cline in CS.collections:
            #    cline.remove()
            #for label in CLS:
            #    label.remove()
            #CS = plt.contour(evap_vec_sort,epsilon1,np.transpose(WLmax_sort)*1000,20,colors='k',linewidths=.5)
            #CLS = plt.clabel(CS, CS.levels[::2],fmt='%d',fontsize=9,inline=True, manual=(new_labels[i] for i in [0]+list(np.arange(2,7))))  

            plt.tight_layout()
            plt.show()
          
            
            fig,ax = plt.subplots(figsize=(5,3))

            norm = MidpointNormalize(midpoint=0)
            ax.axvline(12.5,c='grey',ls='-')
            #ax.plot(sigmai3D_evapcond_sort[0]-sigmai3D_evapcond_sort[-1],epsilon1,c=c[1])
            #ax.axhline(0,c='k',ls='-')
            ax.plot(epsilon1,(sigmai3D_evapcond_sort[-1]-sigmai3D_evapcond_sort[0])/sigmai3D_evapcond_sort[0],color=c[2],lw=2,label='growth rate')
            #ax2 = twiny(ax)
            ax.plot(epsilon1,((WLmax_sort[-1]-WLmax_sort[0])/WLmax_sort[0]),c='k',lw=2,ls='--', label='wavelength')
            #ax.plot(epsilon1,abs(WLmax_sort[0]),c=c[2], label='wavelength')
            #ax.plot(epsilon1,abs(WLmax_sort[-1]),c=c[1], label='wavelength')
        #    ax = plt.contourf(evap_vec_sort,epsilon1,np.transpose(sigmai3D_evapcond_sort),16,cmap=cm)
        #    CS = plt.contour(evap_vec_sort,epsilon1,np.transpose(WLmax_sort)*1000,12,colors='k',linewidths=.5)
            #ax2 = plt.contour(evap_vec_sort,epsilon1,np.transpose(sigmai3D_evapcond_sort),16,colors='k',lw=.5)
        #    cbar = plt.colorbar(ax, orientation="horizontal", pad=0.15)
            #cbar.add_lines(ax2)
        #    cbar.set_label('growth rate (day$\mathregular{^{-1}}$)')#, rotation=270, labelpad=25)
            ax.set_ylabel('relative change')
            ax.set_xlabel('heating parameter $\mathregular{\\varepsilon}$')
            ax.set_xlim(0,15)
            ax.set_ylim(-.2,1.01)
            ax.set_xticks([0,2.5,5,7.5,10,12.5,15])
            ax.set_yticklabels(['{:,.0%}'.format(x) for x in ax.get_yticks()])
            #ax.axhline(.05,c='k',ls='--')
            ax.tick_params(which='both', length=6, width=1)
            plt.legend(handlelength=2.4,prop={'size': 10},loc=2)

            plt.tight_layout()
            plt.show()
            
        #    (sigmai3D_evapcond_sort[1,6]-sigmai3D_evapcond_sort[-1,6])/sigmai3D_evapcond_sort[1,6]
        #    (WLmax_sort[1,6]-WLmax_sort[-1,6])/WLmax_sort[1,6]
        
    
    # making sure that only the 6 first latent cooling intensity experiments are saved

    try:
        evap_vec[7]
    except:
        pass
    else:
        evap_vec[:6]
        PVt_vec = PVt_vec[:6]
        PVb_vec = PVb_vec[:6]
        w_vec = w_vec[:6]
        wd_vec = wd_vec[:6]
        wh_vec = wh_vec[:6]
        wc_vec = wc_vec[:6]
        norm_energy_vec = norm_energy_vec[:6]
        norm_psi_vec = norm_psi_vec[:6]
        h1_vec = h1_vec[:6]
        evap_vec = evap_vec[:6]
    
        
# -----------------------------------------------------------------------------

### checking growth rates for different types of heating profiles

def check_modified_heating_profiles():

    global wl_1994, sigmai_sorted_1994, wl_evap05, sigmai_sorted_evap05
    global wl_1994mod, sigmai_sorted_1994mod, wl_1994mod2, sigmai_sorted_1994mod2
    
    if heating1 == False and heating2 == False:
        wl_ref = wl
        sigmai_sorted_ref = sigmai_sorted
    if heating1 == True and heating2 == False and h1pro == False and evap == False:
        wl_1994 = wl
        sigmai_sorted_1994 = sigmai_sorted
    if heating1 == True and heating2 == False and h1pro == False and evap == True and hblcstep == 1.5:
        wl_evap05 = wl
        sigmai_sorted_evap05 = sigmai_sorted
    if heating1 == True and heating2 == False and h1pro == False and evap == True and hblcstep == 1.3:
        wl_evap03 = wl
        sigmai_sorted_evap03 = sigmai_sorted
    if heating1 == True and heating2 == False and h1pro == True and h1proc == True:
        wl_1994mod = wl
        sigmai_sorted_1994mod = sigmai_sorted
    if heating1 == True and heating2 == False and h1pro == True and h1proa == True:
        wl_1994mod2 = wl
        sigmai_sorted_1994mod2 = sigmai_sorted

    fig = plt.figure(figsize=(12,5), dpi=300)
    gs = gridspec.GridSpec(1, 2, width_ratios=[2.5, 9]) 
    ax = plt.subplot(gs[0])
    ax1 = plt.subplot(gs[1])
    gs.update(wspace=.3,hspace=1) 
    
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):

            try:
                sigmai_sorted_ref1
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_noevap not defined')
            else:#, dashes=(ms,ms)
                ax1.semilogx(wl_ref,sigmai_sorted_ref[eps1_index,e2,:,0],c='lightgrey', linewidth=ms+2, label='No heating')
                for i in range(1,2):
                    ax1.semilogx(wl_ref,sigmai_sorted_ref[eps1_index,e2,:,i],c='lightgrey', linewidth=ms+2)
                    ax1.semilogx(wl_ref,sigmai_sorted_ref[eps1_index,e2,:,-i],c='lightgrey', linewidth=ms+2)            
            
            try:
                sigmai_sorted_1994
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_noevap not defined')
            else:#, dashes=(ms,ms)
                ax1.semilogx(wl_1994,sigmai_sorted_1994[eps1_index,e2,:,0],c='k',linewidth=ms-1.5, label='original w/out latent cooling')#Latent heating')
                for i in range(1,2):#c[2]#(ms+4,ms+2,ms,ms+2)
                    ax1.semilogx(wl_1994,sigmai_sorted_1994[eps1_index,e2,:,i],c='k',linewidth=ms-1.5)
                    ax1.semilogx(wl_1994,sigmai_sorted_1994[eps1_index,e2,:,-i],c='k',linewidth=ms-1.5)
            
            try:
                sigmai_sorted_evap031
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap03 not defined')
            else:
                ax1.semilogx(wl_evap03,sigmai_sorted_evap03[eps1_index,e2,:,0],c=c_blues[2],linewidth=ms+2, label='original w/ latent cooling ($\mathregular{\gamma=0.3}$)')
                for i in range(1,5):
                    ax1.semilogx(wl_evap03,sigmai_sorted_evap03[eps1_index,e2,:,i],c=c_blues[2],linewidth=ms+2)
                    ax1.semilogx(wl_evap03,sigmai_sorted_evap03[eps1_index,e2,:,-i],c=c_blues[2],linewidth=ms+2)

            try:
                sigmai_sorted_evap05
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap05 not defined')
            else:
                ax1.semilogx(wl_evap05,sigmai_sorted_evap05[eps1_index,e2,:,0],c=c_blues[3],linewidth=ms+2, label='original w/ latent cooling ($\mathregular{\gamma=0.5}$)')
                for i in range(1,5):
                    ax1.semilogx(wl_evap05,sigmai_sorted_evap05[eps1_index,e2,:,i],c=c_blues[3],linewidth=ms+2)
                    ax1.semilogx(wl_evap05,sigmai_sorted_evap05[eps1_index,e2,:,-i],c=c_blues[3],linewidth=ms+2)
                    
            try:
                sigmai_sorted_1994mod2
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_mod2 not defined')
            else:#, dashes=(ms,ms)
                ax1.semilogx(wl_1994mod2,sigmai_sorted_1994mod2[eps1_index,e2,:,0],c='k',dashes=(ms+8,ms+8), linewidth=ms-1.5, label='modified w/out latent cooling')
                for i in range(1,2):
                    ax1.semilogx(wl_1994mod2,sigmai_sorted_1994mod2[eps1_index,e2,:,i],c='k',dashes=(ms+8,ms+8), linewidth=ms-1.5)
                    ax1.semilogx(wl_1994mod2,sigmai_sorted_1994mod2[eps1_index,e2,:,-i],c='k',dashes=(ms+8,ms+8), linewidth=ms-1.5)
        
            try:
                sigmai_sorted_1994mod
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_mod1 not defined')
            else:#, dashes=(ms,ms)
                ax1.semilogx(wl_1994mod,sigmai_sorted_1994mod[eps1_index,e2,:,0],c=c_blues[3],dashes=(ms+.3,ms+.3), linewidth=ms+2, label='modified w/ latent cooling')
                for i in range(1,2):
                    ax1.semilogx(wl_1994mod,sigmai_sorted_1994mod[eps1_index,e2,:,i],c=c_blues[3],dashes=(ms+.3,ms+.3), linewidth=ms+2)
                    ax1.semilogx(wl_1994mod,sigmai_sorted_1994mod[eps1_index,e2,:,-i],c=c_blues[3],dashes=(ms+.3,ms+.3), linewidth=ms+2)
    
    ax1.axhline(0,color='dimgrey',linewidth=ms+1)
    ax1.set_xticks([1,2,5,10,50])
    ax1.set_xticklabels([1000,2000,5000,10000,50000])
    
    #ax1.set_xticks([1,3,5,10,30,50])
    #ax.set_xticklabels([1000,3000,5000,10000,30000,50000])
    ax1.tick_params(which='minor', length=3, width=1)
    ax1.tick_params(which='major', length=6, width=1)
#    ax1.tick_params(which='both', length=6, width=1)
    
    ax1.set_xlabel('wavelength (km)')#,fontsize=14)
    ax1.set_xlim((1.3, 60))#.075,60
    ax1.set_ylabel('growth rate (10$\mathregular{^{-5}s^{-1}}$)')#,fontsize=14)
    ax1.set_yticks([0.03,.5,1,1.5])
    ax1.set_yticklabels(['0.0','0.5','1.0','1.5'])
    ax1.set_ylim(0.03,1.5)#5)
#    ax1.tick_params(which='both', length=6, width=1)

    try:
        htemp1
    except NameError:
        print ('htemp1 not defined')
    else:
        ax.plot(htemp1[eps1_index,2:nrws]*p[2:nrws],p[2:nrws], c='k', linewidth=ms-1.5,label='original profile, no evap')#
    try:
        htemp2
    except NameError:
        print ('htemp3 not defined')
    else:
        ax.plot(htemp3[eps1_index,2:nrws]*p[2:nrws],p[2:nrws], c=c_blues[3], linewidth=ms+2,label='30% lc')#
    try:
        htemp3
    except NameError:
        print ('htemp3 not defined')
    else:
        ax.plot(htemp3[eps1_index,2:nrws]*p[2:nrws],p[2:nrws], c=c_blues[3], linewidth=ms+2,label='50% lc')#
    try:
        htemp6
    except NameError:
        print ('htemp6 not defined')
    else:
        ax.plot(htemp6[eps1_index,2:nrws]*p[2:nrws],p[2:nrws], c='k',dashes=(ms+8,ms+8), linewidth=ms-1.5,label='modified profile I')#
    try:
        htemp4
    except NameError:
        print ('htemp4 not defined')
    else:
        ax.plot(htemp4[eps1_index,2:nrws]*p[2:nrws],p[2:nrws], c=c_blues[3],dashes=(ms+.3,ms+.3), linewidth=ms+2,label='Modified profile II')#
    #plt.plot(h1[eps1_index,nrws:],p[:nrws], c=c[1], linewidth=2.5, label='heating profile')#c[0]
    ax.set_xlabel('heating profile')#, fontsize=14)# (real: blue)')
    ax.set_ylim(0.15,1)
    ax.set_yticks([0.15,.4,.9,1])
    ax.set_xticks([-1,0,1])
    ax.invert_yaxis()
    ax.set_ylabel('pressure')
    ax.tick_params(which='both', length=6, width=1)
    plt.legend(loc=1, handlelength=4)#, prop={'size': 10})
    
    ax.text(-1.85,0.152,'a)')
    ax.text(1.75,0.152,'b)')
    
#    fig.savefig(f'/home/kfl078/Downloads/python/fig11_modheating.pdf', transparent=True)
    
    plt.show()
    
# -----------------------------------------------------------------------------

### plotting growth rates for varying amount of latent cooling

def check_growthrates_for_various_gamma():

    global wl_eady, sigmai_sorted_eady, wl_noevap, sigmai_sorted_noevap
    global wl_evap01, sigmai_sorted_evap01, wl_evap02, sigmai_sorted_evap02, wl_evap03, sigmai_sorted_evap03, wl_evap04, sigmai_sorted_evap04, wl_evap05, sigmai_sorted_evap05

    if heating1 == False:
        wl_eady = wl
        sigmai_sorted_eady = sigmai_sorted
    if hblcstep == 1:
        wl_noevap = wl
        sigmai_sorted_noevap = sigmai_sorted
    if hblcstep == 1.1:
        wl_evap01 = wl
        sigmai_sorted_evap01 = sigmai_sorted
    if hblcstep == 1.2:
        wl_evap02 = wl
        sigmai_sorted_evap02 = sigmai_sorted
    if hblcstep == 1.3:
        wl_evap03 = wl
        sigmai_sorted_evap03 = sigmai_sorted
    if hblcstep == 1.4:
        wl_evap04 = wl
        sigmai_sorted_evap04 = sigmai_sorted
    if hblcstep == 1.45:
        wl_evap045 = wl
        sigmai_sorted_evap045 = sigmai_sorted
    if hblcstep == 1.5:
        wl_evap05 = wl
        sigmai_sorted_evap05 = sigmai_sorted
    if hblcstep == 1.6:
        wl_evap06 = wl
        sigmai_sorted_evap06 = sigmai_sorted
    if hblcstep == 1.8:
        wl_evap08 = wl
        sigmai_sorted_evap08 = sigmai_sorted
        
        
    fig, (ax1) = plt.subplots(figsize=(11,6),dpi=300)

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
        
            try:
                sigmai_sorted_eady
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_eady not defined')
            else:#, dashes=(ms,ms)
                ax1.semilogx(wl_eady,sigmai_sorted_eady[e,e2,:,0],c='grey', linestyle='--',linewidth=ms+1, label='dry')
                for i in range(1,2):
                    ax1.semilogx(wl_eady,sigmai_sorted_eady[e,e2,:,i],c='grey', linestyle='--', linewidth=ms+1)
                    ax1.semilogx(wl_eady,sigmai_sorted_eady[e,e2,:,-i],c='grey', linestyle='--', linewidth=ms+1)
        
            try:
                sigmai_sorted_noevap
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_noevap not defined')
            else:#, dashes=(ms,ms)
                ax1.semilogx(wl_noevap,sigmai_sorted_noevap[e,e2,:,0],c=c_blues[0], linewidth=ms+1, label='  0%')
                for i in range(1,2):
                    ax1.semilogx(wl_noevap,sigmai_sorted_noevap[e,e2,:,i],c=c_blues[0], linewidth=ms+1)
                    ax1.semilogx(wl_noevap,sigmai_sorted_noevap[e,e2,:,-i],c=c_blues[0], linewidth=ms+1)
            
            try:
                sigmai_sorted_evap01
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap01 not defined')
            else:
                ax1.semilogx(wl_evap01,sigmai_sorted_evap01[e,e2,:,0],c=c_blues[1],linewidth=ms, label='10%')#,dashes=(ms+8,ms+4)
                for i in range(1,5):
                    ax1.semilogx(wl_evap01,sigmai_sorted_evap01[e,e2,:,i],c=c_blues[1],linewidth=ms)
                    ax1.semilogx(wl_evap01,sigmai_sorted_evap01[e,e2,:,-i],c=c_blues[1],linewidth=ms)
            
            try:
                sigmai_sorted_evap02
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap02 not defined')
            else:
                ax1.semilogx(wl_evap02,sigmai_sorted_evap02[e,e2,:,0],c=c_blues[2], linewidth=ms, label='20%')#,dashes=(ms+4,ms+2,ms,ms+2)
                for i in range(1,5):
                    ax1.semilogx(wl_evap02,sigmai_sorted_evap02[e,e2,:,i],c=c_blues[2],linewidth=ms)
                    ax1.semilogx(wl_evap02,sigmai_sorted_evap02[e,e2,:,-i],c=c_blues[2],linewidth=ms)
            
            try:
                sigmai_sorted_evap03
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap03 not defined')
            else:
                ax1.semilogx(wl_evap03,sigmai_sorted_evap03[e,e2,:,0],c=c_blues[3],linestyle='-', linewidth=ms, label='30%')
                for i in range(1,5):
                    ax1.semilogx(wl_evap03,sigmai_sorted_evap03[e,e2,:,i],c=c_blues[3],linestyle='-',linewidth=ms)
                    ax1.semilogx(wl_evap03,sigmai_sorted_evap03[e,e2,:,-i],c=c_blues[3],linestyle='-',linewidth=ms)#, alpha=.9)

            try:
                sigmai_sorted_evap04
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap04 not defined')
            else:
                ax1.semilogx(wl_evap04,sigmai_sorted_evap04[e,e2,:,0],c=c_blues[4], linewidth=ms, label='40%')#,dashes=(ms+15,ms+2)
                for i in range(1,5):
                    ax1.semilogx(wl_evap04,sigmai_sorted_evap04[e,e2,:,i],c=c_blues[4],linewidth=ms)
                    ax1.semilogx(wl_evap04,sigmai_sorted_evap04[e,e2,:,-i],c=c_blues[4],linewidth=ms)#, alpha=.9)
 
            try:
                sigmai_sorted_evap045
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap045 not defined')
            else:
                ax1.semilogx(wl_evap045,sigmai_sorted_evap045[e,e2,:,0],c=c_blues[5], linewidth=ms, label='45%')#,dashes=(ms+3,ms+2)
                for i in range(1,5):
                    ax1.semilogx(wl_evap045,sigmai_sorted_evap045[e,e2,:,i],c=c_blues[5],linewidth=ms)
                    ax1.semilogx(wl_evap045,sigmai_sorted_evap045[e,e2,:,-i],c=c_blues[5],linewidth=ms)#, alpha=.9)

            try:
                sigmai_sorted_evap05
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap05 not defined')
            else:
                ax1.semilogx(wl_evap05,sigmai_sorted_evap05[e,e2,:,0],c=c_blues[5],linewidth=ms, label='50%')#,dashes=(ms+3,ms+2)
                for i in range(1,5):
                    ax1.semilogx(wl_evap05,sigmai_sorted_evap05[e,e2,:,i],c=c_blues[5],linewidth=ms)
                    ax1.semilogx(wl_evap05,sigmai_sorted_evap05[e,e2,:,-i],c=c_blues[5],linewidth=ms)#, alpha=.9)

            try:
                sigmai_sorted_evap06
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap06 not defined')
            else:
                ax1.semilogx(wl_evap06,sigmai_sorted_evap06[e,e2,:,0],c=c_blues[5],linewidth=ms, label='60%')#,dashes=(ms+3,ms+2)
                for i in range(1,5):
                    ax1.semilogx(wl_evap06,sigmai_sorted_evap06[e,e2,:,i],c=c_blues[5],linewidth=ms)
                    ax1.semilogx(wl_evap06,sigmai_sorted_evap06[e,e2,:,-i],c=c_blues[5],linewidth=ms)#, alpha=.9)

            try:
                sigmai_sorted_evap08
            except NameError:
                if e == 0:
                    print ('sigmai_sorted_evap08 not defined')
            else:
                ax1.semilogx(wl_evap08,sigmai_sorted_evap08[e,e2,:,0],c=c_blues[5],linewidth=ms, label='80%')#,dashes=(ms+3,ms+2)
                for i in range(1,5):
                    ax1.semilogx(wl_evap08,sigmai_sorted_evap08[e,e2,:,i],c=c_blues[5],linewidth=ms)
                    ax1.semilogx(wl_evap08,sigmai_sorted_evap08[e,e2,:,-i],c=c_blues[5],linewidth=ms)#, alpha=.9)
 
    ax1.axhline(0,color='dimgrey',linewidth=ms+1)
    ax1.set_xticks([.1,.5,1,5,10,50])
    ax1.set_xticklabels([100,500,1000,5000,10000,50000])
    ax1.set_xlabel('wavelength (km)',fontsize=16)
    ax1.set_xlim((.6, 60))
    ax1.set_ylabel('growth rate (day$\mathregular{^{-1}}$)',fontsize=16)
    ax1.set_yticks([0,.5,1,1.5,2,2.5,3])
    ax1.set_ylim(0,1.5)
    ax1.tick_params(axis='both', labelsize=14)
    plt.legend(loc=1, handlelength=3.75, prop={'size': 12})

    plt.show()
    
    fig.savefig(f'/home/kfl078/Downloads/python/growthrates_LH+LC_epsilon15.pdf', transparent=True)
    
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# energetics
# -----------------------------------------------------------------------------

kx = np.linspace(0, 2*np.pi, int(round(wl[i_maxunstab[eps1_index,eps2_index]]*1000/10))+1)		# for structure plots, used to be 128 grid points


### defining energetic terms

def dpsidpcalc(arg):
    dpsidp = np.zeros(np.shape(arg), dtype = complex)
    for e in range(len(epsilon1)):
        for i in range(len(k)):
            for j in range(1,nrws-1):
                dpsidp[e,i,j] = (arg[e,i,j+1]-arg[e,i,j-1])/(2*dp)
            dpsidp[e,i,0] = (arg[e,i,1]-arg[e,i,0])/dp
            dpsidp[e,i,-1] = (arg[e,i,-1]-arg[e,i,-2])/dp
    dpsidp = (dpsidp[:,:,:,np.newaxis]*np.exp(kx[np.newaxis,np.newaxis,np.newaxis,:]*1j)).real
    return dpsidp

# total Q
def Qtotcalc(arg1,arg2):
    Qtemp = -epsilon1[:,np.newaxis,np.newaxis,np.newaxis]*h1[:,np.newaxis,:nrws,np.newaxis]*arg1[:,:,np.newaxis]/2 \
            +epsilon2[eps2_index]*h2[eps2_index,np.newaxis,:nrws,np.newaxis]*arg2[:,:,np.newaxis]
    return Qtemp

# latent heating
def Q1acalc(arg1): # :nrws
    Q1temp = -epsilon1[:,np.newaxis,np.newaxis,np.newaxis]*h1[:,np.newaxis,:jblc,np.newaxis]*arg1[:,:,np.newaxis]/2
    return Q1temp

# latent cooling
def Q1bcalc(arg1): # default arg1b = :nrws
    Q1temp = -epsilon1[:,np.newaxis,np.newaxis,np.newaxis]*h1[:,np.newaxis,jblc:nrws,np.newaxis]*arg1[:,:,np.newaxis]/2
    return Q1temp

# surface fluxes
def Q2calc(arg2):
    Q2temp = +epsilon2[eps2_index]*h2[eps2_index,np.newaxis,:nrws,np.newaxis]*arg2[:,:,np.newaxis]
    return Q2temp


def calculate_energetics():

    global vTvec, QT1avec, QT1bvec, QT2vec, wTvec    
    global vTn, QT1an, QT1bn, QT2n, wTn, Qvec
    
    wvec = (-eigvecs_sorted_scaled[:,e2,:,:nrws,-1,np.newaxis]*np.exp(kx[np.newaxis,np.newaxis,:]*1j) ).real
    psivec = (eigvecs_sorted_scaled[:,e2,:,nrws:,-1,np.newaxis]*np.exp(kx[np.newaxis,np.newaxis,:]*1j) ).real
    Tvec = dpsidpcalc(eigvecs_sorted_scaled[:,e2,:,nrws:,-1])
    vvec = (1j*k[np.newaxis,:,np.newaxis,np.newaxis]*eigvecs_sorted_scaled[:,e2,:,nrws:,-1,np.newaxis]*np.exp(kx[np.newaxis,np.newaxis,:]*1j) ).real
    Q1avec = Q1acalc(-wvec[:,:,jtml])
    Q1bvec = Q1bcalc(-wvec[:,:,jtml])
    Q2vec = Q2calc(-Tvec[:,:,-1])
    Qvec = Qtotcalc(-wvec[:,:,jtml],-Tvec[:,:,-1])

    wTvec = simps(simps(wvec*Tvec,kx)/(2*np.pi),p[:nrws])/wl
    vTvec = simps(lambda1[:nrws]/S[:nrws]*simps(vvec*Tvec,kx)/(2*np.pi),p[:nrws])/wl
    QT1avec = simps(1/S[:jblc]*simps(Q1avec*Tvec[:,:,:jblc],kx)/(2*np.pi),p[:jblc])/wl
    QT1bvec = simps(1/S[jblc:nrws]*simps(Q1bvec*Tvec[:,:,jblc:nrws],kx)/(2*np.pi),p[jblc:nrws])/wl
    QT2vec = simps(1/S[:nrws]*simps(Q2vec*Tvec,kx)/(2*np.pi),p[:nrws])/wl
    QTvec = simps(1/S[:nrws]*simps(Qvec*Tvec,kx)/(2*np.pi),p[:nrws])/wl
    
    vTn = nan*np.ones((len(epsilon1),len(k)))#,dtype=complex)
    QT1an = nan*np.ones((len(epsilon1),len(k)))#,dtype=complex)
    QT1bn = nan*np.ones((len(epsilon1),len(k)))#,dtype=complex)
    QT2n = nan*np.ones((len(epsilon1),len(k)))#,dtype=complex)
    wTn = nan*np.ones((len(epsilon1),len(k)))#,dtype=complex)
    
    totvec = (vTvec)+(QT1avec)+(QT1bvec)+(QT2vec)+(wTvec)
    
    for e in range(len(epsilon1)):
        for i in range(len(k)):
            if sigmai_sorted[e,e2,i,-1] > .00001:
                vTn[e,i] = (vTvec[e,i])/(totvec[e,i])
                QT1an[e,i] = (QT1avec[e,i])/(totvec[e,i])
                QT1bn[e,i] = (QT1bvec[e,i])/(totvec[e,i])            
                QT2n[e,i] = (QT2vec[e,i])/(totvec[e,i])
                wTn[e,i] = (wTvec[e,i])/(totvec[e,i])

# -----------------------------------------------------------------------------

### define scaled energetics for most unstable mode(s)
                
def define_energetics():

    global explabel, vT, wT, QT1a, QT2
    global explabel, vT_trop, wT_trop, QT1a_trop, QT2_trop
#    global tot, vTplot, wTplot, QT1aplot, QT2plot

    try:
        explabel
    except:
        explabel = ([])
        vT = ([]) 
        wT = ([]) 
        QT1a = ([]) 
        QT2 = ([])
        vT_trop = ([]) 
        wT_trop = ([]) 
        QT1a_trop = ([]) 
        QT2_trop = ([])
    
    if len(vT) == 0 or (len(vT) > 0 and vT[-1] != simps(lambda1[:nrws]/S[:nrws]*simps(v*T[eps1_index,eps2_index],kx)/(2*np.pi),p[:nrws])/wl[i_maxunstab[eps1_index,eps2_index]]):
        print ('defining terms')

        if heating2 == False and heating1 == False:
            explabel.extend(['Eady'])###
        elif heating2 == False and heating1 == True:
            explabel.extend(['lh'])###
        elif heating2 == True and wpar == False and vpar == False:
            explabel.extend(['$\mathregular{T_{s}}$'])
        elif heating2 == True and wpar == False and vpar == True:
            explabel.extend(['$\mathregular{v_{s}}$'])
        elif heating2 == True and wpar == True and vpar == False and epsilon2[eps2_index].real>0:
            explabel.extend(['$\mathregular{\omega_{\\ast,0^\circ}}$'])
        elif heating2 == True and wpar == True and vpar == False and epsilon2[eps2_index].imag>0:
            explabel.extend(['$\mathregular{\omega_{\\ast,\\minus 90^\circ}}$'])
        elif heating2 == True and wpar == True and vpar == False and epsilon2[eps2_index].imag<0:
            explabel.extend(['$\mathregular{\omega_{\\ast,\\plus 90^\circ}}$'])
        elif heating2 == True and wpar == True and vpar == False and epsilon2[eps2_index].real<0:
            explabel.extend(['$\mathregular{\omega_{\\ast,180^\circ}}$'])
        else:
            explabel.extend(['unknown'])
#            raise AssertionError('make label')
            
        vT.extend([ simps(lambda1[:nrws]/S[:nrws]*simps(v*T[eps1_index,eps2_index],kx)/(2*np.pi),p[:nrws])/wl[i_maxunstab[eps1_index,eps2_index]] ])
        wT.extend([ simps(simps(-w*T[eps1_index,eps2_index],kx)/(2*np.pi),p[:nrws])/wl[i_maxunstab[eps1_index,eps2_index]] ])
        QT1a.extend([ simps(1/S[:jblc]*simps(Q[:jblc]*T[eps1_index,eps2_index,:jblc],kx)/(2*np.pi),p[:jblc])/wl[i_maxunstab[eps1_index,eps2_index]] ])
        QT2.extend([ simps(1/S[jtsf+1:nrws]*simps(Q[jtsf+1:]*T[eps1_index,eps2_index,jtsf+1:],kx)/(2*np.pi),p[jtsf+1:nrws])/wl[i_maxunstab[eps1_index,eps2_index]] ])
        if stratos == True:
            vT_trop.extend([ simps(lambda1[jtrop:nrws]/S[jtrop:nrws]*simps(v[jtrop:]*T[eps1_index,eps2_index,jtrop:],kx)/(2*np.pi),p[jtrop:nrws])/wl[i_maxunstab[eps1_index,eps2_index]] ])
            wT_trop.extend([ simps(simps(-w[jtrop:]*T[eps1_index,eps2_index,jtrop:],kx)/(2*np.pi),p[jtrop:nrws])/wl[i_maxunstab[eps1_index,eps2_index]] ])
            QT1a_trop.extend([ simps(1/S[jtrop:jblc]*simps(Q[jtrop:jblc]*T[eps1_index,eps2_index,jtrop:jblc],kx)/(2*np.pi),p[jtrop:jblc])/wl[i_maxunstab[eps1_index,eps2_index]] ])
            QT2_trop.extend([ simps(1/S[jtsf+1:nrws]*simps(Q[jtsf+1:]*T[eps1_index,eps2_index,jtsf+1:],kx)/(2*np.pi),p[jtsf+1:nrws])/wl[i_maxunstab[eps1_index,eps2_index]] ])
        

# -----------------------------------------------------------------------------

### plot scaled energetics for most unstable mode(s)
                
def plot_energetics_scaled_barchart():    
    
    expvec = np.arange(0,len(vT))
    tot = [vT[j]+QT1a[j]+QT2[j] for j in range(len(vT))]#+wT[j]
    grscale = np.ones(len(vT))#np.max(sigmai_sorted_2)/np.max(sigmai_sorted_1),np.max(sigmai_sorted_4)/np.max(sigmai_sorted_1),np.max(sigmai_sorted_3)/np.max(sigmai_sorted_1),1]
    vTplot = [vT[j]/tot[j]*grscale[j] for j in range(len(vT))]
    wTplot = [wT[j]/tot[j]*grscale[j] for j in range(len(vT))]
    QT1aplot = [QT1a[j]/tot[j]*grscale[j] for j in range(len(vT))]
    QT2plot = [QT2[j]/tot[j]*grscale[j] for j in range(len(vT))]
        
    width = .12#22
    labels = ['$\mathregular{C_a}$','$\mathregular{G_e^{lh}}$','$\mathregular{G_e^{sf}}$','$\mathregular{C_e}$']# = dE/dt   #'$\mathregular{C_e}$ = d(KE)/dt'
    
    col = ['grey','k',c[2],c[1],(.4,.4,.4),(.55,.55,.55),(.8,.8,.8),(.95,.95,.95)]
    fs = 18
    
    fig,(ax) = plt.subplots(figsize=(14.5,7.5), dpi=300)
    #ax.stackplot(expvec,vTplot,wTplot,QT1aplot,QT2plot,colors=([c[i] for i in [5,2,1,0]]),edgecolor='None',labels=labels)
    for i in range(0,8):#len(vT)): ###range(1,len(vT)):
        ax.bar(1-((len(vT))/2)*width+i*width,vTplot[i]*100,width,color=col[i],label=explabel[i])
        ax.bar(2-((len(vT))/2)*width+i*width,QT1aplot[i]*100,width,#bottom=[vTplot[j]+wTplot[j] for j in range(len(vT))],
            color=col[i])#,label=labels[2])
        ax.bar(3-((len(vT))/2)*width+i*width,QT2plot[i]*100,width,#bottom=[vTplot[j]+wTplot[j]+QT1aplot[j] for j in range(len(vT))],
            color=col[i])#,alpha=0,hatch='/',label=labels[3])
        ax.bar(4-((len(vT))/2)*width+i*width,wTplot[i]*100,width,#bottom=vTplot,
            color=col[i])#,label=labels[1])
        ax.text(1.01-((len(vT))/2)*width+i*width,12,f'{vTplot[i]*100:.1f}', horizontalalignment='center', verticalalignment='top', rotation=90, fontsize=fs)
        if QT1a[i] != 0:
            ax.text(2.01-((len(vT))/2)*width+i*width,12,f'{QT1aplot[i]*100:.1f}', horizontalalignment='center', verticalalignment='top', rotation=90, fontsize=fs)
        if QT2[i] != 0:
            ax.text(3.01-((len(vT))/2)*width+i*width,12,f'{QT2plot[i]*100:.1f}', horizontalalignment='center', verticalalignment='top', rotation=90, fontsize=fs)
        ax.text(4.01-((len(vT))/2)*width+i*width,12,f'{wTplot[i]*100:.1f}', horizontalalignment='center', verticalalignment='top', rotation=90, fontsize=fs)
        if i == 1:
            ax.text(1.01-((len(vT))/2)*width+i*width,12,f'{vTplot[i]*100:.1f}', horizontalalignment='center', verticalalignment='top', rotation=90, fontsize=fs, color='w')
            if QT1a[i] != 0:
                ax.text(2.01-((len(vT))/2)*width+i*width,12,f'{QT1aplot[i]*100:.1f}', horizontalalignment='center', verticalalignment='top', rotation=90, fontsize=fs, color='w')
            if QT2[i] != 0:
                ax.text(3.01-((len(vT))/2)*width+i*width,12,f'{QT2plot[i]*100:.1f}', horizontalalignment='center', verticalalignment='top', rotation=90, fontsize=fs, color='w')
            ax.text(4.01-((len(vT))/2)*width+i*width,12,f'{wTplot[i]*100:.1f}', horizontalalignment='center', verticalalignment='top', rotation=90, fontsize=fs, color='w')
#        ax.text(expvec[j],vTplot[j]+wTplot[j]-.05,f'{wTplot[j]:.3}', horizontalalignment='center', fontsize=18)
#        ax.text(expvec[j],vTplot[j]+wTplot[j]+QT1aplot[j]-QT2plot[j]-.05,f'{QT1aplot[j]:.3}', horizontalalignment='center', fontsize=18)

    ax.legend(loc='upper center', ncol=7, bbox_to_anchor=(.5,-.18), handlelength=.7)
    ax.set_ylabel('% of total source of $A_e$')
    ax.set_xlabel('energetic term')
    ax.set_xticks(np.arange(1,5,1))
    ax.set_xticklabels(labels,rotation='vertical')
#    ax.set_xlim(-.5,3.5)
#    ax.set_ylim(.9,1.1)
    ax.axhline(0,color='k')
    
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.show()
    
#    fig.savefig(f'/home/kfl078/Downloads/python/energetics_S4_ratio2.pdf', transparent=True)
    
# -----------------------------------------------------------------------------
    
def reset_last_energetics():

    global explabel, vT, wT, QT1a, QT2

    explabel = explabel[:-1]
    vT = vT[:-1]
    wT = wT[:-1]
    QT1a = QT1a[:-1]
    QT2 = QT2[:-1]

# -----------------------------------------------------------------------------

### comparing relative contribution to energetics
    
def energetics_accumulated():

    dAPE = vTn+QT1an+QT1bn+QT2n-wTn
    
    fig,(ax2) = plt.subplots(figsize=(14,5))
    ax1 = twinx(ax2)
    lns1 = ax1.semilogx(wl,sigmai_sorted[eps1_index,eps2_index,:,-1],c='k',linewidth=2,label='growth rate')#, $\mathregular{\gamma}$=0.0')#$\mathregular{\sigma_i}$')
    labels = ['$\mathregular{C_a}$','$\mathregular{G_e^{lh}}$','$\mathregular{G_e^{sf}}$','$\mathregular{C_e}$ = d(KE)/dt']# = dE/dt
    lns3 = ax2.stackplot(wl,vTn[eps1_index],QT1an[eps1_index]+QT1bn[eps1_index],QT2n[eps1_index],wTn[eps1_index],colors=([c[i] for i in [5,2,1,0]]),edgecolor='None',labels=labels)
    #lns2 = ax2.semilogx((0,0),(0,0),color='w',linewidth=2, path_effects=[pe.Stroke(linewidth=3, foreground='k'), pe.Normal()], label='d(APE)/dt')

    lns = lns1+lns3
    labs = [l.get_label() for l in lns]
    plt.legend(lns, labs, prop={'size': 16}, loc='lower right', framealpha=1,  facecolor='w')#bbox_to_anchor=(1, 0.5), 
    
    ax1.set_xticks([.1,.5,1,5,10,50])
    ax1.set_xticklabels([100,500,1000,5000,10000,50000])
    ax1.set_xlim((1, np.max(wl))) #.04
    ax2.set_xlim((1, np.max(wl))) #.04
    ax1.set_xlabel('wavelength (km)')
    
#    ax1.set_yticks([0,.5,1,1.5,2])
    ax1.set_ylim(0.0,2.7)
    ax1.set_ylabel('growth rate (day$\mathregular{^{-1}}$)', rotation=270, labelpad=25)
    ax2.set_yticks([0,.25,.5,.75,1])
    ax2.set_yticklabels(['0%','25%','50%','75%','100%'])
#    ax2.set_ylim(0,2/sigmai_unstab[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]])#max((vTvec+QTvec+wTvec)/dAPEdt))
#    ax2.set_ylim(0.0,1)    
    ax2.set_ylabel('relative conversion terms')#, color='b')
    
    ax2.tick_params(which='minor', length=3, width=1)
    ax2.tick_params(which='major', length=6, width=1)
    ax1.tick_params(which='both', length=6, width=1)
    
    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------

### checking relative energetic contributions for varying latent cooling intensities

def energetics_latent_cooling():
    
    try:
        ec_vec
    except:
        ec_vec = ([])
        vTn_ec = ([])
        QT1an_ec = ([])
        wTn_ec = ([])
        totfluxes = ([])
            
    if heating1 == True and heating2 == False and evap == False:
        ec_vec.extend([1])
        vTn_ec.extend([vTn[eps1_index,i_maxunstab][0][0]])
        QT1an_ec.extend([QT1an[eps1_index,i_maxunstab][0][0]])
        wTn_ec.extend([wTn[eps1_index,i_maxunstab][0][0]])
        totfluxes.extend([totvec[eps1_index,i_maxunstab][0][0]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.1:
        ec_vec.extend([hblcstep])
        vTn_ec.extend([vTn[eps1_index,i_maxunstab][0][0]])
        QT1an_ec.extend([QT1an[eps1_index,i_maxunstab][0][0]])
        wTn_ec.extend([wTn[eps1_index,i_maxunstab][0][0]])
        totfluxes.extend([totvec[eps1_index,i_maxunstab][0][0]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.2:
        ec_vec.extend([hblcstep])
        vTn_ec.extend([vTn[eps1_index,i_maxunstab][0][0]])
        QT1an_ec.extend([QT1an[eps1_index,i_maxunstab][0][0]])
        wTn_ec.extend([wTn[eps1_index,i_maxunstab][0][0]])
        totfluxes.extend([totvec[eps1_index,i_maxunstab][0][0]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.3:
        ec_vec.extend([hblcstep])
        vTn_ec.extend([vTn[eps1_index,i_maxunstab][0][0]])
        QT1an_ec.extend([QT1an[eps1_index,i_maxunstab][0][0]])
        wTn_ec.extend([wTn[eps1_index,i_maxunstab][0][0]])
        totfluxes.extend([totvec[eps1_index,i_maxunstab][0][0]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.4:
        ec_vec.extend([hblcstep])
        vTn_ec.extend([vTn[eps1_index,i_maxunstab][0][0]])
        QT1an_ec.extend([QT1an[eps1_index,i_maxunstab][0][0]])
        wTn_ec.extend([wTn[eps1_index,i_maxunstab][0][0]])  
        totfluxes.extend([totvec[eps1_index,i_maxunstab][0][0]]) 
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.5:
        ec_vec.extend([hblcstep])
        vTn_ec.extend([vTn[eps1_index,i_maxunstab][0][0]])
        QT1an_ec.extend([QT1an[eps1_index,i_maxunstab][0][0]])
        wTn_ec.extend([wTn[eps1_index,i_maxunstab][0][0]])  
        totfluxes.extend([totvec[eps1_index,i_maxunstab][0][0]]) 

    ec_vec_temp = np.array(ec_vec)
    vTn_ec_temp = np.array(vTn_ec)
    QT1an_ec_temp = np.array(QT1an_ec)
    wTn_ec_temp = np.array(wTn_ec)
    totfluxes_temp = np.array(totfluxes)
    
    ec_vec_sort = ec_vec_temp[ec_vec_temp.argsort()]
    vTn_ec_sort = vTn_ec_temp[ec_vec_temp.argsort()]
    QT1an_ec_sort = QT1an_ec_temp[ec_vec_temp.argsort()]
    wTn_ec_sort = wTn_ec_temp[ec_vec_temp.argsort()]
    totfluxes_sort = totfluxes_temp[ec_vec_temp.argsort()]
    
    fig = plt.figure(figsize=(13,3)) 
    gs = gridspec.GridSpec(1, 2, width_ratios=[6, 4]) 
    ax = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    gs.update(wspace=.4) 
    
    labels = ['$\mathregular{C_a}$','$\mathregular{G^h_e}$','$\mathregular{C_e}$ = dK/dt']# = dE/dt
    #labels = ['$\lambda/S \cdot \overline{\Psi_x\'\Psi_p\'}$','$1/S \cdot \overline{Q\'\Psi_p\'}$','$\overline{W\'\Psi_p\'}$ = d(KE)/dt']# = dE/dt
    ax.axvline(wl[np.argwhere(sigmai_sorted[eps1_index,eps2_index,:,-1]>.01)[0][0]-1],c='k',ls='-',lw=1.5)
    lns3 = ax.stackplot(wl,vTn_noevap[eps1_index],QT1an_noevap[eps1_index],wTn_noevap[eps1_index],colors=([c[i] for i in [5,2,0]]),edgecolor='None',labels=labels)
    #lns3 = ax2.stackplot(wl,vTn[e],QT1an[e],wTn[e],colors=([c[i] for i in [5,2,0]]),hatch='x',alpha=.2,edgecolor='None',labels=labels)
#    ax2.stackplot(wl,y1+y2-y3,hatch='x',alpha=0.3)#,labels=labels)
#    ax.semilogx(wl,dAPE,color='w',linewidth=2)
#    ax2.semilogx(wl,vTn[e]+QT1an[e]+QT1bn[e]+QT2n[e]-wTn[e],color='w',linewidth=2)
#    lns2 = ax.semilogx((0,0),(0,0),color='w',linewidth=2, path_effects=[pe.Stroke(linewidth=3, foreground='k'), pe.Normal()], label='d(APE)/dt')
    
    ax1 = twinx(ax)
    try:
        sigmai_sorted_noevap
    except:
        pass
    else:
        lns1a = ax1.semilogx(wl,sigmai_sorted_noevap[eps1_index,eps2_index,:,-1],c='k',linewidth=ms-.5,label='growth rate, $\mathregular{\gamma}$=0.0')#$\mathregular{\sigma_i}$')
    #if evap == True and hblcstep == 1.3:
    lns1b = ax1.semilogx(wl,sigmai_sorted[e,e2,:,-1],c='k',linestyle='--',linewidth=ms-.5,label='growth rate, $\mathregular{\gamma}$=%1.1f' %(hblcstep-1))#$\mathregular{\sigma_i}$')

    ax.set_xlabel('wavelength (km)')
    ax.set_ylabel('relative conversion terms')
    ax1.set_ylabel('growth rate (10$\mathregular{^{-5}s^{-1}}$)', rotation=270, labelpad=25)
    ax.set_xticks([1,3,5,10,30,50])
    ax1.set_xticks([1,3,5,10,30,50])
    ax.set_xticklabels([1000,3000,5000,10000,30000,50000])
    ax.set_xlim((2.1, 35))
    ax.set_ylim(0,2/sigmai_unstab[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]])#max((vTvec+QTvec+wTvec)/dAPEdt))  
    #ax.set_yticks([0,.25,.5,.75,1])
    #ax.set_yticklabels(['0%','25%','50%','75%','100%'])
    ax.set_ylim(0.0,1)
    ax.set_yticklabels(['{:,.0%}'.format(x) for x in ax.get_yticks()])
    #ax1.set_yticks([0,.5,1,1.5])
    ax1.set_ylim(0.0,1.201)
    ax.tick_params(which='minor', length=3, width=1)
    ax.tick_params(which='major', length=6, width=1)
    ax1.tick_params(which='both', length=6, width=1)
    
#    labels = ['$\lambda/S \cdot \overline{\Psi_x\'\Psi_p\'}$','$1/S \cdot \overline{Q\'\Psi_p\'}$','$\overline{W\'\Psi_p\'}$ = d(KE)/dt']# = dE/dt
#    ax2.stackplot(ec_vec_sort,vTn_ec_sort,QT1an_ec_sort,wTn_ec_sort,colors=([c[i] for i in [5,2,0]]),edgecolor='None',labels=labels)
    ax2.semilogx(ec_vec_sort,vTn_ec_sort,color=c[5],linestyle='-',linewidth=5,label=labels[0])#, path_effects=[pe.Stroke(linewidth=7, foreground='k'), pe.Normal()])
#plt.plot(x, y, color='k', lw=2, path_effects=[pe.Stroke(linewidth=5, foreground='g'), pe.Normal()])
    ax2.semilogx(ec_vec_sort,QT1an_ec_sort,color=c[2],linestyle='-',linewidth=5,label=labels[1])#, path_effects=[pe.Stroke(linewidth=7, foreground='k'), pe.Normal()])
    ax2.semilogx(ec_vec_sort,wTn_ec_sort,color=c[0],linestyle='-',linewidth=5,label=labels[2])#, path_effects=[pe.Stroke(linewidth=7, foreground='k'), pe.Normal()])
#    ax2.semilogx((0,0),(0,0),color='w',linewidth=2, path_effects=[pe.Stroke(linewidth=3, foreground='k'), pe.Normal()], label='d(APE)/dt')
    ax2.set_ylim(0,2/sigmai_unstab[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]])#max((vTvec+QTvec+wTvec)/dAPEdt))
    
    try:
        lns1a
    except:
        lns = lns2+lns3
    else:
        try:
            lns1b
        except:
            lns = lns1a+lns3 #+lns2
        else:
            lns = lns1a+lns1b+lns3 #+lns2
    labs = [l.get_label() for l in lns]
    box = ax2.get_position()
    ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    legend = plt.legend(lns, labs, loc='center', handlelength=2.1,bbox_to_anchor=(.9,-.35), prop={'size': 12}, ncol=6)
    
    ax2.set_xticks([1,1.1,1.2,1.3,1.4,1.5])
    ax2.set_xticklabels(['0.0','0.1','0.2','0.3','0.4','0.5'])
    ax2.set_xlim(1,1.5)
    ax2.set_xlabel('relative cooling parameter $\mathregular{\gamma}$')
    #ax2.set_yticks([0,.25,.5,.75,1])
    ax2.set_yticks([.25,.3,.35,.4,.45])    
    #ax2.set_yticklabels(['0%','25%','50%','75%','100%'])
    #ax2.set_yticklabels(['25%','30%','35%','40%','45%'])
    ax2.set_ylim(.25,.45)#0,1)
    ax2.set_yticklabels(['{:,.0%}'.format(x) for x in ax2.get_yticks()])
    ax2.set_ylabel('relative conversion terms')
    ax2.tick_params(which='both', length=6, width=1)
        

    plt.show()

# -----------------------------------------------------------------------------

### energetics presented in worm plot

def energetics_worms():
    
    fig,(ax2) = plt.subplots(figsize=(7,3))
    #ax1 = twinx(ax2)
    #ax1.semilogx(wl,sigmai_sorted[e,e2,:,-1],c=c[2],linewidth=2,label='$\mathregular{\sigma_i}$')
    #ax1.set_ylabel('Growth rate (day$^{-1}$)', color=c[2])
    totvec = vTvec+QT1avec+QT1bvec+QT2vec+wTvec
    labels = ['$\mathregular{C_a}$','$\mathregular{G^h_e}$','$\mathregular{G^f_e}$','$\mathregular{C_e}$ = dK/dt']# = dE/dt
    
    ax2.semilogx(wl,vTvec[e],color=c[5],linestyle='--',linewidth=3,label=labels[0])
    ax2.semilogx(wl,QT1avec[e],color=c[2],linestyle='--',linewidth=3,label=labels[1])
    ax2.semilogx(wl,QT2vec[e],color=c[1],linestyle='--',linewidth=3,label=labels[2])
    ax2.semilogx(wl,wTvec[e],color=c[0],linestyle='--',linewidth=3,label=labels[3])#'w\'T\'=d(KE)/dt')

    ax2.set_ylabel('fluxes and energetics \n normalized by total fluxes')#, color='b')
#    ax2.set_ylim(0,2/sigmai_unstab[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]])#max((vTvec+QTvec+wTvec)/dAPEdt))
    legend = ax2.legend(loc=5, prop={'size': 12})
    legend.get_frame().set_alpha(0.8)
    ax2.set_xticks([.1,.5,1,5,10,50])
    ax2.set_xticklabels([100,500,1000,5000,10000,50000])
    ax2.set_xlabel('wavelength (km)')
    ax2.set_xlim((.945, 60)) #.04
#    ax2.set_ylim(0,1)

    plt.show()
    
# -----------------------------------------------------------------------------

def energetics_APE_KE():
    
    labels = ['v\'T\'','Q\'$_{LH}$T\'','Q\'$_{LC}$T\'','Q\'$_{SF}$T\'','w\'T\' = d(KE)/dt']# = dE/dt
    
    fig,ax2 = plt.subplots(figsize=(6,3))
    Y1 = nan*np.ones(len(k))
    Y2 = nan*np.ones(len(k))
    ax1 = twinx()
    ax1.semilogx(wl,sigmai_sorted[e,e2,:,-1],'grey',linewidth=2,label='$\mathregular{\sigma_i}$')
    ax1.set_ylabel('growth rate (day$^{-1}$)', color='grey')
    ax1.tick_params('y', colors='grey')
    #ax1.set_ylim(0,3.5)
    dAPEdt = vTvec[e]+QT1avec[e]+QT1bvec[e]+QT2vec[e]-wTvec[e]
    dKEdt = wTvec[e]
    dEdt = vTvec[e]+QT1avec[e]+QT1bvec[e]+QT2vec[e]
    labels = ['d(APE)/dt','d(KE)/dt']
    for i in range(len(k)):
        if sigmai_sorted[e,e2,i,-1] > .1:
            Y1[i] = dAPEdt[i]/dEdt[i]
            Y2[i] = dKEdt[i]/dEdt[i]
    ax2.stackplot(wl,Y1,Y2,colors=c[::2],edgecolor='None',labels=labels)
    ax2.set_ylabel('fraction of energy conversion')
    #ax2.set_ylim(0,3.5/sigmai_unstab[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]])#max((vTvec+QTvec+wTvec)/dAPEdt))
    ax2.legend(loc='best')
    
    plt.show()
    
# -----------------------------------------------------------------------------

### comparing diabatic contribution to energetics and wavelength of most unstable mode with heating and cooling intensity

def diabatic_contribution_to_energetics_for_epsilon_and_gamma():

    if len(epsilon1) > 1 and heating2 == False:

        try:
            QTtemp
        except:
            evap_vec = ([])
            QTmax = ([])
            WLmax = ([])
            QTtemp = np.zeros(len(epsilon1))
                
        if heating1 == True and evap == False:
            evap_vec.extend([1])
            for e in range(len(epsilon1)):
                QTtemp[e] = QT1an[e,i_maxunstab[e]]
            QTmax.append(copy(QTtemp))
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and evap == True and hblcstep == 1.05:
            evap_vec.extend([hblcstep])
            for e in range(len(epsilon1)):
                QTtemp[e] = QT1an[e,i_maxunstab[e]]
            QTmax.append(copy(QTtemp))
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and evap == True and hblcstep == 1.1:
            evap_vec.extend([hblcstep])
            for e in range(len(epsilon1)):
                QTtemp[e] = QT1an[e,i_maxunstab[e]]
            QTmax.append(copy(QTtemp))
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and evap == True and hblcstep == 1.2:
            evap_vec.extend([hblcstep])
            for e in range(len(epsilon1)):
                QTtemp[e] = QT1an[e,i_maxunstab[e]]
            QTmax.append(copy(QTtemp))
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and evap == True and hblcstep == 1.3:
            evap_vec.extend([hblcstep])
            for e in range(len(epsilon1)):
                QTtemp[e] = QT1an[e,i_maxunstab[e]]
            QTmax.append(copy(QTtemp))
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and evap == True and hblcstep == 1.4:
            evap_vec.extend([hblcstep])
            for e in range(len(epsilon1)):
                QTtemp[e] = QT1an[e,i_maxunstab[e]]
            QTmax.append(copy(QTtemp))
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
        if heating1 == True and evap == True and hblcstep == 1.5:
            evap_vec.extend([hblcstep])
            for e in range(len(epsilon1)):
                QTtemp[e] = QT1an[e,i_maxunstab[e]]
            QTmax.append(copy(QTtemp))
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))

        evap_vec_temp = np.array(evap_vec)
        QTmax_temp = np.array(QTmax)
        WLmax_temp = np.array(WLmax)
        evap_vec_sort = evap_vec_temp[evap_vec_temp.argsort()]
        QTmax_sort = QTmax_temp[evap_vec_temp.argsort()]
        WLmax_sort = WLmax_temp[evap_vec_temp.argsort()]

        norm = MidpointNormalize(midpoint=0)
        ax = plt.contourf(evap_vec_sort,epsilon1,np.transpose(QTmax_sort),16,cmap=cm_br)
        CS = plt.contour(evap_vec_sort,epsilon1,np.transpose(WLmax_sort)*1000,20,colors='k',linewidths=.5)
        cbar = plt.colorbar(ax)
        CLS = plt.clabel(CS, CS.levels[::2],fmt='%d')#,inline=True)
        new_labels = []
        for label in CLS:
            lx,ly = label.get_position()
            new_labels.append((1.25,ly))
        for cline in CS.collections:
            cline.remove()
        for label in CLS:
            label.remove()
        CS = plt.contour(evap_vec_sort,epsilon1,np.transpose(WLmax_sort)*1000,16,colors='k',linewidths=.5)
        CLS = plt.clabel(CS, CS.levels[::2],fmt='%d',fontsize=9,inline=True, manual=(new_labels[i] for i in [0]+list(np.arange(2,7))))  
    #    cbar.add_lines(ax2)
        #cbar.set_label('(day$\mathregular{^{-1}}$)', fontsize=14)
        plt.ylabel('latent heating intensity $\mathregular{\\varepsilon}$')#, fontsize=14)
        plt.xlabel('relative cooling parameter $\mathregular{\gamma}$')#, fontsize=14)
        plt.title('latent heating contribution to energetics (shading) and \n wavelength (contours, in km) for maximum instability')#, fontsize=16)
        plt.xticks([1,1.1,1.2,1.3,1.4,1.5])
        gca().set_xticklabels(['0','10','20','30','40','50'])
        plt.tick_params(axis='both')#, labelsize=14)
        #cbar.ax.tick_params(labelsize=14) 
        
        plt.show()
        
    else:
        print ('len(epsilon1) must be > 1 and heating2 must be off')

# -----------------------------------------------------------------------------

# ---------------------------------------------------------------
# compare relative size of terms in thermodynamic equation
# ---------------------------------------------------------------

def compare_mean_terms_in_thermodynamic_eq():
    
    global t7, maxQG
    
    wfac = np.linspace(.1,1,len(epsilon1))
    
    # average over which domain? 0:nrws = full, jtrop:nrws = troposphere, 0:jtrop = stratosphere, jtrop-1:jtrop+1 = tropopause
    p1start=0; p1end=nrws
    p2start=jtrop-1; p2end=jtrop+1
    
#    t1 = np.zeros((len(epsilon1),len(epsilon2))) # local tendency
#    t2 = np.zeros((len(epsilon1),len(epsilon2))) # zonal geostrophic advection
#    t3 = np.zeros((len(epsilon1),len(epsilon2))) # meridional advection
#    t4 = np.zeros((len(epsilon1),len(epsilon2))) # stratification
#    t5 = np.zeros((len(epsilon1),len(epsilon2))) # zonal ageostrophic advection
#    if heating1 == True or heating2==True:
#        t6 = np.zeros((len(epsilon1),len(epsilon2))) # diabatic
#    t7 = np.zeros((len(epsilon1),len(epsilon2))) # vertical advection term, neglected in QG
#    scale = np.ones((len(epsilon1),len(epsilon2))) # scale factor
    
#    for e in range(len(epsilon1)):
#        for e2 in range(len(epsilon2)):
#            scale[e,e2] = .5/k[i_maxunstab[e,e2]]/np.max(abs(psi_maxunstab[e,e2,jtml:])) # 1 corresponds to max "surface" velocity of 10 m/s
#            t1[e,e2] = mean(abs(tempcalc(psi_maxunstab)[e,e2,pstart:pend]*sigmai_sorted[e,e2,i_maxunstab[e,e2],-1]))*scale[e,e2] # nondimensional psi = 1 corresponds to psi = 10^7
#            t2[e,e2] = mean(abs(tempcalc(psi_maxunstab)[e,e2,pstart:pend]*k[i_maxunstab[e,e2]]*u[pstart:pend]))*scale[e,e2]
#            t3[e,e2] = mean(abs(lambda1[pstart:pend]*k[i_maxunstab[e,e2]]*psi_maxunstab[e,e2,pstart:pend]))*scale[e,e2]
#            t4[e,e2] = mean(abs(S[pstart:pend]*w_maxunstab[e,e2,pstart:pend]))*scale[e,e2]
#            t5[e,e2] = mean(abs(tempcalc(psi_maxunstab)[e,e2,pstart:pend]*dwdpcalc(w_maxunstab[e,e2])[pstart:pend]))*scale[e,e2]**2
#            if heating1 == True or heating2==True:
#                t6[e,e2] = mean(abs(epsilon1[e]*h1[pstart:pend]/2*w_maxunstab[e,e2,jblc]))*scale[e,e2]
#            t7[e,e2] = mean(abs(-tempcalc(tempcalc(psi_maxunstab))[e,e2,pstart:pend]*w_maxunstab[e,e2,pstart:pend]))*scale[e,e2]**2
    
    t1 = np.zeros((nrws,len(kx))) # local tendency
    t2 = np.zeros((nrws,len(kx))) # zonal geostrophic advection
    t3 = np.zeros((nrws,len(kx))) # meridional advection
    t4 = np.zeros((nrws,len(kx))) # stratification
    t5 = np.zeros((nrws,len(kx))) # zonal ageostrophic advection
    if heating1 == True or heating2==True:
        t6 = np.zeros((nrws,len(kx))) # diabatic
    t7 = np.zeros((nrws,len(kx))) # vertical advection term, neglected in QG
    maxQG = np.zeros((nrws,len(kx))) # maximum of QG terms
#    scale = np.ones((nrws)) # scale factor
    #x = np.zeros((nrws),dtype=int)
    
    e=0; e2=0
    xstart = 0; xend = len(kx)
    
    scale = .5/k[i_maxunstab[e,e2]]/np.max(abs(psi[jtml:])) # 1 corresponds to max "surface" velocity of 10 m/s
    for j in range(nrws):
        for i in range(len(kx)):
        #x[j]  = np.argwhere(T[e,e2,j] == np.max(T[e,e2,j]))[0,0]-int(len(kx)/4)#psi[j] == np.max(psi[j]))[0,0]#w[j] == np.max(w[j]))[0,0]#
            t1[j,i] = (abs(T[e,e2,j,i]*sigmai_sorted[e,e2,i_maxunstab[e,e2],-1]))*scale # nondimensional psi = 1 corresponds to psi = 10^7
            t2[j,i] = (abs(T[e,e2,j,i]*k[i_maxunstab[e,e2]]*u[j]))*scale
            t3[j,i] = (abs(psi[j,i]*lambda1[j]*k[i_maxunstab[e,e2]]))*scale
            t4[j,i] = (abs(w[j,i]*S[j]))*scale
            t5[j,i] = (abs(T[e,e2,j,i]*dwdp[j,i]))*scale**2
            if stratos == True and smoothshearstrat == False and j == jtrop-1:
                t7[j,i] = (abs(- (T[e,e2,jtrop-1,i]-T[e,e2,jtrop-2,i])/(dp) *w[j,i]))*scale**2
            elif stratos == True and smoothshearstrat == False and j == jtrop:
                t7[j,i] = NaN
            elif stratos == True and smoothshearstrat == False and j == jtrop+1:
                t7[j,i] = (abs(- (T[e,e2,jtrop+2,i]-T[e,e2,jtrop+1,i])/(dp) *w[j,i]))*scale**2
            else:
                t7[j,i] = (abs(-tempcalc(T)[e,e2,j,i]*w[j,i]))*scale**2
            maxQG[j,i] = np.nanmax([t1[j,i],t2[j,i],t3[j,i],t4[j,i]])
            

    fig,ax = plt.subplots(figsize=(11,9), dpi=300)


    norm = MidpointNormalize(midpoint=0)
    levels = [0,0.25,0.5,1,2,3]
    levels = [0,0.25,10,20,30]
    #ax.contour(kx,p[:nrws],T[eps1_index,eps2_index],colors='k')
    adv = ax.contourf(kx,p[:nrws],t7/maxQG,norm=norm,cmap=cm_br)#,levels=levels)
    bar = plt.colorbar(adv)#,spacing='proportional')
    bar.update_ticks()
    bw = .3
#    ax.bar(epsilon1-5.5*bw/2,mean(t1[p1start:p1end]),bw/2.2,color='k',alpha=.1,label='local tendency') #t1[:,eps2_index]
#    ax.bar(epsilon1-4.5*bw/2,mean(t1[p2start:p2end]),bw/2.2,color='k',hatch='/',alpha=.1) #t1[:,eps2_index]
#    ax.bar(epsilon1-3.5*bw/2,mean(t2[p1start:p1end]),bw/2.2,color='k',alpha=.25,label='zonal adv.')
#    ax.bar(epsilon1-2.5*bw/2,mean(t2[p2start:p2end]),bw/2.2,color='k',hatch='/',alpha=.25)
#    ax.bar(epsilon1-1.5*bw/2,mean(t3[p1start:p1end]),bw/2.2,color='k',alpha=.4,label='meridional adv.')
#    ax.bar(epsilon1-0.5*bw/2,mean(t3[p2start:p2end]),bw/2.2,color='k',hatch='/',alpha=.4)
#    ax.bar(epsilon1+0.5*bw/2,mean(t4[p1start:p1end]),bw/2.2,color='k',alpha=.55,label='stratification')
#    ax.bar(epsilon1+1.5*bw/2,mean(t4[p2start:p2end]),bw/2.2,color='k',hatch='/',alpha=.55)
#    ax.bar(epsilon1+2.5*bw/2,mean(t5[p1start:p1end]),bw/2.2,color=(0, 109/255., 136/255.),label='ageostrophic zonal adv.')#, $10^{-4}$ hPa/s < w < $10^{-3}$ hPa/s')
#    ax.bar(epsilon1+3.5*bw/2,mean(t5[p2start:p2end]),bw/2.2,color=(0, 109/255., 136/255.),hatch='/')
#    ax.bar(epsilon1+4.5*bw/2,mean(t7[p1start:p1end]),bw/2.2,color=(0, 109/255., 136/255.),alpha=.5,label='vertical adv.')
#    ax.bar(epsilon1+5.5*bw/2,mean(t7[p2start:p2end]),bw/2.2,color=(0, 109/255., 136/255.),hatch='/',alpha=.5)
#    ax.bar(0,0,bw/2.2,color='w',edgecolor='k',label='full domain')
#    ax.bar(0,0,bw/2.2,color='w',hatch='/',edgecolor='k',label='tropopause')
#    ax.bar(epsilon1+3*bw/2,t5a[:,eps2_index],bw,color=(0, 109/255., 136/255.),alpha=0.5,label='nonlin. zonal adv., w ~ $10^{-3}$ hPa/s')
    #if heating1 == True or heating2==True:
    #    ax.bar(epsilon1+7*bw/2,t6[:,eps2_index],bw,color=(209/255, 98/255, 76/255),label='diabatic')
#    ax.legend(loc='best',fontsize=16, bbox_to_anchor=(1,1))
    ax.set_xlabel('kx')#heating intensity parameter $\\varepsilon$')
#    ax.set_ylabel('size of terms in thermodyn. eq.')
    ax.set_ylabel('pressure')
    structureplotcustom(ax)
    ax.set_title('$\omega \partial T/\partial p$ relative to largest QG term (shading)', fontsize=24)# \nand structure of T (contours)', fontsize=24)
#    ax.set_ylim(0,1.4)
#    ax.set_xlim(-1,1)#31.5)
#    ax.set_xticks([])
#    ax.set_yscale('log')

#    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#    axins = inset_axes(ax, 3.85,2. , loc=2,bbox_to_anchor=(0.14, 0.85),bbox_transform=ax.figure.transFigure) # no zoom
#    axins.bar(epsilon1-5*bw/2,t1,bw,color='k',alpha=.1)
#    axins.bar(epsilon1-3*bw/2,t2,bw,color='k',alpha=.25)
#    axins.bar(epsilon1-1*bw/2,t3,bw,color='k',alpha=.4)
#    axins.bar(epsilon1+1*bw/2,t4,bw,color='k',alpha=.55)
#    axins.bar(epsilon1+3*bw/2,t5,bw,color=(0, 109/255., 136/255.))
#    axins.bar(epsilon1+5*bw/2,t6,bw,color=(209/255, 98/255, 76/255))
#    x1, x2, y1, y2 = -1.25, 13.75, 0, 1.1*np.max([t2[:6],t3[:6],t4[:6],t5[:6],t6[:6]]) # specify the limits
#    axins.set_xlim(x1, x2) # apply the x-limits
#    axins.set_ylim(y1, y2) # apply the y-limits
#    plt.yticks([])
#    plt.xticks([])
#    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
#    mark_inset(ax, axins, loc1=2, loc2=1, fc="none", ec="0.5",linestyle='--', edgecolor='k')
#    ax.set_yscale('log')


#    plt.grid()
    plt.show()
    
    #for e in range(len(epsilon1)):
     #   for e2 in range(len(epsilon2)):
      #      if epsilon1[e] == 15:
       #         print ('---')
        #    print (f't1-t6: {t1[e,e2]:.1E}, {t2[e,e2]:.1E}, {t3[e,e2]:.1E}, {t4[e,e2]:.1E}, {t5[e,e2]:.1E}, {t6[e,e2]:.1E}; nonlin vs. lin (%): {t5[e,e2]/max(t1[e,e2],t2[e,e2],t3[e,e2],t4[e,e2],t6[e,e2])*100:.4}; w scale: {np.max(abs(w_maxunstab[e,e2]))*10**(-3):.1E} hPa/s') #,t5b[e],t1[e],t2[e],t3[e],t4[e],t6[e])
#    for e in range(len(epsilon1)):
#        print (mean(abs( tempcalc(psi_maxunstab)[e,:]*dwdpcalc(w_maxunstab[e,eps2_index]) )/k[i_maxunstab[e,eps2_index]]),mean(abs(tempcalc(psi_maxunstab)[e,:]*u[:nrws])))
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            print (f'e2={epsilon2[e2]}, max psi: {np.max(abs(psi_maxunstab[e,e2,:]))*10**(7):.2E}, mean omega: {np.mean(abs(w_maxunstab[e,e2,:]))*10**(-3):.2E}') #*scale[e,e2]
    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            if heating2 == True and vpar == False and wpar == False:
                print (f'nondimensional ratio between max lh and max sf for epsilon2={epsilon2[e2]}: {(abs(w_maxunstab[e,e2,jblc])*abs(epsilon1[e])/2 / (np.max(abs(tempcalc(psi_maxunstab)[e,e2,-1]))*abs(epsilon2[e2])))}')
            if heating2 == True and vpar == True and wpar == False:
                print (f'nondimensional ratio between max lh and max sf for epsilon2={epsilon2[e2]}: {(abs(w_maxunstab[e,e2,jblc])*abs(epsilon1[e])/2 / (abs(psi_maxunstab[e,e2,-1])*k[i_maxunstab[e,e2]]*abs(epsilon2[e2])))}')
            if heating2 == True and vpar == False and wpar == True:
                print (f'nondimensional ratio between max lh and max sf for epsilon2={epsilon2[e2]}: {(abs(w_maxunstab[e,e2,jblc])*abs(epsilon1[e])/2 / (abs(w_maxunstab[e,e2,jblc])*abs(epsilon2[e2])))}')

                

# ---------------------------------------------------------------
# compare tendency terms in thermodynamic equation for specific pressure levels and wavenumbers
# ---------------------------------------------------------------

def compare_tendency_terms_in_thermodynamic_eq_at_defined_pressure_levels():

    global tropup_index, tropdown_index

    tropup_index = np.argwhere(dqdy[1:jtrop]>=.1*np.max(dqdy))[0][0]+1
    tropdown_index = jtrop + np.argwhere(dqdy[jtrop+1:]<=.1*np.max(dqdy))[0][0]

    tot_index = np.argwhere(kx == 2*np.pi)[0][0]

    Ttrop_index = np.argwhere(T[eps1_index,eps2_index,jtrop] == np.max(T[eps1_index,eps2_index,jtrop]))[0][0]
    T2trop_index = np.argwhere(T2[eps1_index,eps2_index,jtrop] == np.max(T2[eps1_index,eps2_index,jtrop]))[0][0]
    T2trop90_index = T2trop_index+int((tot_index-1)*1/4)
    if T2trop90_index > tot_index:
        T2trop90_index = T2trop90_index-tot_index
    T3trop_index = np.argwhere(T3[eps1_index,eps2_index,jtrop] == np.max(T3[eps1_index,eps2_index,jtrop]))[0][0]
    Ttropup_index = np.argwhere(T[eps1_index,eps2_index,tropup_index] == np.max(T[eps1_index,eps2_index,tropup_index]))[0][0]
    T2tropup_index = np.argwhere(T2[eps1_index,eps2_index,tropup_index] == np.max(T2[eps1_index,eps2_index,tropup_index]))[0][0]
    T3tropup_index = np.argwhere(T3[eps1_index,eps2_index,tropup_index] == np.max(T3[eps1_index,eps2_index,tropup_index]))[0][0]
    Ttropdown_index = np.argwhere(T[eps1_index,eps2_index,tropdown_index] == np.max(T[eps1_index,eps2_index,tropdown_index]))[0][0]
    T2tropdown_index = np.argwhere(T2[eps1_index,eps2_index,tropdown_index] == np.max(T2[eps1_index,eps2_index,tropdown_index]))[0][0]
    T2tropdown90_index = T2tropdown_index+int((tot_index-1)*1/4)
    if T2tropdown90_index > tot_index:
        T2tropdown90_index = T2tropdown90_index-tot_index
    T3tropdown_index = np.argwhere(T3[eps1_index,eps2_index,tropdown_index] == np.max(T3[eps1_index,eps2_index,tropdown_index]))[0][0]
    Tsurf_index = np.argwhere(T[eps1_index,eps2_index,-1] == np.max(T[eps1_index,eps2_index,-1]))[0][0]
    T2surf_index = np.argwhere(T2[eps1_index,eps2_index,-1] == np.max(T2[eps1_index,eps2_index,-1]))[0][0]
    T3surf_index = np.argwhere(T3[eps1_index,eps2_index,-1] == np.max(T3[eps1_index,eps2_index,-1]))[0][0]
    Tsurfeps_index = np.argwhere(T[eps1_index,eps2_index,-2] == np.max(T[eps1_index,eps2_index,-2]))[0][0]


    # NB! order: unstab2, unstab, unstab3
    Ttrop_amp = np.array([np.max(T2[eps1_index,eps2_index,jtrop]),np.max(T[eps1_index,eps2_index,jtrop]),np.max(T3[eps1_index,eps2_index,jtrop])])
    Ttropup_amp = np.array([np.max(T2[eps1_index,eps2_index,tropup_index]),np.max(T[eps1_index,eps2_index,tropup_index]),np.max(T3[eps1_index,eps2_index,tropup_index])])
    Ttropdown_amp = np.array([np.max(T2[eps1_index,eps2_index,tropdown_index]),np.max(T[eps1_index,eps2_index,tropdown_index]),np.max(T3[eps1_index,eps2_index,tropdown_index])])
    Tsurf_amp = np.array([np.max(T2[eps1_index,eps2_index,-1]),np.max(T[eps1_index,eps2_index,-1]),np.max(T3[eps1_index,eps2_index,-1])])
        
    Ttrop_index_vec = np.array([T2trop_index, Ttrop_index, T3trop_index])
    Ttropup_index_vec = np.array([T2tropup_index, Ttropup_index, T3tropup_index])
    Ttropdown_index_vec = np.array([T2tropdown_index, Ttropdown_index, T3tropdown_index])
    Tsurf_index_vec = np.array([T2surf_index, Tsurf_index, T3surf_index])
    
    vtrop_index_vec = np.array([np.argwhere(v2[jtrop] == np.max(v2[jtrop]))[0][0], np.argwhere(v[jtrop] == np.max(v[jtrop]))[0][0], np.argwhere(v3[jtrop] == np.max(v3[jtrop]))[0][0]])
    vtropup_index_vec = np.array([np.argwhere(v2[tropup_index] == np.max(v2[tropup_index]))[0][0], np.argwhere(v[tropup_index] == np.max(v[tropup_index]))[0][0], np.argwhere(v3[tropup_index] == np.max(v3[tropup_index]))[0][0]])
    vtropdown_index_vec = np.array([np.argwhere(v2[tropdown_index] == np.max(v2[tropdown_index]))[0][0], np.argwhere(v[tropdown_index] == np.max(v[tropdown_index]))[0][0], np.argwhere(v3[tropdown_index] == np.max(v3[tropdown_index]))[0][0]])
    vsurf_index_vec = np.array([np.argwhere(v2[-1] == np.max(v2[-1]))[0][0], np.argwhere(v[-1] == np.max(v[-1]))[0][0], np.argwhere(v3[-1] == np.max(v3[-1]))[0][0]])

    wtrop_index_vec = np.array([np.argwhere(w2[jtrop] == np.max(w2[jtrop]))[0][0], np.argwhere(w[jtrop] == np.max(w[jtrop]))[0][0], np.argwhere(w3[jtrop] == np.max(w3[jtrop]))[0][0]])
    wtropup_index_vec = np.array([np.argwhere(w2[tropup_index] == np.max(w2[tropup_index]))[0][0], np.argwhere(w[tropup_index] == np.max(w[tropup_index]))[0][0], np.argwhere(w3[tropup_index] == np.max(w3[tropup_index]))[0][0]])
    wtropdown_index_vec = np.array([np.argwhere(w2[tropdown_index] == np.max(w2[tropdown_index]))[0][0], np.argwhere(w[tropdown_index] == np.max(w[tropdown_index]))[0][0], np.argwhere(w3[tropdown_index] == np.max(w3[tropdown_index]))[0][0]])


    vterm_Tmax_tropup = np.array([v2[tropup_index,T2tropup_index]*lambda1[tropup_index],v[tropup_index,Ttropup_index]*lambda1[tropup_index],v3[tropup_index,T3tropup_index]*lambda1[tropup_index]])
    wterm_Tmax_tropup = np.array([w2[tropup_index,T2tropup_index]*S[tropup_index],w[tropup_index,Ttropup_index]*S[tropup_index],w3[tropup_index,T3tropup_index]*S[tropup_index]])
    uterm_T90_tropup = np.array([u[tropup_index]*k[i_maxunstab2[eps1_index,eps2_index]]*T2[eps1_index,eps2_index,tropup_index,T2tropup_index],u[tropup_index]*k[i_maxunstab[eps1_index,eps2_index]]*T[eps1_index,eps2_index,tropup_index,Ttropup_index],u[tropup_index]*k[i_maxunstab3[eps1_index,eps2_index]]*T3[eps1_index,eps2_index,tropup_index,T3tropup_index]])
    vterm_T90_tropup = np.array([v2[tropup_index,T2tropup_index+int((tot_index-1)*1/4)]*lambda1[tropup_index],v[tropup_index,Ttropup_index+int((tot_index-1)*1/4)]*lambda1[tropup_index],v3[tropup_index,T3tropup_index+int((tot_index-1)*1/4)]*lambda1[tropup_index]])
    wterm_T90_tropup = np.array([w2[tropup_index,T2tropup_index+int((tot_index-1)*1/4)]*S[tropup_index],w[tropup_index,Ttropup_index+int((tot_index-1)*1/4)]*S[tropup_index],w3[tropup_index,T3tropup_index+int((tot_index-1)*1/4)]*S[tropup_index]])

    vterm_Tmax_trop = np.array([v2[jtrop,T2trop_index]*lambda1[jtrop],v[jtrop,Ttrop_index]*lambda1[jtrop],v3[jtrop,T3trop_index]*lambda1[jtrop]])
    wterm_Tmax_trop = np.array([w2[jtrop,T2trop_index]*S[jtrop],w[jtrop,Ttrop_index]*S[jtrop],w3[jtrop,T3trop_index]*S[jtrop]])
    uterm_T90_trop = np.array([u[jtrop]*k[i_maxunstab2[eps1_index,eps2_index]]*T2[eps1_index,eps2_index,jtrop,T2trop_index],u[jtrop]*k[i_maxunstab[eps1_index,eps2_index]]*T[eps1_index,eps2_index,jtrop,Ttrop_index],u[jtrop]*k[i_maxunstab3[eps1_index,eps2_index]]*T3[eps1_index,eps2_index,jtrop,T3trop_index]])
    vterm_T90_trop = np.array([v2[jtrop,T2trop90_index]*lambda1[jtrop],v[jtrop,Ttrop_index+int((tot_index-1)*1/4)]*lambda1[jtrop],v3[jtrop,T3trop_index+int((tot_index-1)*1/4)]*lambda1[jtrop]])
    wterm_T90_trop = np.array([w2[jtrop,T2trop90_index]*S[jtrop],w[jtrop,Ttrop_index+int((tot_index-1)*1/4)]*S[jtrop],w3[jtrop,T3trop_index+int((tot_index-1)*1/4)]*S[jtrop]])

    vterm_Tmax_tropdown = np.array([v2[tropdown_index,T2tropdown_index]*lambda1[tropdown_index],v[tropdown_index,Ttropdown_index]*lambda1[tropdown_index],v3[tropdown_index,T3tropdown_index]*lambda1[tropdown_index]])
    wterm_Tmax_tropdown = np.array([w2[tropdown_index,T2tropdown_index]*S[tropdown_index],w[tropdown_index,Ttropdown_index]*S[tropdown_index],w3[tropdown_index,T3tropdown_index]*S[tropdown_index]])
    uterm_T90_tropdown = np.array([u[tropdown_index]*k[i_maxunstab2[eps1_index,eps2_index]]*T2[eps1_index,eps2_index,tropdown_index,T2tropdown_index],u[tropdown_index]*k[i_maxunstab[eps1_index,eps2_index]]*T[eps1_index,eps2_index,tropdown_index,Ttropdown_index],u[tropdown_index]*k[i_maxunstab3[eps1_index,eps2_index]]*T3[eps1_index,eps2_index,tropdown_index,T3tropdown_index]])
    vterm_T90_tropdown = np.array([v2[tropdown_index,T2tropdown90_index]*lambda1[tropdown_index],v[tropdown_index,Ttropdown_index+int((tot_index-1)*1/4)]*lambda1[tropdown_index],v3[tropdown_index,T3tropdown_index+int((tot_index-1)*1/4)]*lambda1[tropdown_index]])
    wterm_T90_tropdown = np.array([w2[tropdown_index,T2tropdown90_index]*S[tropdown_index],w[tropdown_index,Ttropdown_index+int((tot_index-1)*1/4)]*S[tropdown_index],w3[tropdown_index,T3tropdown_index+int((tot_index-1)*1/4)]*S[tropdown_index]])

    vterm_Tmax_surf = np.array([v2[-1,T2surf_index]*lambda1[-1],v[-1,Tsurf_index]*lambda1[-1],v3[-1,T3surf_index]*lambda1[-1]])
    wterm_Tmax_surf = np.array([w2[-1,T2surf_index]*S[-1],w[-1,Tsurf_index]*S[-1],w3[-1,T3surf_index]*S[-1]])
    uterm_T90_surf = np.array([u[-1]*k[i_maxunstab2[eps1_index,eps2_index]]*T2[eps1_index,eps2_index,-1,T2surf_index],u[-1]*k[i_maxunstab[eps1_index,eps2_index]]*T[eps1_index,eps2_index,-1,Tsurf_index],u[-1]*k[i_maxunstab3[eps1_index,eps2_index]]*T3[eps1_index,eps2_index,-1,T3surf_index]])
    vterm_T90_surf = np.array([v2[-1,T2surf_index+int((tot_index-1)*1/4)]*lambda1[-1],v[-1,Tsurf_index+int((tot_index-1)*1/4)]*lambda1[-1],v3[-1,T3surf_index+int((tot_index-1)*1/4)]*lambda1[-1]])
    wterm_T90_surf = np.array([w2[-1,T2surf_index+int((tot_index-1)*1/4)]*S[-1],w[-1,Tsurf_index+int((tot_index-1)*1/4)]*S[-1],w3[-1,T3surf_index+int((tot_index-1)*1/4)]*S[-1]])

# ----------------------

    global dTdt, dT2dt, dT3dt

    dTdt = (-1j*(sigmar_sorted[0,0,i_maxunstab[0,0],-1]+1j*sigmai_sorted[0,0,i_maxunstab[0,0],-1])*tempcalc(psi_maxunstab)[0,0])#.real
    dTdt = (dTdt[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real
    dT2dt = (-1j*(sigmar_sorted[0,0,i_maxunstab2[0,0],-1]+1j*sigmai_sorted[0,0,i_maxunstab2[0,0],-1])*tempcalc(psi_maxunstab2)[0,0])#.real
    dT2dt = (dT2dt[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift2])*1j)).real
    dT3dt = (-1j*(sigmar_sorted[0,0,i_maxunstab3[0,0],-1]+1j*sigmai_sorted[0,0,i_maxunstab3[0,0],-1])*tempcalc(psi_maxunstab3)[0,0])#.real
    dT3dt = (dT3dt[:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift3])*1j)).real
   
#    print (dTdt[tropup_index,150:],dTdt[jtrop,150:])#,Ttropup_index],dTdt[jtrop,Ttrop_index],dTdt[tropdown_index,Ttropdown_index],dTdt[-1,Tsurf_index])

# ----------------------
    
    T_real_scale = True
    T_complex_scale = False
    
    tropup_scale = 1
    trop_scale = 1
    tropdown_scale = 1
    surf_scale = 1
    
    if T_real_scale == True:
        tropup_scale = Ttropup_amp
        trop_scale = Ttrop_amp
        tropdown_scale = Ttropdown_amp
        surf_scale = Tsurf_amp

    if T_complex_scale == True:
        tropup_scale = np.array([dT2dt,dTdt,dT3dt])[:,tropup_index,Ttropup_index]
        trop_scale = np.array([dT2dt,dTdt,dT3dt])[:,jtrop,Ttrop_index]
        tropdown_scale = np.array([dT2dt,dTdt,dT3dt])[:,tropdown_index,Ttropdown_index]
        surf_scale = np.array([dT2dt,dTdt,dT3dt])[:,-1,Tsurf_index]

    ms = 200
    delta = .2

    fig, (ax1) = plt.subplots(figsize=(6,9))
#    plt.axhline(1,c='k',ls='--')
    plt.axhline(0,c='k',ls=':')
    ax2 = plt.twinx(ax1)
    ax2.axhline(0,c='k',ls='--')

    

    ax1.scatter([4-delta,4,4+delta],vterm_Tmax_tropup/tropup_scale,ms/2,color=c_blues[1])
    ax1.scatter([3-delta,3,3+delta],vterm_Tmax_trop/trop_scale,ms/2,color=c_blues[1])
    ax1.scatter([2-delta,2,2+delta],vterm_Tmax_tropdown/tropdown_scale,ms/2,color=c_blues[1])
    ax1.scatter([1-delta,1,1+delta],vterm_Tmax_surf/surf_scale,ms/2,color=c_blues[1])
    ax1.scatter([4-delta,4,4+delta],wterm_Tmax_tropup/tropup_scale,ms/2,color=c_reds[1])
    ax1.scatter([3-delta,3,3+delta],wterm_Tmax_trop/trop_scale,ms/2,color=c_reds[1])
    ax1.scatter([2-delta,2,2+delta],wterm_Tmax_tropdown/tropdown_scale,ms/2,color=c_reds[1])
    ax1.scatter([1-delta,1,1+delta],wterm_Tmax_surf/surf_scale,ms/2,color=c_reds[1])
    ax1.scatter([4-delta,4,4+delta],(vterm_Tmax_tropup+wterm_Tmax_tropup)/tropup_scale,ms/8,color='k')
    ax1.scatter([3-delta,3,3+delta],(vterm_Tmax_trop+wterm_Tmax_trop)/trop_scale,ms/8,color='k')
    ax1.scatter([2-delta,2,2+delta],(vterm_Tmax_tropdown+wterm_Tmax_tropdown)/tropdown_scale,ms/8,color='k')
    ax1.scatter([1-delta,1,1+delta],(vterm_Tmax_surf+wterm_Tmax_surf)/surf_scale,ms/8,color='k')

    ax2.scatter([4-delta,4,4+delta],uterm_T90_tropup/tropup_scale,ms,color=c_greys[0],marker='x')
    ax2.scatter([3-delta,3,3+delta],uterm_T90_trop/trop_scale,ms,color=c_greys[0],marker='x')
    ax2.scatter([2-delta,2,2+delta],uterm_T90_tropdown/tropdown_scale,ms,color=c_greys[0],marker='x')
    ax2.scatter([1-delta,1,1+delta],uterm_T90_surf/surf_scale,ms,color=c_greys[0],marker='x')
    ax2.scatter([4-delta,4,4+delta],vterm_T90_tropup/tropup_scale,ms,color=c_blues[1],marker='x')
    ax2.scatter([3-delta,3,3+delta],vterm_T90_trop/trop_scale,ms,color=c_blues[1],marker='x')
    ax2.scatter([2-delta,2,2+delta],vterm_T90_tropdown/tropdown_scale,ms,color=c_blues[1],marker='x')
    ax2.scatter([1-delta,1,1+delta],vterm_T90_surf/surf_scale,ms,color=c_blues[1],marker='x')
    ax2.scatter([4-delta,4,4+delta],wterm_T90_tropup/tropup_scale,ms,color=c_reds[1],marker='x')
    ax2.scatter([3-delta,3,3+delta],wterm_T90_trop/trop_scale,ms,color=c_reds[1],marker='x')
    ax2.scatter([2-delta,2,2+delta],wterm_T90_tropdown/tropdown_scale,ms,color=c_reds[1],marker='x')
    ax2.scatter([1-delta,1,1+delta],wterm_T90_surf/surf_scale,ms,color=c_reds[1],marker='x')
    ax2.scatter([4-delta,4,4+delta],(uterm_T90_tropup+vterm_T90_tropup+wterm_T90_tropup)/tropup_scale,ms/4,color='k',marker='x')
    ax2.scatter([3-delta,3,3+delta],(uterm_T90_trop+vterm_T90_trop+wterm_T90_trop)/trop_scale,ms/4,color='k',marker='x')
    ax2.scatter([2-delta,2,2+delta],(uterm_T90_tropdown+vterm_T90_tropdown+wterm_T90_tropdown)/tropdown_scale,ms/4,color='k',marker='x')
    ax2.scatter([1-delta,1,1+delta],(uterm_T90_surf+vterm_T90_surf+wterm_T90_surf)/surf_scale,ms/4,color='k',marker='x')

    plt.scatter((),(),color=c_greys[0],marker='s',label='$\overline{u} \cdot d/dx(-d\psi/dp)$')
    plt.scatter((),(),color=c_blues[1],marker='s',label='$v \lambda$')
    plt.scatter((),(),color=c_reds[1],marker='s',label='$\omega S$')
    plt.scatter((),(),color='k',marker='s',label='total')
    plt.scatter((),(),color='k',marker='o',label='amplification (@ $T_{max}$)')
    plt.scatter((),(),color='k',marker='x',label='propagation (@ $T_{90^\circ}$)')

    ax1.set_ylabel('amplification scaled by $\Re\{-i\sigma\hat{T}exp(ikx)\}$ @ given level')
    ax2.set_ylabel('propagation scaled by $\Re\{-i\sigma\hat{T}exp(ikx)\}$ @ given level',rotation=270,labelpad=30)
#    ax1.set_ylim(-5,5)#.05,.05)#-2.1,2.1)#-1.1*np.max(np.abs(wterm_Tmax_trop/vterm_Tmax_surf)),1.1*np.max(np.abs(wterm_Tmax_trop/vterm_Tmax_surf)))
#    ax2.set_ylim(-50,50)#-1.1,3.1)#-1.1*np.max(np.abs(uterm_T90_tropdown/vterm_T90_surf)),1.1*np.max(np.abs(uterm_T90_tropdown/vterm_T90_surf)))
    plt.xlabel('3 WL for each pressure level')# (hPa)')
    plt.xticks(np.arange(1,5,1))
    gca().set_xticklabels(['surf','trop-','trop','trop+'])#int(1000*p[jtrop-delrange]),int(1000*p[jtrop]),int(1000*p[jtrop+delrange]),int(1000*p[-1])])
    plt.legend(loc='center left',bbox_to_anchor=(1.3,.5))#, prop={'size': 12})
    plt.show()


    fig, (ax1) = plt.subplots(figsize=(6,5))
    plt.axhline(0,c='k',ls=':')
    plt.axhline(-90,c='k',ls=':')
    plt.axhline(90,c='k',ls=':')

    ax1.scatter([4-delta,4,4+delta],(vtropup_index_vec-Ttropup_index_vec)/tot_index*360,ms/2,color=c_blues[1],marker='s')
    ax1.scatter([3-delta,3,3+delta],(vtrop_index_vec-Ttrop_index_vec)/tot_index*360,ms/2,color=c_blues[1],marker='s')
    for i in range(len(vsurf_index_vec)):
        if (vtropdown_index_vec[i]-Ttropdown_index_vec[i])/tot_index*360 > 180:
            ax1.scatter(2-delta+i*delta,(vtropdown_index_vec[i]-Ttropdown_index_vec[i])/tot_index*360-360,ms/2,color=c_blues[1],marker='s')
        elif (vtropdown_index_vec[i]-Ttropdown_index_vec[i])/tot_index*360 < -180:
            ax1.scatter(2-delta+i*delta,(vtropdown_index_vec[i]-Ttropdown_index_vec[i])/tot_index*360+360,ms/2,color=c_blues[1],marker='s')
        else:
            ax1.scatter(2-delta+i*delta,(vtropdown_index_vec[i]-Ttropdown_index_vec[i])/tot_index*360,ms/2,color=c_blues[1],marker='s')

        if (vsurf_index_vec[i]-Tsurf_index_vec[i])/tot_index*360 > -180:
            ax1.scatter(1-delta+i*delta,(vsurf_index_vec[i]-Tsurf_index_vec[i])/tot_index*360,ms/2,color=c_blues[1],marker='s')
        else:
            ax1.scatter(1-delta+i*delta,(vsurf_index_vec[i]-Tsurf_index_vec[i])/tot_index*360+360,ms/2,color=c_blues[1],marker='s')

    for i in range(len(wtrop_index_vec)):    
        if (Ttropup_index_vec[i]-wtropup_index_vec[i])/tot_index*360 > 180:
            ax1.scatter(4-delta+i*delta,(Ttropup_index_vec[i]-wtropup_index_vec[i])/tot_index*360-360,ms/2,color=c_reds[1],marker='s')
        elif (Ttropup_index_vec[i]-wtropup_index_vec[i])/tot_index*360 < -180:
            ax1.scatter(4-delta+i*delta,(Ttropup_index_vec[i]-wtropup_index_vec[i])/tot_index*360+360,ms/2,color=c_reds[1],marker='s')
        else:
            ax1.scatter(4-delta+i*delta,(Ttropup_index_vec[i]-wtropup_index_vec[i])/tot_index*360,ms/2,color=c_reds[1],marker='s')

        if (Ttrop_index_vec[i]-wtrop_index_vec[i])/tot_index*360 > 180:
            ax1.scatter(3-delta+i*delta,(Ttrop_index_vec[i]-wtrop_index_vec[i])/tot_index*360-360,ms/2,color=c_reds[1],marker='s')
        elif (Ttrop_index_vec[i]-wtrop_index_vec[i])/tot_index*360 < -180:
            ax1.scatter(3-delta+i*delta,(Ttrop_index_vec[i]-wtrop_index_vec[i])/tot_index*360+360,ms/2,color=c_reds[1],marker='s')
        else:
            ax1.scatter(3-delta+i*delta,(Ttrop_index_vec[i]-wtrop_index_vec[i])/tot_index*360,ms/2,color=c_reds[1],marker='s')

        if (Ttropdown_index_vec[i]-wtropdown_index_vec[i])/tot_index*360 > 180:
            ax1.scatter(2-delta+i*delta,(Ttropdown_index_vec[i]-wtropdown_index_vec[i])/tot_index*360-360,ms/2,color=c_reds[1],marker='s')
        elif (Ttropdown_index_vec[i]-wtropdown_index_vec[i])/tot_index*360 < -180:
            ax1.scatter(2-delta+i*delta,(Ttropdown_index_vec[i]-wtropdown_index_vec[i])/tot_index*360+360,ms/2,color=c_reds[1],marker='s')
        else:
            ax1.scatter(2-delta+i*delta,(Ttropdown_index_vec[i]-wtropdown_index_vec[i])/tot_index*360,ms/2,color=c_reds[1],marker='s')
    
    ax1.scatter((),(),ms/2,color=c_blues[1],marker='s',label='$v,T$')
    ax1.scatter((),(),ms/2,color=c_reds[1],marker='s',label='$-\omega,T$')
    
    ax1.set_ylabel('phase difference (deg)')#between v\' and T\'')
#    ax2.set_ylabel('phase between $\omega\'$ and T\'',rotation=270,labelpad=20)
#    ax1.set_ylim(-2.1,2.1)#-1.1*np.max(np.abs(wterm_Tmax_trop/vterm_Tmax_surf)),1.1*np.max(np.abs(wterm_Tmax_trop/vterm_Tmax_surf)))
#    ax2.set_ylim(-1.1,3.1)#-1.1*np.max(np.abs(uterm_T90_tropdown/vterm_T90_surf)),1.1*np.max(np.abs(uterm_T90_tropdown/vterm_T90_surf)))
    plt.xlabel('3 WL for each pressure level')# (hPa)')
    plt.yticks([-180,-90,0,90])
    plt.xticks(np.arange(1,5,1))
    gca().set_xticklabels(['surf','trop-','trop','trop+'])#int(1000*p[jtrop-delrange]),int(1000*p[jtrop]),int(1000*p[jtrop+delrange]),int(1000*p[-1])])
    plt.legend(loc=3)#9)
    plt.show()



# ---------------------------------------------------------------
# split into dynamic and diabatic components of omega
# ---------------------------------------------------------------

def wsplit():

    global wd_noevap,wh_noevap,wc_noevap,wf_noevap
    global wd_sf,wh_sf,wc_sf,wf_sf
    global wd_sf1,wh_sf1,wc_sf1,wf_sf1
    global wd_sf2,wh_sf2,wc_sf2,wf_sf2
    global wd,wh,wc,wf,wtot
    
    try:
        wh_noevap
    except:
        wh_noevap = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wc_noevap = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wd_noevap = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wf_noevap = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        #wl_noevap = np.zeros((len(epsilon1),len(epsilon2)),dtype=complex)  
    else:  
        pass
    try:
        wh_sf
    except:
        wh_sf = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wc_sf = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wd_sf = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wf_sf = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        #wl_sf = np.zeros((len(epsilon1),len(epsilon2)),dtype=complex)
    else:
        pass
    try:
        wh_sf1
    except:
        wh_sf1 = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wc_sf1 = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wd_sf1 = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wf_sf1 = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        #wl_sf1 = np.zeros((len(epsilon1),len(epsilon2)),dtype=complex)
    else:
        pass
    try:
        wh_sf2
    except:
        wh_sf2 = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wc_sf2 = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wd_sf2 = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        wf_sf2 = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
        #wl_sf2 = np.zeros((len(epsilon1),len(epsilon2)),dtype=complex)
    else:
        pass
        
    M = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws,nrws),dtype=complex) # matrix for omega equation
    Fd = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)     # dynamic forcing
    Fh = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)     # latent heating forcing
    Fc = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)     # latent cooling forcing
    Ff = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)     # surface flux forcing
    wd = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)     # dynamic component
    wh = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)     # heating component
    wc = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)     # cooling component
    wf = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)     # surface flux component
    wtot = np.zeros((len(epsilon1),len(epsilon2),len(k),nrws),dtype=complex)   # total (for comparison)

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            for i in range(len(k)):
                for j in range(1,nrws-1):
                    M[e,e2,i,j,j-1] = 1/dp**2
                    M[e,e2,i,j,j]   = -2/dp**2-S[j]*k[i]**2
                    M[e,e2,i,j,j+1] = 1/dp**2
                    Fd[e,e2,i,j] = 1j*2*lambda1[j]*k[i]**3*eigvecs_sorted_scaled[e,eps2_index,i,nrws+j,-1]#psi_maxunstab[e,eps2_index,j]
                for j in range(1,jblc+1):
                    Fh[e,e2,i,j] = -epsilon1[e]/2*k[i]**2*h1[e,j]*eigvecs_sorted_scaled[e,eps2_index,i,jtml,-1]#w_maxunstab[e,eps2_index,jblc]
                for j in range(jblc+1,nrws-1):
                    Fc[e,e2,i,j] = -epsilon1[e]/2*k[i]**2*h1[e,j]*eigvecs_sorted_scaled[e,eps2_index,i,jtml,-1]#w_maxunstab[e,eps2_index,jblc]
                for j in range(1,nrws-1):
                    if vpar == False and wpar == False:
                        Ff[e,e2,i,j] = -epsilon2[e2]*k[i]**2.*h2[e2,j]* (3/2*eigvecs_sorted_scaled[e,e2,i,-1,-1]-2*eigvecs_sorted_scaled[e,e2,i,-2,-1]+1/2*eigvecs_sorted_scaled[e,e2,i,-3,-1])/dp ### e,e2 vs eps1_index,eps2_index!
                    if vpar == True and wpar == False:
                        Ff[e,e2,i,j] = -1j*epsilon2[e2]*k[i]**3.*h2[e2,j]* (eigvecs_sorted_scaled[e,e2,i,-1,-1])
                    if vpar == False and wpar == True:
                        Ff[e,e2,i,j] = epsilon2[e2]*k[i]**2.*h2[e2,j]* (eigvecs_sorted_scaled[e,eps2_index,i,jtml,-1])
        
                M[e,e2,i,0,0] = 1
                M[e,e2,i,nrws-1,nrws-1] = 1

                wd[e,e2,i] = solve(M[e,e2,i],Fd[e,e2,i])
                wh[e,e2,i] = solve(M[e,e2,i],Fh[e,e2,i])
                wc[e,e2,i] = solve(M[e,e2,i],Fc[e,e2,i])
                wf[e,e2,i] = solve(M[e,e2,i],Ff[e,e2,i])
                wtot[e,e2,i] = solve(M[e,e2,i],Fd[e,e2,i]+Fh[e,e2,i]+Fc[e,e2,i]+Ff[e,e2,i])
                
            # scaling omega
            wd[e,e2] = wd[e,e2]*scale[e,e2]
            wh[e,e2] = wh[e,e2]*scale[e,e2]                
            wc[e,e2] = wc[e,e2]*scale[e,e2]
            wf[e,e2] = wf[e,e2]*scale[e,e2]
            wtot[e,e2] = wtot[e,e2]*scale[e,e2]
                        
    # testing omega components for various amounts of latent cooling    
    
    v_eps = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
    t_eps = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)
    norm_energy_eps = np.zeros((len(epsilon1),len(epsilon2),nrws),dtype=complex)

    for e in range(len(epsilon1)):
        for e2 in range(len(epsilon2)):
            v_eps[e,e2] = (1j*k[i_maxunstab[e,e2]]*psi_maxunstab[e,e2])
            t_eps[e,e2] = tempcalc(psi_maxunstab)[e,e2]
            norm_energy_eps[e,e2] = simps(abs(v_eps[e,e2]**2+t_eps[e,e2]**2/S[:nrws]),p[:nrws])

    if heating1 == True and heating2 == False and evap == False and hblcstep == 1:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_noevap[e,e2] = wd[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_noevap[e,e2] = wh[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_noevap[e,e2] = wc[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_noevap[e,e2] = wf[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_noevap = wl[i_maxunstab[e,e2]]
    if heating1 == True and evap == True and hblcstep == 1.11:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_evap01[e,e2] = wd[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_evap01[e,e2] = wh[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_evap01[e,e2] = wc[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_evap01[e,e2] = wf[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_evap01 = wl[i_maxunstab[e,e2]]
    if heating1 == True and evap == True and hblcstep == 1.21:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_evap02[e,e2] = wd[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_evap02[e,e2] = wh[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_evap02[e,e2] = wc[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_evap02[e,e2] = wf[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_evap02 = wl[i_maxunstab[e,e2]]
    if heating1 == True and evap == True and hblcstep == 1.3:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_evap03[e,e2] = wd[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_evap03[e,e2] = wh[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_evap03[e,e2] = wc[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_evap03[e,e2] = wf[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_evap03 = wl[i_maxunstab[e,e2]]
    if heating1 == True and evap == True and hblcstep == 1.4:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_evap04[e,e2] = wd[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_evap04[e,e2] = wh[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_evap04[e,e2] = wc[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_evap04[e,e2] = wf[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_evap04 = wl[i_maxunstab[e,e2]]
    if heating1 == True and evap == True and hblcstep == 1.55:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_evap05[e,e2] = wd[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_evap05[e,e2] = wh[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_evap05[e,e2] = wc[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_evap05[e,e2] = wf[:,i_maxunstab[e,e2]]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_evap05 = wl[i_maxunstab[e,e2]]

    if heating2 == True and vpar == False and wpar == False:#epsilon2 == 1:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_sf[e,e2] = wd[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_sf[e,e2] = wh[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_sf[e,e2] = wc[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_sf[e,e2] = wf[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_sf[e,e2] = wl[i_maxunstab[e,e2]]
    if heating2 == True and vpar == True and wpar == False:#epsilon2 == (1-1j)/np.sqrt(2):
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_sf1[e,e2] = wd[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_sf1[e,e2] = wh[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_sf1[e,e2] = wc[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_sf1[e,e2] = wf[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_sf1[e,e2] = wl[i_maxunstab[e,e2]]
    if heating2 == True and vpar == False and wpar == True:# and epsilon2 == -1j:
        for e in range(len(epsilon1)):
            for e2 in range(len(epsilon2)):
                wd_sf2[e,e2] = wd[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wh_sf2[e,e2] = wh[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wc_sf2[e,e2] = wc[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                wf_sf2[e,e2] = wf[e,e2,i_maxunstab[e,e2],:]#/scale[e,e2]#norm_energy_eps[e,e2]
                #wl_sf2[e,e2] = wl[i_maxunstab[e,e2]]
        
    if heating2 == True and epsilon2 == 10:
        wh_sf3 = wh
        wc_sf3 = wc
        wd_sf3 = wd
        wf_sf3 = wf
        t_sf3 = tempcalc(psi_maxunstab)
        T_sf3 = (t_sf3[eps1_index,eps2_index,:,np.newaxis]*exp(kx[np.newaxis,:]*1j)).real
        wl_sf3 = wl[i_maxunstab[eps1_index,eps2_index]]
    if heating2 == True and epsilon2 == 10*(1-1j)/np.sqrt(2):
        wh_sf4 = wh
        wc_sf4 = wc
        wd_sf4 = wd
        wf_sf4 = wf
        t_sf4 = tempcalc(psi_maxunstab)
        T_sf4 = (t_sf4[eps1_index,eps2_index,:,np.newaxis]*exp(kx[np.newaxis,:]*1j)).real
        wl_sf4 = wl[i_maxunstab[eps1_index,eps2_index]]
    if heating2 == True and epsilon2 == -10j:
        wh_sf5 = wh
        wc_sf5 = wc
        wd_sf5 = wd
        wf_sf5 = wf
        t_sf5 = tempcalc(psi_maxunstab)
        T_sf5 = (t_sf5[eps1_index,eps2_index,:,np.newaxis]*exp(kx[np.newaxis,:]*1j)).real
        wl_sf5 = wl[i_maxunstab[eps1_index,eps2_index]]
       
       
    wsplit_plot = False    
    if wsplit_plot == True:
        
        fig,ax = plt.subplots(figsize=(10,6))

        ax.plot((),(),c='grey',linestyle='-.')

        try:
            wd_noevap
        except:
            pass
        else:
            ax.plot(abs(wd_noevap[eps1_index,eps2_index]),p[:nrws],c=c_greys[0],linestyle='-.')
            ax.plot(abs(wh_noevap[eps1_index,eps2_index]),p[:nrws],c=c_greys[0],linestyle='--')
            ax.plot(abs(wc_noevap[eps1_index,eps2_index]),p[:nrws],c=c_greys[0],linestyle=':')
            ax.plot(abs(wf_noevap[eps1_index,eps2_index]),p[:nrws],c=c_greys[0],linestyle=':')#dashes=[4,1])
            ax.plot(abs(wd_noevap[eps1_index,eps2_index]+wh_noevap[eps1_index,eps2_index]+wc_noevap[eps1_index,eps2_index]+wf_noevap[eps1_index,eps2_index]),p[:nrws],c=c_greys[0],linestyle='-',label='no sf')#, linewidth=2.5)
            #ax.plot(abs(w_maxunstab[eps1_index,eps2_index]),p[:nrws],c='grey',linestyle='-')
        try:
            wd_evap01
        except:
            pass
        else:    
            ax.plot(abs(wd_evap01[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[2],linestyle='-.')
            ax.plot(abs(wh_evap01[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[2],linestyle='--')
            ax.plot(abs(wc_evap01[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[2],linestyle=':')
            ax.plot(abs(wd_evap01[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wh_evap01[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wc_evap01[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[2],linestyle='-',label='20%')
            #ax.plot(abs(wd_evap02[eps1_index]+whc_evap02[eps1_index]),p[:nrws],c=c_greys[1],linestyle='-',label='20%')
        try:
            wd_evap02
        except:
            pass
        else:    
            ax.plot(abs(wd_evap02[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[2],linestyle='-.')
            ax.plot(abs(wh_evap02[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[2],linestyle='--')
            ax.plot(abs(wc_evap02[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[2],linestyle=':')
            ax.plot(abs(wd_evap02[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wh_evap02[eps1_index,i_maxunstab[eps1_index,eps2_index]]+wc_evap02[eps1_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[2],linestyle='-',label='20%')
            #ax.plot(abs(wd_evap02[eps1_index]+whc_evap02[eps1_index]),p[:nrws],c=c_greys[1],linestyle='-',label='20%')
        try:
            wd_evap04
        except:
            pass
        else:
            ax.plot(abs(wd_evap04[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[4],linestyle='-.')
            ax.plot(abs(wh_evap04[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[4],linestyle='--')
            ax.plot(abs(wc_evap04[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[4],linestyle=':')
            ax.plot(abs(wd_evap04[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wh_evap04[eps1_index,i_maxunstab[eps1_index,eps2_index]]+wc_evap04[eps1_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[4],linestyle='-',label='40%')
            #ax.plot(abs(w_maxunstab[eps1_index,eps2_index]),p[:nrws],c=c_blues[4],linestyle='-',label='40%')
            #ax.plot(abs(wd_evap04[eps1_index]+whc_evap04[eps1_index]),p[:nrws],c=c_greys[2],linestyle='-',label='40%')
        try:
            wd_evap05111
        except:
            pass
        else:
            ax.plot(abs(wd_evap05[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[5],linestyle='-.')
            ax.plot(abs(wh_evap05[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[5],linestyle='--')
            ax.plot(abs(wc_evap05[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[5],linestyle=':')
            ax.plot(abs(wd_evap05[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wh_evap05[eps1_index,i_maxunstab[eps1_index,eps2_index]]+wc_evap05[eps1_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[5],linestyle='-',label='50%')
            #ax.plot(abs(w_maxunstab[eps1_index,eps2_index]),p[:nrws],c=c_blues[4],linestyle='-',label='40%')
            #ax.plot(abs(wd_evap04[eps1_index]+whc_evap04[eps1_index]),p[:nrws],c=c_greys[2],linestyle='-',label='40%')


        sfsplit = True
        if sfsplit == True:
            try:
                wd_sf
            except:
                pass
            else:
                ax.plot(abs(wd_sf[eps1_index,eps2_index]),p[:nrws],c=c_reds[0],linestyle='-.')
                ax.plot(abs(wh_sf[eps1_index,eps2_index]),p[:nrws],c=c_reds[0],linestyle='--')
                ax.plot(abs(wf_sf[eps1_index,eps2_index]),p[:nrws],c=c_reds[0],linestyle=':')
                ax.plot(abs(wd_sf[eps1_index,eps2_index]+wh_sf[eps1_index,eps2_index]+wf_sf[eps1_index,eps2_index]),p[:nrws],c=c_reds[0],linestyle='-',label='Tpar')
#                ax.plot(abs(w_maxunstab[eps1_index,eps2_index]),p[:nrws],c=c_reds[0],linestyle='-')#,label='tot')
                #ax.plot(abs(wd_evap04[eps1_index]+whc_evap04[eps1_index]),p[:nrws],c=c_greys[2],linestyle='-',label='40%')
            try:
                wd_sf1
            except:
                pass
            else:
                ax.plot(abs(wd_sf1[eps1_index,eps2_index]),p[:nrws],c=c_greys[2],linestyle='-.')
                ax.plot(abs(wh_sf1[eps1_index,eps2_index]),p[:nrws],c=c_greys[2],linestyle='--')
                ax.plot(abs(wf_sf1[eps1_index,eps2_index]),p[:nrws],c=c_greys[2],linestyle=':')
                ax.plot(abs(wd_sf1[eps1_index,eps2_index]+wh_sf1[eps1_index,eps2_index]+wf_sf1[eps1_index,eps2_index]),p[:nrws],c=c_greys[2],linestyle='-',label='vpar')
            try:
                wd_sf2
            except:
                pass
            else:
                ax.plot(abs(wd_sf2[eps1_index,eps2_index]),p[:nrws],c=c_blues[0],linestyle='-.')
                ax.plot(abs(wh_sf2[eps1_index,eps2_index]),p[:nrws],c=c_blues[0],linestyle='--')
                ax.plot(abs(wf_sf2[eps1_index,eps2_index]),p[:nrws],c=c_blues[0],linestyle=':')
                ax.plot(abs(wd_sf2[eps1_index,eps2_index]+wh_sf2[eps1_index,eps2_index]+wf_sf2[eps1_index,eps2_index]),p[:nrws],c=c_blues[0],linestyle='-',label='wpar')
            try:
                wd_sf3
            except:
                pass
            else:
                ax.plot(abs(wd_sf3[eps1_index,eps2_index]),p[:nrws],c=c_reds[3],linestyle='-.')
                ax.plot(abs(wh_sf3[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_reds[3],linestyle='--')
                ax.plot(abs(wf_sf3[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_reds[3],linestyle=':')
                ax.plot(abs(wd_sf3[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wh_sf3[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wf_sf3[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_reds[3],linestyle='-',label='10')
            try:
                wd_sf4
            except:
                pass
            else:
                ax.plot(abs(wd_sf4[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_greys[0],linestyle='-.')
                ax.plot(abs(wh_sf4[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_greys[0],linestyle='--')
                ax.plot(abs(wf_sf4[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_greys[0],linestyle=':')
                ax.plot(abs(wd_sf4[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wh_sf4[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wf_sf4[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_greys[0],linestyle='-',label='10(1-i)/$\mathregular{\sqrt{2}}$')
            try:
                wd_sf5
            except:
                pass
            else:
                ax.plot(abs(wd_sf5[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[3],linestyle='-.')
                ax.plot(abs(wh_sf5[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[3],linestyle='--')
                ax.plot(abs(wf_sf5[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[3],linestyle=':')
                ax.plot(abs(wd_sf5[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wh_sf5[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]+wf_sf5[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index]]),p[:nrws],c=c_blues[3],linestyle='-',label='-10i')
        ax1 = ax.twinx()
        ax1.plot((),(),c='k',linestyle='-.',label='$\omega_d$')
        ax1.plot((),(),c='k',linestyle='--',label='$\omega_h$')
        ax1.plot((),(),c='k',linestyle=':',label='$\omega_f$')
        ax1.plot((),(),c='k',linestyle='-',label='$\omega$')
        ax.invert_yaxis()
        ax.set_ylabel('pressure')
        ax.set_xlabel('normalised amplitude')
    #    ax.set_xlim(0.04,0.06)
        import itertools
        def flip(items, ncol):
            return itertools.chain(*[items[i::ncol] for i in range(ncol)])
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(bbox_to_anchor=(0.5,-0.2), loc='upper center', ncol=4, fancybox=True) #flip(handles, 3), flip(labels, 3), 
        ax1.legend(loc='best')

        plt.show()
        
        
        


# -----------------------------------------------------------------------------

### checking growth rate for various latent heating and cooling intensities

def check_growthrates_for_various_epsilon_and_gamma():
    
    if len(epsilon1) > 1:
        
        try:
            wfrac
        except:
            evap_vec = ([])
            sigmai3D_evapcond = ([])
            #sigtemp = ([])
            WLmax = ([])
            wce = ([])
            wfrac = ([])
            norm_kenergy_vec = ([])
            wcetemp = np.zeros(len(epsilon1))
            wfractemp = np.zeros(len(epsilon1))
            #Ttemp = np.zeros(np.shape(T))
            vtemp = np.zeros((len(epsilon1),nrws))
            kenergytemp = np.zeros((len(epsilon1)))
                
        if heating1 == True and heating2 == False and evap == False:
            evap_vec.extend([1])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
            for e in range(len(epsilon1)):
                wcetemp[e]=abs(wd_noevap[e,i_maxunstab[e,eps2_index],jblc]+wc_noevap[e,i_maxunstab[e,eps2_index],jblc]+wh_noevap[e,i_maxunstab[e,eps2_index],jblc])
            wce.extend([copy(wcetemp)])
            for e in range(len(epsilon1)):
                wfractemp[e]=abs(wc_noevap[e,i_maxunstab[e,eps2_index],jblc])/abs(wh_noevap[e,i_maxunstab[e,eps2_index],jblc])
            wfrac.extend([copy(wfractemp)])      
            for e in range(len(epsilon1)):
                #Ttemp[e] = tempcalc(eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                vtemp[e] = abs(1j*k[i_maxunstab[e,eps2_index]]*eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                kenergytemp[e] = simps(abs(vtemp[e]**2),p[:nrws])
            norm_kenergy_vec.extend([copy(kenergytemp)])
            
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.1:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
            for e in range(len(epsilon1)):
                wcetemp[e]=abs(wd_evap01[e,i_maxunstab[e,eps2_index],jblc]+wc_evap01[e,i_maxunstab[e,eps2_index],jblc]+wh_evap01[e,i_maxunstab[e,eps2_index],jblc])
            wce.extend([copy(wcetemp)])
            for e in range(len(epsilon1)):
                wfractemp[e]=abs(wc_evap01[e,i_maxunstab[e,eps2_index],jblc])/abs(wh_evap01[e,i_maxunstab[e,eps2_index],jblc])
            wfrac.extend([copy(wfractemp)])      
            for e in range(len(epsilon1)):
                #Ttemp[e] = tempcalc(eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                vtemp[e] = abs(1j*k[i_maxunstab[e,eps2_index]]*eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                kenergytemp[e] = simps(abs(vtemp[e]**2),p[:nrws])
            norm_kenergy_vec.extend([copy(kenergytemp)])
            
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.2:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
            for e in range(len(epsilon1)):
                wcetemp[e]=abs(wd_evap02[e,i_maxunstab[e,eps2_index],jblc]+wc_evap02[e,i_maxunstab[e,eps2_index],jblc]+wh_evap02[e,i_maxunstab[e,eps2_index],jblc])
            wce.extend([copy(wcetemp)])
            for e in range(len(epsilon1)):
                wfractemp[e]=abs(wc_evap02[e,i_maxunstab[e,eps2_index],jblc])/abs(wh_evap02[e,i_maxunstab[e,eps2_index],jblc])
            wfrac.extend([copy(wfractemp)])      
            for e in range(len(epsilon1)):
                #Ttemp[e] = tempcalc(eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                vtemp[e] = abs(1j*k[i_maxunstab[e,eps2_index]]*eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                kenergytemp[e] = simps(abs(vtemp[e]**2),p[:nrws])
            norm_kenergy_vec.extend([copy(kenergytemp)])
            
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.3:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
            for e in range(len(epsilon1)):
                wcetemp[e]=abs(wd_evap03[e,i_maxunstab[e,eps2_index],jblc]+wc_evap03[e,i_maxunstab[e,eps2_index],jblc]+wh_evap03[e,i_maxunstab[e,eps2_index],jblc])
            wce.extend([copy(wcetemp)])
            for e in range(len(epsilon1)):
                wfractemp[e]=abs(wc_evap03[e,i_maxunstab[e,eps2_index],jblc])/abs(wh_evap03[e,i_maxunstab[e,eps2_index],jblc])
            wfrac.extend([copy(wfractemp)])      
            for e in range(len(epsilon1)):
                #Ttemp[e] = tempcalc(eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                vtemp[e] = abs(1j*k[i_maxunstab[e,eps2_index]]*eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                kenergytemp[e] = simps(abs(vtemp[e]**2),p[:nrws])
            norm_kenergy_vec.extend([copy(kenergytemp)])
            
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.4:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
            for e in range(len(epsilon1)):
                wcetemp[e]=abs(wd_evap04[e,i_maxunstab[e,eps2_index],jblc]+wc_evap04[e,i_maxunstab[e,eps2_index],jblc]+wh_evap04[e,i_maxunstab[e,eps2_index],jblc])
            wce.extend([copy(wcetemp)])
            for e in range(len(epsilon1)):
                wfractemp[e]=abs(wc_evap04[e,i_maxunstab[e,eps2_index],jblc])/abs(wh_evap04[e,i_maxunstab[e,eps2_index],jblc])
            wfrac.extend([copy(wfractemp)])      
            for e in range(len(epsilon1)):
                #Ttemp[e] = tempcalc(eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                vtemp[e] = abs(1j*k[i_maxunstab[e,eps2_index]]*eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                kenergytemp[e] = simps(abs(vtemp[e]**2),p[:nrws])
            norm_kenergy_vec.extend([copy(kenergytemp)])
            
        if heating1 == True and heating2 == False and evap == True and hblcstep == 1.5:
            evap_vec.extend([hblcstep])
            sigmai3D_evapcond.extend([np.amax(sigmai_sorted[:,e2,:,-1], axis=1)])
            WLmax.extend(np.array([wl[np.squeeze(i_maxunstab[:])]]))
            for e in range(len(epsilon1)):
                wcetemp[e]=abs(wd_evap05[e,i_maxunstab[e,eps2_index],jblc]+wc_evap05[e,i_maxunstab[e,eps2_index],jblc]+wh_evap05[e,i_maxunstab[e,eps2_index],jblc])
            wce.extend([copy(wcetemp)])
            for e in range(len(epsilon1)):
                wfractemp[e]=abs(wc_evap05[e,i_maxunstab[e,eps2_index],jblc])/abs(wh_evap05[e,i_maxunstab[e,eps2_index],jblc])
            wfrac.extend([copy(wfractemp)])      
            for e in range(len(epsilon1)):
                #Ttemp[e] = tempcalc(eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                vtemp[e] = abs(1j*k[i_maxunstab[e,eps2_index]]*eigvecs_sorted_scaled[e,eps2_index,i_maxunstab[e,eps2_index],nrws:,-1])
                kenergytemp[e] = simps(abs(vtemp[e]**2),p[:nrws])
            norm_kenergy_vec.extend([copy(kenergytemp)])
            
        #evap_vec, sigmai3D_evapcond

        #evap_vec_temp = ([])
        #sigmai3D_evapcond_temp = ([])

        evap_vec_temp = np.array(evap_vec)
        sigmai3D_evapcond_temp = np.array(sigmai3D_evapcond)
        WLmax_temp = np.array(WLmax)
        wce_temp = np.array(wce)
        wfrac_temp = np.array(wfrac)
        norm_kenergy_vec_temp = np.array(norm_kenergy_vec)
        evap_vec_sort = evap_vec_temp[evap_vec_temp.argsort()]
        sigmai3D_evapcond_sort = sigmai3D_evapcond_temp[evap_vec_temp.argsort()]
        WLmax_sort = WLmax_temp[evap_vec_temp.argsort()]
        wce_sort = wce_temp[evap_vec_temp.argsort()]
        wfrac_sort = wfrac_temp[evap_vec_temp.argsort()]
        norm_kenergy_vec_sort = norm_kenergy_vec_temp[evap_vec_temp.argsort()]
        
        fig = plt.subplots(figsize=(10,8),dpi=300)

        norm = MidpointNormalize(midpoint=0)
    #    ax = plt.contourf(evap_vec_sort,epsilon1,np.transpose(sigmai3D_evapcond_sort),16,cmap=cm)
        ax = plt.contourf(evap_vec_sort,epsilon1,np.transpose(wce_sort/norm_kenergy_vec_sort),20,cmap=cm_br)
    #    CS = plt.contour(evap_vec_sort,epsilon1,np.transpose(WLmax_sort)*1000,12,colors='k',linewidths=.5)
        CS = plt.contour(evap_vec_sort,epsilon1,np.transpose(wfrac_sort)*1000,12,colors='k',linewidths=.5)
        #CS2 = plt.contour(evap_vec_sort,epsilon1,np.transpose(wfrac_sort)*1000,12,colors='grey',linewidths=.5)
        #ax2 = plt.contour(evap_vec_sort,epsilon1,np.transpose(sigmai3D_evapcond_sort),16,colors='k',lw=.5)
        cbar = plt.colorbar(ax)
        #cbar.add_lines(ax2)
        cbar.set_label('growth rate (day$\mathregular{^{-1}}$)', rotation=270, labelpad=25)
    #    cbar.set_label('$\mathregular{\omega_{lc}/\omega_{lh}}$', rotation=270, labelpad=25)
        cbar.set_label('vertical velocity at bottom of heating layer\nnormalized by kinetic energy', rotation=270, labelpad=25)
        plt.ylabel('heating intensity parameter $\mathregular{\\varepsilon}$')
        plt.xlabel('relative cooling parameter $\mathregular{\gamma}$')
        #plt.title('Maximum growth rate (day$\mathregular{^{-1}}$)', fontsize=16)
        plt.xticks([1,1.1,1.2,1.3,1.4,1.5])
        #plt.xlim(.95,1.55)
        gca().set_xticklabels(['0.0','0.1','0.2','0.3','0.4','0.5'])
        #plt.tick_params(axis='both', labelsize=14)
        #cbar.ax.tick_params(labelsize=14)
        manual_locations = [(1.2, 10.2),(1.2,11.9),(1.2,13),(1.2,13.9),(1.2,14.7)]
        manual_locations = [(1.07, 12.5),(1.12,12.5),(1.2,12.5),(1.27,12.5),(1.32,12.5),(1.4,12.5),(1.45,12.5)]
        CLS = plt.clabel(CS, CS.levels[:-2],fmt='%d', fontsize=10, manual=manual_locations)#,inline=True)
        #CLS2 = plt.clabel(CS2, CS2.levels[2::2],fmt='%d', fontsize=10)#,inline=True)
        #new_labels = []
        #for label in CLS:
        #    lx,ly = label.get_position()
        #    new_labels.append((1.25,ly))
        #for cline in CS.collections:
        #    cline.remove()
        #for label in CLS:
        #    label.remove()
        #CS = plt.contour(evap_vec_sort,epsilon1,np.transpose(WLmax_sort)*1000,20,colors='k',linewidths=.5)
        #CLS = plt.clabel(CS, CS.levels[::2],fmt
        gca().tick_params(which='both', length=6, width=1)

        plt.tight_layout()
        plt.show()

# -----------------------------------------------------------------------------

### checking growthrates for various latent heating intensities vs wavelength

def check_growthrates_for_various_epsilon_and_wavelengths():

    if len(epsilon1) > 1:
        
        #maxval = (np.max(sigmai_sorted))
        #minval = .01
        #inc = float("{0:.1f}".format((maxval-minval)/(lev2-1)))
        #bounds = np.arange(minval,minval+inc*(lev2-1),inc)
        #norm = mpl.colors.BoundaryNorm(bounds, cm2)

        norm = MidpointNormalize(midpoint=0.13)

        fig, ax = plt.subplots(figsize=(7,3.5)) ####(12,5)
    #    gs = gridspec.GridSpec(1, 2, width_ratios=[9, 2]) 
    #    ax = plt.subplot(gs[0])
    #    ax3 = plt.subplot(gs[1])
    #    gs.update(wspace=.1,hspace=1) 
        
    #  fig = plt.subplots(figsize=(12,5))
        CP = ax.contourf(wl,epsilon1,(sigmai_sorted[:,e2,:,-1]),11,norm=norm,cmap=cm_wrr)
        #ax.contour(wl,epsilon1,(sigmai_sorted[:,e2,:,-1]),levels=[.25],colors='darkgrey')
        #ax = plt.scatter(wl[:,np.newaxis]*np.ones((len(wl),len(epsilon1))),epsilon1[np.newaxis,:]*np.ones((len(wl),len(epsilon1))),c=(sigmai_sorted[:,e2,:,-1]),s=20,norm=norm,cmap=cm_wr,lw=0)
        cbar = fig.colorbar(CP,ax=ax)
    #    cbar.ax.set_ylabel('10$\mathregular{^{-5}s^{-1}}$', rotation=270, labelpad=18)
        #cbar.set_label('growth rate (day$\mathregular{^{-1}}$)', rotation=270, labelpad=25, fontsize=14)
        ax.set_ylabel('heating intensity parameter $\mathregular{\\varepsilon}$')
        ax.set_xscale('log')
        ax.set_xticks([.1,.5,1,5,10,50])
        ax.set_xticklabels([100,500,1000,5000,10000,50000])
        ax.set_xlim((.2, 35))
        ax.set_xlabel('wavelength (km)')
        #plt.title('Maximum growth rate (day$\mathregular{^{-1}}$)', fontsize=16)

        fig, ax3 = plt.subplots(figsize=(1.8,3.5)) ####(12,5)    
        
        ratio = np.zeros(len(epsilon1))
        for e in range(len(epsilon1)):
            ratio[e] = abs(wh[e,eps2_index,i_maxunstab[e,eps2_index],jblc]+wc[e,eps2_index,i_maxunstab[e,eps2_index],jblc])/abs(wd[e,eps2_index,i_maxunstab[e,eps2_index],jblc])
        lns7 = ax3.scatter(ratio,epsilon1,c='grey',edgecolor='k',label='$\omega_{h}/\omega_d$')#,colors='k',lw=1.5,ls='-'
        ax3.set_xlabel('$\mathregular{\omega_{h}/\omega_d}$')
        #plt.tick_params(axis='both', labelsize=14)
        #ax3.tick_params(axis='both', labelsize=14)
        #cbar.ax.tick_params(labelsize=14) 
        ax3.axhline(15, c='k',ls='--')
    #    ax3.axhline(17, c='grey',ls='--')
        #ax3.axvline(1, c='k',ls='--')
        ax.axhline(15, c='k',ls='--')
    #    ax.axhline(17, c='grey',ls='--')
        #ax3.set_xlim((0, 5))
        ax3.set_ylim((0, 60))
        ax.tick_params(which='minor', length=3, width=1)
        ax.tick_params(which='major', length=6, width=1)
        ax3.tick_params(which='both', length=6, width=1)
        for label in ax3.xaxis.get_ticklabels()[::2]:
            label.set_visible(False)
        #plt.annotate('$\mathregular{\\varepsilon}$ = 16',xy=(.2,17),fontsize=14)
        plt.tight_layout()
        plt.show()

    #abs(whc_noevap[eps1_index,i_maxunstab[eps1_index,eps2_index],jblc]+whe_noevap[eps1_index,i_maxunstab[eps1_index,eps2_index],jblc])/abs(wd_noevap[eps1_index,i_maxunstab[eps1_index,eps2_index],jblc])

# -----------------------------------------------------------------------------

### comparing changes in growth rate and wavelength between epsilon1[0] and epsilon1[-1] for different heating boundaries

def delta_growthrate_wavelength_vs_cloudtop():
    
    try:
        dsigb1
    except:
        dptlcb1 = ([])
        dsigb1 = ([])
        dwlb1 = ([])
        dwb1 = ([])
        dptlcb2 = ([])
        dsigb2 = ([])
        dwlb2 = ([])
        dwb2 = ([])
        dptlcb3 = ([])
        dsigb3 = ([])
        dwlb3 = ([])
        dwb3 = ([])
        dptlcb4 = ([])
        dsigb4 = ([])
        dwlb4 = ([])
        dwb4 = ([])
        dptlcb5 = ([])
        dsigb5 = ([])
        dwlb5 = ([])
        dwb5 = ([])
                  
    if heating1 == True and heating2 == False and evap == False and .99 < pblc:
        pblc1 = pblc
        dptlcb1.extend([ptlc])
        dsigb1.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwlb1.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
        tt0 = tempcalc(psi_maxunstab)[0]
        vt0 = 1j*k[i_maxunstab[0,eps2_index]]*psi_maxunstab[0,eps2_index]
        tt1 = tempcalc(psi_maxunstab)[-1]
        vt1 = 1j*k[i_maxunstab[-1,eps2_index]]*psi_maxunstab[-1,eps2_index]
        dwb1.extend([abs(w_maxunstab[0,eps2_index,jtml])/simps(abs(vt0**2+tt0**2/S[:nrws]),p[:nrws])-abs(w_maxunstab[-1,eps2_index,jtml])/simps(abs(vt1**2+tt1**2/S[:nrws]),p[:nrws])])
    if heating1 == True and heating2 == False and evap == False and .94 < pblc < .96:
        pblc2 = pblc
        dptlcb2.extend([ptlc])
        dsigb2.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwlb2.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
        tt0 = tempcalc(psi_maxunstab)[0]
        vt0 = 1j*k[i_maxunstab[0,eps2_index]]*psi_maxunstab[0,eps2_index]
        tt1 = tempcalc(psi_maxunstab)[-1]
        vt1 = 1j*k[i_maxunstab[-1,eps2_index]]*psi_maxunstab[-1,eps2_index]
        dwb2.extend([abs(w_maxunstab[0,eps2_index,jtml])/simps(abs(vt0**2+tt0**2/S[:nrws]),p[:nrws])-abs(w_maxunstab[-1,eps2_index,jtml])/simps(abs(vt1**2+tt1**2/S[:nrws]),p[:nrws])])
    if heating1 == True and heating2 == False and evap == False and .89 < pblc < .91:
        pblc3 = pblc
        dptlcb3.extend([ptlc])
        dsigb3.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwlb3.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
        tt0 = tempcalc(psi_maxunstab)[0]
        vt0 = 1j*k[i_maxunstab[0,eps2_index]]*psi_maxunstab[0,eps2_index]
        tt1 = tempcalc(psi_maxunstab)[-1]
        vt1 = 1j*k[i_maxunstab[-1,eps2_index]]*psi_maxunstab[-1,eps2_index]
        dwb3.extend([abs(w_maxunstab[0,eps2_index,jtml])/simps(abs(vt0**2+tt0**2/S[:nrws]),p[:nrws])-abs(w_maxunstab[-1,eps2_index,jtml])/simps(abs(vt1**2+tt1**2/S[:nrws]),p[:nrws])])
    if heating1 == True and heating2 == False and evap == False and .84 < pblc < .86:
        pblc4 = pblc
        dptlcb4.extend([ptlc])
        dsigb4.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwlb4.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
        tt0 = tempcalc(psi_maxunstab)[0]
        vt0 = 1j*k[i_maxunstab[0,eps2_index]]*psi_maxunstab[0,eps2_index]
        tt1 = tempcalc(psi_maxunstab)[-1]
        vt1 = 1j*k[i_maxunstab[-1,eps2_index]]*psi_maxunstab[-1,eps2_index]
        dwb4.extend([abs(w_maxunstab[0,eps2_index,jtml])/simps(abs(vt0**2+tt0**2/S[:nrws]),p[:nrws])-abs(w_maxunstab[-1,eps2_index,jtml])/simps(abs(vt1**2+tt1**2/S[:nrws]),p[:nrws])])
    if heating1 == True and heating2 == False and evap == False and .79 < pblc < .81:
        pblc5 = pblc
        dptlcb5.extend([ptlc])
        dsigb5.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwlb5.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
        tt0 = tempcalc(psi_maxunstab)[0]
        vt0 = 1j*k[i_maxunstab[0,eps2_index]]*psi_maxunstab[0,eps2_index]
        tt1 = tempcalc(psi_maxunstab)[-1]
        vt1 = 1j*k[i_maxunstab[-1,eps2_index]]*psi_maxunstab[-1,eps2_index]
        dwb5.extend([abs(w_maxunstab[0,eps2_index,jtml])/simps(abs(vt0**2+tt0**2/S[:nrws]),p[:nrws])-abs(w_maxunstab[-1,eps2_index,jtml])/simps(abs(vt1**2+tt1**2/S[:nrws]),p[:nrws])])
        
    dptlcb1_temp = np.array(dptlcb1)
    dsigb1_temp = np.array(dsigb1)
    dwlb1_temp = np.array(dwlb1)
    dwb1_temp = np.array(dwb1)
    dptlcb2_temp = np.array(dptlcb2)
    dsigb2_temp = np.array(dsigb2)
    dwlb2_temp = np.array(dwlb2) 
    dwb2_temp = np.array(dwb2)   
    dptlcb3_temp = np.array(dptlcb3)
    dsigb3_temp = np.array(dsigb3)
    dwlb3_temp = np.array(dwlb3) 
    dwb3_temp = np.array(dwb3)  
    dptlcb4_temp = np.array(dptlcb4)
    dsigb4_temp = np.array(dsigb4)
    dwlb4_temp = np.array(dwlb4)
    dwb4_temp = np.array(dwb4)   
    dptlcb5_temp = np.array(dptlcb5)
    dsigb5_temp = np.array(dsigb5)
    dwlb5_temp = np.array(dwlb5)
    dwb5_temp = np.array(dwb5)
    
    dptlcb1_sort = dptlcb1_temp[dptlcb1_temp.argsort()]
    dsigb1_sort = dsigb1_temp[dptlcb1_temp.argsort()]
    dwlb1_sort = dwlb1_temp[dptlcb1_temp.argsort()]
    dwb1_sort = dwb1_temp[dptlcb1_temp.argsort()]
    dptlcb2_sort = dptlcb2_temp[dptlcb2_temp.argsort()]
    dsigb2_sort = dsigb2_temp[dptlcb2_temp.argsort()]
    dwlb2_sort = dwlb2_temp[dptlcb2_temp.argsort()]
    dwb2_sort = dwb2_temp[dptlcb2_temp.argsort()]
    dptlcb3_sort = dptlcb3_temp[dptlcb3_temp.argsort()]
    dsigb3_sort = dsigb3_temp[dptlcb3_temp.argsort()]
    dwlb3_sort = dwlb3_temp[dptlcb3_temp.argsort()]
    dwb3_sort = dwb3_temp[dptlcb3_temp.argsort()]
    dptlcb4_sort = dptlcb4_temp[dptlcb4_temp.argsort()]
    dsigb4_sort = dsigb4_temp[dptlcb4_temp.argsort()]
    dwlb4_sort = dwlb4_temp[dptlcb4_temp.argsort()]
    dwb4_sort = dwb4_temp[dptlcb4_temp.argsort()]
    dptlcb5_sort = dptlcb5_temp[dptlcb5_temp.argsort()]
    dsigb5_sort = dsigb5_temp[dptlcb5_temp.argsort()]
    dwlb5_sort = dwlb5_temp[dptlcb5_temp.argsort()]
    dwb5_sort = dwb5_temp[dptlcb5_temp.argsort()]


    # plotting changes in growth rate and wavelength for different heating boundaries
    
    try:
        pblc1 and pblc3 and pblc5
    except:
        pass
    else:
        
    #    if len(dptlcb1_sort) == len(dptlcb2_sort) and len(dptlcb1_sort) == len(dptlcb3_sort) and len(dptlcb1_sort) == len(dptlcb4_sort):
        if len(dptlcb1_sort) == len(dptlcb3_sort) and len(dptlcb1_sort) == len(dptlcb5_sort):
            sigmattb = np.array([dsigb1_sort,dsigb3_sort,dsigb5_sort])
            wlmattb = np.array([dwlb1_sort,dwlb3_sort,dwlb5_sort])
            wmattb = np.array([dwb1_sort,dwb3_sort,dwb5_sort])
            pblcvec = np.array([pblc1,pblc3,pblc5])
            if len(dptlcb1_sort) == len(dptlcb2_sort):
                sigmattb = np.array([dsigb1_sort,dsigb2_sort,dsigb3_sort,dsigb5_sort])
                wlmattb = np.array([dwlb1_sort,dwlb2_sort,dwlb3_sort,dwlb5_sort])
                wmattb = np.array([dwb1_sort,dwb2_sort,dwb3_sort,dwb5_sort])
                pblcvec = np.array([pblc1,pblc2,pblc3,pblc5])
                if len(dptlcb1_sort) == len(dptlcb4_sort):
                    sigmattb = np.array([dsigb1_sort,dsigb2_sort,dsigb3_sort,dsigb4_sort,dsigb5_sort])
                    wlmattb = np.array([dwlb1_sort,dwlb2_sort,dwlb3_sort,dwlb4_sort,dwlb5_sort])
                    wmattb = np.array([dwb1_sort,dwb2_sort,dwb3_sort,dwb4_sort,dwb5_sort])
                    pblcvec = np.array([pblc1,pblc2,pblc3,pblc4,pblc5])

            norm = MidpointNormalize(midpoint=0.4)
            
            fig,ax = plt.subplots(figsize=(10,3.2))
            
            sigplot = ax.contourf(pblcvec,dptlcb1_sort,abs(sigmattb.T),10,norm=norm,cmap=cm_gwrr)
            cbar1 = plt.colorbar(sigplot)#, orientation="horizontal", pad=.2, shrink=.5)
            cbar1.set_label('abs. change in growth rate',rotation=270,labelpad=15)
            CS = plt.contour(pblcvec,dptlcb1_sort,(wlmattb.T),13,cmap=c_yb,linewidths=2)
            #manual_locations = [(.15, .7),(.25,.75),(.4,.885)]
    #        plt.clabel(CS, CS.levels[::2], inline=True, fontsize=10)#, manual=manual_locations)
            cbar2 = plt.colorbar(CS, pad=.15)
            cbar2.set_label('abs. change in wavelength',rotation=270,labelpad=15)
            cbar2.ax.get_children()[0].set_linewidths(5.0)
            CS2 = plt.contour(pblcvec,dptlcb1_sort,abs(wmattb.T),13,cmap=c_wb,linewidths=1.5)#[c[1]],ls='-')
            #manual_locations = [(.15, .7),(.25,.75),(.4,.885)]
            cbar3 = plt.colorbar(CS2)
            cbar3.set_label('abs. change in normalized $\mathregular{\omega_{cb}}$',rotation=270,labelpad=15)
            cbar3.ax.get_children()[0].set_linewidths(5.0)
            #cbar.lines[0].set_lineheight(10)
    #        plt.clabel(CS2, CS2.levels[::2], inline=True, fontsize=10)#, manual=manual_locations)
        #    plt.plot((dwl2_sort),dpblc_sort,'r')
            plt.ylabel('pressure at top of heating layer')
        #    plt.xlabel('change in growth rate (blue) and wavelength (red) from eps=0 to eps=15')
            plt.xlabel('pressure at bottom of heating layer')
            plt.ylim(.15,.45000001)
            gca().invert_yaxis()
            gca().tick_params(which='both', length=6, width=1)

            norm = MidpointNormalize(midpoint=0.006)

            fig = plt.subplots(figsize=(4,5))
            
            wplot = plt.contourf(pblcvec,dptlcb1_sort,abs(wmattb.T),11,norm=norm,cmap=cm_gwrr)
            cbar = plt.colorbar(wplot, orientation="horizontal", pad=.2)
            cbar.set_label('abs. change in vertical velocity')
    #        for label in cbar.ax.xaxis.get_ticklabels()[::2]:
    #            label.set_visible(False)
    #        CS = plt.contour(pblcvec,dptlcb1_sort,(wlmattb.T),15,colors='k')
            #manual_locations = [(.15, .7),(.25,.75),(.4,.885)]
    #        plt.clabel(CS, CS.levels[::2], inline=True, fontsize=10)#, manual=manual_locations)
        #    plt.plot((dwl2_sort),dpblc_sort,'r')
            plt.ylabel('pressure at top of heating layer')
        #    plt.xlabel('change in growth rate (blue) and wavelength (red) from eps=0 to eps=15')
            plt.xlabel('pressure at bottom of heating layer')
            plt.ylim(.15,.45000001)
            gca().invert_yaxis()
            gca().tick_params(which='both', length=6, width=1)
            
            plt.show()

# -----------------------------------------------------------------------------

### comparing changes in growth rate and wavelength between epsilon1[0] and epsilon1[-1] for varying latent cooling and top of heating layer

def delta_growthrate_wavelength_vs_gamma_and_cloudtop():
    
    try:
        dsig
    except:
        dptlc = ([])
        dsig = ([])
        dwl = ([])
        dptlce = ([])
        dsige = ([])
        dwle = ([])
        dptlce2 = ([])
        dsige2 = ([])
        dwle2 = ([])
        dptlce22 = ([])
        dsige22 = ([])
        dwle22 = ([])
        dptlce3 = ([])
        dsige3 = ([])
        dwle3 = ([])
                  
    if heating1 == True and heating2 == False and evap == False and .89 < pblc < .91:
        ev1 = 0
        dptlc.extend([ptlc])
        dsig.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwl.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.1 and .89 < pblc < .91:
        ev2 = hblcstep-1
        dptlce.extend([ptlc])
        dsige.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwle.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.2 and .89 < pblc < .91:
        ev2 = hblcstep-1
        dptlce22.extend([ptlc])
        dsige22.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwle22.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.3 and .89 < pblc < .91:
        ev3 = hblcstep-1
        dptlce3.extend([ptlc])
        dsige3.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwle3.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.5 and .89 < pblc < .91:
        ev4 = hblcstep-1
        dptlce2.extend([ptlc])
        dsige2.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwle2.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
        
    dptlc_temp = np.array(dptlc)
    dsig_temp = np.array(dsig)
    dwl_temp = np.array(dwl)
    dptlce_temp = np.array(dptlce)
    dsige_temp = np.array(dsige)
    dwle_temp = np.array(dwle)
    dptlce22_temp = np.array(dptlce22)
    dsige22_temp = np.array(dsige22)
    dwle22_temp = np.array(dwle22)
    dptlce2_temp = np.array(dptlce2)
    dsige2_temp = np.array(dsige2)
    dwle2_temp = np.array(dwle2)
    dptlce3_temp = np.array(dptlce3)
    dsige3_temp = np.array(dsige3)
    dwle3_temp = np.array(dwle3)
    
    dptlc_sort = dptlc_temp[dptlc_temp.argsort()]
    dsig_sort = dsig_temp[dptlc_temp.argsort()]
    dwl_sort = dwl_temp[dptlc_temp.argsort()]
    dptlce_sort = dptlce_temp[dptlce_temp.argsort()]
    dsige_sort = dsige_temp[dptlce_temp.argsort()]
    dwle_sort = dwle_temp[dptlce_temp.argsort()]
    dptlce22_sort = dptlce22_temp[dptlce22_temp.argsort()]
    dsige22_sort = dsige22_temp[dptlce22_temp.argsort()]
    dwle22_sort = dwle22_temp[dptlce22_temp.argsort()]
    dptlce2_sort = dptlce2_temp[dptlce2_temp.argsort()]
    dsige2_sort = dsige2_temp[dptlce2_temp.argsort()]
    dwle2_sort = dwle2_temp[dptlce2_temp.argsort()]
    dptlce3_sort = dptlce3_temp[dptlce3_temp.argsort()]
    dsige3_sort = dsige3_temp[dptlce3_temp.argsort()]
    dwle3_sort = dwle3_temp[dptlce3_temp.argsort()]

    # plotting changes in growth rate and wavelength for various latent cooling and top of heating layer
    
    try:
        ev1 and ev2 and ev3 and ev4
    except:
        pass
    else:    
        if len(dptlc_sort) == len(dptlce22_sort) and len(dptlc_sort) == len(dptlce2_sort) and len(dptlc_sort) == len(dptlce3_sort):
            sigmatt = np.array([dsig_sort,dsige22_sort,dsige3_sort,dsige2_sort])
            wlmatt = np.array([dwl_sort,dwle22_sort,dwle3_sort,dwle2_sort])
            ev = np.array([ev1,ev2,ev3,ev4])

            norm = MidpointNormalize(midpoint=0.45)
            
            fig = plt.subplots(figsize=(3.3,5))
            
            sigplot = plt.contourf(ev,dptlce2_sort,abs(sigmatt.T),10,norm=norm,cmap=cm_gwrr)
            cbar = plt.colorbar(sigplot, orientation="horizontal", pad=.2)
            cbar.set_label('change in growth rate')
            CS = plt.contour(ev,dptlc_sort,abs(wlmatt.T),colors='k')
            #manual_locations = [(.15, .7),(.25,.75),(.4,.885)]
            plt.clabel(CS, CS.levels[1:-2], inline=True, fontsize=10)#, manual=manual_locations)
        #    plt.plot((dwl2_sort),dpblc_sort,'r')
            plt.ylabel('pressure at top of heating layer')
        #    plt.xlabel('change in growth rate (blue) and wavelength (red) from eps=0 to eps=15')
            plt.xlabel('relative cooling parameter $\mathregular{\gamma}$')
            #plt.ylim(.2,.4000001)
            gca().invert_yaxis()
            gca().tick_params(which='both', length=6, width=1)
            
            plt.show()

# -----------------------------------------------------------------------------

### comparing changes in growth rate and wavelength between epsilon1[0] and epsilon1[-1] for varying latent cooling and bottom of heating layer

def delta_growthrate_wavelength_vs_gamma_and_cloudbase():
    
    try:
        dsig2
    except:
        dpblc = ([])
        dsig2 = ([])
        dwl2 = ([])
        dpblce = ([])
        dsig2e = ([])
        dwl2e = ([])
        dpblce2 = ([])
        dsig2e2 = ([])
        dwl2e2 = ([])
        dpblce22 = ([])
        dsig2e22 = ([])
        dwl2e22 = ([])
        dpblce3 = ([])
        dsig2e3 = ([])
        dwl2e3 = ([])
                  
    if heating1 == True and heating2 == False and evap == False and .39 < ptlc < .41:
        ev1 = 0
        dpblc.extend([pblc])
        dsig2.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwl2.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.1 and .39 < ptlc < .41:
        ev2 = hblcstep-1
        dpblce.extend([pblc])
        dsig2e.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwl2e.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.2 and .39 < ptlc < .41:
        ev2 = hblcstep-1
        dpblce22.extend([pblc])
        dsig2e22.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwl2e22.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.3 and .39 < ptlc < .41:
        ev3 = hblcstep-1
        dpblce3.extend([pblc])
        dsig2e3.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwl2e3.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
    if heating1 == True and heating2 == False and evap == True and hblcstep == 1.5 and .39 < ptlc < .41:
        ev4 = hblcstep-1
        dpblce2.extend([pblc])
        dsig2e2.extend([sigmai_sorted[0,e2,np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0],-1]-sigmai_sorted[-1,e2,np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0],-1]])
        dwl2e2.extend([wl[np.argwhere(sigmai_sorted[0,e2,:,-1]==np.max(sigmai_sorted[0,e2,:,-1]))[0][0]]-wl[np.argwhere(sigmai_sorted[-1,e2,:,-1]==np.max(sigmai_sorted[-1,e2,:,-1]))[0][0]]])
        
    dpblc_temp = np.array(dpblc)
    dsig2_temp = np.array(dsig2)
    dwl2_temp = np.array(dwl2)
    dpblce_temp = np.array(dpblce)
    dsig2e_temp = np.array(dsig2e)
    dwl2e_temp = np.array(dwl2e)
    dpblce2_temp = np.array(dpblce2)
    dsig2e2_temp = np.array(dsig2e2)
    dwl2e2_temp = np.array(dwl2e2)
    dpblce22_temp = np.array(dpblce22)
    dsig2e22_temp = np.array(dsig2e22)
    dwl2e22_temp = np.array(dwl2e22)
    dpblce3_temp = np.array(dpblce3)
    dsig2e3_temp = np.array(dsig2e3)
    dwl2e3_temp = np.array(dwl2e3)
    
    dpblc_sort = dpblc_temp[dpblc_temp.argsort()]
    dsig2_sort = dsig2_temp[dpblc_temp.argsort()]
    dwl2_sort = dwl2_temp[dpblc_temp.argsort()]
    dpblce_sort = dpblce_temp[dpblce_temp.argsort()]
    dsig2e_sort = dsig2e_temp[dpblce_temp.argsort()]
    dwl2e_sort = dwl2e_temp[dpblce_temp.argsort()]
    dpblce22_sort = dpblce22_temp[dpblce22_temp.argsort()]
    dsig2e22_sort = dsig2e22_temp[dpblce22_temp.argsort()]
    dwl2e22_sort = dwl2e22_temp[dpblce22_temp.argsort()]
    dpblce2_sort = dpblce2_temp[dpblce2_temp.argsort()]
    dsig2e2_sort = dsig2e2_temp[dpblce2_temp.argsort()]
    dwl2e2_sort = dwl2e2_temp[dpblce2_temp.argsort()]
    dpblce3_sort = dpblce3_temp[dpblce3_temp.argsort()]
    dsig2e3_sort = dsig2e3_temp[dpblce3_temp.argsort()]
    dwl2e3_sort = dwl2e3_temp[dpblce3_temp.argsort()]
    
    
    # plotting changes in growth rate and wavelength for various latent cooling and bottom of heating layer
    
    if len(dpblc_sort) == len(dpblce22_sort) and len(dpblc_sort) == len(dpblce2_sort) and len(dpblc_sort) == len(dpblce3_sort):
        sigmat = np.array([dsig2_sort,dsig2e22_sort,dsig2e3_sort,dsig2e2_sort])
        wlmat = np.array([dwl2_sort,dwl2e22_sort,dwl2e3_sort,dwl2e2_sort])
        ev = np.array([ev1,ev2,ev3,ev4])
        
        fig = plt.subplots(figsize=(3.3,5))

        norm = MidpointNormalize(midpoint=0.6)
        
        sigplot = plt.contourf(ev,dpblc_sort,abs(sigmat.T),10,norm=norm,cmap=cm_gwrr)
        cbar = plt.colorbar(sigplot, orientation="horizontal", pad=.2)
        cbar.set_label('change in growth rate')
        CS = plt.contour(ev,dpblc_sort,abs(wlmat.T),colors='k')
        #manual_locations = [(.15, .7),(.25,.75),(.4,.885)]
        plt.clabel(CS, CS.levels[:], inline=True, fontsize=10)#, manual=manual_locations)
    #    plt.plot((dwl2_sort),dpblc_sort,'r')
        plt.ylabel('pressure at bottom of heating layer')
    #    plt.xlabel('change in growth rate (blue) and wavelength (red) from eps=0 to eps=15')
        plt.xlabel('relative cooling parameter $\mathregular{\gamma}$')
        #plt.ylim(.6,.9000001)
        gca().invert_yaxis()
        gca().tick_params(which='both', length=6, width=1)
        
        plt.show()
        
# -----------------------------------------------------------------------------

### normalising variables in order to compare the absolute value of e.g. vertical velocity

def normalise_variables():

    # what should be the normalisation constant?

    norm_t = False				# potential energy (temperature squared)?
    if norm_t == True:
        norm_t_int = True		# integrated potential energy?
    norm_v = False				# kinetic energy (meridional velocity squared)?
    if norm_v == True:
        norm_v_int = True		# integrated kinetic energy?
    norm_energy = True
    if norm_energy == True:
        norm_energy_int = True
    norm_gr = False				# growth rate (to the power of something)?
    norm_psi = False			# minimum (absolute) pressure?
    norm_psis = False			# surface pressure?
    norm_wcb = False				# omega @ bottom of heating layer?

    PVnorm = True				# plot normalised PV?

    # saving useful variables from different runs:

    normalise = True
    
    if normalise == True:
        if heating1 == False:
            psi_eady = psi_maxunstab[eps1_index,eps2_index]
            w_eady = w_maxunstab[eps1_index,eps2_index]
            t_eady = tempcalc(psi_maxunstab)[eps1_index]
            v_eady = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_eady = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_eady = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_eady = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_eady = h1
        if heating1 == True and evap == False:
            psi_noevap = psi_maxunstab[eps1_index,eps2_index]
            w_noevap = w_maxunstab[eps1_index,eps2_index]
            t_noevap = tempcalc(psi_maxunstab)[eps1_index]
            v_noevap = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_noevap = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_noevap = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_noevap = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_noevap = h1
        if heating1 == True and hblcstep == 1.1:
            psi_evap01 = psi_maxunstab[eps1_index,eps2_index]
            w_evap01 = w_maxunstab[eps1_index,eps2_index]
            t_evap01 = tempcalc(psi_maxunstab)[eps1_index]
            v_evap01 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_evap01 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0] 
            #wl_evap01 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_evap01 = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_evap01 = h1
        if heating1 == True and hblcstep == 1.2:
            psi_evap02 = psi_maxunstab[eps1_index,eps2_index]
            w_evap02 = w_maxunstab[eps1_index,eps2_index]
            t_evap02 = tempcalc(psi_maxunstab)[eps1_index]
            v_evap02 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_evap02 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap02 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_evap02 = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_evap02 = h1
        if heating1 == True and hblcstep == 1.3:
            psi_evap03 = psi_maxunstab[eps1_index,eps2_index]
            w_evap03 = w_maxunstab[eps1_index,eps2_index]
            t_evap03 = tempcalc(psi_maxunstab)[eps1_index]
            v_evap03 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_evap03 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap03 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_evap03 = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_evap03 = h1
        if heating1 == True and hblcstep == 1.4:
            psi_evap04 = psi_maxunstab[eps1_index,eps2_index]
            w_evap04 = w_maxunstab[eps1_index,eps2_index]
            t_evap04 = tempcalc(psi_maxunstab)[eps1_index]
            v_evap04 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_evap04 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap04 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_evap04 = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_evap04 = h1
        if heating1 == True and hblcstep == 1.45:
            psi_evap045 = psi_maxunstab[eps1_index,eps2_index]
            w_evap045 = w_maxunstab[eps1_index,eps2_index]
            t_evap045 = tempcalc(psi_maxunstab)[eps1_index]
            v_evap045 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_evap045 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap045 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_evap045 = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
        if heating1 == True and hblcstep == 1.5:
            psi_evap05 = psi_maxunstab[eps1_index,eps2_index]
            w_evap05 = w_maxunstab[eps1_index,eps2_index]
            t_evap05 = tempcalc(psi_maxunstab)[eps1_index]
            v_evap05 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_evap05 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap05 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_evap05 = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_evap05 = h1
        if heating1 == True and hblcstep == 1.6:
            psi_evap06 = psi_maxunstab[eps1_index,eps2_index]
            w_evap06 = w_maxunstab[eps1_index,eps2_index]
            t_evap06 = tempcalc(psi_maxunstab)[eps1_index]
            v_evap06 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_evap06 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap06 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_evap06 = PV_u[eps1_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_evap06 = h1

        if heating2 == True and epsilon2[eps2_index] == 1:
            psi_sf = psi_maxunstab[eps1_index,eps2_index]
            w_sf = w_maxunstab[eps1_index,eps2_index]
            t_sf = tempcalc(psi_maxunstab)[eps1_index]
            v_sf = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_sf = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            PV_sf = PV_u[eps1_index,eps2_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_sf = h1
        if heating2 == True and epsilon2[eps2_index] == (1-1j)/np.sqrt(2):
            psi_sf1 = psi_maxunstab[eps1_index,eps2_index]
            w_sf1 = w_maxunstab[eps1_index,eps2_index]
            t_sf1 = tempcalc(psi_maxunstab)[eps1_index]
            v_sf1 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_sf1 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0] 
            #wl_evap01 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_sf1 = PV_u[eps1_index,eps2_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_sf1 = h1
        if heating2 == True and epsilon2[eps2_index] == -1j:
            psi_sf2 = psi_maxunstab[eps1_index,eps2_index]
            w_sf2 = w_maxunstab[eps1_index,eps2_index]
            t_sf2 = tempcalc(psi_maxunstab)[eps1_index]
            v_sf2 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_sf2 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap02 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_sf2 = PV_u[eps1_index,eps2_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_sf2 = h1
        if heating2 == True and epsilon2[eps2_index] == 10:
            psi_sf3 = psi_maxunstab[eps1_index,eps2_index]
            w_sf3 = w_maxunstab[eps1_index,eps2_index]
            t_sf3 = tempcalc(psi_maxunstab)[eps1_index]
            v_sf3 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_sf3 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap03 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_sf3 = PV_u[eps1_index,eps2_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_sf3 = h1
        if heating2 == True and epsilon2[eps2_index] == 10*(1-1j)/np.sqrt(2):
            psi_sf4 = psi_maxunstab[eps1_index,eps2_index]
            w_sf4 = w_maxunstab[eps1_index,eps2_index]
            t_sf4 = tempcalc(psi_maxunstab)[eps1_index]
            v_sf4 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_sf4 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap04 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_sf4 = PV_u[eps1_index,eps2_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_sf4 = h1
        if heating2 == True and epsilon2[eps2_index] == -10j:
            psi_sf5 = psi_maxunstab[eps1_index,eps2_index]
            w_sf5 = w_maxunstab[eps1_index,eps2_index]
            t_sf5 = tempcalc(psi_maxunstab)[eps1_index]
            v_sf5 = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
            gr_sf5 = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
            #wl_evap05 = wl[i_maxunstab[eps1_index,eps2_index]]
            PV_sf5 = PV_u[eps1_index,eps2_index].max(axis=1)#simps(PV,kx)#/(2*np.pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            h1_sf5 = h1
        
# -----------------------------------------------------------------------------

def plot_normalised_variables_vertical():

    if norm_v == True or norm_t == True or norm_energy == True or PVnorm == True:
        fig, (ax1,ax2,ax3,ax4) = plt.subplots(4, figsize=(6,10))
    else:
        fig, (ax1,ax2) = plt.subplots(2, figsize=(6,6))
    #ax1.set_xlabel('Phase angle (rad)')
    #ax1.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    #ax1.set_xticklabels(['-2$\mathregular{\pi}$','-$\mathregular{\pi}$', '0', '$\mathregular{\pi}$', '2$\mathregular{\pi}$',])
    #ax2 = ax1.twiny()
    ax1.axhline(0.9, c='grey')
    try:
        psi_eady
    except NameError:
        print ('psi_eady not defined')
    else:
        if norm_t == True:
            if norm_t_int == False:
                ax1.plot(abs(w_eady)/max(abs(t_eady**2)),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
                ax2.plot(abs(psi_eady)/max(abs(t_eady**2)),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
                ax3.plot(abs(t_eady**2),p[:nrws], 'grey', linewidth=ms, label='Eady')
            if norm_t_int == True:
                ax1.plot(abs(w_eady)/max(simps(abs(t_eady**2),p[:nrws])),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
                ax2.plot(abs(psi_eady)/max(simps(abs(t_eady**2),p[:nrws])),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
                ax3.plot(abs(t_eady**2),p[:nrws], 'grey', linewidth=ms, label='Eady')            
        if norm_v == True:
            if norm_v_int == False:
                ax1.plot(abs(w_eady)/max(abs(v_eady**2)),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
                ax2.plot(abs(psi_eady)/max(abs(v_eady**2)),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
                ax3.plot(abs(v_eady**2),p[:nrws], 'grey', linewidth=ms, label='Eady')
            if norm_v_int == True:
                ax1.plot(abs(w_eady)/(simps(abs(v_eady**2),p[:nrws])),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
                ax2.plot(abs(psi_eady)/(simps(abs(v_eady**2),p[:nrws])),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
                ax3.plot(abs(v_eady**2),p[:nrws], 'grey', linewidth=ms, label='Eady')  
        if norm_energy == True:
            if norm_energy_int == False:
                ax1.plot(abs(w_eady)/max(abs(v_eady**2+t_eady**2/S[:nrws])),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
                ax2.plot(abs(psi_eady)/max(abs(v_eady**2+t_eady**2/S[:nrws])),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
                ax3.plot(abs(v_eady**2+t_eady**2/S[:nrws]),p[:nrws], 'grey', linewidth=ms, label='Eady')
            if norm_energy_int == True:
                ax1.plot(abs(w_eady)/(simps(abs(v_eady**2+t_eady**2/S[:nrws]),p[:nrws])),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
                ax2.plot(abs(psi_eady)/(simps(abs(v_eady**2+t_eady**2/S[:nrws]),p[:nrws])),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
                if PVnorm == False:
                    ax3.plot(abs(v_eady**2+t_eady**2/S[:nrws]),p[:nrws], 'grey', linewidth=ms, label='Eady')  
                if PVnorm == True:
                    ax3.scatter(abs(PV_eady)/(simps(abs(v_eady**2+t_eady**2/S[:nrws]),p[:nrws])),p[:nrws], c='grey', linestyle='--', linewidth=0,s=30, label='Eady')
        if norm_gr == True:
            ax1.plot(abs(w_eady)*(abs(gr_eady)**10),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
            ax2.plot(abs(psi_eady)*(abs(gr_eady)**10),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
        if norm_psi == True:
            ax1.plot(abs(w_eady)/min(abs(psi_eady)),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
            ax2.plot(abs(psi_eady)/min(abs(psi_eady)),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
            if PVnorm == True:
                ax3.scatter(abs(PV_eady)/min(abs(psi_eady)),p[:nrws], c='grey', linestyle='--', linewidth=0,s=30, label='Eady')
        if norm_psis == True:
            ax1.plot(abs(w_eady)/(abs(psi_eady[-1])),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
            ax2.plot(abs(psi_eady)/(abs(psi_eady[-1])),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
        if norm_wcb == True:
            ax1.plot(abs(w_eady)/(abs(w_eady[jtml])),p[:nrws], c='grey', linestyle='--',linewidth=ms, label='Eady')
            ax2.plot(abs(psi_eady)/(abs(w_eady[jtml])),p[:nrws], c='grey', linestyle='--', linewidth=ms, label='Eady')
    try:
        psi_noevap
    except NameError:
        print ('psi_noevap not defined')
    else:
        if norm_t == True:
            if norm_t_int == False:
                ax1.plot(abs(w_noevap)/max(abs(t_noevap**2)),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax2.plot(abs(psi_noevap)/max(abs(t_noevap**2)),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax3.plot(abs(t_noevap**2),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')#/max(abs(t_noevap**2))
            if norm_t_int == True:
                ax1.plot(abs(w_noevap)/(simps(abs(t_noevap**2),p[:nrws])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax2.plot(abs(psi_noevap)/(simps(abs(t_noevap**2),p[:nrws])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax3.plot(abs(t_noevap**2),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')            
        if norm_v == True:
            if norm_v_int == False:
                ax1.plot(abs(w_noevap)/max(abs(v_noevap**2)),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax2.plot(abs(psi_noevap)/max(abs(v_noevap**2)),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax3.plot(abs(v_noevap**2),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')#/max(abs(t_noevap**2))
            if norm_v_int == True:
                ax1.plot(abs(w_noevap)/(simps(abs(v_noevap**2),p[:nrws])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax2.plot(abs(psi_noevap)/(simps(abs(v_noevap**2),p[:nrws])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax3.plot(abs(v_noevap**2),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')            
        if norm_energy == True:
            if norm_energy_int == False:
                ax1.plot(abs(w_noevap)/max(abs(v_noevap**2+t_noevap**2/S[:nrws])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax2.plot(abs(psi_noevap)/max(abs(v_noevap**2+t_noevap**2/S[:nrws])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax3.plot(abs(v_noevap**2+t_noevap**2/S[:nrws]),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')#/max(abs(t_noevap**2))
            if norm_energy_int == True:
                ax1.plot(abs(w_noevap)/(simps(abs(v_noevap**2+t_noevap**2/S[:nrws]),p[:nrws])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                ax2.plot(abs(psi_noevap)/(simps(abs(v_noevap**2+t_noevap**2/S[:nrws]),p[:nrws])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
                if PVnorm == False:
                    ax3.plot(abs(v_noevap**2+t_noevap**2/S[:nrws]),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')            
                if PVnorm == True:
                    ax3.scatter(abs(PV_noevap)/simps(abs(v_noevap**2+t_noevap**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[0], linewidth=0, label='  0%')                                           
                ax4.plot(epsilon1[eps1_index]/2*h1_noevap[eps1_index,:nrws]*abs(w_noevap[jblc])/simps(abs(v_noevap**2+t_noevap**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[0], linewidth=ms, label='0.0')
        if norm_gr == True:
            ax1.plot(abs(w_noevap)*(abs(gr_noevap)**10),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
            ax2.plot(abs(psi_noevap)*(abs(gr_noevap)**10),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
        if norm_psi == True:
            ax1.plot(abs(w_noevap)/min(abs(psi_noevap)),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
            ax2.plot(abs(psi_noevap)/min(abs(psi_noevap)),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
            if PVnorm == True:
                ax3.scatter(abs(PV_noevap)/min(abs(psi_noevap)),p[:nrws], c=c_blues[0], linewidth=0,s=30, label='  0%')
        if norm_psis == True:
            ax1.plot(abs(w_noevap)/(abs(psi_noevap[-1])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
            ax2.plot(abs(psi_noevap)/(abs(psi_noevap[-1])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
        if norm_wcb == True:
            ax1.plot(abs(w_noevap)/(abs(w_noevap[jtml])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
            ax2.plot(abs(psi_noevap)/(abs(w_noevap[jtml])),p[:nrws], c=c_blues[0], linewidth=ms, label='  0%')
    try:
        psi_evap01
    except NameError:
        print ('psi_evap01 not defined')
    else:
        if norm_t == True:
            if norm_t_int == False:
                ax1.plot(abs(w_evap01)/max(abs(t_evap01**2)),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax2.plot(abs(psi_evap01)/max(abs(t_evap01**2)),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax3.plot(abs(t_evap01**2),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
            if norm_t_int == True:
                ax1.plot(abs(w_evap01)/simps(abs(t_evap01**2),p[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax2.plot(abs(psi_evap01)/simps(abs(t_evap01**2),p[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax3.plot(abs(t_evap01**2),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
        if norm_v == True:
            if norm_v_int == False:
                ax1.plot(abs(w_evap01)/max(abs(v_evap01**2)),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax2.plot(abs(psi_evap01)/max(abs(v_evap01**2)),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax3.plot(abs(v_evap01**2),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
            if norm_v_int == True:
                ax1.plot(abs(w_evap01)/simps(abs(v_evap01**2),p[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax2.plot(abs(psi_evap01)/simps(abs(v_evap01**2),p[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax3.plot(abs(v_evap01**2),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
        if norm_energy == True:
            if norm_energy_int == False:
                ax1.plot(abs(w_evap01)/max(abs(v_evap01**2+t_evap01**2/S[:nrws])),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax2.plot(abs(psi_evap01)/max(abs(v_evap01**2+t_evap01**2/S[:nrws])),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax3.plot(abs(v_evap01**2+t_evap01**2/S[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
            if norm_energy_int == True:
                ax1.plot(abs(w_evap01)/simps(abs(v_evap01**2+t_evap01**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                ax2.plot(abs(psi_evap01)/simps(abs(v_evap01**2+t_evap01**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                if PVnorm == False:
                    ax3.plot(abs(v_evap01**2+t_evap01**2/S[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
                if PVnorm == True:
                    ax3.scatter(abs(PV_evap01)/simps(abs(v_evap01**2+t_evap01**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[1], linewidth=0, label='10%')
                ax4.plot(epsilon1[eps1_index]/2*h1_evap01[eps1_index,:nrws]*abs(w_evap01[jblc])/simps(abs(v_evap01**2+t_evap01**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[1], linewidth=ms, label='0.1')                                           
        if norm_gr == True:
            ax1.plot(abs(w_evap01)*(abs(gr_evap01)**10),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
            ax2.plot(abs(psi_evap01)*(abs(gr_evap01)**10),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
        if norm_psi == True:
            ax1.plot(abs(w_evap01)/min(abs(psi_evap01)),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
            ax2.plot(abs(psi_evap01)/min(abs(psi_evap01)),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
            if PVnorm == True:
                ax3.scatter(abs(PV_evap01)/min(abs(psi_evap01)),p[:nrws], c=c_blues[1],s=30, linewidth=0, label='10%')                
        if norm_psis == True:
            ax1.plot(abs(w_evap01)/(abs(psi_evap01[-1])),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
            ax2.plot(abs(psi_evap01)/(abs(psi_evap01[-1])),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
        if norm_wcb == True:
            ax1.plot(abs(w_evap01)/(abs(w_evap01[jtml])),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
            ax2.plot(abs(psi_evap01)/(abs(w_evap01[jtml])),p[:nrws], c=c_blues[1], linewidth=ms, label='10%')
    try:
        psi_evap02
    except NameError:
        print ('psi_evap02 not defined')
    else:
        if norm_t == True:
            if norm_t_int == False:
                ax1.plot(abs(w_evap02)/max(abs(t_evap02**2)),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax2.plot(abs(psi_evap02)/max(abs(t_evap02**2)),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax3.plot(abs(t_evap02**2),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')#/max(abs(t_evap02**2))
            if norm_t_int == True:
                ax1.plot(abs(w_evap02)/simps(abs(t_evap02**2),p[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax2.plot(abs(psi_evap02)/simps(abs(t_evap02**2),p[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax3.plot(abs(t_evap02**2),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')#/max(abs(t_evap02**2))
        if norm_v == True:
            if norm_v_int == False:
                ax1.plot(abs(w_evap02)/max(abs(v_evap02**2)),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax2.plot(abs(psi_evap02)/max(abs(v_evap02**2)),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax3.plot(abs(v_evap02**2),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')#/max(abs(t_evap02**2))
            if norm_v_int == True:
                ax1.plot(abs(w_evap02)/simps(abs(v_evap02**2),p[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax2.plot(abs(psi_evap02)/simps(abs(v_evap02**2),p[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax3.plot(abs(v_evap02**2),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')#/max(abs(t_evap02**2))
        if norm_energy == True:
            if norm_energy_int == False:
                ax1.plot(abs(w_evap02)/max(abs(v_evap02**2+t_evap02**2/S[:nrws])),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax2.plot(abs(psi_evap02)/max(abs(v_evap02**2+t_evap02**2/S[:nrws])),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax3.plot(abs(v_evap02**2+t_evap02**2/S[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')#/max(abs(t_evap02**2))
            if norm_energy_int == True:
                ax1.plot(abs(w_evap02)/simps(abs(v_evap02**2+t_evap02**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                ax2.plot(abs(psi_evap02)/simps(abs(v_evap02**2+t_evap02**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
                if PVnorm == False:
                    ax3.plot(abs(v_evap02**2+t_evap02**2/S[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')#/max(abs(t_evap02**2))
                if PVnorm == True:
                    ax3.scatter(abs(PV_evap02)/simps(abs(v_evap02**2+t_evap02**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[2], linewidth=0, label='20%')
                ax4.plot(epsilon1[eps1_index]/2*h1_evap02[eps1_index,:nrws]*abs(w_evap02[jblc])/simps(abs(v_evap02**2+t_evap02**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[2], linewidth=ms, label='0.2')                                           
        if norm_gr == True:
            ax1.plot(abs(w_evap02)*(abs(gr_evap02)**10),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
            ax2.plot(abs(psi_evap02)*(abs(gr_evap02)**10),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
        if norm_psi == True:
            ax1.plot(abs(w_evap02)/min(abs(psi_evap02)),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
            ax2.plot(abs(psi_evap02)/min(abs(psi_evap02)),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
            if PVnorm == True:
                ax3.scatter(abs(PV_evap02)/min(abs(psi_evap02)),p[:nrws], c=c_blues[2], linewidth=0,s=30, label='20%')                
        if norm_psis == True:
            ax1.plot(abs(w_evap02)/(abs(psi_evap02[-1])),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
            ax2.plot(abs(psi_evap02)/(abs(psi_evap02[-1])),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
        if norm_wcb == True:
            ax1.plot(abs(w_evap02)/(abs(w_evap02[jtml])),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
            ax2.plot(abs(psi_evap02)/(abs(w_evap02[jtml])),p[:nrws], c=c_blues[2], linewidth=ms, label='20%')
    try:
        psi_evap03
    except NameError:
        print ('psi_evap03 not defined')
    else:
        if norm_t == True:
            if norm_t_int == False:
                ax1.plot(abs(w_evap03)/max(abs(t_evap03**2)),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax2.plot(abs(psi_evap03)/max(abs(t_evap03**2)),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax3.plot(abs(t_evap03**2),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
            if norm_t_int == True:
                ax1.plot(abs(w_evap03)/simps(abs(t_evap03**2),p[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax2.plot(abs(psi_evap03)/simps(abs(t_evap03**2),p[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax3.plot(abs(t_evap03**2),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
        if norm_v == True:
            if norm_v_int == False:
                ax1.plot(abs(w_evap03)/max(abs(v_evap03**2)),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax2.plot(abs(psi_evap03)/max(abs(v_evap03**2)),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax3.plot(abs(v_evap03**2),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
            if norm_v_int == True:
                ax1.plot(abs(w_evap03)/simps(abs(v_evap03**2),p[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax2.plot(abs(psi_evap03)/simps(abs(v_evap03**2),p[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax3.plot(abs(v_evap03**2),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
        if norm_energy == True:
            if norm_energy_int == False:
                ax1.plot(abs(w_evap03)/max(abs(v_evap03**2+t_evap03**2/S[:nrws])),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax2.plot(abs(psi_evap03)/max(abs(v_evap03**2+t_evap03**2/S[:nrws])),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax3.plot(abs(v_evap03**2+t_evap03**2/S[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
            if norm_energy_int == True:
                ax1.plot(abs(w_evap03)/simps(abs(v_evap03**2+t_evap03**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                ax2.plot(abs(psi_evap03)/simps(abs(v_evap03**2+t_evap03**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                if PVnorm == False:
                    ax3.plot(abs(v_evap03**2+t_evap03**2/S[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
                if PVnorm == True:
                    ax3.scatter(abs(PV_evap03)/simps(abs(v_evap03**2+t_evap03**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[3], linewidth=0, label='30%')
                ax4.plot(epsilon1[eps1_index]/2*h1_evap03[eps1_index,:nrws]*abs(w_evap03[jblc])/simps(abs(v_evap03**2+t_evap03**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[3], linewidth=ms, label='0.3')
        if norm_gr == True:
            ax1.plot(abs(w_evap03)*(abs(gr_evap03)**10),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
            ax2.plot(abs(psi_evap03)*(abs(gr_evap03)**10),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
        if norm_psi == True:
            ax1.plot(abs(w_evap03)/min(abs(psi_evap03)),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
            ax2.plot(abs(psi_evap03)/min(abs(psi_evap03)),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
            if PVnorm == True:
                ax3.scatter(abs(PV_evap03)/min(abs(psi_evap03)),p[:nrws], c=c_blues[3],s=30, linewidth=0, label='30%')
        if norm_psis == True:
            ax1.plot(abs(w_evap03)/(abs(psi_evap03[-1])),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
            ax2.plot(abs(psi_evap03)/(abs(psi_evap03[-1])),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
        if norm_wcb == True:
            ax1.plot(abs(w_evap03)/(abs(w_evap03[jtml])),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
            ax2.plot(abs(psi_evap03)/(abs(w_evap03[jtml])),p[:nrws], c=c_blues[3], linewidth=ms, label='30%')
    try:
        psi_evap04
    except NameError:
        print ('psi_evap04 not defined')
    else:
        if norm_t == True:
            if norm_t_int == False:
                ax1.plot(abs(w_evap04)/max(abs(t_evap04**2)),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax2.plot(abs(psi_evap04)/max(abs(t_evap04**2)),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax3.plot(abs(t_evap04**2),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')#/max(abs(t_evap04**2))
            if norm_t_int == True:
                ax1.plot(abs(w_evap04)/simps(abs(t_evap04**2),p[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax2.plot(abs(psi_evap04)/simps(abs(t_evap04**2),p[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax3.plot(abs(t_evap04**2),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')#/max(abs(t_evap04**2))
        if norm_v == True:
            if norm_v_int == False:
                ax1.plot(abs(w_evap04)/max(abs(v_evap04**2)),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax2.plot(abs(psi_evap04)/max(abs(v_evap04**2)),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax3.plot(abs(v_evap04**2),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')#/max(abs(t_evap04**2))
            if norm_v_int == True:
                ax1.plot(abs(w_evap04)/simps(abs(v_evap04**2),p[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax2.plot(abs(psi_evap04)/simps(abs(v_evap04**2),p[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax3.plot(abs(v_evap04**2),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')#/max(abs(t_evap04**2))
        if norm_energy == True:
            if norm_energy_int == False:
                ax1.plot(abs(w_evap04)/max(abs(v_evap04**2+t_evap04**2/S[:nrws])),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax2.plot(abs(psi_evap04)/max(abs(v_evap04**2+t_evap04**2/S[:nrws])),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax3.plot(abs(v_evap04**2+t_evap04**2/S[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')#/max(abs(t_evap04**2))
            if norm_energy_int == True:
                ax1.plot(abs(w_evap04)/simps(abs(v_evap04**2+t_evap04**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                ax2.plot(abs(psi_evap04)/simps(abs(v_evap04**2+t_evap04**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
                if PVnorm == False:
                    ax3.plot(abs(v_evap04**2+t_evap04**2/S[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')#/max(abs(t_evap04**2))
                if PVnorm == True:
                    ax3.scatter(abs(PV_evap04)/simps(abs(v_evap04**2+t_evap04**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[4], linewidth=0, label='40%')
                ax4.plot(epsilon1[eps1_index]/2*h1_evap04[eps1_index,:nrws]*abs(w_evap04[jblc])/simps(abs(v_evap04**2+t_evap04**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[4], linewidth=ms, label='0.4')
        if norm_gr == True:
            ax1.plot(abs(w_evap04)*(abs(gr_evap04)**10),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
            ax2.plot(abs(psi_evap04)*(abs(gr_evap04)**10),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
        if norm_psi == True:
            ax1.plot(abs(w_evap04)/min(abs(psi_evap04)),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
            ax2.plot(abs(psi_evap04)/min(abs(psi_evap04)),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
            if PVnorm == True:
                ax3.scatter(abs(PV_evap04)/min(abs(psi_evap04)),p[:nrws], c=c_blues[4], linewidth=0,s=30,edgecolors='k', label='40%')                
        if norm_psis == True:
            ax1.plot(abs(w_evap04)/(abs(psi_evap04[-1])),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
            ax2.plot(abs(psi_evap04)/(abs(psi_evap04[-1])),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
        if norm_wcb == True:
            ax1.plot(abs(w_evap04)/(abs(w_evap04[jtml])),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
            ax2.plot(abs(psi_evap04)/(abs(w_evap04[jtml])),p[:nrws], c=c_blues[4], linewidth=ms, label='40%')
    try:
        psi_evap05
    except NameError:
        print ('psi_evap05 not defined')
    else:
        if norm_t == True:
            if norm_t_int == False:
                ax1.plot(abs(w_evap05)/max(abs(t_evap05**2)),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax2.plot(abs(psi_evap05)/max(abs(t_evap05**2)),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax3.plot(abs(t_evap05**2),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
            if norm_t_int == True:
                ax1.plot(abs(w_evap05)/simps(abs(t_evap05**2),p[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax2.plot(abs(psi_evap05)/simps(abs(t_evap05**2),p[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax3.plot(abs(t_evap05**2),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
        if norm_v == True:
            if norm_v_int == False:
                ax1.plot(abs(w_evap05)/max(abs(v_evap05**2)),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax2.plot(abs(psi_evap05)/max(abs(v_evap05**2)),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax3.plot(abs(v_evap05**2),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
            if norm_v_int == True:
                ax1.plot(abs(w_evap05)/simps(abs(v_evap05**2),p[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax2.plot(abs(psi_evap05)/simps(abs(v_evap05**2),p[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax3.plot(abs(v_evap05**2),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
        if norm_energy == True:
            if norm_energy_int == False:
                ax1.plot(abs(w_evap05)/max(abs(v_evap05**2+t_evap05**2/S[:nrws])),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax2.plot(abs(psi_evap05)/max(abs(v_evap05**2+t_evap05**2/S[:nrws])),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax3.plot(abs(v_evap05**2+t_evap05**2/S[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
            if norm_energy_int == True:
                ax1.plot(abs(w_evap05)/simps(abs(v_evap05**2+t_evap05**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                ax2.plot(abs(psi_evap05)/simps(abs(v_evap05**2+t_evap05**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                if PVnorm == False:
                    ax3.plot(abs(v_evap05**2+t_evap05**2/S[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
                if PVnorm == True:
                    ax3.scatter(abs(PV_evap05)/simps(abs(v_evap05**2+t_evap05**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[5], linewidth=0, label='50%')
                ax4.plot(epsilon1[eps1_index]/2*h1_evap05[eps1_index,:nrws]*abs(w_evap05[jblc])/simps(abs(v_evap05**2+t_evap05**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[5], linewidth=ms, label='0.5')
        if norm_gr == True:
            ax1.plot(abs(w_evap05)*(abs(gr_evap05)**10),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
            ax2.plot(abs(psi_evap05)*(abs(gr_evap05)**10),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
        if norm_psi == True:
            ax1.plot(abs(w_evap05)/min(abs(psi_evap05)),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
            ax2.plot(abs(psi_evap05)/min(abs(psi_evap05)),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
            if PVnorm == True:
                ax3.scatter(abs(PV_evap05)/min(abs(psi_evap05)),p[:nrws], c=c_blues[5], linewidth=0,s=30, label='50%')                
        if norm_psis == True:
            ax1.plot(abs(w_evap05)/(abs(psi_evap05[-1])),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
            ax2.plot(abs(psi_evap05)/(abs(psi_evap05[-1])),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
        if norm_wcb == True:
            ax1.plot(abs(w_evap05)/(abs(w_evap05[jtml])),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
            ax2.plot(abs(psi_evap05)/(abs(w_evap05[jtml])),p[:nrws], c=c_blues[5], linewidth=ms, label='50%')
    try:
        psi_evap06
    except NameError:
        print ('psi_evap06 not defined')
    else:
        if norm_energy == True:
            if norm_energy_int == True:
                ax1.plot(abs(w_evap06)/simps(abs(v_evap06**2+t_evap06**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
                ax2.plot(abs(psi_evap06)/simps(abs(v_evap06**2+t_evap06**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
                if PVnorm == False:
                    ax3.plot(abs(v_evap06**2+t_evap06**2/S[:nrws]),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
                if PVnorm == True:
                    ax3.scatter(abs(PV_evap06)/simps(abs(v_evap06**2+t_evap06**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[6], linewidth=0, label='60%')
                ax4.plot(epsilon1[eps1_index]/2*h1_evap06[eps1_index,:nrws]*abs(w_evap06[jblc])/simps(abs(v_evap06**2+t_evap06**2/S[:nrws]),p[:nrws]),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
        if norm_psi == True:
            ax1.plot(abs(w_evap06)/min(abs(psi_evap06)),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
            ax2.plot(abs(psi_evap06)/min(abs(psi_evap06)),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
            if PVnorm == True:
                ax3.scatter(abs(PV_evap06)/min(abs(psi_evap06)),p[:nrws], c=c_blues[6], linewidth=0,s=30, label='60%')                
        if norm_psis == True:
            ax1.plot(abs(w_evap06)/(abs(psi_evap06[-1])),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
            ax2.plot(abs(psi_evap06)/(abs(psi_evap06[-1])),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
        if norm_wcb == True:
            ax1.plot(abs(w_evap06)/(abs(w_evap06[jtml])),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
            ax2.plot(abs(psi_evap06)/(abs(w_evap06[jtml])),p[:nrws], c=c_blues[6], linewidth=ms, label='60%')
    ax1.set_xlabel('amplitude omega (normalized)')
    ax2.set_xlabel('amplitude psi (normalized)')
    ax1.set_ylabel('pressure')
    ax2.set_ylabel('pressure')
    ax1.invert_yaxis()
    ax2.invert_yaxis()
    if norm_t == True or norm_v == True or norm_energy == True or PVnorm == True:
        ax3.set_ylabel('pressure')
        ax3.invert_yaxis()
        ax4.set_ylabel('pressure')
        ax4.invert_yaxis()
    if norm_t == True:
        ax3.set_xlabel('amplitude potential energy')
    if norm_v == True:
        ax3.set_xlabel('amplitude kinetic energy')
    if norm_energy == True:
        ax3.set_xlabel('amplitude total energy')
    if PVnorm == True:
        ax3.set_xlabel('amplitude PV (normalized)')
        ax4.set_xlabel('normalized amplitude of diabatic heating')
        #if norm_energy == True:
        #    ax3.set_xlim(0,1.1*max(max(abs(PV_noevap)/simps(abs(v_noevap**2+t_noevap**2/S[:nrws]),p[:nrws])),max(abs(PV_evap02)/simps(abs(v_evap02**2+t_evap02**2/S[:nrws]),p[:nrws])),max(abs(PV_evap04)/simps(abs(v_evap04**2+t_evap04**2/S[:nrws]),p[:nrws]))))
        ax3.set_ylim(1,.1)
        ax4.set_ylim(1,.1)
    ax4.legend(bbox_to_anchor=(0.5,-0.4), loc='upper center',
               ncol=6, fancybox=True, prop={'size':12}) 

    plt.tight_layout()
    plt.show()
    
# -----------------------------------------------------------------------------

### comparing normalised PV anomalies and vertical velocity for varying latent cooling

def prepare_normalised_PV_w_vs_gamma():
    
    global evap_vec,PVt_vec,PVb_vec,w_vec,wd_vec,wh_vec,wc_vec,wf_vec,norm_energy_vec,h1_vec
    
    try:
        norm_energy_vec
    except:
        evap_vec = ([])
        PVt_vec = ([])
        PVb_vec = ([])
        PVmt_vec = ([])
        PVmb_vec = ([])
        PVtbl_vec = ([])
        PVtsf_vec = ([])
        w_vec = ([])
        wd_vec = ([])
        wh_vec = ([])
        wc_vec = ([])
        wf_vec = ([])
        norm_energy_vec = ([])
        norm_kenergy_vec = ([])
        norm_penergy_vec = ([])
        norm_psi_vec = ([])
        norm_psis_vec = ([])
        h1_vec = ([])        

    t = tempcalc(psi_maxunstab)[eps1_index]
    v = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
    #PV_sf = PV_u[eps1_index].max(axis=1)
    
    evap_vec.extend([hblcstep])
    PVt_vec.extend([np.max(abs(PV_u[eps1_index].max(axis=1)[jtlc-1:jtlc+2]))])
    PVb_vec.extend([np.max(abs(PV_u[eps1_index].max(axis=1)[jblc-1:jblc+2]))])
    w_vec.extend([(w_maxunstab[eps1_index,eps2_index,jblc])])
    wd_vec.extend([(wd[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],jtml])])
    wh_vec.extend([(wh[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],jtml])])
    wc_vec.extend([(wc[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],jtml])])
    wf_vec.extend([(wf[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],jtml])])
    norm_energy_vec.extend([simps(abs(v**2+t**2/S[:nrws]),p[:nrws])])
    h1_vec.extend([h1[eps1_index,:nrws]])

# -----------------------------------------------------------------------------

def plot_normalised_PV_w_vs_gamma():
        
    evap_vec_temp = np.array(evap_vec)
    PVt_vec_temp = np.array(PVt_vec)
    PVb_vec_temp = np.array(PVb_vec)
    #PVmt_vec_temp = np.array(PVmt_vec)
    #PVmb_vec_temp = np.array(PVmb_vec)
    #PVtbl_vec_temp = np.array(PVtbl_vec)
    #PVtsf_vec_temp = np.array(PVtsf_vec)
    w_vec_temp = np.array(w_vec)
    wd_vec_temp = np.array(wd_vec)
    wh_vec_temp = np.array(wh_vec)
    wc_vec_temp = np.array(wc_vec)
    wf_vec_temp = np.array(wf_vec)
    norm_energy_vec_temp = np.array(norm_energy_vec)
    #norm_kenergy_vec_temp = np.array(norm_kenergy_vec)
    #norm_penergy_vec_temp = np.array(norm_penergy_vec)
    #norm_psi_vec_temp = np.array(norm_psi_vec)
    #norm_psis_vec_temp = np.array(norm_psis_vec)
    h1_vec_temp = np.array(h1_vec)
    
    evap_vec_sort = evap_vec_temp[evap_vec_temp.argsort()]
    PVt_vec_sort = PVt_vec_temp[evap_vec_temp.argsort()]
    PVb_vec_sort = PVb_vec_temp[evap_vec_temp.argsort()]
    #PVmt_vec_sort = PVmt_vec_temp[evap_vec_temp.argsort()]
    #PVmb_vec_sort = PVmb_vec_temp[evap_vec_temp.argsort()]
    #PVtbl_vec_sort = PVtbl_vec_temp[evap_vec_temp.argsort()]
    #PVtsf_vec_sort = PVtsf_vec_temp[evap_vec_temp.argsort()]
    w_vec_sort = w_vec_temp[evap_vec_temp.argsort()]
    wd_vec_sort = wd_vec_temp[evap_vec_temp.argsort()]
    wh_vec_sort = wh_vec_temp[evap_vec_temp.argsort()]
    wc_vec_sort = wc_vec_temp[evap_vec_temp.argsort()]
    wf_vec_sort = wf_vec_temp[evap_vec_temp.argsort()]
    norm_energy_vec_sort = norm_energy_vec_temp[evap_vec_temp.argsort()]
    #norm_kenergy_vec_sort = norm_kenergy_vec_temp[evap_vec_temp.argsort()]
    #norm_penergy_vec_sort = norm_penergy_vec_temp[evap_vec_temp.argsort()]
    #norm_psi_vec_sort = norm_psi_vec_temp[evap_vec_temp.argsort()]
    #norm_psis_vec_sort = norm_psis_vec_temp[evap_vec_temp.argsort()]
    h1_vec_sort = h1_vec_temp[evap_vec_temp.argsort()]

    ### comparing PV anomalies, components of vertical velocity, and heating steps for varying latent cooling

    norm_energy = True
    norm_kenergy = False
    norm_penergy = False
    norm_psi = False
    norm_psis = False

    omega_components = True

    if omega_components == True:

        fig = plt.figure(figsize=(3.7,13)) 

        gs = gridspec.GridSpec(5, 1, height_ratios=[2, .3, 2, .3, 2]) 
        #gs.update(hspace=0.6)
        ax = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[2])
        ax1 = plt.subplot(gs[4])
        #gs.update(hspace=.5)

    #    ax = host_subplot(111, axes_class=AA.Axes)
        ax2 = ax.twinx()
        if norm_psi == True:
            ax.scatter(evap_vec_sort,PVt_vec_sort/norm_psi_vec_sort,s=80,c=c_blues[0],marker='*',lw=0,label='PV$\mathregular{_{ht}}$')
            ax.scatter(evap_vec_sort,PVb_vec_sort/norm_psi_vec_sort,s=80,color=c[2],marker='*',lw=0,label='PV$\mathregular{_{hb}}$')
        if norm_psis == True:
            ax.scatter(evap_vec_sort,PVt_vec_sort/norm_psis_vec_sort,s=80,c=c_blues[0],marker='*',lw=0,label='PV$\mathregular{_{ht}}$')
            ax.scatter(evap_vec_sort,PVb_vec_sort/norm_psis_vec_sort,s=80,color=c[2],marker='*',lw=0,label='PV$\mathregular{_{hb}}$')
        if norm_energy == True:
            ax.scatter(evap_vec_sort,PVt_vec_sort/norm_energy_vec_sort,c=c_blues[0],marker='*',s=80,lw=0,label='PV$\mathregular{_{ht}}$')
            ax.scatter(evap_vec_sort,PVb_vec_sort/norm_energy_vec_sort,color=c[2],marker='*',s=80,lw=0,label='PV$\mathregular{_{hb}}$')
        if norm_kenergy == True:
            ax.scatter(evap_vec_sort,PVt_vec_sort/norm_kenergy_vec_sort,c=c_blues[0],marker='*',s=80,lw=0,label='PV$\mathregular{_{ht}}$')
            ax.scatter(evap_vec_sort,PVb_vec_sort/norm_kenergy_vec_sort,color=c[2],marker='*',s=80,lw=0,label='PV$\mathregular{_{hb}}$')
        if norm_penergy == True:
            ax.scatter(evap_vec_sort,PVt_vec_sort/norm_penergy_vec_sort,c=c_blues[0],marker='*',s=80,lw=0,label='PV$\mathregular{_{ht}}$')
            ax.scatter(evap_vec_sort,PVb_vec_sort/norm_penergy_vec_sort,color=c[2],marker='*',s=80,lw=0,label='PV$\mathregular{_{hb}}$')
        ax.scatter((),(),c=(.7,.7,.7),marker='*',lw=0,s=80,label='PV$\mathregular{_{ht}}$/PV$\mathregular{_{hb}}$')
        ax2.scatter(evap_vec_sort,PVt_vec_sort/PVb_vec_sort,c=(.7,.7,.7),marker='*',lw=0,s=80)
        ax.set_xticks([1,1.1,1.2,1.3,1.4,1.5])
        ax.set_xticklabels(['0.0','0.1','0.2','0.3','0.4','0.5'])
        ax.set_xlim(0.95,1.55)
        ax.set_ylabel('amplitude of normalized PV')
        ax2.set_ylabel('PV$\mathregular{_{ht}}$/PV$\mathregular{_{hb}}$',rotation=270,labelpad=20)
        ax.tick_params(which='both', length=6, width=1)
        ax2.tick_params(which='both', length=6, width=1)

        ax.legend(prop={'size':12}, scatterpoints=1,bbox_to_anchor=(.5,-.32),ncol=3,loc='lower center')#,bbox_to_anchor=(1.85,0.5), loc='right')
        #new_fixed_axis = ax2.get_grid_helper().new_fixed_axis
        #ax2.axis["right"] = new_fixed_axis(loc="left",axes=ax2,offset=(-60, 0))
        
        ax4=twinx(ax3)
        if norm_psi == True:
            ax3.scatter(evap_vec_sort,(epsilon1[eps1_index]/2*(h1_vec_sort[:,jtlc+1]-h1_vec_sort[:,jtlc-1])*abs(w_vec_sort)/norm_psi_vec_sort),c=c_blues[0],marker='s',s=70,lw=0,label='$\mathregular{\Delta Q_{ht}}$')
            ax3.scatter(evap_vec_sort,-(epsilon1[eps1_index]/2*(h1_vec_sort[:,jblc+1]-h1_vec_sort[:,jblc-1])*abs(w_vec_sort)/norm_psi_vec_sort),color=c[2],marker='D',edgecolor=c[-1],s=50,lw=0,label='$\mathregular{\Delta Q_{hb}}$')
        if norm_psis == True:
            ax3.scatter(evap_vec_sort,(epsilon1[eps1_index]/2*(h1_vec_sort[:,jtlc+1]-h1_vec_sort[:,jtlc-1])*abs(w_vec_sort)/norm_psis_vec_sort),c=c_blues[0],marker='s',s=70,lw=0,label='$\mathregular{\Delta Q_{ht}}$')
            ax3.scatter(evap_vec_sort,-(epsilon1[eps1_index]/2*(h1_vec_sort[:,jblc+1]-h1_vec_sort[:,jblc-1])*abs(w_vec_sort)/norm_psis_vec_sort),color=c[2],marker='D',edgecolor=c[-1],s=50,lw=0,label='$\mathregular{\Delta Q_{hb}}$')
        if norm_energy == True:
            ax3.scatter(evap_vec_sort,(epsilon1[eps1_index]/2*(h1_vec_sort[:,jtlc+1]-h1_vec_sort[:,jtlc-1])*abs(w_vec_sort)/norm_energy_vec_sort),c=c_blues[0],marker='s',s=70,lw=0,label='$\mathregular{\Delta Q_{ht}}$')
            ax3.scatter(evap_vec_sort,-(epsilon1[eps1_index]/2*(h1_vec_sort[:,jblc+1]-h1_vec_sort[:,jblc-1])*abs(w_vec_sort)/norm_energy_vec_sort),color=c[2],marker='D',edgecolor=c[-1],s=50,lw=0,label='$\mathregular{\Delta Q_{hb}}$')
        if norm_kenergy == True:
            ax3.scatter(evap_vec_sort,(epsilon1[eps1_index]/2*(h1_vec_sort[:,jtlc+1]-h1_vec_sort[:,jtlc-1])*abs(w_vec_sort)/norm_kenergy_vec_sort),c=c_blues[0],marker='s',s=70,lw=0,label='$\mathregular{\Delta Q_{ht}}$')
            ax3.scatter(evap_vec_sort,-(epsilon1[eps1_index]/2*(h1_vec_sort[:,jblc+1]-h1_vec_sort[:,jblc-1])*abs(w_vec_sort)/norm_kenergy_vec_sort),color=c[2],marker='D',edgecolor=c[-1],s=50,lw=0,label='$\mathregular{\Delta Q_{hb}}$')
        if norm_penergy == True:
            ax3.scatter(evap_vec_sort,(epsilon1[eps1_index]/2*(h1_vec_sort[:,jtlc+1]-h1_vec_sort[:,jtlc-1])*abs(w_vec_sort)/norm_penergy_vec_sort),c=c_blues[0],marker='s',s=70,lw=0,label='$\mathregular{\Delta Q_{ht}}$')
            ax3.scatter(evap_vec_sort,-(epsilon1[eps1_index]/2*(h1_vec_sort[:,jblc+1]-h1_vec_sort[:,jblc-1])*abs(w_vec_sort)/norm_penergy_vec_sort),color=c[2],marker='D',edgecolor=c[-1],s=50,lw=0,label='$\mathregular{\Delta Q_{hb}}$')
        ax4.scatter(evap_vec_sort,(epsilon1[eps1_index]/2*(h1_vec_sort[:,jtlc+1]-h1_vec_sort[:,jtlc-1])*abs(w_vec_sort))/(-epsilon1[eps1_index]/2*(h1_vec_sort[:,jblc+1]-h1_vec_sort[:,jblc-1])*abs(w_vec_sort)),c=(.7,.7,.7),marker='^',s=70,lw=0,label='$\mathregular{\Delta Q_{ct}}$')
        ax3.scatter((),(),c=(.7,.7,.7),marker='^',lw=0,s=70,label='$\mathregular{\Delta Q_{ht}/\Delta Q_{hb}}$')
        #ax4.scatter(evap_vec_sort,PVt_vec_sort/PVb_vec_sort,c=(.7,.7,.7),marker='*',lw=0,s=80)
        ax3.set_xticks([1,1.1,1.2,1.3,1.4,1.5])
        ax3.set_xticklabels(['0.0','0.1','0.2','0.3','0.4','0.5'])
        ax3.set_xlim(0.95,1.55)
        
        ax3.set_ylabel('amplitude of normalized\n heating step $\mathregular{\Delta Q}$')
        ax1.set_xlabel('relative cooling parameter $\mathregular{\gamma}$')
        ax4.set_ylabel('$\mathregular{\Delta Q_{ht}/\Delta Q_{hb}}$', rotation=270,labelpad=20)
        ax3.tick_params(which='both', length=6, width=1)
        ax4.tick_params(which='both', length=6, width=1)

        ax3.legend(prop={'size':12}, scatterpoints=1,bbox_to_anchor=(.5,-.32),ncol=3,loc='lower center')#,bbox_to_anchor=(1.85,0.5), loc='right')
            
        w_wl = abs(eigvecs_sorted_scaled[:,e2,:,:nrws,-1])
        
        labels = ['$\mathregular{\omega_d}$','$\mathregular{\omega_{h}}$','$\mathregular{\omega_d+\omega_{h}}$','$\mathregular{\omega_d+\omega_{h}+\omega_{c}+\omega_{f}=\omega}$']# = dE/dt
                
        #fig = plt.figure(figsize=(5, 5)) 
        #gs = gridspec.GridSpec(2,1,height_ratios=[3, 2]) 
        #ax1 = plt.subplot(gs[0])
        #ax2 = plt.subplot(gs[1])
        
        #lns3 = ax2.stackplot(evap_vec_sort,abs(wd_vec_sort)/abs(wd_vec_sort+whc_vec_sort+whe_vec_sort),abs(whc_vec_sort)/abs(wd_vec_sort+whc_vec_sort+whe_vec_sort),abs(whe_vec_sort)/abs(wd_vec_sort+whc_vec_sort+whe_vec_sort),colors=([c[i] for i in [5,2,1]]),edgecolor='None',labels=labels)
        
        if norm_psi == True:
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort+wc_vec_sort)/norm_psi_vec_sort,color=c[1],edgecolor=c[-1],s=140,lw=0,label=labels[3])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort)/norm_psi_vec_sort,c='None',edgecolor=(.7,.7,.7),s=80,lw=1.5,label=labels[0])
            ax1.scatter(evap_vec_sort,abs(wh_vec_sort)/norm_psi_vec_sort,color=c[2],s=20,lw=0,label=labels[1])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort)/norm_psi_vec_sort,color=c[2],edgecolor=(.7,.7,.7),s=50,lw=1.5,label=labels[2])
        if norm_psis == True:
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort+wc_vec_sort)/norm_psis_vec_sort,color=c[1],edgecolor=c[-1],s=140,lw=0,label=labels[3])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort)/norm_psis_vec_sort,c='None',edgecolor=(.7,.7,.7),s=80,lw=1.5,label=labels[0])
            ax1.scatter(evap_vec_sort,abs(wh_vec_sort)/norm_psis_vec_sort,color=c[2],s=20,lw=0,label=labels[1])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort)/norm_psis_vec_sort,color=c[2],edgecolor=(.7,.7,.7),s=50,lw=1.5,label=labels[2])
        if norm_energy == True:
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort+wc_vec_sort+wf_vec_sort)/norm_energy_vec_sort,color=c[1],edgecolor=c[-1],s=140,lw=0,label=labels[3])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort)/norm_energy_vec_sort,color=c[2],edgecolor=(.7,.7,.7),s=50,lw=1.5,label=labels[2])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort)/norm_energy_vec_sort,c='None',edgecolor=(.7,.7,.7),s=80,lw=1.5,label=labels[0])
            ax1.scatter(evap_vec_sort,abs(wh_vec_sort)/norm_energy_vec_sort,color=c[2],s=20,lw=0,label=labels[1])
        if norm_kenergy == True:
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort+wc_vec_sort)/norm_kenergy_vec_sort,color=c[1],edgecolor=c[-1],s=140,lw=0,label=labels[3])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort)/norm_kenergy_vec_sort,c='None',edgecolor=(.7,.7,.7),s=80,lw=1.5,label=labels[0])
            ax1.scatter(evap_vec_sort,abs(wh_vec_sort)/norm_kenergy_vec_sort,color=c[2],s=20,lw=0,label=labels[1])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort)/norm_kenergy_vec_sort,color=c[2],edgecolor=(.7,.7,.7),s=50,lw=1.5,label=labels[2])
        if norm_penergy == True:
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort+wc_vec_sort)/norm_penergy_vec_sort,color=c[1],edgecolor=c[-1],s=140,lw=0,label=labels[3])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort)/norm_penergy_vec_sort,c='None',edgecolor=(.7,.7,.7),s=80,lw=1.5,label=labels[0])
            ax1.scatter(evap_vec_sort,abs(wh_vec_sort)/norm_penergy_vec_sort,color=c[2],s=20,lw=0,label=labels[1])
            ax1.scatter(evap_vec_sort,abs(wd_vec_sort+wh_vec_sort)/norm_penergy_vec_sort,color=c[2],edgecolor=(.7,.7,.7),s=50,lw=1.5,label=labels[2])

        ax1.set_ylabel('amplitude of normalized \n $\mathregular{\omega}$ components at $\mathregular{p_{hb}}$')# at $p_{hb}$')
        #ax1.set_ylim(0,80)
        ax1.set_xlim(0.95,1.55)
        ax1.set_xticks([1,1.1,1.2,1.3,1.4,1.5])
        ax1.set_xticklabels(['0.0','0.1','0.2','0.3','0.4','0.5'])
        ax1.tick_params(which='both', length=6, width=1)
        
        ax1.legend(prop={'size':12}, scatterpoints=1,bbox_to_anchor=(.5,-.57),ncol=2,loc='lower center')#(1.85,0.5), loc='right')
        plt.show()
        
        if len(evap_vec_sort) > 2:
            test = ([])
            for i in range(1,len(evap_vec_sort)+1):
                for j in range(len(evap_vec_sort)):
                    #abs(wd_vec_sort+whc_vec_sort)/abs(wd_vec_sort+whc_vec_sort+whe_vec_sort)
                    test.extend([[(abs(wd_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j])/norm_energy_vec_sort[j])/(abs(wd_vec_sort[-i]+wh_vec_sort[-i]+wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j]+wh_vec_sort[j]+wc_vec_sort[j])/norm_energy_vec_sort[j]), (abs(wh_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wh_vec_sort[j])/norm_energy_vec_sort[j])/(abs(wd_vec_sort[-i]+wh_vec_sort[-i]+wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j]+wh_vec_sort[j]+wc_vec_sort[j])/norm_energy_vec_sort[j]), (abs(wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wc_vec_sort[j])/norm_energy_vec_sort[j])/(abs(wd_vec_sort[-i]+wh_vec_sort[-i]+wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j]+wh_vec_sort[j]+wc_vec_sort[j])/norm_energy_vec_sort[j])]])
            for i in range(3):
                print ('max:',np.nanmax(np.array(test)[:,i]),'min:',np.nanmin(np.array(test)[:,i]))
        
            abs(wd_vec_sort[-1]+wh_vec_sort[-1]+wc_vec_sort[-1])/abs(wd_vec_sort[-1]+wh_vec_sort[-1])
            i=1
            j=0
            (abs(wd_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j])/norm_energy_vec_sort[j])/(abs(wd_vec_sort[-i]+wh_vec_sort[-i]+wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j]+wh_vec_sort[j]+wc_vec_sort[j])/norm_energy_vec_sort[j]), (abs(wh_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wh_vec_sort[j])/norm_energy_vec_sort[j])/(abs(wd_vec_sort[-i]+wh_vec_sort[-i]+wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j]+wh_vec_sort[j]+wc_vec_sort[j])/norm_energy_vec_sort[j]), (abs(wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wc_vec_sort[j])/norm_energy_vec_sort[j])/(abs(wd_vec_sort[-i]+wh_vec_sort[-i]+wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j]+wh_vec_sort[j]+wc_vec_sort[j])/norm_energy_vec_sort[j])
#            abs(wh_vec_sort)/norm_kenergy_vec_sort
            print ('100% - contribution from lc:', (abs(wd_vec_sort[-i]+wh_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j]+wh_vec_sort[j])/norm_energy_vec_sort[j])/(abs(wd_vec_sort[-i]+wh_vec_sort[-i]+wc_vec_sort[-i])/norm_energy_vec_sort[-i]-abs(wd_vec_sort[j]+wh_vec_sort[j]+wc_vec_sort[j])/norm_energy_vec_sort[j]))
            #print (abs(whe_vec_sort[-i])/norm_energy_vec_sort[-i],abs(whe_vec_sort[1])/norm_energy_vec_sort[1],abs(whe_vec_sort[j])/norm_energy_vec_sort[j])
        
# -----------------------------------------------------------------------------

### comparing normalised PV anomalies and vertical velocity for varying surface flux parametrisations and intensities

def prepare_normalised_PV_w_vs_sfparam():

    global sf_label, sf_vec, wl_vec
    global PVt_sf_vec, PVb_sf_vec, PVdztt_sf_vec, PVdzbb_sf_vec, PVdzt_sf_vec, PVdzb_sf_vec
    global w_sf_vec, wd_sf_vec, wh_sf_vec, wc_sf_vec, wf_sf_vec
    global norm_energy_sf_vec, norm_kenergy_sf_vec, norm_penergy_sf_vec, norm_psi_sf_vec, norm_psis_sf_vec
    global Q_phaseshift_vec, Q_lh_vec, Q_sf_vec
    global vamp_vec
    global cph_vec, stlev_vec, gr_vec, wl_vec
    global PVfromvt, PVfromvs, PVfromQs, PVfromQhb, PVfromQht
    global PVfromvtmax, PVfromvsmax, PVfromQsmax, PVfromQhbmax, PVfromQhtmax

    try:
        norm_energy_sf_vec
    except:
        sf_label = ([])
        sf_vec = ([])      
        wl_vec = ([])  
        PVt_sf_vec = ([])
        PVb_sf_vec = ([])
        PVdztt_sf_vec = ([])
        PVdzbb_sf_vec = ([])
        PVdzt_sf_vec = ([])
        PVdzb_sf_vec = ([])
        #t_sf_vec = ([])
        w_sf_vec = ([])
        wd_sf_vec = ([])
        wh_sf_vec = ([])
        wc_sf_vec = ([])
        wf_sf_vec = ([])
        norm_energy_sf_vec = ([])
        norm_kenergy_sf_vec = ([])
        norm_penergy_sf_vec = ([])
        norm_psi_sf_vec = ([])
        norm_psis_sf_vec = ([])
        #h2_sf_vec = ([])
        #eps2_sf_vec = ([])
        Q_phaseshift_vec = ([])
        Q_lh_vec = ([])
        Q_sf_vec = ([])  
        vamp_vec = ([])
        cph_vec  = ([])
        stlev_vec = ([])
        gr_vec = ([])
        PVfromvt = ([])
        PVfromvs = ([])
        PVfromQs = ([])
        PVfromQhb = ([])
        PVfromQht = ([])
        PVfromvtmax = ([])
        PVfromvsmax = ([])
        PVfromQsmax = ([])
        PVfromQhbmax = ([])
        PVfromQhtmax = ([])
        
    psi_sf = psi_maxunstab[eps1_index,eps2_index]
    w_sf = w_maxunstab[eps1_index,eps2_index]
    t_sf = tempcalc(psi_maxunstab)[eps1_index,eps2_index]
    v_sf = 1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]
    gr_sf = (sigmai_sorted[0,0,i_maxunstab,-1])[0,0]
    PV_sf = PV_u[eps1_index,eps2_index].max(axis=1)
    wh_sf = wh
    wc_sf = wc
    wd_sf = wd
    wf_sf = wf
    wl_sf = wl[i_maxunstab[eps1_index,eps2_index]]
    Q_phaseshift = (kx[np.argwhere(Q[jblc-1] == np.max(Q[jblc-1]))[0,0]]-kx[np.argwhere(Q[jtsf+1] == np.max(Q[jtsf+1]))[0,0]])*180/np.pi
    if heating2 == False:
        Q_phaseshift = NaN
    Q_lh = np.max(Q[jtlc+1])
    Q_sf = np.max(Q[jtsf+1])
    if heating2 == False:
        Q_sf = NaN
        
    if len(sf_vec) == 0 or len(sf_vec) > 0 and PVt_sf_vec[-1] != abs(PV_sf[jtlc]):

        if heating2 == False and heating1 == False:
            sf_label.extend(['Eady'])###    
        elif heating2 == False and heating1 == True:
            sf_label.extend(['lh'])###
        elif heating2 == True and wpar == False and vpar == False:
            sf_label.extend(['$\mathregular{T_s}$'])
        elif heating2 == True and wpar == False and vpar == True:
            sf_label.extend(['$\mathregular{v_s}$'])
        elif heating2 == True and epsilon2.real > 0 and wpar == True and vpar == False:
            sf_label.extend(['$\mathregular{\omega_{\\ast,0^\circ}}$'])
        elif heating2 == True and epsilon2.imag > 0 and wpar == True and vpar == False:
            sf_label.extend(['$\mathregular{\omega_{\\ast,\\minus 90^\circ}}$'])
        elif heating2 == True and epsilon2.imag < 0 and wpar == True and vpar == False:
            sf_label.extend(['$\mathregular{\omega_{\\ast,\\plus 90^\circ}}$'])
        elif heating2 == True and epsilon2.real < 0 and wpar == True and vpar == False:
            sf_label.extend(['$\mathregular{\omega_{\\ast,180^\circ}}$'])
        else:
            sf_label.extend(['unknown'])
#            raise AssertionError('make label')
    
        sf_vec.extend([len(sf_vec)])
        wl_vec.extend([wl_sf])
        PVt_sf_vec.extend([abs(PV_sf[jtlc])])
        PVb_sf_vec.extend([abs(PV_sf[jtsf])])
        PVdztt_sf_vec.extend([max(T[eps1_index,eps2_index,0])])#abs(PV_sf[0])])
        PVdzbb_sf_vec.extend([max(T[eps1_index,eps2_index,-1])])#abs(PV_sf[-1])])
        PVdzt_sf_vec.extend([max(T[eps1_index,eps2_index,jtlc-1]-T[eps1_index,eps2_index,jtlc+1])])
        PVdzb_sf_vec.extend([max(T[eps1_index,eps2_index,jblc-1]-T[eps1_index,eps2_index,jblc+1])])
        if heating1 == False and heating2 == False:
            PVdzt_sf_vec[-1] = NaN
            PVdzb_sf_vec[-1] = NaN
        #t_sf_vec.extend([(t_sf[jblc])])
        w_sf_vec.extend([(w_sf[jblc])])
        wd_sf_vec.extend([(wd_sf[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],jtml])])
        wh_sf_vec.extend([(wh_sf[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],jtml])])
        if heating1 == False and heating2 == False:
            wh_sf_vec[-1] = NaN
        wc_sf_vec.extend([(wc_sf[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],jtml])])
        wf_sf_vec.extend([(wf_sf[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],jtml])])
        norm_energy_sf_vec.extend([simps(abs(v_sf**2+t_sf**2/S[:nrws]),p[:nrws])])
        norm_kenergy_sf_vec.extend([simps(abs(v_sf**2),p[:nrws])])
        norm_penergy_sf_vec.extend([simps(abs(t_sf**2/S[:nrws]),p[:nrws])])
        norm_psi_sf_vec.extend([min(abs(psi_sf))])
        norm_psis_sf_vec.extend([(abs(psi_sf[-1]))])
        #h2_sf_vec.extend([h2[eps1_index,:nrws]])
        #eps2_sf_vec.extend([epsilon2[0]])
        Q_phaseshift_vec.extend([Q_phaseshift])
        Q_lh_vec.extend([Q_lh])
        Q_sf_vec.extend([Q_sf])
        vamp_vec.extend([(abs(1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index]))])
        cph_vec.extend([sigmar_sorted[eps1_index,eps2_index,i_maxunstab[0,0],-1]/k[i_maxunstab[0,0]]])
        stlev_vec.extend([(p[np.argwhere(u < sigmar_sorted[eps1_index,eps2_index,i_maxunstab[0,0],-1]/k[i_maxunstab[0,0]])[0][0]])])
        gr_vec.extend([sigmai_sorted[eps1_index,eps2_index,i_maxunstab[0,0],-1]])
        #PVfromv.extend([np.max(v[-1])*lambda1[-1]])
        #PVfromQ.extend([np.max(Q[-1])])
        PVfromvt.extend([-v[ 0,np.argwhere(T[eps1_index,eps2_index,0]==min(T[eps1_index,eps2_index,0]))[0][0] ]*lambda1[0]])
        PVfromvs.extend([ v[ -1,np.argwhere(T[eps1_index,eps2_index,-1]==max(T[eps1_index,eps2_index,-1]))[0][0] ]*lambda1[-1]])
        PVfromQs.extend([ Q[ -1,np.argwhere(T[eps1_index,eps2_index,-1]==max(T[eps1_index,eps2_index,-1]))[0][0] ]])
        PVfromvtmax.extend([np.max(v[0,:])*lambda1[0]])
        PVfromvsmax.extend([np.max(v[-1,:])*lambda1[-1]])
        PVfromQsmax.extend([np.max(Q[-1,:])])
        if np.max(Q[-1]) == 0:
            PVfromQs[-1] = NaN
            PVfromQsmax[-1] = NaN
        #PVfromQhb.extend([np.max(Q[jblc-1]-Q[jblc+1])])
        #PVfromQht.extend([np.max(Q[jtlc-1]-Q[jtlc+1])])
        PVfromQhb.extend([(Q[jblc-1,np.argwhere(PV_u[eps1_index,eps2_index,jblc]==max(PV_u[eps1_index,eps2_index,jblc]))[0][0]]-Q[jblc+1,np.argwhere(PV_u[eps1_index,eps2_index,jblc]==max(PV_u[eps1_index,eps2_index,jblc]))[0][0]])])
        PVfromQht.extend([(Q[jtlc-1,np.argwhere(PV_u[eps1_index,eps2_index,jtlc]==max(PV_u[eps1_index,eps2_index,jtlc]))[0][0]]-Q[jtlc+1,np.argwhere(PV_u[eps1_index,eps2_index,jtlc]==max(PV_u[eps1_index,eps2_index,jtlc]))[0][0]])])
        PVfromQhbmax.extend([np.max(Q[jblc-1]-Q[jblc+1])])
        PVfromQhtmax.extend([np.max(Q[jtlc-1]-Q[jtlc+1])])
              
# -----------------------------------------------------------------------------        
                        
def reset_last_sfparam():

    global sf_label, sf_vec, wl_vec
    global PVt_sf_vec, PVb_sf_vec, PVdztt_sf_vec, PVdzbb_sf_vec, PVdzt_sf_vec, PVdzb_sf_vec
    global w_sf_vec, wd_sf_vec, wh_sf_vec, wc_sf_vec, wf_sf_vec
    global norm_energy_sf_vec, norm_kenergy_sf_vec, norm_penergy_sf_vec, norm_psi_sf_vec, norm_psis_sf_vec
    global Q_phaseshift_vec, Q_lh_vec, Q_sf_vec
    global vamp_vec
    global cph_vec, stlev_vec, gr_vec, wl_vec
    global PVfromvt, PVfromvs, PVfromQs, PVfromQhb, PVfromQht
    global PVfromvtmax, PVfromvsmax, PVfromQsmax, PVfromQhbmax, PVfromQhtmax

    sf_label = sf_label[:-1]
    sf_vec = sf_vec[:-1]
    wl_vec = wl_vec[:-1]
    PVt_sf_vec = PVt_sf_vec[:-1]
    PVb_sf_vec = PVb_sf_vec[:-1]
    PVdztt_sf_vec = PVdztt_sf_vec[:-1]
    PVdzbb_sf_vec = PVdzbb_sf_vec[:-1]
    PVdzt_sf_vec = PVdzt_sf_vec[:-1]
    PVdzb_sf_vec = PVdzb_sf_vec[:-1]
    w_sf_vec = w_sf_vec[:-1]
    wd_sf_vec = wd_sf_vec[:-1]
    wh_sf_vec = wh_sf_vec[:-1]
    wc_sf_vec = wc_sf_vec[:-1]
    wf_sf_vec = wf_sf_vec[:-1]
    norm_energy_sf_vec = norm_energy_sf_vec[:-1]
    norm_kenergy_sf_vec = norm_energy_sf_vec[:-1]
    norm_penergy_sf_vec = norm_energy_sf_vec[:-1]
    norm_psi_sf_vec = norm_energy_sf_vec[:-1]
    norm_psis_sf_vec = norm_energy_sf_vec[:-1]
    Q_phaseshift_vec = Q_phaseshift_vec[:-1]
    Q_lh_vec = Q_lh_vec[:-1]
    Q_sf_vec = Q_sf_vec[:-1]
    vamp_vec = vamp_vec[:-1]
    cph_vec  = cph_vec[:-1]
    stlev_vec = stlev_vec[:-1]
    gr_vec = gr_vec[:-1]
    PVfromvt = PVfromvt[:-1]
    PVfromvs = PVfromvs[:-1]
    PVfromQs = PVfromQs[:-1]
    PVfromQhb = PVfromQhb[:-1]
    PVfromQht = PVfromQht[:-1]
    PVfromvtmax = PVfromvtmax[:-1]
    PVfromvsmax = PVfromvsmax[:-1]
    PVfromQsmax = PVfromQsmax[:-1]
    PVfromQhbmax = PVfromQhbmax[:-1]
    PVfromQhtmax = PVfromQhtmax[:-1]
        
# -----------------------------------------------------------------------------

### plotting normalised PV anomalies and vertical velocity for varying surface flux parametrisations and intensities

def plot_normalised_PV_w_vs_sfparam():

    sf_vec_array = np.array(sf_vec)
    wl_vec_array = np.array(wl_vec)
    PVt_sf_vec_array = np.array(PVt_sf_vec)#/wl_vec_array**2
    PVb_sf_vec_array = np.array(PVb_sf_vec)#/wl_vec_array**2
    PVdztt_sf_vec_array = np.array(PVdztt_sf_vec)#/wl_vec_array**2
    PVdzbb_sf_vec_array = np.array(PVdzbb_sf_vec)#/wl_vec_array**2
    PVdzt_sf_vec_array = np.array(PVdzt_sf_vec)
    PVdzb_sf_vec_array = np.array(PVdzb_sf_vec)
    #t_sf_vec_array = np.array(t_sf_vec)
    w_sf_vec_array = np.array(w_sf_vec)
    wd_sf_vec_array = np.array(wd_sf_vec)
    wh_sf_vec_array = np.array(wh_sf_vec)
    wc_sf_vec_array = np.array(wc_sf_vec)
    wf_sf_vec_array = np.array(wf_sf_vec)
    norm_sf_vec_array = np.array(norm_energy_sf_vec)
#    norm_sf_vec_array = np.array(norm_kenergy_sf_vec)
#    norm_sf_vec_array = np.array(norm_penergy_sf_vec)
#    norm_sf_vec_array = np.array(norm_psi_sf_vec)
#    norm_sf_vec_array = np.array(norm_psis_sf_vec)
#    norm_sf_vec_array = np.ones(len(norm_energy_sf_vec))
    #h2_sf_vec_array = np.array(h2_sf_vec)
    #eps2_sf_vec_array = np.array(eps2_sf_vec)
    Q_phaseshift_vec_array = np.array(Q_phaseshift_vec)
    Q_lh_vec_array = np.array(Q_lh_vec)
    Q_sf_vec_array = np.array(Q_sf_vec)
    cph_vec_array = np.array(cph_vec)
    stlev_vec_array = np.array(stlev_vec)
    gr_vec_array = np.array(gr_vec)
    PVfromvt_array = np.array(PVfromvt)
    PVfromvs_array = np.array(PVfromvs)
    PVfromQs_array = np.array(PVfromQs)
    PVfromQhb_array = np.array(PVfromQhb)
    PVfromQht_array = np.array(PVfromQht)
    PVfromvtmax_array = np.array(PVfromvtmax)
    PVfromvsmax_array = np.array(PVfromvsmax)
    PVfromQsmax_array = np.array(PVfromQsmax)
    PVfromQhbmax_array = np.array(PVfromQhbmax)
    PVfromQhtmax_array = np.array(PVfromQhtmax)
    
    for j in range(len(Q_phaseshift_vec)):
        if Q_phaseshift_vec_array[j] < 0:
            Q_phaseshift_vec_array[j] = Q_phaseshift_vec_array[j]+360

    if len(sf_vec) > 0:
        fig, (ax1,ax5) = plt.subplots(2,1,figsize=(8,17), dpi=300)
        ms = 300

        #gs = gridspec.GridSpec(5, 1, height_ratios=[2, .4, 2, .4, 2]) 
#        gs = gridspec.GridSpec(3, 1, height_ratios=[2, .7, 2]) #, 1.45, 2
        #gs.update(hspace=0.6)
#        ax1 = plt.subplot(gs[0])
        #ax3 = plt.subplot(gs[2])
#        ax5 = plt.subplot(gs[2])
#        ax6 = plt.subplot(gs[5])
        #gs.update(hspace=.5)

        #ax1 = brokenaxes(ylims=((0.9*np.min(PVb_sf_vec_array/norm_energy_sf_vec_array),1.1*np.max(PVb_sf_vec_array/norm_energy_sf_vec_array)),(0.95*np.min(PVt_sf_vec_array/norm_energy_sf_vec_array),1.05*np.max(PVt_sf_vec_array/norm_energy_sf_vec_array))), wspace=.1, subplot_spec = gs[0], despine=False)
#        ax2 = twinx(ax1)
#        lns1=ax2.scatter(sf_vec_array,PVt_sf_vec_array/norm_energy_sf_vec_array,c=c_blues[0],marker='*',s=300,lw=0,label='PV$\mathregular{_{0.4}}$')
#        lns2=ax2.scatter(sf_vec_array,PVb_sf_vec_array/norm_energy_sf_vec_array,color=c[2],marker='*',s=300,lw=0,label='PV$\mathregular{_{0.9}}$')
        #    ax.scatter((),(),c=(.7,.7,.7),marker='*',lw=0,s=80,label='PV$\mathregular{_{ht}}$/PV$\mathregular{_{hb}}$')
        #    ax2.scatter(sf_vec_sort,PVt_sf_vec_sort/PVb_sf_vec_sort,c=(.7,.7,.7),marker='*',lw=0,s=80)
        #ax1.set_xticks(sf_vec)
#        ax1.set_xlim(np.min(sf_vec)-.5,np.max(sf_vec)+.5)
#        if norm_energy_sf_vec_array[0] == 1:
#            ax1.set_ylabel('amplitude of scaled \nPV at p$\mathregular{_{ht}}$ and p$\mathregular{_{hb}}$')#, labelpad=50)#, rotation=270,labelpad=25)
        #ax2.set_ylabel('PV$\mathregular{_{ht}}$/PV$\mathregular{_{hb}}$',rotation=270,labelpad=20)
#        ax1.tick_params(which='both', length=6, width=1)
#        ax1.axvline(.5,c='k',ls='--',lw=1.5)
#        ax1.axvline(3.5,c='k',ls='--',lw=1.5)
#        ax1.axvline(6.5,c='k',ls='--',lw=1.5)
#        ax1.set_ylim(bottom=0, top=360) 
#        ax1.axvline(6,c='k',ls='-',lw=1.5)
#        ax1.axvline(8,c='k',ls='-',lw=1.5)
#        ax1.axvline(12,c='k',ls='-',lw=1.5)
#        ax1.axhline(PVdztt_sf_vec_array[0]/norm_energy_sf_vec_array[0],c=(.7,.7,.7),ls='-',lw=1.5)
#        ax1.axhline(PVdzt_sf_vec_array[0]/norm_energy_sf_vec_array[0],c=c_blues[0],ls='-',lw=1.5)
#        ax1.axhline(PVdzb_sf_vec_array[0]/norm_energy_sf_vec_array[0],c=c[2],ls='-',lw=1.5)
#        ax1.axhline(PVdzbb_sf_vec_array[0]/norm_energy_sf_vec_array[0],c='k',ls='-',lw=1.5)
        
#        ax1.legend(scatterpoints=1,bbox_to_anchor=(.5,-.75),ncol=3,loc='lower center')#,bbox_to_anchor=(1.85,0.5), loc='right')
        #new_fixed_axis = ax2.get_grid_helper().new_fixed_axis
        #ax2.axis["right"] = new_fixed_axis(loc="left",axes=ax2,offset=(-60, 0))
        #ax2.set_xticks(sf_vec)
        ax1.set_xticks(sf_vec)
        ax1.set_xticklabels(sf_label, rotation='vertical')
        ax1.set_xticks(sf_vec)   
#        ax1.set_xlim(-.5,3.5)    
        #ax1.axs[1].set_xticks(sf_vec)
        #ax1.axs[1].set_xticklabels(sf_label, rotation='vertical')
        #ax1.axs[1].set_xticks(sf_vec)
#        ax1.set_ylim(bottom=0, top=10) 
        
        #ax2=twinx(ax1)
        lns3=ax1.scatter(sf_vec_array,PVdztt_sf_vec_array/norm_sf_vec_array,color=(.7,.7,.7),marker='o',s=500+ms,lw=0,label='$\mathregular{PV_{p_t}}$')#$\mathregular{\int PV_{p_t} dp}$')
        lns4=ax1.scatter(sf_vec_array,PVdzbb_sf_vec_array/norm_sf_vec_array,color='k',marker='o',s=50+ms,lw=0,label='$\mathregular{PV_{p_b}}$')#$\mathregular{\int PV_{p_b} dp}$')
        lns5=ax1.scatter(sf_vec_array,PVdzt_sf_vec_array/norm_sf_vec_array,color=c_blues[0],marker='o',s=500+ms,lw=0,label='$\mathregular{PV_{p_{lht}}}$')#$\mathregular{\int PV_{p_{lht}} dp}$')#, edgecolors='k'
        lns6=ax1.scatter(sf_vec_array,PVdzb_sf_vec_array/norm_sf_vec_array,color=c[2],marker='o',s=50+ms,lw=0,label='$\mathregular{PV_{p_{lhb}}}$')#$\mathregular{\int PV_{p_{lhb}} dp}$')#, edgecolors='k'
        ax1.set_ylabel('vertical integral of scaled PV')#,rotation=270,labelpad=25)  

        lns = lns5,lns6,lns3,lns4#lns1,lns2,
        labs = [l.get_label() for l in lns]
        legend = ax1.legend((lns), (labs), scatterpoints=1,ncol=2,loc='upper left')#loc='center', handlelength=2.1,bbox_to_anchor=(.9,-.35), prop={'size': 12}, ncol=2)
             
        if len(PVdzt_sf_vec_array[~np.isnan(PVdzt_sf_vec_array)]) > 0:
            ax1.text(-1.37,1.04*np.nanmax(PVdzt_sf_vec_array/norm_sf_vec_array),'a)')

#        ax4=twinx(ax3)
#        ax3.scatter(sf_vec_array,Q_phaseshift_vec_array,c=(.7,.7,.7),marker='^',s=200,lw=0,label='Q$\mathregular{_{shift}}$')
#        ax3.scatter((),(),color=c[2],marker='X',s=200,lw=0,label='Q$\mathregular{_{lh}}$')
#        ax3.scatter((),(),c='k',marker='.',s=150,lw=0, label='10$\mathregular{\cdot Q_{sf}}$')
#        ax4.scatter(sf_vec_array,Q_lh_vec_array/norm_energy_sf_vec_array,color=c[2],marker='X',s=200,lw=0)
#        ax4.scatter(sf_vec_array,10*Q_sf_vec_array/norm_energy_sf_vec_array,c='k',marker='.',s=150,lw=0)
        
#        ax3.set_ylabel('phase shift ($^\circ$) of Q$\mathregular{_{sf}}$ \nrelative to Q$\mathregular{_{lh}}$')
#        if norm_energy_sf_vec_array[0] == 1:
#            ax4.set_ylabel('amplitude of scaled \nQ$\mathregular{_{lh}}$ and 10$\mathregular{\cdot Q_{sf}}$', rotation=270,labelpad=45)
#        ax3.set_xticks(sf_vec)
#        ax3.set_xlim(np.min(sf_vec)-.5,np.max(sf_vec)+.5)
#        ax3.set_yticks([0,90,180,270,360])
#        ax3.set_ylim([0,360])
#        ax3.tick_params(which='both', length=6, width=1)
#        ax3.axvline(.5,c='k',ls='--',lw=1.5)
#        ax3.axvline(3.5,c='k',ls='--',lw=1.5)
#        ax3.axvline(6.5,c='k',ls='--',lw=1.5)
        #ax3.axhline(0,c='grey',ls='--',lw=1.5)
        
#        ax3.legend(scatterpoints=1,bbox_to_anchor=(.5,-.8),ncol=3,loc='lower center')#,bbox_to_anchor=(1.85,0.5), loc='right')
#        ax3.set_xticklabels(sf_label, rotation='vertical')
        
        w_wl = abs(eigvecs_sorted_scaled[:,e2,:,:nrws,-1])

        labels = ['$\mathregular{\omega_d}$','$\mathregular{\omega_{lh}}$','$\mathregular{\omega_d+\omega_{lh}}$','$\mathregular{\omega_d+\omega_{lh}+\omega_{sf}=\omega}$']# = dE/dt

        #lns3 = ax2.stackplot(evap_vec_sort,abs(wd_vec_sort)/abs(wd_vec_sort+whc_vec_sort+whe_vec_sort),abs(whc_vec_sort)/abs(wd_vec_sort+whc_vec_sort+whe_vec_sort),abs(whe_vec_sort)/abs(wd_vec_sort+whc_vec_sort+whe_vec_sort),colors=([c[i] for i in [5,2,1]]),edgecolor='None',labels=labels)
        
#        ax5.axhline(abs(w_sf_vec_array[0])/norm_energy_sf_vec_array[0])        
#        ax5 = brokenaxes(ylims=((.8*np.min(abs(wd_sf_vec_array)/norm_energy_sf_vec_array),1.2*np.max(abs(wd_sf_vec_array)/norm_energy_sf_vec_array)), (.95*np.min(abs(wh_sf_vec_array)/norm_energy_sf_vec_array),1.1*np.max(abs(wd_sf_vec_array+wh_sf_vec_array+wf_sf_vec_array)/norm_energy_sf_vec_array))), wspace=.1, subplot_spec = gs[4], despine=False)
#        ax5.scatter(sf_vec_array,abs(w_sf_vec_array)/norm_energy_sf_vec_array,color=c[1],edgecolor=c[-1],s=950+ms,lw=0,label=labels[3])
#        ax5.scatter(sf_vec_array,abs(wd_sf_vec_array+wh_sf_vec_array+wf_sf_vec_array)/norm_sf_vec_array,color=c[1],edgecolor=c[-1],s=1200,lw=0,label=labels[3])
        ax5.scatter(sf_vec_array,abs(w_sf_vec_array)/norm_sf_vec_array,color=c[1],edgecolor=c[-1],s=1200,lw=0,label=labels[3])
        ax5.scatter(sf_vec_array,abs(wd_sf_vec_array+wh_sf_vec_array)/norm_sf_vec_array,color=c[2],edgecolor=(.7,.7,.7),s=250+ms,lw=2.5,label=labels[2])
        ax5.scatter(sf_vec_array,abs(wh_sf_vec_array)/norm_sf_vec_array,color=c[2],s=80+ms,lw=0,label=labels[1])
        ax5.scatter(sf_vec_array,abs(wd_sf_vec_array)/norm_sf_vec_array,color='None',edgecolor=(.7,.7,.7),s=250+ms,lw=2.5,label=labels[0])###

        #if norm_energy_sf_vec_array[0] == 1:
        ax5.set_ylabel('amplitude of scaled $\mathregular{\omega}$ components at $\mathregular{p_{lhb}}$  ')#, labelpad=16)
#        ax5.set_xlim(np.min(sf_vec)-.5,np.max(sf_vec)+.5)
#        plt.locator_params(axis='x', nbins=len(sf_vec))
#        ax5.set_xticks(sf_vec)
#        sf_label_manip = sf_label.insert(0,'')
        #ax5.tick_params(which='both', length=6, width=1)
#        ax5.axvline(.5,c='k',ls='--',lw=1.5)
#        ax5.axvline(3.5,c='k',ls='--',lw=1.5)
#        ax5.axvline(6.5,c='k',ls='--',lw=1.5)
        
#        ax5.axvline(6,c='k',ls='-',lw=1.5)
#        ax5.axvline(8,c='k',ls='-',lw=1.5)
#        ax5.axvline(12,c='k',ls='-',lw=1.5)
        
        ax5.legend(scatterpoints=1,ncol=2,loc='upper left')#(1.85,0.5), loc='right')
        ax5.set_xlabel('surface flux experiment', labelpad=15)
        ax5.set_xticklabels(sf_label, rotation='vertical')
#        ax5.axs[1].set_xticks(sf_vec)
        ax5.set_xticks(sf_vec)   
#        ax5.set_xlim(-.5,3.5)

#        for tick in ax5.yaxis.get_ticklabels()[1::2]:
#            tick.set_visible(False)
#        ax5.yaxis.set_major_formatter(FormatStrFormatter('%d'))
#        ax5.set_yticks(np.arange(2,15,2))

        if len(w_sf_vec_array) > 2:
            ax5.text(-1.34,1.05*np.max(abs(w_sf_vec_array)/norm_sf_vec_array),'b)')
        
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        fig.savefig(f'/home/kfl078/Downloads/python/PVdz_w_energyscaling_S4_ratio2.pdf', transparent=True)
  
  
#        col = [5,1,2]
#        fig,ax = plt.subplots(figsize=(6,3.5))
#        ax.plot(10*vamp_vec[0][jtsf:],1000*p[jtsf:nrws],color='k',ls='--',lw=3,label=sf_label[0])
#        for j in range(1,len(vamp_vec[:])):
#            if j < 4:
#                ax.plot(10*vamp_vec[j][jtsf:],1000*p[jtsf:nrws],color=(c[col[j-1-3*int((j-1)/3)]]),lw=3,label=sf_label[j])
#            elif j < 7:
#                ax.plot(10*vamp_vec[j][jtsf:],1000*p[jtsf:nrws],color=(c[col[j-1-3*int((j-1)/3)]]),ls=':',lw=3,label=sf_label[j])
#            else:
#                ax.plot(10*vamp_vec[j][jtsf:],1000*p[jtsf:nrws],color=(c[col[j-3*int((j-1)/3)]]),ls='-.',lw=3,label=sf_label[j])
#        ax.invert_yaxis()
#        ax.set_xlabel('v (m/s)')
#        ax.set_ylabel('p (hPa)')
        
#        ax.legend(bbox_to_anchor=(1,0.5), loc='center left', fancybox=True) 

        gr_wl_cph = False
        if gr_wl_cph == True:
            fig,ax = plt.subplots(figsize=(6,3.5))
            lns1 = ax.scatter(sf_vec_array,10*cph_vec_array,s=80,color=c[5],marker='$c$',label='ps')
            ax2 = twinx(ax)
    #        lns2 = ax2.scatter(sf_vec_array,1000*stlev_vec_array,c=c[2],label='st.level')
            lns2 = ax2.scatter(sf_vec_array,gr_vec_array,s=100,color=c[2],marker='$g$',label='gr')
            ax3 = twinx(ax)
            lns3 = ax3.scatter(sf_vec_array,1000*wl_vec_array,s=100,color=c[1],marker='$w$',label='wl')
            ax3.spines["right"].set_position(("axes", 1.3))        
            ax.set_ylabel('phase speed (m/s)')
    #        ax2.set_ylabel('steering level (hPa)',rotation=270,labelpad=30)
            ax2.set_ylabel('growth rate (day$^{-1}}$)',rotation=270,labelpad=30)
            ax3.set_ylabel('wavelength (km)',rotation=270,labelpad=30)
    #        ax2.invert_yaxis()
            ax.set_xlabel('surface flux experiment')
            ax.set_xticklabels(sf_label, rotation='vertical')
            ax.set_xticks(sf_vec)
            ax.axvline(.5,c='k',ls='--',lw=1.5)
            ax.axvline(3.5,c='k',ls='--',lw=1.5)
            ax.axvline(6.5,c='k',ls='--',lw=1.5)
            #ax.set_xlim([-.5,4.5])
            
            lns = lns1,lns2,lns3
            labs = [l.get_label() for l in lns]
            plt.legend((lns),(labs), scatterpoints=1,ncol=3,bbox_to_anchor=(.5,-.85),loc='lower center')


        PVtendency_surface = False
        if PVtendency_surface == True:
            fig,ax = plt.subplots(figsize=(6,3.5))
            lns1 = ax.scatter(sf_vec_array,PVfromvs_array,s=80,color=c[5],marker='$v$',label='v')
            ax2 = twinx(ax)
    #        lns2 = ax2.scatter(sf_vec_array,1000*stlev_vec_array,c=c[2],label='st.level')
            lns2 = ax2.scatter(sf_vec_array,PVfromQs_array,s=100,color=c[2],marker='$Q$',label='Q')
    #        ax3 = twinx(ax)
    #        lns3 = ax3.scatter(sf_vec_array,1000*wl_vec_array,s=100,c=c[1],marker='$w$',label='wl')
    #        ax3.spines["right"].set_position(("axes", 1.3))        
            ax.set_ylabel('meridional adv. term')
            ax2.set_ylabel('diabatic term',rotation=270,labelpad=30)
    #        ax3.set_ylabel('wavelength (km)',rotation=270,labelpad=30)
            ax.set_xlabel('surface flux experiment')
            ax.set_xticklabels(sf_label, rotation='vertical')
            ax.set_xticks(sf_vec)
            ax.axvline(.5,c='k',ls='--',lw=1.5)
            ax.axvline(3.5,c='k',ls='--',lw=1.5)
            ax.axvline(6.5,c='k',ls='--',lw=1.5)
    #        ax.set_ylim(.95*np.min([np.nanmin(PVfromv_array),np.nanmin(PVfromQ_array)]),1.05*np.max([np.nanmax(PVfromv_array),np.nanmax(PVfromQ_array)]))
    #        ax2.set_ylim(.95*np.min([np.nanmin(PVfromv_array),np.nanmin(PVfromQ_array)]),1.05*np.max([np.nanmax(PVfromv_array),np.nanmax(PVfromQ_array)]))
            ax.set_xlim([-.5,4.5])
                    
            #lns = lns1,lns2
            #labs = [l.get_label() for l in lns]
            #plt.legend((lns),(labs), scatterpoints=1,ncol=3,bbox_to_anchor=(.5,-.85),loc='lower center')

        fig,ax = plt.subplots(figsize=(8,6))
        lns1 = ax.scatter(sf_vec_array,PVfromQhb_array/norm_sf_vec_array,s=400,color=c[2],marker='*',label='Q$\mathregular{_{0.9}}$')
        lns2 = ax.scatter(sf_vec_array,PVfromQht_array/norm_sf_vec_array,s=400,color=c_blues[0],marker='*',label='Q$\mathregular{_{0.4}}$') 
        lns3 = ax.scatter(sf_vec_array,PVfromvs_array/norm_sf_vec_array,s=100,color='grey',marker='o',label='v$\mathregular{_{1.0}}$')
        lns4 = ax.scatter(sf_vec_array,PVfromQs_array/norm_sf_vec_array,s=100,color='k',marker='o',label='Q$\mathregular{_{1.0}}$')    
        lns5 = ax.scatter(sf_vec_array,(PVfromvs_array+PVfromQs_array)/norm_sf_vec_array,s=400,color='k',marker='_',label='v$\mathregular{_{1.0}}$+Q$\mathregular{_{1.0}}$')   
        lns6 = ax.scatter(sf_vec_array,PVfromvt_array/norm_sf_vec_array,s=60,color='y',marker='o',label='v$\mathregular{_{0.15}}$')
        
        ax.scatter(sf_vec_array,PVfromQhbmax_array/norm_sf_vec_array,s=100,color=c[2],marker='*',label='Q$\mathregular{_{0.9}}$')
        ax.scatter(sf_vec_array,PVfromQhtmax_array/norm_sf_vec_array,s=100,color=c_blues[0],marker='*',label='Q$\mathregular{_{0.4}}$')
        ax.scatter(sf_vec_array,PVfromvsmax_array/norm_sf_vec_array,s=25,color='grey',marker='o',label='v$\mathregular{_{1.0}}$')
        ax.scatter(sf_vec_array,PVfromQsmax_array/norm_sf_vec_array,s=25,color='k',marker='o',label='Q$\mathregular{_{1.0}}$')    
#        ax.scatter(sf_vec_array,PVfromvsmax_array+PVfromQs_array,s=100,color='k',marker='_',label='v$\mathregular{_{1.0}}$+Q$\mathregular{_{1.0}}$')   
        ax.scatter(sf_vec_array,PVfromvtmax_array/norm_sf_vec_array,s=15,color='y',marker='o',label='v$\mathregular{_{0.15}}$')
        
        ax.set_ylabel('PV tendency at \nmax PV (big) or \nmax tendency (small)')#interfaces')
        #ax2.set_ylabel('PV tendency \nat loc. of max tendency',rotation=270,labelpad=65)
#        ax3.set_ylabel('wavelength (km)',rotation=270,labelpad=30)
        ax.set_xlabel('surface flux experiment')
        ax.set_xticklabels(sf_label, rotation='vertical')
        ax.set_xticks(sf_vec)
        ax.axvline(.5,c='k',ls='--',lw=1.5)
#        ax.axvline(3.5,c='k',ls='--',lw=1.5)
#        ax.axvline(6.5,c='k',ls='--',lw=1.5)
#        ax.set_ylim(.95*np.min([np.nanmin(PVfromQhb_array),np.nanmin(PVfromQht_array)]),1.05*np.max([np.nanmax(PVfromQhb_array),np.nanmax(PVfromQht_array)]))
#        ax2.set_ylim(.95*np.min([np.nanmin(PVfromQhb_array),np.nanmin(PVfromQht_array)]),1.05*np.max([np.nanmax(PVfromQhb_array),np.nanmax(PVfromQht_array)]))
#        ax.set_xlim([-.5,4.5])

        lns = lns2,lns1,lns4,lns3,lns5,lns6
        labs = [l.get_label() for l in lns]
        plt.legend((lns),(labs), scatterpoints=1,ncol=3,bbox_to_anchor=(.5,-.75),loc='lower center')

        plt.minorticks_on()
        ax.yaxis.grid(True, which='both', linewidth=.5)
        
        plt.show()

# -----------------------------------------------------------------------------

### comparing vertical structure of normalised variables for varying latent heating intensity

def vertical_structure_of_normalised_variables_vs_epsilon1():

    psi_vec = psi_maxunstab[:,eps2_index]
    w_vec = w_maxunstab[:,eps2_index]
    t_vec = tempcalc(psi_maxunstab)
    v_vec = 1j*k[i_maxunstab[:,eps2_index],np.newaxis]*psi_maxunstab[:,eps2_index]
#    PV_vec = PV.max(axis=1)

    fig, (ax1,ax2) = plt.subplots(2, figsize=(6,8))
    ax1.axhline(0.9, c='grey')
    try:
        psi_vec
    except NameError:
        print ('psi_vec not defined')
    else:
        for e in range(len(epsilon1)):
            ax1.plot(abs(w_vec[e])/(simps(abs(v_vec[e]**2+t_vec[e]**2/S[:nrws]),p[:nrws])),p[:nrws], c=c_blues[0], linestyle='-',linewidth=ms, label='%d' %(epsilon1[e]))#/(simps(abs(v_vec[e]**2+t_vec[e]**2/S[:nrws]),p[:nrws]))
            ax2.plot(abs(psi_vec[e])/(simps(abs(v_vec[e]**2+t_vec[e]**2/S[:nrws]),p[:nrws])),p[:nrws], c=c_blues[0], linestyle='-', linewidth=ms, label='%d' %(epsilon1[e]))#/np.max(abs(psi_vec[e]))
            #ax3.scatter(abs(PV_vec)/(simps(abs(v_vec**2+t_vec**2/S[:nrws]),p[:nrws])),p[:nrws], c=cevap[e], linestyle='-', linewidth=0,s=30, label='%d' %(epsilon1[e]))
    ax1.set_xlabel('Amplitude omega (normalized)')
    ax2.set_xlabel('Amplitude psi (normalized)')
    ax1.set_ylabel('Pressure')
    ax2.set_ylabel('Pressure')
    ax1.invert_yaxis()
    ax2.invert_yaxis()
#    ax3.set_ylabel('Pressure')
#    ax3.invert_yaxis()
#    ax3.set_xlabel('Amplitude total energy')
    
    ax2.legend(bbox_to_anchor=(0.5,-0.2), loc='upper center',
               ncol=7, fancybox=True) 

    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------------------------

### plotting phase and amplitude of eigenfunctions (first mode)
        
def phase(var):
    name = np.angle(var)
    for i in range(len(name)):
        if abs(name[i] - name[i-1]) > np.pi/2. and name[i] > 0:
            name[i] = name[i] - 2*np.pi
        if abs(name[i] - name[i-1]) > np.pi/2. and name[i] < 0:
            name[i] = name[i] + 2*np.pi
    return name
         
def plot_phase_and_amplitude_of_eigenfunctions():

    global phase_psi, phase_w, phase_T

    vTplots = False

    phase_w = phase(w_maxunstab[eps1_index,eps2_index,1:-1]) 
    phase_psi = phase(psi_maxunstab[eps1_index,eps2_index,1:-1])
    phase_T = phase(tempcalc(psi_maxunstab)[eps1_index,eps2_index,1:-1])#T[1:-1,0])
#    phase_u = phase(ua[1:-1])
    phase_v = phase(1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index,1:-1])#(v[1:-1,0])
            
    if unstab2 == True:
        phase_w2 = phase(w_maxunstab2[eps1_index,eps2_index,1:-1])
        phase_psi2 = phase(psi_maxunstab2[eps1_index,eps2_index,1:-1])
        
    fig, (ax1) = plt.subplots(1, figsize=(6,4))
    ax1.plot(phase_w,p[1:nrws-1], 'b--', linewidth=2)
    ax1.plot(phase_psi,p[1:nrws-1], 'g--', linewidth=2)
    ax1.plot(phase_T,p[1:nrws-1], 'r--', linewidth=2)
#    ax1.plot(wphtest,p[1:nrws-1], 'b.', linewidth=2)
#    ax1.plot(psiphtest,p[1:nrws-1], 'g.', linewidth=2)
#    ax1.plot(tempphtest,p[1:nrws-1], 'r.', linewidth=2)
#    ax1.plot(phase_v,p[1:nrws-1], 'k--', linewidth=2)
    if unstab2 == True and vTplots == False:
        ax1.plot(phase_w2,p[1:nrws-1], 'b--', linewidth=.5)
        ax1.plot(phase_psi2,p[1:nrws-1], 'g--', linewidth=.5)
    if unstab2 == True and vTplots == True:
        ax1.plot(phase_T,p[1:nrws-1], 'b--', linewidth=.5)
        ax1.plot(phase_v,p[1:nrws-1], 'g--', linewidth=.5)
    ax1.set_xlabel('Phase angle (rad)')
    ax1.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    ax1.set_xticklabels(['-2$\mathregular{\pi}$','-$\mathregular{\pi}$', '0', '$\mathregular{\pi}$', '2$\mathregular{\pi}$',])
    #ttl = ax1.set_title('Moist Eady mode')
    #ttl.set_position([.5, 1.2])
    ax2 = ax1.twiny()    
#    ax2.plot(wtest,p[:nrws], 'b.', linewidth=2)
#    ax2.plot(psitest,p[:nrws], 'g.', linewidth=2)       
#    ax2.plot(temptest,p[1:nrws-1], 'r.', linewidth=2)
#    ax2.plot(uatest,p[:nrws], 'k.', linewidth=2)
    ax2.plot(abs(w_maxunstab[eps1_index,eps2_index])/np.max(abs(w_maxunstab[eps1_index,eps2_index])),p[:nrws], 'b', linewidth=2)
    ax2.plot(abs(psi_maxunstab[eps1_index,eps2_index])/np.max(abs(psi_maxunstab[eps1_index,eps2_index])),p[:nrws], 'g', linewidth=2)       
    ax2.plot(abs(tempcalc(psi_maxunstab)[eps1_index,eps2_index,1:-1])/np.max(abs(tempcalc(psi_maxunstab)[eps1_index,eps2_index,1:-1])),p[1:nrws-1], 'r', linewidth=2)
    ax2.plot((abs(ua).max(axis=1))/np.max((abs(ua).max(axis=1))),p[:nrws], 'k', linewidth=2)
#    ax2.plot(abs(1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index,:])/max(abs(1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index,:])),p[:nrws], 'k', linewidth=2)
    print('average w', mean(abs(w_maxunstab[eps1_index,eps2_index])))              
    print('w at cloud base', (abs(w_maxunstab[eps1_index,eps2_index,jblc])))           
    print('average psi', mean(abs(psi_maxunstab[eps1_index,eps2_index])))
    print('average dpsi/dp', mean(abs(tempcalc(psi_maxunstab)[eps1_index,eps2_index,1:-1])))
    if unstab2 == True and vTplots == False:
        ax2.plot(abs(w_maxunstab2[eps1_index,eps2_index])/max(abs(w_maxunstab2[eps1_index,eps2_index])),p[:nrws], 'b', linewidth=.5)
        ax2.plot(abs(psi_maxunstab2[eps1_index,eps2_index])/max(abs(psi_maxunstab2[eps1_index,eps2_index])),p[:nrws], 'g', linewidth=.5)
    if unstab2 == True and vTplots == True:
        ax2.plot(abs(tempcalc(psi_maxunstab))/max(abs(tempcalc(psi_maxunstab))),p[:nrws], 'b', linewidth=.5)
        ax2.plot(abs(1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index])/max(abs(1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index])),p[:nrws], 'g', linewidth=.5)
    ax2.set_xlabel('Amplitude')
    ax2.invert_yaxis()
    ax2.set_ylim(1,0)#15)
    ax2.set_xlim(0,1)
        
    ax2.plot((),(),'b-',label='$\omega$', linewidth=2)
    ax2.plot((),(),'g-',label='$\Psi$', linewidth=2)
    ax2.plot((),(),'r-',label='$T$', linewidth=2)
#    ax2.plot((),(),'k-',label='$v$', linewidth=2)
    ax2.plot((),(),'k-',label='$u_a$', linewidth=2)
    ax2.plot((),(),'grey',label='Amplitude', linewidth=2)
    if unstab2 == True and vTplots == False:
        ax2.plot((),(),'b-',label='$\omega_2$', linewidth=.5)
        ax2.plot((),(),'g-',label='$\Psi_2$', linewidth=.5)
    if unstab2 == True and vTplots == True:
        ax2.plot((),(),'b-',label='$T$', linewidth=.5)
        ax2.plot((),(),'g-',label='$v$', linewidth=.5)
    ax2.plot((),(),'grey', linestyle='--',label='Phase', linewidth=2)
    ax2.legend(bbox_to_anchor=(0.5,-0.2), loc='upper center',
               ncol=3, fancybox=True) 
#    ax2.axhline(psmoothrangemin[-1],color='y')
#    ax2.axhline(psmoothrangemax[-1],color='y')
#    ax2.axhline(p[np.argwhere(dqdy==np.max(dqdy[1:-2]))[0][0]],color='orange')

    plt.show()

    ### plotting phase and amplitude of eigenfunctions (second mode)

    if unstab2 == True:
        phase_w = phase(w_maxunstab2[eps1_index,eps2_index,1:-1]) 
        phase_psi = phase(psi_maxunstab2[eps1_index,eps2_index,1:-1])
        phase_T = phase(tempcalc(psi_maxunstab2)[eps1_index,1:-1])#T[1:-1,0])
        phase_v = phase(1j*k[i_maxunstab2[eps1_index,eps2_index]]*psi_maxunstab2[eps1_index,eps2_index,1:-1])#(v[1:-1,0])
        
        fig, (ax1) = plt.subplots(1, figsize=(6,4))
        ax1.plot(phase_w,p[1:nrws-1], 'b--', linewidth=2)
        ax1.plot(phase_psi,p[1:nrws-1], 'g--', linewidth=2)
        if unstab3 == True and vTplots == True:
            ax1.plot(phase_T,p[1:nrws-1], 'b--', linewidth=.5)
            ax1.plot(phase_v,p[1:nrws-1], 'g--', linewidth=.5)
        ax1.set_xlabel('Phase angle (rad)')
        ax1.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
        ax1.set_xticklabels(['-2$\mathregular{\pi}$','-$\mathregular{\pi}$', '0', '$\mathregular{\pi}$', '2$\mathregular{\pi}$',])
        #ttl = ax1.set_title('Moist Eady mode')
        #ttl.set_position([.5, 1.2])
        ax2 = ax1.twiny()
        ax2.plot(abs(w_maxunstab2[eps1_index,eps2_index])/max(abs(w_maxunstab[eps1_index,eps2_index])),p[:nrws], 'b', linewidth=2)
        ax2.plot(abs(psi_maxunstab2[eps1_index,eps2_index])/max(abs(psi_maxunstab[eps1_index,eps2_index])),p[:nrws], 'g', linewidth=2)
        if unstab3 == True and vTplots == True:
            ax2.plot(abs(tempcalc(psi_maxunstab2))/max(abs(tempcalc(psi_maxunstab))),p[:nrws], 'b', linewidth=.5)
            ax2.plot(abs(1j*k[i_maxunstab2[eps1_index,eps2_index]]*psi_maxunstab2[eps1_index,eps2_index])/max(abs(1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index])),p[:nrws], 'g', linewidth=.5)
        ax2.set_xlabel('Amplitude')
        ax2.invert_yaxis()
        
        ax2.plot((),(),'b-',label='$\omega_2$', linewidth=2)
        ax2.plot((),(),'g-',label='$\Psi_2$', linewidth=2)
        ax2.plot((),(),'grey',label='Amplitude', linewidth=1.3)
        if unstab3 == True and vTplots == True:
            ax2.plot((),(),'b-',label='$T_2$', linewidth=.5)
            ax2.plot((),(),'g-',label='$v_2$', linewidth=.5)
        ax2.plot((),(),'grey', linestyle='--',label='Phase')
        ax2.legend(bbox_to_anchor=(0.5,-0.2), loc='upper center',
                   ncol=2, fancybox=True) 

        plt.show()
        
    ### plotting phase and amplitude of eigenfunctions (third mode)

    if unstab3 == True:
        phase_w = phase(w_maxunstab3[eps1_index,eps2_index,1:-1]) 
        phase_psi = phase(psi_maxunstab3[eps1_index,eps2_index,1:-1])
        phase_T = phase(tempcalc(psi_maxunstab3)[eps1_index,1:-1])#T[1:-1,0])
        phase_v = phase(1j*k[i_maxunstab3[eps1_index,eps2_index]]*psi_maxunstab3[eps1_index,eps2_index,1:-1])#(v[1:-1,0])
        
        fig, (ax1) = plt.subplots(1, figsize=(6,4))
        ax1.plot(phase_w,p[1:nrws-1], 'b--', linewidth=2)
        ax1.plot(phase_psi,p[1:nrws-1], 'g--', linewidth=2)
        if unstab3 == True and vTplots == True:
            ax1.plot(phase_T,p[1:nrws-1], 'b--', linewidth=.5)
            ax1.plot(phase_v,p[1:nrws-1], 'g--', linewidth=.5)
        ax1.set_xlabel('Phase angle (rad)')
        ax1.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
        ax1.set_xticklabels(['-2$\mathregular{\pi}$','-$\mathregular{\pi}$', '0', '$\mathregular{\pi}$', '2$\mathregular{\pi}$',])
        #ttl = ax1.set_title('Moist Eady mode')
        #ttl.set_position([.5, 1.2])
        ax2 = ax1.twiny()
        ax2.plot(abs(w_maxunstab3[eps1_index,eps2_index])/max(abs(w_maxunstab[eps1_index,eps2_index])),p[:nrws], 'b', linewidth=2)
        ax2.plot(abs(psi_maxunstab3[eps1_index,eps2_index])/max(abs(psi_maxunstab[eps1_index,eps2_index])),p[:nrws], 'g', linewidth=2)
        if unstab3 == True and vTplots == True:
            ax2.plot(abs(tempcalc(psi_maxunstab3))/max(abs(tempcalc(psi_maxunstab))),p[:nrws], 'b', linewidth=.5)
            ax2.plot(abs(1j*k[i_maxunstab3[eps1_index,eps2_index]]*psi_maxunstab3[eps1_index,eps2_index])/max(abs(1j*k[i_maxunstab[eps1_index,eps2_index]]*psi_maxunstab[eps1_index,eps2_index])),p[:nrws], 'g', linewidth=.5)
        ax2.set_xlabel('Amplitude')
        ax2.invert_yaxis()
        
        ax2.plot((),(),'b-',label='$\omega_3$', linewidth=2)
        ax2.plot((),(),'g-',label='$\Psi_3$', linewidth=2)
        ax2.plot((),(),'grey',label='Amplitude', linewidth=1.3)
        if unstab3 == True and vTplots == True:
            ax2.plot((),(),'b-',label='$T_3$', linewidth=.5)
            ax2.plot((),(),'g-',label='$v_3$', linewidth=.5)
        ax2.plot((),(),'grey', linestyle='--',label='Phase')
        ax2.legend(bbox_to_anchor=(0.5,-0.2), loc='upper center',
                   ncol=2, fancybox=True) 

        plt.show()
       

# -----------------------------------------------------------------------------

# ---------------------------------------------------------------------
# full wave structures
# ---------------------------------------------------------------------

# more plotting settings

csfont = {'fontname':'Sans'}

#frame = {'axes.linewidth':4, 'axes.edgecolor':cval}#, 'xtick.color':cval, 'ytick.color':cval}
frame = {'axes.linewidth':1, 'axes.edgecolor':'k'}#cevap[-1]}#, 'xtick.color':cval, 'ytick.color':cval} (153/255,153/255,153/255)

structureplot = True

def structureplotcustom(ax):
#    mpl.rc('font',size=22)
    ax.set_xlabel('kx')
    ax.set_ylabel('pressure (hPa)')
    ax.set_xticks([])
    if structureplot == True:
        ax.set_xlabel('kx')
        ax.set_xticks([])#0,np.pi,2*np.pi])
        #ax.set_xticklabels([-int(wl[i_maxunstab[eps1_index,eps2_index]]/2*1000),0,int(wl[i_maxunstab[eps1_index,eps2_index]]/2*1000)])
        ax.set_ylabel('pressure (hPa)')
#        ax.set_yscale('log')
        ax.set_yticks([0,.25,.4,.9,1])###
        ax.set_yticklabels(['0','250','400','900','1000'])###
        ax.tick_params(axis='both')
        ax.set_title('')  
    ax.invert_yaxis()

# transition to z coordinates
R = 287
Tref = 273
g = 10
z = np.insert(-R*Tref/g*np.log(p[1:nrws]/1),0,np.array([nan]))

# -----------------------------------------------------------------------------

### plotting streamfunction ------------------------------------------------------

def plot_psi_structure():

    with plt.rc_context(frame):
        fig, (ax0) = plt.subplots(1, figsize=(8,7.2), dpi=300)#10,9

        norm = MidpointNormalize(midpoint=0)

        psiplot = ax0.contourf(kx, p[:nrws], psi, lev, cmap=cm_br, norm=norm, origin='lower')
        ax0.contour(kx, p[:nrws], T[eps1_index,eps2_index], (np.linspace(-np.max(T),-np.max(T)/12,6)), colors='k')
        ax0.contour(kx, p[:nrws], T[eps1_index,eps2_index], (np.linspace(np.max(T)/12,np.max(T),6)), colors='k')
        wplot = ax0.contour(kx, p[:nrws], w,  10, colors='grey')
                
#        ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,-1]==np.max(T[eps1_index,eps2_index,-1 ]))[0][0]],p[-4],'o',ms=30,c=(.8,.8,.8),markeredgecolor='k')
#        ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,jtrop+1]-T[eps1_index,eps2_index,jtrop-1]==np.min(T[eps1_index,eps2_index,jtrop+1]-T[eps1_index,eps2_index,jtrop-1]))[0][0]],p[jtrop],'o',ms=30,c=(.8,.8,.8),markeredgecolor='k')
#        ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,-1]==np.max(T[eps1_index,eps2_index,-1 ]))[0][0]],p[-4],'+',ms=20,c='k',markeredgecolor='k')
#        ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,jtrop+1]-T[eps1_index,eps2_index,jtrop-1]==np.min(T[eps1_index,eps2_index,jtrop+1]-T[eps1_index,eps2_index,jtrop-1]))[0][0]],p[jtrop],'+',ms=20,c='k',markeredgecolor='k')
#        ax0.axvline(kx[-1]/2,c='grey',lw=5,ls='--')
#        ax0.axvline(kx[-1]/4,c='grey',lw=5,ls='--')
#        ax0.axvline(kx[-1]*3/4,c='grey',lw=5,ls='--')
            
        structureplotcustom(ax0)
        ax0.tick_params(which='both', length=6, width=1)
#        ax0.set_ylabel('p [hPa]')
#        plt.text(-.78,.142,'a)')
#        ax0.set_ylim(1,0)
        #ax0.axhline(ptrop,c='y')
        try:
            tropup_index
        except:
            pass
        else:
            ax0.axhline(p[tropup_index],c='y')
            ax0.axhline(p[tropdown_index],c='y')
        #ax0.axhline(p[np.argwhere(dqdy == np.max(dqdy[1:-1]))[-1][0]],c='y',ls='--')
        #ax0.set_ylabel('')

        ax0.text(-1.35,0.019,'(a)')
                
        fig.tight_layout()
        fig.savefig(f'/home/kfl078/Downloads/structure_psi.pdf', transparent=True)
        
        
    if unstab2 == True:
        with plt.rc_context(frame):
            fig, (ax1) = plt.subplots(1, figsize=(10,9), dpi=300)
#            fig, (ax1) = plt.subplots(figsize=((4.4,3.7)))
            psiplot2 = ax1.contourf(kx, p[:nrws], psi2, lev, cmap=cm_br, origin='lower')
            ax1.contour(kx, p[:nrws], T2[eps1_index,eps2_index], (np.linspace(-np.max(T2),-np.max(T2)/12,6)), colors='k')
            ax1.contour(kx, p[:nrws], T2[eps1_index,eps2_index], (np.linspace(np.max(T2)/12,np.max(T2),6)), colors='k')
            ax1.contour(kx, p[:nrws], w2,  10, colors='grey')
            structureplotcustom(ax1)
            if structureplot == True:
                #ax1.set_xlabel(' ')
                ax1.set_xticklabels(['0','0','0'])
                plt.setp(ax1.get_xticklabels(), color='w')
            ax1.axhline(ptrop,c='y')
            try:
                tropup_index
            except:
                pass
            else:
                ax1.axhline(p[tropup_index],c='y')
                ax1.axhline(p[tropdown_index],c='y')
            fig.tight_layout()
            
    if unstab3 == True:
        with plt.rc_context(frame):
            fig, (ax1) = plt.subplots(1, figsize=(10,9), dpi=300)
            psiplot3 = ax1.contourf(kx, p[:nrws], psi3, lev, cmap=cm_br, origin='lower')
            ax1.contour(kx, p[:nrws], T3[eps1_index,eps2_index], (np.linspace(-np.max(T3),-np.max(T3)/12,6)), colors='k')
            ax1.contour(kx, p[:nrws], T3[eps1_index,eps2_index], (np.linspace(np.max(T3)/12,np.max(T3),6)), colors='k')
            ax1.contour(kx, p[:nrws], w3,  10, colors='grey')
            structureplotcustom(ax1)
            #ax1.set_ylabel('')
            ax1.axhline(ptrop,c='y')
            try:
                tropup_index
            except:
                pass
            else:
                ax1.axhline(p[tropup_index],c='y')
                ax1.axhline(p[tropdown_index],c='y')
            fig.tight_layout()

    if stab == True:
        with plt.rc_context(frame):
            fig, (ax1) = plt.subplots(figsize=(6,4))
            psiplot_s2 = ax1.contourf(kx, p[:nrws], psi_s[eps1_index], lev, cmap=cm_br, origin='lower')
            ax1.set_title('Structure of (stable) streamfunction $\mathregular{\Psi}$ with a wavelength of %d km' %(wl[i_maxstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
            structureplotcustom(ax1)
        
    if stab2 == True:
        with plt.rc_context(frame):
            fig, (ax1) = plt.subplots(figsize=(6,4))
            psiplot_s2 = ax1.contourf(kx, p[:nrws], psi_s2[eps1_index], lev, cmap=cm_br, origin='lower')
            ax1.set_title('Structure of (stable) streamfunction $\mathregular{\Psi}$ with a wavelength of %d km' %(wl[i_maxstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
            structureplotcustom(ax1)
        
    if stab3 == True:
        with plt.rc_context(frame):
            fig, (ax1) = plt.subplots(figsize=(6,4))
            psiplot_s2 = ax1.contourf(kx, p[:nrws], psi_s3[eps1_index], lev, cmap=cm_br, origin='lower')
            ax1.set_title('Structure of (stable) streamfunction $\mathregular{\Psi}$ with a wavelength of %d km' %(wl[i_maxstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
            structureplotcustom(ax1)
        
    plt.show()

# -----------------------------------------------------------------------------

### plotting omega vertical velocity -------------------------------------------------

def plot_omega_structure():

    lev = 20
    omegacomp = True

    with plt.rc_context(frame):
        
        fig, (ax0) = plt.subplots(1, figsize=(10,9), dpi=300)           
        
        if omegacomp == False:
            wplot = ax0.contourf(kx, p[:nrws], w,  lev, cmap=cm_br)
            #wplot = ax0.contourf(kx, p[:nrws], v, lev, cmap=cm_br, origin='lower', hold='on')
    #        wplot = ax0.contourf(kx, p[:nrws], w, lev, cmap=cm_br, origin='lower', hold='on')
            #CS = ax0.contour(kx, p[:nrws], ((wd[0,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real, int(lev/2), colors='k', hold='on')
            #cbar = plt.colorbar(wplot, ax = ax0)
            #cbar.locator = ticker.MaxNLocator(nbins=8)
            #plt.clabel(CS, inline=1, fontsize=10)
            #cbar.update_ticks()
            if heating1 == True or heating2 == True:
                CS1 = ax0.contour(kx, p[:nrws], Q, (np.linspace(-np.max(Q)*.9,-np.max(Q)/12,4)), colors='k')
                CS2 = ax0.contour(kx, p[:nrws], Q*p[:nrws,np.newaxis], (np.linspace(-np.max(Q*p[:nrws,np.newaxis])*.9,-np.max(Q*p[:nrws,np.newaxis])/12,4)), colors='grey', linewidths=2.5)    #psiplot2 = ax0.contour(psiplot, levels=psiplot.levels[::c/2], colors='k', hold='on')
                ax0.contour(kx, p[:nrws], Q, (np.linspace(np.max(Q)/12,np.max(Q)*.9,4)), colors='k')
                ax0.contour(kx, p[:nrws], Q*p[:nrws,np.newaxis], (np.linspace(np.max(Q*p[:nrws,np.newaxis])/12,np.max(Q*p[:nrws,np.newaxis])*.9,4)), colors='grey', linewidths=2.5)    #psiplot2 = ax0.contour(psiplot, levels=psiplot.levels[::c/2], colors='k', hold='on')
            try:
                CS1
            except:
                pass
            else:
                for c1 in CS1.collections:
                    c1.set_dashes([(0,(5.,5.))])
                for c2 in CS2.collections:
                    c2.set_dashes([(0,(5.,5.))])
        if omegacomp == True:
            wplot = ax0.contourf(kx, p[:nrws], ((wd[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real, lev, cmap=cm_br)
            #wplot = ax0.contourf(kx, p[:nrws], ((whc[0,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real, lev, cmap=cm_br, origin='lower',hold='on')
        #psiplot2 = ax0.contour(psiplot, levels=psiplot.levels[::c/2],colors='k', hold='on')
            ax0.contour(kx, p[:nrws], T[eps1_index,eps2_index], (np.linspace(-np.max(T),-np.max(T)/12,6)), colors='k')
            ax0.contour(kx, p[:nrws], T[eps1_index,eps2_index], (np.linspace(np.max(T)/12,np.max(T),6)), colors='k')
            cbar = plt.colorbar(wplot, ax = ax0)
            cbar.locator = ticker.MaxNLocator(nbins=8)
            cbar.update_ticks()
            #for label in cbar.ax.yaxis.get_ticklabels()[:]:
            #    label.set_visible(False)
            #for label in cbar.ax.yaxis.get_ticklabels()[::4]:
            #    label.set_visible(True)
            leva = (np.linspace(-np.max(((wh[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real),-np.max(((wh[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real)/8,4))
            levb = (np.linspace(np.max(((wh[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real)/8,np.max(((wh[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real),4))
            CSa = ax0.contour(kx, p[:nrws], ((wh[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real, leva, colors='k')
            CSb = ax0.contour(kx, p[:nrws], ((wh[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real, levb, colors='k')
            #plt.clabel(CSa, leva[-1::-2], inline=1, use_clabeltext=True)#, fontsize=10)
            #plt.clabel(CSb, levb[0::2], inline=1, use_clabeltext=True)#, fontsize=10)
            if evap == True:
                lev2a = (np.linspace(-5/4*np.max(((wc[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real),-np.max(((wc[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real)/4,3))
                lev2b = (np.linspace(np.max(((wc[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real)/4,5/4*np.max(((wc[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real),3))
                CS2a = ax0.contour(kx, p[:nrws], ((wc[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real, lev2a, colors='grey', linewidths=2, format='%1.5f')
                CS2b = ax0.contour(kx, p[:nrws], ((wc[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis])*exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j)).real, lev2b, colors='grey', linewidths=2)
                plt.clabel(CS2a, lev2a[-2::-2], inline=1, use_clabeltext=True)#, fontsize=10)
                plt.clabel(CS2b, lev2b[1::2], inline=1, use_clabeltext=True)#, fontsize=10)
        #cbar.locator = ticker.MaxNLocator(nbins=6)
        #cbar.update_ticks()
        #cbar.add_lines(psiplot2)
        #ax0.set_title('Structure of omega with a wavelength of %d km' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
        #ax0.set_title('$\mathregular{\\varepsilon}$ = %d, $\mathregular{\gamma}$ = %1.1f' %(epsilon1[eps1_index],abs(1-hblcstep)))#, fontsize=18)
        structureplotcustom(ax0)
        if h1pro == True and h1proc == False or evap == False:
            #ax0.set_xlabel('')
            ax0.set_xticklabels(['0','0','0'])
            plt.setp(ax0.get_xticklabels(), color='w')
        ax0.tick_params(which='both', length=6, width=1)
        #plt.text(-.88,.142,'c)')
        plt.text(-1.15,.142,'a)')
        
        fig.tight_layout()
#        fig.savefig(f'/home/kfl078/Downloads/structure_omegacomp_epsilon12,5_gamma0,0.pdf', transparent=True)
            
    if unstab2 == True:
        fig, (ax1) = plt.subplots(figsize=(4.4,3.9))#(6,4))
        w2plot = ax1.contourf(kx, p[:nrws], w2, lev, cmap=cm_br)
        ax1.contour(kx, p[:nrws], w2, 1, colors='k')
        ax1.set_title('Structure of omega with a wavelength of %d km' %(wl[i_maxunstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)

    if unstab3 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        w2plot = ax1.contourf(kx, p[:nrws], w3, lev, cmap=cm_br)
        ax1.set_title('Structure of omega with a wavelength of %d km' %(wl[i_maxunstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)

    if stab == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        w2plot = ax1.contourf(kx, p[:nrws], w_s, lev, cmap=cm_br)
        ax1.set_title('Structure of (stable) omega with a wavelength of %d km' %(wl[i_maxstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)  
        
    if stab2 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        w2plot = ax1.contourf(kx, p[:nrws], w_s2, lev, cmap=cm_br)
        ax1.set_title('Structure of (stable) omega with a wavelength of %d km' %(wl[i_maxstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1) 
        
    if stab3 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        w2plot = ax1.contourf(kx, p[:nrws], w_s3, lev, cmap=cm_br)
        ax1.set_title('Structure of (stable) omega with a wavelength of %d km' %(wl[i_maxstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)   

    plt.show()

# -----------------------------------------------------------------------------

### plotting omega vertical velocity -------------------------------------------------

def plot_omega_components_structure():

    wdstruc = (wd[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    whstruc = (wh[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    wfstruc = (wf[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],:,np.newaxis]*np.exp((kx[np.newaxis,:]+kx[np.newaxis,shift])*1j) ).real
    
    with plt.rc_context(frame):
        
        fig, ((ax0,ax1),(ax2,ax3)) = plt.subplots(2,2, figsize=(15,12))           
        
        wplot = ax0.contourf(kx, p[:nrws], w,  lev, cmap=cm_br)
        cbar = plt.colorbar(wplot, ax = ax0)
        #cbar.locator = ticker.MaxNLocator(nbins=8)
        #cbar.update_ticks()
        wplot = ax1.contourf(kx, p[:nrws], wdstruc,  lev, cmap=cm_br)
        cbar = plt.colorbar(wplot, ax = ax1)
        wplot = ax2.contourf(kx, p[:nrws], whstruc,  lev, cmap=cm_br)
        cbar = plt.colorbar(wplot, ax = ax2)
        wplot = ax3.contourf(kx, p[:nrws], wfstruc,  lev, cmap=cm_br)
        cbar = plt.colorbar(wplot, ax = ax3)
        structureplotcustom(ax0)
        structureplotcustom(ax1)
        structureplotcustom(ax2)
        structureplotcustom(ax3)
        ax0.tick_params(which='both', length=6, width=1)
        plt.tight_layout()

    plt.show()

# -----------------------------------------------------------------------------

### plotting meridional velocity -------------------------------------------------

def plot_v_structure():

    fig, (ax0) = plt.subplots(figsize=(8,6))
        
    vplot = ax0.contourf(kx, p[:nrws], v, lev, cmap=cm_br, origin='lower')
    ax0.set_title('Structure of meridional velocity with a wavelength of %d km' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
    structureplotcustom(ax0)
    plt.colorbar(vplot,ax=ax0)

    if unstab2 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        v2plot = ax1.contourf(kx, p[:nrws], v2, lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of meridional velocity with a wavelength of %d km' %(wl[i_maxunstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)
        plt.colorbar(v2plot,ax=ax1)
        
    if unstab3 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], v3, lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of meridional velocity with a wavelength of %d km' %(wl[i_maxunstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)

    if stab == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], v_s, lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of (stable) meridional velocity with a wavelength of %d km' %(wl[i_maxstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)
        
    if stab2 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], v_s2, lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of (stable) meridional velocity with a wavelength of %d km' %(wl[i_maxstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)
        
    if stab3 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], v_s3, lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of (stable) meridional velocity with a wavelength of %d km' %(wl[i_maxstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)
        
    plt.show()

# -----------------------------------------------------------------------------

### plotting temperature -------------------------------------------------

def plot_T_structure():

    fig, (ax0) = plt.subplots(figsize=(8,6))
    ax0.contourf(kx, p[:nrws], T[eps1_index,eps2_index], lev, cmap=cm_br, origin='lower')
    ax0.set_title('Structure of temperature with a wavelength of %d km' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
    structureplotcustom(ax0)

    if unstab2 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], T2[eps1_index,eps2_index], lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of temperature with a wavelength of %d km' %(wl[i_maxunstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)
        
    if unstab3 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], T3[eps1_index,eps2_index], lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of temperature with a wavelength of %d km' %(wl[i_maxunstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)

    if stab == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], T_s[eps1_index,eps2_index], lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of temperature with a wavelength of %d km' %(wl[i_maxstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)
        
    if stab2 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], T_s2[eps1_index,eps2_index], lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of temperature with a wavelength of %d km' %(wl[i_maxstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)
        
    if stab3 == True:
        fig, (ax1) = plt.subplots(figsize=(6,4))
        ax1.contourf(kx, p[:nrws], T_s3[eps1_index,eps2_index], lev, cmap=cm_br, origin='lower')
        ax1.set_title('Structure of temperature with a wavelength of %d km' %(wl[i_maxstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax1)

    plt.show()

# -----------------------------------------------------------------------------

### plotting total stability -------------------------------------------------

def plot_Stot_structure():

    fig, (ax0) = plt.subplots(figsize=(6,4))
    ax0.contourf(kx, p[:nrws], (Stot2+Stot3)[eps1_index], lev, cmap=cm_br)
    #ax0.set_title('Structure of temperature with a wavelength of %d km' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
    structureplotcustom(ax0)

    fig, (ax0) = plt.subplots(figsize=(6,4))
    ax0.contourf(kx, p[:nrws], Stot2[eps1_index], lev, cmap=cm_br)
    structureplotcustom(ax0)

    fig, (ax0) = plt.subplots(figsize=(6,4))
    ax0.contourf(kx, p[:nrws], Stot3[eps1_index], lev, cmap=cm_br)
    structureplotcustom(ax0)

    plt.show()

# -----------------------------------------------------------------------------

### plotting phase and amplitude of potential temperature -----------------------

def plot_theta_phase_and_amplitude():
    
    phase_T = phase(tempcalc(psi_maxunstab)[eps1_index,eps2_index,1:-1]*np.exp(-p[1:nrws-1]))
#    phase_T = phase(tempcalc(psi_maxunstab)[eps1_index,eps2_index,1:-1])#T[1:-1,0])
    if unstab2 == True:
        phase_T2 = phase(T2[eps1_index,eps2_index,1:-1,0]*np.exp(-p[1:nrws-1]))
    
    fig, (ax1) = plt.subplots(1, figsize=(6,4))
    ax1.plot(phase_T,p[1:nrws-1], 'g--', linewidth=2)
    if unstab2 == True:
        ax1.plot(phase_T2,p[1:nrws-1], 'g--', linewidth=.5)
    ax1.set_xlabel('Phase angle (rad)')
    ax1.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
    ax1.set_xticklabels(['-2$\mathregular{\pi}$','-$\mathregular{\pi}$', '0', '$\mathregular{\pi}$', '2$\mathregular{\pi}$',])
    ax2 = ax1.twiny()
    ax2.plot(abs(tempcalc(psi_maxunstab)[eps1_index,eps2_index,:]*np.exp(-p[:nrws]))/max(abs(tempcalc(psi_maxunstab)[eps1_index,eps2_index,:]*np.exp(-p[:nrws]))),p[:nrws], 'g', linewidth=2)
    if unstab2 == True:
        ax2.plot(abs(T2[eps1_index,eps2_index,:,0]*np.exp(-p[:nrws]))/max(abs(T2[eps1_index,eps2_index,:,0]*np.exp(-p[:nrws]))),p[:nrws], 'g', linewidth=.5)
    ax2.set_xlabel('Amplitude')
    ax2.invert_yaxis()

    if unstab2 == False:
        ax2.plot((),(),'g',label='Amplitude', linewidth=2)
        ax2.plot((),(),'g', linestyle='--',label='Phase', linewidth=2)
    else:
        ax2.plot((),(),'g-',label='$\\theta$', linewidth=2)
        ax2.plot((),(),'grey',label='Amplitude', linewidth=1.3)
        ax2.plot((),(),'g-',label='$\\theta_2$', linewidth=.5)
        ax2.plot((),(),'grey', linestyle='--',label='Phase')
    ax2.legend(bbox_to_anchor=(0.5,-0.2), loc='upper center',
               ncol=2, fancybox=True)

    plt.show()
    
# -----------------------------------------------------------------------------

### plotting zonal velocity -------------------------------------------------

def plot_u_structure():

    fig, (ax0) = plt.subplots(figsize=(6,4))
    uplot = ax0.contourf(kx, p[:nrws], ua, lev, cmap=cm_br)
    #cbar = plt.colorbar(uplot, ax = ax0)
    ax0.set_title('Structure of zonal velocity with a wavelength of %d km' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
    structureplotcustom(ax0)

    if unstab2 == True:
        fig, (ax0) = plt.subplots(figsize=(6,4))
        uplot = ax0.contourf(kx, p[:nrws], ua2, lev, cmap=cm_br)
        ax0.set_title('Structure of zonal velocity with a wavelength of %d km' %(wl[i_maxunstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)

    if unstab3 == True:
        fig, (ax0) = plt.subplots(figsize=(6,4))
        uplot = ax0.contourf(kx, p[:nrws], ua3, lev, cmap=cm_br)
        ax0.set_title('Structure of zonal velocity with a wavelength of %d km' %(wl[i_maxunstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
        
    plt.show()

# -----------------------------------------------------------------------------

### plotting diabatic heating ---------------------------------------------------

def plot_Q_structure():

    if heating1 == True or heating1 == False:

        blobs = True

        mrot = mpl.markers.MarkerStyle(marker='_')
        mrot._transform = mrot.get_transform().rotate_deg(45)
        prot = mpl.markers.MarkerStyle(marker='+')
        prot._transform = prot.get_transform().rotate_deg(45)

        fig, (ax0) = plt.subplots(figsize=(8,6.1), dpi=300)
        
#        ax0.contourf(kx, p[:nrws], psi, lev, cmap=cm_br)
#        ax0.plot(kx[([np.argwhere(T[eps1_index,eps2_index,j]>=.99*np.max(T[eps1_index,eps2_index,j]))[-1][0] for j in range(jtlc)])],p[:jtlc],c=c[2],ls=':',lw=5)        
#        ax0.plot(kx[([np.argwhere(T[eps1_index,eps2_index,j]>=.99*np.max(T[eps1_index,eps2_index,j]))[-1][0] for j in range(jtlc+1,jblc)])],p[jtlc+1:jblc],c=c[2],ls=':',lw=5)        
#        ax0.plot(kx[([np.argwhere(T[eps1_index,eps2_index,j]>=.99*np.max(T[eps1_index,eps2_index,j]))[-1][0] for j in range(jblc+1,nrws)])],p[jblc+1:nrws],c=c[2],ls=':',lw=5)        

    #    ax0.contourf(kx, p[:jblc+5], Q[:jblc+5], lev, cmap=cm_br, origin='lower', hold='on')
    #    ax0.contourf(kx, p[jblc+5:nrws], Q[jblc+5:], lev, cmap=cm_br, origin='lower', hold='on')
#        ax0.contourf(kx, p[:jblc], Q[:jblc], lev, cmap=cm_br)
#        ax0.contourf(kx, p[jtsf:nrws], Q[jtsf:], cmap=cm_br)        
        if heating1 == True or heating2 == True:
            ax0.contour(kx, p[:jblc+2], Q[:jblc+2], 8, colors='k',linewidths=1.5)
            ax0.contour(kx, p[jtsf+1:nrws], Q[jtsf+1:], 8, colors=[(.55,.55,.55)],linewidths=2.5)        
        ax0.contour(kx, p[:nrws], v, 18, colors='y',linewidths=1.5)
        ax0.contourf(kx, p[:nrws], T[eps1_index,eps2_index], lev, cmap=cm_br)
#        ax0.plot(kx[([np.argwhere(-w[j]==np.max(-w[j]))[0][0] for j in range(1,nrws-1)])],p[1:nrws-1],'grey',ls=':',lw=5)
#        ax0.plot(kx[([np.argwhere(v[j]==np.max(v[j]))[0][0] for j in range(nrws)])],p[:nrws],'y:',lw=5)
#        ax0.plot(kx[([np.argwhere(T[eps1_index,eps2_index,j]>=.99*np.max(T[eps1_index,eps2_index,j]))[-1][0] for j in range(nrws)])],p[:nrws],c=c[2],ls=':',lw=5)
#        ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,0]==max(T[eps1_index,eps2_index,0]))[0][0]],p[2],'*',ms=10,c=c[2])
#        ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,-1]==max(T[eps1_index,eps2_index,-1]))[0][0]],p[-3],'*',ms=10,c=c[2])
        if heating1 == True:
#            ax0.plot(kx[np.argwhere((T[eps1_index,eps2_index,jtlc-1]-T[eps1_index,eps2_index,jtlc+1])==max((T[eps1_index,eps2_index,jtlc-1]-T[eps1_index,eps2_index,jtlc+1])))[0][0]],p[jtlc],'o',ms=40,c='grey',markeredgecolor='k')
            if blobs == True:
                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jtlc]==max(PV_u[eps1_index,eps2_index,jtlc]))[0][0]],p[jtlc],'o',ms=30,c=(.3,.3,.3),markeredgecolor='k')
                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jtlc]==min(PV_u[eps1_index,eps2_index,jtlc]))[0][0]],p[jtlc],'o',ms=30,c=(.8,.8,.8),markeredgecolor='k')
#                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jtlc]==min(PV_u[eps1_index,eps2_index,jtlc]))[0][0]],p[jtlc], marker=u'$\u25CC$',ms=30,c='k',markeredgecolor='k')
            else:
                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jtlc]==max(PV_u[eps1_index,eps2_index,jtlc]))[0][0]],p[jtlc],'o',ms=25,c='w',markeredgecolor='k')            
                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jtlc]==max(PV_u[eps1_index,eps2_index,jtlc]))[0][0]],p[jtlc],'+',ms=20,mew=2,c='k')            
            if blobs == True:
                ax0.plot(kx[np.argwhere((Q[jtlc-1]-Q[jtlc+1])==np.min(Q[jtlc-1]-Q[jtlc+1]))[0][0]],p[jtlc],'o',ms=22,c='w',markeredgecolor='k')
                ax0.plot(kx[np.argwhere((Q[jtlc-1]-Q[jtlc+1])==np.min(Q[jtlc-1]-Q[jtlc+1]))[0][0]],p[jtlc],'_',mew=2,ms=17,c='k')
                ax0.plot(kx[np.argwhere((Q[jtlc-1]-Q[jtlc+1])==np.max(Q[jtlc-1]-Q[jtlc+1]))[0][0]],p[jtlc],'o',ms=22,c='w',markeredgecolor='k')
                ax0.plot(kx[np.argwhere((Q[jtlc-1]-Q[jtlc+1])==np.max(Q[jtlc-1]-Q[jtlc+1]))[0][0]],p[jtlc],'+',mew=2,ms=17,c='k')
        if heating1 == True or heating2 == True:
#            ax0.plot(kx[np.argwhere((T[eps1_index,eps2_index,jblc-1]-T[eps1_index,eps2_index,jblc+1])==max((T[eps1_index,eps2_index,jblc-1]-T[eps1_index,eps2_index,jblc+1])))[0][0]],p[jblc],'o',ms=40,c='grey',markeredgecolor='k')
            if blobs == True:
                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jblc]==max(PV_u[eps1_index,eps2_index,jblc]))[0][0]],p[jblc],'o',ms=30,c=(.3,.3,.3),markeredgecolor='k')
                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jblc]==min(PV_u[eps1_index,eps2_index,jblc]))[0][0]],p[jblc],'o',ms=30,c=(.8,.8,.8),markeredgecolor='k')
            else:
                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jblc]==max(PV_u[eps1_index,eps2_index,jblc]))[0][0]],p[jblc],'o',ms=25,c='w',markeredgecolor='k')
                ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,jblc]==max(PV_u[eps1_index,eps2_index,jblc]))[0][0]],p[jblc],'+',ms=20,mew=2,c='k')
            if blobs == True:
                ax0.plot(kx[np.argwhere((Q[jblc-1]-Q[jblc+1])==np.min(Q[jblc-1]-Q[jblc+1]))[0][0]],p[jblc],'o',ms=22,c='w',markeredgecolor='k')
                ax0.plot(kx[np.argwhere((Q[jblc-1]-Q[jblc+1])==np.min(Q[jblc-1]-Q[jblc+1]))[0][0]],p[jblc],'_',mew=2,ms=17,c='k')
                ax0.plot(kx[np.argwhere((Q[jblc-1]-Q[jblc+1])==np.max(Q[jblc-1]-Q[jblc+1]))[0][0]],p[jblc],'o',ms=22,c='w',markeredgecolor='k')
                ax0.plot(kx[np.argwhere((Q[jblc-1]-Q[jblc+1])==np.max(Q[jblc-1]-Q[jblc+1]))[0][0]],p[jblc],'+',mew=2,ms=17,c='k')
        #ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,0]==max(PV_u[eps1_index,eps2_index,0]))[0][0]],p[2],'o',ms=10,c='k')
        #ax0.plot(kx[np.argwhere(PV_u[eps1_index,eps2_index,-1]==max(PV_u[eps1_index,eps2_index,-1]))[0][0]],p[-3],'o',ms=10,c='k')
        if blobs == True:
            ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,0]<=.99*min(T[eps1_index,eps2_index,0]))[0][0]],p[3],'o',ms=30,c=(.3,.3,.3),markeredgecolor='k')
            ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,-1]==max(T[eps1_index,eps2_index,-1 ]))[0][0]],p[-4],'o',ms=30,c=(.3,.3,.3),markeredgecolor='k')
            ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,0]>=.99*max(T[eps1_index,eps2_index,0]))[0][0]],p[3],'o',ms=30,c=(.8,.8,.8),markeredgecolor='k')
            ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,-1]==min(T[eps1_index,eps2_index,-1 ]))[0][0]],p[-4],'o',ms=30,c=(.8,.8,.8),markeredgecolor='k')
        else:
            ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,0]<=.99*min(T[eps1_index,eps2_index,0]))[0][0]],p[3],'o',ms=25,c='w',markeredgecolor='k')
            ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,0]<=.99*min(T[eps1_index,eps2_index,0]))[0][0]],p[3],'+',mew=2,ms=20,c='k')
            ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,-1]==max(T[eps1_index,eps2_index,-1 ]))[0][0]],p[-4],'o',ms=25,c='w',markeredgecolor='k')
            ax0.plot(kx[np.argwhere(T[eps1_index,eps2_index,-1]==max(T[eps1_index,eps2_index,-1 ]))[0][0]],p[-4],'+',mew=2,ms=20,c='k')
        if heating2 == True and blobs == True:
#            ax0.plot(kx[np.argwhere((Q[-1])==np.min(Q[-1]))[0][0]],p[-3],marker=u'$\u25CC$',ms=20,c='w',markeredgecolor='k')
            ax0.plot(kx[np.argwhere((Q[-1])==np.min(Q[-1]))[0][0]],p[-4],'o',ms=22,c='w',markeredgecolor='k')
            ax0.plot(kx[np.argwhere((Q[-1])==np.min(Q[-1]))[0][0]],p[-4],'_',mew=2,ms=17,c='k')
            ax0.plot(kx[np.argwhere((Q[-1])==np.max(Q[-1]))[0][0]],p[-4],'o',ms=22,c='w',markeredgecolor='k')
            ax0.plot(kx[np.argwhere((Q[-1])==np.max(Q[-1]))[0][0]],p[-4],'+',mew=2,ms=17,c='k')
        if blobs == True:
            ax0.plot(kx[np.argwhere((v[-1])==np.max(v[-1]))[0][0]],p[-4],'o',ms=22,c='None',alpha=1,markeredgecolor='k')
            ax0.plot(kx[np.argwhere((v[-1])==np.max(v[-1]))[0][0]],p[-4],'o',ms=22,c='w',alpha=.2,markeredgecolor='k')
            ax0.plot(kx[np.argwhere((v[-1])==np.max(v[-1]))[0][0]],p[-4],'x',mew=2,ms=14,c='k')
            ax0.plot(kx[np.argwhere((v[-1])==np.min(v[-1]))[0][0]],p[-4],'o',ms=22,c='None',alpha=1,markeredgecolor='k')
            ax0.plot(kx[np.argwhere((v[-1])==np.min(v[-1]))[0][0]],p[-4],'o',ms=22,c='w',alpha=.2,markeredgecolor='k')
            ax0.plot(kx[np.argwhere((v[-1])==np.min(v[-1]))[0][0]],p[-4],marker=(2, 0, -45),mew=2,ms=17,c='k')
            ax0.plot(kx[np.argwhere((v[0])==np.max(v[0]))[0][0]],p[3],'o',ms=22,c='None',alpha=1,markeredgecolor='k')
            ax0.plot(kx[np.argwhere((v[0])==np.max(v[0]))[0][0]],p[3],'o',ms=22,c='w',alpha=.2,markeredgecolor='k')
            ax0.plot(kx[np.argwhere((v[0])==np.max(v[0]))[0][0]],p[3],marker=(2, 0, -45),mew=2,ms=17,c='k')
            ax0.plot(kx[np.argwhere((v[0])==np.min(v[0]))[0][0]],p[3],'o',ms=22,c='None',alpha=1,markeredgecolor='k')
            ax0.plot(kx[np.argwhere((v[0])==np.min(v[0]))[0][0]],p[3],'o',ms=22,c='w',alpha=.2,markeredgecolor='k')
            ax0.plot(kx[np.argwhere((v[0])==np.min(v[0]))[0][0]],p[3],'x',mew=2,ms=14,c='k')
            #ax0.scatter((kx[np.argwhere((v[0])==np.min(v[0]))[0][0]]),(p[2]),100,marker='+',c='k')

#        ax0.plot(kx[np.argwhere(w[jtml]==max(w[jtml]))[0][0]],p[jtml],'*',ms=10,c='k')
        ax0.set_title('Structure of the diabatic heating with a wavelength of %d km' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
#        ax0.set_ylim(1,.9)
                
        if heating1 == False and heating2 == False:
            plt.text(-1.15,.19,'a)')
            plt.text(1.9*np.pi,.17,'$\mathregular{Eady}$',horizontalalignment='right',verticalalignment='top', bbox=dict(facecolor='w', alpha=.8), fontsize=24)
            plt.xlabel('')
        if heating1 == True and heating2 == False:
            plt.text(-1.15,.19,'b)')
            plt.text(1.9*np.pi,.17,'$\mathregular{lh}$',horizontalalignment='right',verticalalignment='top', bbox=dict(facecolor='w', alpha=.8), fontsize=24)
            plt.xlabel('')
            plt.ylabel('')
        if heating2 == True and vpar == False and wpar == False:
            plt.text(-1.15,.19,'c)')
            plt.text(1.9*np.pi,.17,'$\mathregular{T_s}$',horizontalalignment='right',verticalalignment='top', bbox=dict(facecolor='w', alpha=.8), fontsize=24)
        if heating2 == True and vpar == True and wpar == False:# and epsilon2[0] == 2.2:
            plt.text(-1.15,.19,'d)')
            plt.text(1.9*np.pi,.17,'$\mathregular{v_s}$',horizontalalignment='right',verticalalignment='top', bbox=dict(facecolor='w', alpha=.8), fontsize=24)
            plt.ylabel('')
        if heating2 == True and vpar == False and wpar == True and (epsilon2[0]).real > 0:
            plt.text(-1.15,.19,'a)')
            plt.text(1.9*np.pi,.17,'$\mathregular{\omega_{\\ast,0^\circ}}$',horizontalalignment='right',verticalalignment='top', bbox=dict(facecolor='w', alpha=.8), fontsize=24)
            plt.xlabel('')
        if heating2 == True and vpar == False and wpar == True and (epsilon2[0]).imag > 0:
            plt.text(-1.15,.19,'b)')
            plt.text(1.9*np.pi,.17,'$\mathregular{\omega_{\\ast,\\minus 90^\circ}}$',horizontalalignment='right',verticalalignment='top', bbox=dict(facecolor='w', alpha=.8), fontsize=24)
            plt.xlabel('')
            plt.ylabel('')
        if heating2 == True and vpar == False and wpar == True and (epsilon2[0]).imag < 0:
            plt.text(-1.15,.19,'c)')
            plt.text(1.9*np.pi,.17,'$\mathregular{\omega_{\\ast,\\plus 90^\circ}}$',horizontalalignment='right',verticalalignment='top', bbox=dict(facecolor='w', alpha=.8), fontsize=24)
        if heating2 == True and vpar == False and wpar == True and (epsilon2[0]).real < 0:
            plt.text(-1.15,.19,'d)')
            plt.text(1.9*np.pi,.17,'$\mathregular{\omega_{\\ast,180^\circ}}$',horizontalalignment='right',verticalalignment='top', bbox=dict(facecolor='w', alpha=.8), fontsize=24)
            plt.ylabel('')        
        
        # test if ratio between lh and sf is reasonable
        # 100 W/m^2 corresponds to ~10 K/day, ratio should therefore probably not exceed ~3 (ratio=2 ideal?)
        if heating2 == True and vpar == False and wpar == True:
            print ('ratio between max lh and max sf:', np.max(abs(Q[:jblc]))/np.max(abs(Q[jtsf+1:])))
        elif heating2 == True and vpar == True and wpar == False:
            print ('ratio between max lh and max sf:', np.max(abs(Q[:jblc]))/np.max(abs(Q[jtsf+1:])))#/30*10) # R/fp~30, 10 because of difference in dimensions when using v instead of T  #*(10**-1/(3*10**3))/(10/10**5)   *10**2/3/10**2) # /10**2 because of different dimension of v relative to w.  *10**2/3 because of different dimension of epsilon.
        elif heating2 == True and vpar == False and wpar == False:
            print ('ratio between max lh and max sf:', np.max(abs(Q[:jblc]))/np.max(abs(Q[jtsf+1:])))#/30) #*10**2/3/10**3)
        
                
        if unstab2 == True:
            fig, (ax1) = plt.subplots(figsize=(8,6))
    #        Q2 = Qcalc(w2[jtml,0],T2[eps1_index,-1,0],psi2[-1,0],i_maxunstab2)
            ax1.contour(kx, p[:jblc+2], Q2[:jblc+2], 8, colors='k',linewidths=1.5)
            ax1.contour(kx, p[jtsf+1:nrws], Q2[jtsf+1:], 8, colors='grey',linewidths=1.5)        
            ax1.contour(kx, p[:nrws], v2, 10, colors='y',linewidths=1.5)
            ax1.contourf(kx, p[:nrws], T2[eps1_index,eps2_index], lev, cmap=cm_br)
            ax1.set_title('Structure of the diabatic heating with a wavelength of %d km' %(wl[i_maxunstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
            structureplotcustom(ax1)   

        if unstab3 == True:
            fig, (ax1) = plt.subplots(figsize=(8,6))
    #        Q3 = Qcalc(w3,T3[eps1_index,-1],psi[-1],i_maxunstab3)
            ax1.contour(kx, p[:jblc+1], Q3[:jblc+1], 18, colors='k',linewidths=1.5)
            ax1.contour(kx, p[jtsf:nrws], Q3[jtsf:], 8, colors='grey',linewidths=1.5)        
            ax1.contour(kx, p[:nrws], v3, 10, colors='y',linewidths=1.5)
            ax1.contourf(kx, p[:nrws], T3[eps1_index,eps2_index], lev, cmap=cm_br)
            ax1.set_title('Structure of the diabatic heating with a wavelength of %d km' %(wl[i_maxunstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
            structureplotcustom(ax1) 
        
        if stab == True:
            Q_s = Qcalc(w_s,T_s[eps1_index,-1],psi[-1],i_maxstab)
            fig, (ax1) = plt.subplots(figsize=(6,4))
            ax1.contourf(kx, p[:nrws], Q_s, lev, cmap=cm_br)
            ax1.set_title('Structure of the (stable) diabatic heating with a wavelength of %d km' %(wl[i_maxstab[eps1_index,eps2_index]]*1000))#, fontsize=16)
            structureplotcustom(ax1)
        
        if stab2 == True:
            Q_s2 = Qcalc(w_s2,T_s2[eps1_index,-1],psi[-1],i_maxstab2)
            fig, (ax1) = plt.subplots(figsize=(6,4))
            ax1.contourf(kx, p[:nrws], Q_s2, lev, cmap=cm_br)
            ax1.set_title('Structure of the (stable) diabatic heating with a wavelength of %d km' %(wl[i_maxstab2[eps1_index,eps2_index]]*1000))#, fontsize=16)
            structureplotcustom(ax1) 
        
        if stab3 == True:
            Q_s3 = Qcalc(w_s3,T_s3[eps1_index,-1],psi[-1],i_maxstab3)
            fig, (ax1) = plt.subplots(figsize=(6,4))
            ax1.contourf(kx, p[:nrws], Q_s3, lev, cmap=cm_br)
            ax1.set_title('Structure of the (stable) diabatic heating with a wavelength of %d km' %(wl[i_maxstab3[eps1_index,eps2_index]]*1000))#, fontsize=16)
            structureplotcustom(ax1)
        
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        plt.show()
#        if heating2 == True and wpar == False and vpar == False:
#            fig.savefig(f'/home/kfl078/Downloads/python/structure2_T{str(epsilon2[0])}_S4_ratio2.pdf', transparent=True)
#        elif heating2 == True and vpar == True:
#            fig.savefig(f'/home/kfl078/Downloads/python/structure2_v{str(epsilon2[0])}_S4_ratio2.pdf', transparent=True)
#        elif heating2 == True and wpar == True:
#            fig.savefig(f'/home/kfl078/Downloads/python/structure2_w{str(epsilon2[0])}_S4_ratio2.pdf', transparent=True)
#        elif heating1 == True and heating2 == False:
#            fig.savefig(f'/home/kfl078/Downloads/python/structure2_nf_S4_ratio2.pdf', transparent=True)
#        elif heating1 == False and heating2 == False:
#            fig.savefig(f'/home/kfl078/Downloads/python/structure2_dry_S4_ratio2.pdf', transparent=True)
        fig.savefig(f'/home/kfl078/Downloads/structure.pdf', transparent=True)
        
# -----------------------------------------------------------------------------

### plotting potential vorticity (and its components) --------------------------------

def plot_PV_structure():

    norm = MidpointNormalize(midpoint=0)

    two_subplots = True
    if two_subplots == True:
        fig = plt.figure(figsize=(15*4/5.4*.75, 7.2*.75)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1.3]) 
    else:
        fig = plt.figure(figsize=(15, 7.2))
        gs = gridspec.GridSpec(1, 3, width_ratios=[3, 1, 1.4]) 
        ax2 = plt.subplot(gs[2])
    ax0 = plt.subplot(gs[0])
    ax1 = plt.subplot(gs[1])
#    fig, (ax0,ax1) = plt.subplots(2, figsize=(10,9), dpi=300)

    PVplot = ax0.contourf(kx, p[:nrws], PV_u[eps1_index,eps2_index], lev, norm=norm, cmap=cm_br)
    ax0.contour(kx, p[:nrws], psi, colors='k')
    #fig.colorbar(PVplot)
#    ax0.set_ylim(0.14,1)
    #ax0.set_title('Structure of potential vorticity with a wavelength of %d km \n PV @ %1.1f = %1.1f, PV @ %1.1f = %1.1f, PV @ %1.1f = %1.1f, PV @ %1.1f = %1.1f' %(wl[i_maxunstab[eps1_index]]*1000, ptrop, np.max(PV[jtrop-5:jtrop+5]), ptlc, np.max(PV[jtlc-5:jtlc+5]), pblc, np.max(PV[jblc-5:jblc+5]), ps, np.max(PV[-5:])))#, fontsize=16)
    ax0.set_title('Structure of potential vorticity with a wavelength of %d km' %(wl[i_maxunstab[eps1_index]]*1000))
    structureplotcustom(ax0)
#    ax0.set_title('$\mathregular{\\varepsilon}$ = %d' %(epsilon1[eps1_index]), fontsize=18)
#    ax0.set_xlabel('%d km wavelength' %(wl[i_maxunstab[eps1_index]]*1000), fontsize=14)
    ax1.set_xlim([-.1*np.max(np.max(PV_u[eps1_index,eps2_index],axis=1)[1:-2]),1.1*np.max(np.max(PV_u[eps1_index,eps2_index],axis=1)[1:-2])])
    ax1.set_ylim(pt,ps)
    structureplotcustom(ax1)
    ax1.plot(np.max(PV_u[eps1_index,eps2_index],axis=1),p[:nrws], c='k')
    ax1.set_ylabel('')
    if two_subplots == False:
        ax0.set_xlabel('kx',labelpad=31)
        ax1.set_xlabel('PV amplitude',labelpad=31)
        for j in range(nrws):
            if np.max(PV_u[eps1_index,eps2_index,j]) > .01*np.max(PV_u[eps1_index,eps2_index]):
                ax2.scatter(360/len(kx)*np.argwhere(PV_u[eps1_index,eps2_index,j] == np.max(PV_u[eps1_index,eps2_index,j]))[0][0],p[j],c='k',alpha=.5,s=30+200*np.max(PV_u[eps1_index,eps2_index,j])/np.max(PV_u[eps1_index,eps2_index]))
        ax2.axvline(90,c='k',ls='--')
        ax2.axvline(180,c='k',ls='--')
        ax2.axvline(270,c='k',ls='--')
        structureplotcustom(ax2)
        ax2.set_xlabel('phase of max PV')
        ax2.set_xticks([0,90,180,270])
        ax1.set_ylim([1,0])
        ax2.set_ylim([1,0])
        ax2.set_ylabel('')
#        ax2.set_ylim(pt,ps)

        fig.tight_layout()
        ax0.text(-1.4,0.019,'(a)')
        ax1.text(-6,0.019,'(b)')
        ax2.text(-120,0.019,'(c)')
    
    else:
        ax0.set_xlabel('kx')#,labelpad=31)
        ax1.set_xlabel('PV amplitude')#,labelpad=31)
        ax1.set_yticklabels('')
        #fig.tight_layout()
        ax0.text(-1.95,0.019,'(a)')
        ax1.text(-1.,0.019,'(b)')

    fig.savefig(f'/home/kfl078/Downloads/structure_PV.pdf', transparent=True, bbox_inches='tight', pad_inches=0.1)
    
    fig, (ax0) = plt.subplots(1, figsize=(10,9), dpi=300)
    Cplot = ax0.contourf(kx, p[:nrws], PV3_u[eps1_index,eps2_index], lev, cmap=cm_br)
    fig.colorbar(Cplot)
#    ax0.set_ylim(0.14,1)
    ax0.set_title('Structure of $\mathregular{d^2\Psi/dx^2}$ with a wavelength of %d km' %(wl[i_maxunstab[eps1_index]]*1000))#, fontsize=16)
    structureplotcustom(ax0)

    fig, (ax0) = plt.subplots(1, figsize=(10,9), dpi=300)
    SSplot = ax0.contourf(kx, p[:nrws], PV1_u[eps1_index,eps2_index], lev, cmap=cm_br)
    fig.colorbar(SSplot)
#    ax0.set_ylim(0.14,1)
    ax0.set_title('Structure of $\mathregular{S^{-1}d^2\Psi/dp^2}$ with a wavelength of %d km' %(wl[i_maxunstab[eps1_index]]*1000))#, fontsize=16)
    structureplotcustom(ax0)

    norm = MidpointNormalize(midpoint=0)

    fig, (ax0) = plt.subplots(1, figsize=(10,9), dpi=300)
    SSplot = ax0.contourf(kx, p[:nrws], PV2_u[eps1_index,eps2_index], lev, norm=norm,cmap=cm_br)
    fig.colorbar(SSplot)
#    ax0.set_ylim(0.14,1)
    ax0.set_title('Structure of $\mathregular{dS^{-1}/dp \cdot d\Psi/dp}$ with a wavelength of %d km' %(wl[i_maxunstab[eps1_index]]*1000))#, fontsize=16)
    structureplotcustom(ax0)

    if unstab2 == True:
        fig = plt.figure(figsize=(15, 7)) 
        gs = gridspec.GridSpec(1, 3, width_ratios=[3, 1, 1]) 
        ax0 = plt.subplot(gs[0])
        ax1 = plt.subplot(gs[1])
        ax2 = plt.subplot(gs[2])
#        fig, (ax0) = plt.subplots(figsize=(6,4)) 
        PV2plot = ax0.contourf(kx, p[:nrws], PV_u2[eps1_index,eps2_index], lev, cmap=cm_br)
        ax0.contour(kx, p[:nrws], psi2, colors='k')
        ax0.set_ylim(0.14,1)
        ax0.set_title('Structure of potential vorticity with a wavelength of %d km' %(wl[i_maxunstab2[eps1_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
        #fig.colorbar(PV2plot)    
#        ax1.set_ylim(pt,ps)
        structureplotcustom(ax1)
        ax1.plot(np.max(PV_u2[eps1_index,eps2_index],axis=1),p[:nrws], c='k')
        ax1.set_xlabel('zonal max of PV')
        ax1.set_ylabel('')
        for j in range(nrws):
            if np.max(PV_u2[eps1_index,eps2_index,j]) > .01*np.max(PV_u2[eps1_index,eps2_index]):
                ax2.scatter(360/len(kx)*np.argwhere(PV_u2[eps1_index,eps2_index,j] == np.max(PV_u2[eps1_index,eps2_index,j]))[0][0],p[j],c='k',alpha=.5,s=30+200*np.max(PV_u2[eps1_index,eps2_index,j])/np.max(PV_u2[eps1_index,eps2_index]))
        ax2.axvline(90,c='k',ls='--')
        ax2.axvline(180,c='k',ls='--')
        ax2.axvline(270,c='k',ls='--')
        structureplotcustom(ax2)
        ax2.set_xlabel('deg of max PV')
        ax2.set_xticks([0,90,180,270])
        ax2.set_ylabel('')
#        ax2.set_ylim(pt,ps)

    if unstab3 == True:
        fig = plt.figure(figsize=(15, 7)) 
        gs = gridspec.GridSpec(1, 3, width_ratios=[3, 1, 1]) 
        ax0 = plt.subplot(gs[0])
        ax1 = plt.subplot(gs[1])
        ax2 = plt.subplot(gs[2])
#        fig, (ax0) = plt.subplots(figsize=(6,4)) 
        PV3plot = ax0.contourf(kx, p[:nrws], PV_u3[eps1_index,eps2_index], lev, cmap=cm_br)
        ax0.contour(kx, p[:nrws], psi3, colors='k')
        ax0.set_ylim(0.14,1.0)
        ax0.set_title('Structure of potential vorticity with a wavelength of %d km' %(wl[i_maxunstab3[eps1_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
        #fig.colorbar(PV3plot)
#        ax1.set_ylim(pt,ps)
        structureplotcustom(ax1)
        ax1.plot(np.max(PV_u3[eps1_index,eps2_index],axis=1),p[:nrws], c='k')
        ax1.set_xlabel('zonal max of PV')
        ax1.set_ylabel('')
        for j in range(nrws):
            if np.max(PV_u3[eps1_index,eps2_index,j]) > .01*np.max(PV_u3[eps1_index,eps2_index]):
                ax2.scatter(360/len(kx)*np.argwhere(PV_u3[eps1_index,eps2_index,j] == np.max(PV_u3[eps1_index,eps2_index,j]))[0][0],p[j],c='k',alpha=.5,s=30+200*np.max(PV_u3[eps1_index,eps2_index,j])/np.max(PV_u3[eps1_index,eps2_index]))
        ax2.axvline(90,c='k',ls='--')
        ax2.axvline(180,c='k',ls='--')
        ax2.axvline(270,c='k',ls='--')
        structureplotcustom(ax2)
        ax2.set_xlabel('deg of max PV')
        ax2.set_xticks([0,90,180,270])
        ax2.set_ylabel('')
#        ax2.set_ylim(pt,ps)

    if stab == True:
        fig, (ax0) = plt.subplots(figsize=(6,4)) 
        PV_splot = ax0.contourf(kx, p[:nrws], PV_s[eps1_index,eps2_index], lev, cmap=cm_br)
        ax0.set_ylim(0.14,1.0)
        ax0.set_title('Structure of (stable) potential vorticity with a wavelength of %d km' %(wl[i_maxstab[eps1_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
        #fig.colorbar(PV_splot)

        fig, (ax0) = plt.subplots(figsize=(6,4))
        Csplot = ax0.contourf(kx, p[:nrws], PV3_s[eps1_index,eps2_index], lev, cmap=cm_br)
        fig.colorbar(Csplot)
        ax0.set_ylim(0.14,1)
        ax0.set_title('Structure of (stable) $\mathregular{d^2\Psi/dx^2}$ with a wavelength of %d km' %(wl[i_maxstab[eps1_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)

        fig, (ax0) = plt.subplots(figsize=(6,4))
        SSsplot = ax0.contourf(kx, p[:nrws], PV1_s[eps1_index,eps2_index], lev, cmap=cm_br)
        fig.colorbar(SSsplot)
        ax0.set_ylim(0.14,1)
        ax0.set_title('Structure of (stable) $\mathregular{S^{-1}d^2\Psi/dp^2}$ with a wavelength of %d km' %(wl[i_maxstab[eps1_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
        
        fig, (ax0) = plt.subplots(figsize=(6,4))
        SSsplot = ax0.contourf(kx, p[:nrws], PV2_s[eps1_index,eps2_index], lev, cmap=cm_br)
        fig.colorbar(SSsplot)
        ax0.set_ylim(0.14,1)
        ax0.set_title('Structure of (stable) $\mathregular{dS^{-1}/dp \cdot d\Psi/dp}$ with a wavelength of %d km' %(wl[i_maxstab[eps1_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
        
    if stab2 == True:
        fig, (ax0) = plt.subplots(figsize=(6,4)) 
        PV_s2plot = ax0.contourf(kx, p[:nrws], PV_s2[eps1_index,eps2_index], lev, cmap=cm_br)
        ax0.set_ylim(0.14,1.0)
        ax0.set_title('Structure of (stable) potential vorticity with a wavelength of %d km' %(wl[i_maxstab2[eps1_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
        fig.colorbar(PV_s2plot)
        
    if stab3 == True:
        fig, (ax0) = plt.subplots(figsize=(6,4)) 
        PV_s3plot = ax0.contourf(kx, p[:nrws], PV_s3[eps1_index,eps2_index], lev, cmap=cm_br)
        ax0.set_ylim(0.14,1.0)
        ax0.set_title('Structure of (stable) potential vorticity with a wavelength of %d km' %(wl[i_maxstab3[eps1_index]]*1000))#, fontsize=16)
        structureplotcustom(ax0)
        fig.colorbar(PV_s3plot)
        
    plt.show()

# -----------------------------------------------------------------------------

def PV_vs_gamma():

    if evap == False:
        x1 = [np.max(PV_u[e,:5]), np.max(PV_u[e,jtlc-5:jtlc+5]), np.max(PV_u[e,jblc-5:jblc+5]), np.max(PV_u[e,-5:])]
        x1 = x1/sum(x1)
    if hblcstep == 1.2:
        x2 = [np.max(PV_u[e,:5]), np.max(PV_u[e,jtlc-5:jtlc+5]), np.max(PV_u[e,jblc-5:jblc+5]), np.max(PV_u[e,-5:])]
        x2 = x2/sum(x2)
    if hblcstep == 1.3:
        x3 = [np.max(PV_u[e,:5]), np.max(PV_u[e,jtlc-5:jtlc+5]), np.max(PV_u[e,jblc-5:jblc+5]), np.max(PV_u[e,-5:])]
        x3 = x3/sum(x3)
    if hblcstep == 1.5:
        x4 = [np.max(PV_u[e,:5]), np.max(PV_u[e,jtlc-5:jtlc+5]), np.max(PV_u[e,jblc-5:jblc+5]), np.max(PV_u[e,-5:])]
        x4 = x4/sum(x4)
    
    
    try:
        x1
    except NameError:
        print ('PV max for no latent cooling not defined')
        x1 = np.zeros(4)
    try:
        x2
    except NameError:
        print ('PV max for 20 % latent cooling not defined')
        x2 = np.zeros(4)
    try:
        x3
    except NameError:
        print ('PV max for 30 % latent cooling not defined')
        x3 = np.zeros(4)
    try:
        x4
    except NameError:
        print ('PV max for 50 % latent cooling not defined')
        x4 = np.zeros(4)
    
    
    y = np.zeros((4,3))        
    
    for i in range(4):
        y[-(i+1)] = [x1[i],x2[i],x3[i]]
    
    x = np.arange(4)
    
    fig, ax = plt.subplots()
    
    labels = ('No lc', '20% lc', '30% lc', '50% lc')
    width = .2
    
    #ax.bar(x,y[0],width,color='grey',label=labels[3])
    #for i in range(1,4):
    #    ax.bar(x,y[i],width,color=c[i-1],label=labels[-(i+1)])#,bottom=y[i-1]+1)
    
    ax.bar(x-.3,x1,width,color=c[0], label=labels[0])
    ax.bar(x-.1,x2,width,color=c[2], label=labels[1])
    ax.bar(x+.1,x3,width,color=c[4], label=labels[2])
    ax.bar(x+.3,x4,width,color=c[1], label=labels[3])
    #ax.bar(x+.3,y[3],width,color=c[4])
    
    #ax.stackplot(x,y[3],y[2],y[1],y[0],edgecolor='None',alpha=.7,labels=labels[::-1])
    plt.ylabel('PV contribution (of total)')
    ax.set_xticks(x+width/2)
    ax.set_xticklabels(['PV$\mathregular{_t}$','PV$\mathregular{_{ht}}$','PV$\mathregular{_{hb}}$','PV$\mathregular{_s}$'])
    ax.set_xlim(min(x)-.3,max(x)+width+.3)
    plt.legend()
    
    plt.show()
    
# -----------------------------------------------------------------------------

### structure of energetics w'T' ----------------------------------------------------

def plot_wT_structure():

    zonalaverage = True

    with plt.rc_context(frame):
        if zonalaverage == True:
            fig = plt.figure(figsize=(12.5, 7)) 
            gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
            ax2 = plt.subplot(gs[0])
            ax3 = plt.subplot(gs[1])
        else:
            fig, (ax2) = plt.subplots(1, figsize=(10,9))
            

        ax2.axhline(p[np.argwhere(v*T[eps1_index,eps2_index]==np.max(np.min(v[jtrop+1:]*T[eps1_index,eps2_index,jtrop+1:],axis=1)))[-1][0]], c='grey',ls='--')
        ax2.text(0,p[np.argwhere(v*T[eps1_index,eps2_index]==np.max(np.min(v[jtrop+1:]*T[eps1_index,eps2_index,jtrop+1:],axis=1)))[-1][0]], f' u={10*u[np.argwhere(v*T[eps1_index,eps2_index]==np.max(np.min(v[jtrop+1:]*T[eps1_index,eps2_index,jtrop+1:],axis=1)))[0][0]]:1.1f} m/s')
        #ax2.axhline(p[np.argwhere(u>=sigmar_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1]/k[i_maxunstab[eps1_index,eps2_index]])[-1][0]], c='grey',ls='--')
        #ax2.text(0,p[np.argwhere(u>=sigmar_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1]/k[i_maxunstab[eps1_index,eps2_index]])[-1][0]], f' c$_p$={10*(sigmar_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1])/k[i_maxunstab[eps1_index,eps2_index]]:1.1f} m/s',verticalalignment='top')
#        ax2.text(0,ptrop,f' v\'T\'<0: {100*len(np.argwhere((v[jtrop+1]*T[eps1_index,eps2_index,jtrop+1])<0))/len(kx):1.1f}%',verticalalignment='top')
#        ax2.text(0,1,f' v\'T\'<0: {100*len(np.argwhere((v[-1]*T[eps1_index,eps2_index,-1])<0))/len(kx):1.1f}%',verticalalignment='bottom')

        
        norm = MidpointNormalize(midpoint=0)
        ax2.contour(kx, p[:nrws], w, 1, colors='grey')
        ax2.contour(kx, p[:nrws], T[eps1_index,eps2_index], 1, colors='k')
        wt = ax2.contourf(kx, p[:nrws], -w*T[eps1_index,eps2_index], lev, cmap=cm_br, norm=norm, origin='lower')
#                          vmin = -max(abs(np.amin(-wtemp)),abs(np.amax(-wtemp))), 
#                          vmax = max(abs(np.amin(-wtemp)),abs(np.amax(-wtemp))))  
        ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxunstab[eps1_index,eps2_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        if structureplot == True:
            ax2.set_xlabel('kx')#6000 km wavelength', fontsize=fs, labelpad=20)
        
        if zonalaverage == True:
            wenergy = (simps(-w*T,kx))/(2*pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            fw=interp1d(p[:nrws],wenergy[eps1_index,eps2_index])
            pext = np.linspace(pt,p[-2],100*len(p[:-1]))
            
            ax3.plot()
            en = ax3.scatter(fw(pext), pext, 8, fw(pext), edgecolor='None', 
                             norm=norm, cmap=cm_br,
                             vmin = -max(abs(fw(pext))), 
                             vmax = max(abs(fw(pext))))
            #ax3.plot(energy,p[:-1])
            ax3.set_facecolor('0.8')
    #        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
    #        ax3.set_xlabel('C(A,K)')#, fontsize=14)
            plt.ylim(pt,ps)
    #        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
            structureplotcustom(ax3)
            plt.xlim(-max(abs(fw(pext)))*1.3, max(abs(fw(pext)))*1.3)
            ax3.set_ylabel('')
            ax3.set_xlabel('')
            ax3.set_xticks([0])
            ax3.set_xticklabels([0])
            plt.text(0,0,f'<w\'T\'> = {np.sum(fw(pext)):1.1f}',ha='center',va='top')
            fig.tight_layout()

    if unstab2 == True:
        with plt.rc_context(frame):
            if zonalaverage == True:
                fig = plt.figure(figsize=(12.5, 7)) 
                gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
                ax2 = plt.subplot(gs[0])
                ax3 = plt.subplot(gs[1])
            else:
                fig, (ax2) = plt.subplots(1, figsize=(10,9))
                
            norm = MidpointNormalize(midpoint=0)
            wt = ax2.contourf(kx, p[:nrws], -w2*T2[eps1_index,eps2_index], 30, norm=norm, cmap=cm_br)#,
                              #vmin = -max(abs(np.amin(-wtemp2)),abs(np.amax(-wtemp2))), 
                              #vmax = max(abs(np.amin(-wtemp2)),abs(np.amax(-wtemp2))))
            #plt.colorbar(wt)
            ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxunstab2[eps1_index,eps2_index]]*1000), fontsize=16)
            structureplotcustom(ax2)
            #if structureplot == True:
            #    ax2.set_ylabel('')
            #    ax2.set_xlabel('x')#3300 km wavelength', fontsize=fs, labelpad=20)
            
            if zonalaverage == True:
                w2energy = (simps(-w2*T2[eps1_index,eps2_index],kx))/(2*pi)/wl[i_maxunstab2[eps1_index,eps2_index]]
                fw2=interp1d(p[:nrws],w2energy)
                
                ax3.plot()
                en = ax3.scatter(fw2(pext), pext, 5, fw2(pext), edgecolor='None', 
                                 norm=norm, cmap=cm_br,
                                 vmin = -max(abs(fw2(pext))), 
                                 vmax = max(abs(fw2(pext))))
                ax3.set_facecolor('0.8')
        #        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
                plt.ylim(pt,ps)
                structureplotcustom(ax3)
                plt.xlim(-max(abs(fw2(pext)))*1.3, max(abs(fw2(pext)))*1.3)
                ax3.set_ylabel('')
                ax3.set_xlabel('')
                ax3.set_xticks([0])
                ax3.set_xticklabels([0])
                plt.text(0,0,f'<w\'T\'> = {np.sum(fw2(pext)):1.1f}',ha='center',va='top')
                fig.tight_layout()

    if unstab3 == True:
        with plt.rc_context(frame):
            wtemp3	= -w3*T3
            if zonalaverage == True:        
                fig = plt.figure(figsize=(12.5, 7)) 
                gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
                ax2 = plt.subplot(gs[0])
                ax3 = plt.subplot(gs[1])
            else:
                fig, (ax2) = plt.subplots(1, figsize=(8,5))
            
            norm = MidpointNormalize(midpoint=0)
            wt = ax2.contourf(kx, p[:nrws], wtemp3[eps1_index,eps2_index], 30, norm=norm, cmap=cm_br,
                              vmin = -max(abs(np.amin(-wtemp3)),abs(np.amax(-wtemp3))), 
                              vmax = max(abs(np.amin(-wtemp3)),abs(np.amax(-wtemp3))))
            ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxunstab3[eps1_index,eps2_index]]*1000), fontsize=16)
            structureplotcustom(ax2)
            #if structureplot == True:
                #ax2.set_ylabel('')
                #ax2.set_xlabel('x')#300 km wavelength', fontsize=fs, labelpad=20)
            
            if zonalaverage == True:        
                w3energy = (simps(wtemp3,kx))/(2*pi)/wl[i_maxunstab3[eps1_index,eps2_index]]
                fw3=interp1d(p[:nrws],w3energy[eps1_index,eps2_index])
                
                norm = MidpointNormalize(midpoint=0)
                
                ax3.plot()
                en = ax3.scatter(fw3(pext), pext, 5, fw3(pext), edgecolor='None', 
                                 norm=norm, cmap=cm_br,
                                 vmin = -max(abs(fw3(pext))), 
                                 vmax = max(abs(fw3(pext))))
                ax3.set_facecolor('0.8')
        #        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
                plt.ylim(pt,ps)
                structureplotcustom(ax3)
                plt.xlim(-max(abs(fw3(pext)))*1.3, max(abs(fw3(pext)))*1.3)
                ax3.set_ylabel('')
                ax3.set_xlabel('')
                ax3.set_xticks([0])
                ax3.set_xticklabels([0])
                plt.text(0,0,f'<w\'T\'> = {np.sum(fw3(pext)):1.1f}',ha='center',va='top')
                fig.tight_layout()

    if stab == True:
        wtemp_s	= -w_s*T_s
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], wtemp_s[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(-wtemp_s)),abs(np.amax(-wtemp_s))), 
		    vmax = max(abs(np.amin(-wtemp_s)),abs(np.amax(-wtemp_s))))
        ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        wsenergy = (simps(wtemp_s,kx))/(2*pi)/wl[i_maxstab[eps1_index,eps2_index]]
        fvs=interp1d(p[:nrws],wsenergy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fvs(pext), pext, 5, fvs(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fvs(pext))), 
                         vmax = max(abs(fvs(pext))))
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fvs(pext)))*1.1, max(abs(fvs(pext)))*1.1)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
        
    if stab2 == True:
        wtemp_s2	= -w_s2*T_s2
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], wtemp_s2[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(-wtemp_s2)),abs(np.amax(-wtemp_s2))), 
		    vmax = max(abs(np.amin(-wtemp_s2)),abs(np.amax(-wtemp_s2))))
        ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab2[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        ws2energy = (simps(wtemp_s2,kx))/(2*pi)/wl[i_maxstab2[eps1_index,eps2_index]]
        fvs2=interp1d(p[:nrws],ws2energy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fvs2(pext), pext, 5, fvs2(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fvs2(pext))), 
                         vmax = max(abs(fvs2(pext))))
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fvs2(pext)))*1.1, max(abs(fvs2(pext)))*1.1)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
        
    if stab3 == True:
        wtemp_s3	= -w_s3*T_s3
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], wtemp_s3[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(-wtemp_s3)),abs(np.amax(-wtemp_s3))), 
		    vmax = max(abs(np.amin(-wtemp_s3)),abs(np.amax(-wtemp_s3))))
        ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab3[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        ws3energy = (simps(wtemp_s3,kx))/(2*pi)/wl[i_maxstab3[eps1_index,eps2_index]]
        fvs3=interp1d(p[:nrws],ws3energy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fvs3(pext), pext, 5, fvs3(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fvs3(pext))), 
                         vmax = max(abs(fvs3(pext))))
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fvs3(pext)))*1.1, max(abs(fvs3(pext)))*1.1)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
        
    plt.show()
    
# -----------------------------------------------------------------------------

### structure of energetics - v'T' ----------------------------------------------------

def plot_vT_structure():

    venergy = (lambda1[:nrws]/S[:nrws]*simps(v*T[eps1_index,eps2_index],kx))/(2*pi)/wl[i_maxunstab[eps1_index,eps2_index]]
    fv=interp1d(p[:nrws],venergy)
    pext = np.linspace(pt,p[-2],100*len(p[:-1]))
    
    zonalaverage = True

    with plt.rc_context(frame):
        if zonalaverage == True:
            fig = plt.figure(figsize=(12.5, 7)) 
            gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
            ax2 = plt.subplot(gs[0])
            ax3 = plt.subplot(gs[1])
        else:
            fig, (ax2) = plt.subplots(1, figsize=(10,9))
        
        norm = MidpointNormalize(midpoint=0)
        ax2.contour(kx, p[:nrws], v, 1, colors='grey')
        wt = ax2.contourf(kx, p[:nrws], lambda1[:nrws,np.newaxis]/S[:nrws,np.newaxis]*v*T[eps1_index,eps2_index], lev, cmap=cm_br, norm=norm, origin='lower')
        #cbar = plt.colorbar(wt, ax = ax2)
        ax2.contour(kx, p[:nrws], T[eps1_index,eps2_index], 1, colors='k')#(np.linspace(-np.max(T),-np.max(T)/12,6)), colors='k')
            
        structureplotcustom(ax2)
        ax2.tick_params(which='both', length=6, width=1)
        ax2.set_ylim(1,0)

        ax2.axhline(p[np.argwhere(lambda1[:nrws,np.newaxis]/S[:nrws,np.newaxis]*v*T[eps1_index,eps2_index]==np.max(np.min(lambda1[jtrop+1:nrws,np.newaxis]/S[jtrop+1:nrws,np.newaxis]*v[jtrop+1:]*T[eps1_index,eps2_index,jtrop+1:],axis=1)))[-1][0]], c='grey',ls='--')
        ax2.text(0,p[np.argwhere(lambda1[:nrws,np.newaxis]/S[:nrws,np.newaxis]*v*T[eps1_index,eps2_index]==np.max(np.min(lambda1[jtrop+1:nrws,np.newaxis]/S[jtrop+1:nrws,np.newaxis]*v[jtrop+1:]*T[eps1_index,eps2_index,jtrop+1:],axis=1)))[-1][0]], f' u={10*u[np.argwhere(v*T[eps1_index,eps2_index]==np.max(np.min(v[jtrop+1:]*T[eps1_index,eps2_index,jtrop+1:],axis=1)))[0][0]]:1.1f} m/s')
        #ax2.axhline(p[np.argwhere(u>=sigmar_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1]/k[i_maxunstab[eps1_index,eps2_index]])[-1][0]], c='grey',ls='--')
        #ax2.text(0,p[np.argwhere(u>=sigmar_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1]/k[i_maxunstab[eps1_index,eps2_index]])[-1][0]], f' c$_p$={10*(sigmar_sorted[eps1_index,eps2_index,i_maxunstab[eps1_index,eps2_index],-1])/k[i_maxunstab[eps1_index,eps2_index]]:1.1f} m/s',verticalalignment='top')
        #ax2.text(0,ptrop,f' v\'T\'<0: {100*len(np.argwhere((v[jtrop+1]*T[eps1_index,eps2_index,jtrop+1])<0))/len(kx):1.1f}%',verticalalignment='top')
        #ax2.text(0,1,f' v\'T\'<0: {100*len(np.argwhere((v[-1]*T[eps1_index,eps2_index,-1])<0))/len(kx):1.1f}%',verticalalignment='bottom')
               
               
        if zonalaverage == True:            
            ax3.plot()
#            en = ax3.scatter(venergy[:], p[:nrws], 8, venergy[:], edgecolor='None', norm=norm, cmap=cm_br,
#                             vmin = -max(abs(venergy)), vmax = max(abs(venergy)))
            en = ax3.scatter(fv(pext), pext, 8, fv(pext), edgecolor='None', norm=norm, cmap=cm_br,
                             vmin = -max(abs(fv(pext))), vmax = max(abs(fv(pext))))
            #ax3.plot(energy,p[:-1])
            ax3.set_facecolor('0.8')
            structureplotcustom(ax3)
            plt.ylim(pt,ps)
            ax3.invert_yaxis()
#            structureplotcustom(ax3)
#            plt.xlim(-max(abs(fv(pext)))*1.3, max(abs(fv(pext)))*1.3)
#            ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
            plt.xlim(-max(abs(venergy))*1.1, max(abs(venergy))*1.1)
            ax3.set_ylabel('')
            ax3.set_xlabel('')
            ax3.set_xticks([0])
            ax3.set_xticklabels([0])
            plt.text(0,0,f'<v\'T\'> = {np.sum(fv(pext)):1.1f}',ha='center',va='top')
            fig.tight_layout()

    if unstab2 == True:
        with plt.rc_context(frame):
            if zonalaverage == True:
                fig = plt.figure(figsize=(12.5, 7)) 
                gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
                ax2 = plt.subplot(gs[0])
                ax3 = plt.subplot(gs[1])
            else:
                fig, (ax2) = plt.subplots(1, figsize=(10,9))
                
            norm = MidpointNormalize(midpoint=0)
            wt = ax2.contourf(kx, p[:nrws], lambda1[:nrws,np.newaxis]/S[:nrws,np.newaxis]*v2*T2[eps1_index,eps2_index], 30, norm=norm, cmap=cm_br)
            #cbar = plt.colorbar(wt, ax = ax2)
            ax2.set_title('Structure of $\mathregular{v \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxunstab2[eps1_index]]*1000), fontsize=16)
            structureplotcustom(ax2)
            #if structureplot == True:
                #ax2.set_ylabel('')
                #ax2.set_xlabel('x')#3300 km wavelength', fontsize=fs, labelpad=20)
            
            if zonalaverage == True:
                v2energy = (lambda1[:nrws]/S[:nrws]*simps(v2*T2,kx))/(2*pi)/wl[i_maxunstab2[eps1_index,eps2_index]]
                fv2=interp1d(p[:nrws],v2energy[eps1_index,eps2_index])
                
                ax3.plot()
                en = ax3.scatter(fv2(pext), pext, 5, fv2(pext), edgecolor='None', norm=norm, cmap=cm_br,
                                 vmin = -max(abs(fv2(pext))), vmax = max(abs(fv2(pext))))
                ax3.set_facecolor('0.8')
                structureplotcustom(ax3)
                plt.ylim(pt,ps)
                ax3.invert_yaxis()
#                structureplotcustom(ax3)
#                plt.xlim(-max(abs(fv2(pext)))*1.3, max(abs(fv2(pext)))*1.3)
#                ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
                plt.xlim(-max(abs(fv2(pext)))*1.1, max(abs(fv2(pext)))*1.1)
                ax3.set_ylabel('')
                ax3.set_xlabel('')
                ax3.set_xticks([0])
                ax3.set_xticklabels([0])
                plt.text(0,0,f'<v\'T\'> = {np.sum(fv2(pext)):1.1f}',ha='center',va='top')
                fig.tight_layout()

    if unstab3 == True:
        with plt.rc_context(frame):
            if zonalaverage == True:
                fig = plt.figure(figsize=(12.5, 7)) 
                gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
                ax2 = plt.subplot(gs[0])
                ax3 = plt.subplot(gs[1])
            else:
                fig, (ax2) = plt.subplots(1, figsize=(10,9))
            
            norm = MidpointNormalize(midpoint=0)
            wt = ax2.contourf(kx, p[:nrws], lambda1[:nrws,np.newaxis]/S[:nrws,np.newaxis]*v3*T3[eps1_index,eps2_index], 30, norm=norm, cmap=cm_br)
            #cbar = plt.colorbar(wt, ax = ax2)
            ax2.set_title('Structure of $\mathregular{v \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxunstab3[eps1_index]]*1000), fontsize=16)
            structureplotcustom(ax2)
            #if structureplot == True:
                #ax2.set_ylabel('')
                #ax2.set_xlabel('x')#300 km wavelength', fontsize=fs, labelpad=20)
            
            if zonalaverage == True:        
                v3energy = (lambda1[:nrws]/S[:nrws]*simps(v3*T3,kx))/(2*pi)/wl[i_maxunstab3[eps1_index,eps2_index]]
                fv3=interp1d(p[:nrws],v3energy[eps1_index,eps2_index])
                
                norm = MidpointNormalize(midpoint=0)
                
                ax3.plot()
                en = ax3.scatter(fv3(pext), pext, 5, fv3(pext), edgecolor='None', norm=norm, cmap=cm_br,
                                 vmin = -max(abs(fv3(pext))), vmax = max(abs(fv3(pext))))
                #ax3.plot(energy,p[:-1])
                ax3.set_facecolor('0.8')
                structureplotcustom(ax3)
        #        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
                plt.ylim(pt,ps)
                ax3.invert_yaxis()
#                structureplotcustom(ax3)
#                plt.xlim(-max(abs(fv3(pext)))*1.3, max(abs(fv3(pext)))*1.3)
                #ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
                plt.xlim(-max(abs(fv3(pext)))*1.1, max(abs(fv3(pext)))*1.1)
                ax3.set_ylabel('')
                ax3.set_xlabel('')
                ax3.set_xticks([0])
                ax3.set_xticklabels([0])
                plt.text(0,0,f'<v\'T\'> = {np.sum(fv3(pext)):1.1f}',ha='center',va='top')
                fig.tight_layout()

    if stab == True:
        vtemp_s	= v_s*T_s
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], vtemp_s[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(-vtemp_s)),abs(np.amax(-vtemp_s))), 
		    vmax = max(abs(np.amin(-vtemp_s)),abs(np.amax(-vtemp_s))))
        ax2.set_title('Structure of $\mathregular{v \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        vsenergy = (simps(vtemp_s,kx))/(2*pi)/wl[i_maxstab[eps1_index,eps2_index]]
        fvs=interp1d(p[:nrws],vsenergy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fvs(pext), pext, 5, fvs(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fvs(pext))), 
                         vmax = max(abs(fvs(pext))))
        #ax3.plot(energy,p[:-1])
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fvs(pext)))*1.1, max(abs(fvs(pext)))*1.1)
        #ax3.set_ylabel('pressure')#, fontsize=14)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))

    if stab2 == True:
        vtemp_s2	= v_s2*T_s2
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], vtemp_s2[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(-vtemp_s2)),abs(np.amax(-vtemp_s2))), 
		    vmax = max(abs(np.amin(-vtemp_s2)),abs(np.amax(-vtemp_s2))))
        ax2.set_title('Structure of $\mathregular{v \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab2[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        vs2energy = (simps(vtemp_s2,kx))/(2*pi)/wl[i_maxstab2[eps1_index,eps2_index]]
        fvs2=interp1d(p[:nrws],vs2energy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fvs2(pext), pext, 5, fvs2(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fvs2(pext))), 
                         vmax = max(abs(fvs2(pext))))
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fvs2(pext)))*1.1, max(abs(fvs2(pext)))*1.1)
        #ax3.set_ylabel('pressure')#, fontsize=14)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
        
    if stab3 == True:
        vtemp_s3	= v_s3*T_s3
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], vtemp_s3[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(-vtemp_s3)),abs(np.amax(-vtemp_s3))), 
		    vmax = max(abs(np.amin(-vtemp_s3)),abs(np.amax(-vtemp_s3))))
        #cbar = plt.colorbar(wt, ax = ax2)
        ax2.set_title('Structure of $\mathregular{v \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab3[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        vs3energy = (simps(vtemp_s3,kx))/(2*pi)/wl[i_maxstab3[eps1_index,eps2_index]]
        fvs3=interp1d(p[:nrws],vs3energy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fvs3(pext), pext, 5, fvs3(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fvs3(pext))), 
                         vmax = max(abs(fvs3(pext))))
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fvs3(pext)))*1.1, max(abs(fvs3(pext)))*1.1)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
        
    plt.show()

# -----------------------------------------------------------------------------

def plot_QT_structure():

    ### structure of energetics Q'T' ----------------------------------------------------

    zonalaverage = True

    with plt.rc_context(frame):
        Qtemp	= (Q*T)[eps1_index,eps2_index]
        if zonalaverage == True:
            fig = plt.figure(figsize=(6.5, 3.9)) 
            gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
            ax2 = plt.subplot(gs[0])
            ax3 = plt.subplot(gs[1])
        else:
            fig, (ax2) = plt.subplots(1, figsize=(8,5))

        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], Qtemp, 30, norm=norm, cmap=cm_br)#,
                          #vmin = -max(abs(np.amin(Qtemp)),abs(np.amax(Qtemp))), 
                          #vmax = max(abs(np.amin(Qtemp)),abs(np.amax(Qtemp))))
        ax2.set_title('Structure of $\mathregular{Q \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxunstab[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        if structureplot == True:
            ax2.set_ylabel('')
            ax2.set_xlabel('x')#6000 km wavelength', fontsize=fs, labelpad=20)
        
        if zonalaverage == True:
            Qenergy = (simps(Qtemp,kx))/(2*pi)/wl[i_maxunstab[eps1_index,eps2_index]]
            fQ=interp1d(p[:nrws],Qenergy)
            pext = np.linspace(pt,p[-2],100*len(p[:-1]))
            
            ax3.plot()
            en = ax3.scatter(fQ(pext), pext, 8, fQ(pext), edgecolor='None', 
                             norm=norm, cmap=cm_br,
                             vmin = -max(abs(fQ(pext))), 
                             vmax = max(abs(fQ(pext))))
            #ax3.plot(energy,p[:-1])
            ax3.set_facecolor('0.8')
    #        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
    #        ax3.set_xlabel('C(A,K)')#, fontsize=14)
            plt.ylim(pt,ps)
    #        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
            structureplotcustom(ax3)
            plt.xlim(-max(abs(fQ(pext)))*1.3, max(abs(fQ(pext)))*1.3)
            ax3.set_ylabel('')
            ax3.set_xlabel('')
            ax3.set_xticks([0])
            ax3.set_xticklabels([0])
            fig.tight_layout()

    if unstab2 == True:
        with plt.rc_context(frame):    
            Qtemp2	= Q2*T2[eps1_index,eps2_index]
            if zonalaverage == True:
                fig = plt.figure(figsize=(6.5, 3.9)) 
                gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
                ax2 = plt.subplot(gs[0])
                ax3 = plt.subplot(gs[1])
            else:
                fig, (ax2) = plt.subplots(1, figsize=(8,5))
                
            norm = MidpointNormalize(midpoint=0)
            wt = ax2.contourf(kx, p[:nrws], Qtemp2, 30, norm=norm, cmap=cm_br)#,
                              #vmin = -max(abs(np.amin(Qtemp2)),abs(np.amax(Qtemp2))), 
                              #vmax = max(abs(np.amin(Qtemp2)),abs(np.amax(Qtemp2))))
            ax2.set_title('Structure of $\mathregular{Q \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxunstab2[eps1_index]]*1000), fontsize=16)
            structureplotcustom(ax2)
            if structureplot == True:
                ax2.set_ylabel('')
                ax2.set_xlabel('x')#3300 km wavelength', fontsize=fs, labelpad=20)
            
            if zonalaverage == True:
                Q2energy = (simps(Qtemp2,kx))/(2*pi)/wl[i_maxunstab2[eps1_index,eps2_index]]
                fQ2=interp1d(p[:nrws],Q2energy)
                
                ax3.plot()
                en = ax3.scatter(fQ2(pext), pext, 5, fQ2(pext), edgecolor='None', 
                                 norm=norm, cmap=cm_br,
                                 vmin = -max(abs(fQ2(pext))), 
                                 vmax = max(abs(fQ2(pext))))
                ax3.set_facecolor('0.8')
        #        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
                plt.ylim(pt,ps)
                structureplotcustom(ax3)
                plt.xlim(-max(abs(fQ2(pext)))*1.3, max(abs(fQ2(pext)))*1.3)
                ax3.set_ylabel('')
                ax3.set_xlabel('')
                ax3.set_xticks([0])
                ax3.set_xticklabels([0])
                fig.tight_layout()

    if unstab3 == True:
        with plt.rc_context(frame):
            Qtemp3	= Q3*T3[eps1_index,eps2_index]
            if zonalaverage == True:        
                fig = plt.figure(figsize=(7, 3.9)) 
                gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
                ax2 = plt.subplot(gs[0])
                ax3 = plt.subplot(gs[1])
            else:
                fig, (ax2) = plt.subplots(1, figsize=(8,5))
            
            norm = MidpointNormalize(midpoint=0)
            wt = ax2.contourf(kx, p[:nrws], Qtemp3, 30, norm=norm, cmap=cm_br)#,
                              #vmin = -max(abs(np.amin(Qtemp3)),abs(np.amax(Qtemp3))), 
                              #vmax = max(abs(np.amin(Qtemp3)),abs(np.amax(Qtemp3))))
            ax2.set_title('Structure of $\mathregular{Q \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxunstab3[eps1_index]]*1000), fontsize=16)
            structureplotcustom(ax2)
            if structureplot == True:
                #ax2.set_ylabel('')
                ax2.set_xlabel('x')#300 km wavelength', fontsize=fs, labelpad=20)
            #plt.colorbar(wt)
            
            if zonalaverage == True:        
                Q3energy = (simps(Qtemp3,kx))/(2*pi)/wl[i_maxunstab3[eps1_index,eps2_index]]
                fQ3=interp1d(p[:nrws],Q3energy)
                
                norm = MidpointNormalize(midpoint=0)
                
                ax3.plot()
                en = ax3.scatter(fQ3(pext), pext, 5, fQ3(pext), edgecolor='None', 
                                 norm=norm, cmap=cm_br,
                                 vmin = -max(abs(fQ3(pext))), 
                                 vmax = max(abs(fQ3(pext))))
                ax3.set_facecolor('0.8')
        #        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
                plt.ylim(pt,ps)
                structureplotcustom(ax3)
                plt.xlim(-max(abs(fQ3(pext)))*1.3, max(abs(fQ3(pext)))*1.3)
                ax3.set_ylabel('')
                ax3.set_xlabel('')
                ax3.set_xticks([0])
                ax3.set_xticklabels([0])
                fig.tight_layout()

    if stab == True:
        Qtemp_s	= Q_s*T_s
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], Qtemp_s[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(Qtemp_s)),abs(np.amax(Qtemp_s))), 
		    vmax = max(abs(np.amin(Qtemp_s)),abs(np.amax(Qtemp_s))))
        ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        Qsenergy = (simps(Qtemp_s,kx))/(2*pi)/wl[i_maxstab[eps1_index,eps2_index]]
        fQs=interp1d(p[:nrws],Qsenergy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fQs(pext), pext, 5, fQs(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fQs(pext))), 
                         vmax = max(abs(fQs(pext))))
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fQs(pext)))*1.1, max(abs(fQs(pext)))*1.1)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
        
    if stab2 == True:
        Qtemp_s2	= Q_s2*T_s2
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], Qtemp_s2[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(Qtemp_s2)),abs(np.amax(Qtemp_s2))), 
		    vmax = max(abs(np.amin(Qtemp_s2)),abs(np.amax(Qtemp_s2))))
        ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab2[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        Qs2energy = (simps(Qtemp_s2,kx))/(2*pi)/wl[i_maxstab2[eps1_index,eps2_index]]
        fQs2=interp1d(p[:nrws],Qs2energy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fQs2(pext), pext, 5, fQs2(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fQs2(pext))), 
                         vmax = max(abs(fQs2(pext))))
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fQs2(pext)))*1.1, max(abs(fQs2(pext)))*1.1)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
        
    if stab3 == True:
        Qtemp_s3	= Q_s3*T_s3
        fig = plt.figure(figsize=(9, 4)) 
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1]) 
        ax2 = plt.subplot(gs[0])
        ax3 = plt.subplot(gs[1])
        
        norm = MidpointNormalize(midpoint=0)
        wt = ax2.contourf(kx, p[:nrws], Qtemp_s3[e], 30, norm=norm, cmap=cm_br,
		    vmin = -max(abs(np.amin(Qtemp_s3)),abs(np.amax(Qtemp_s3))), 
		    vmax = max(abs(np.amin(Qtemp_s3)),abs(np.amax(Qtemp_s3))))
        ax2.set_title('Structure of $\mathregular{\omega \, times \, d\psi/dp}$ \n for a wavelength of %d$\mathregular{\cdot 10^6}$ m \n' %(wl[i_maxstab3[eps1_index]]*1000), fontsize=16)
        structureplotcustom(ax2)
        
        Qs3energy = (simps(Qtemp_s3,kx))/(2*pi)/wl[i_maxstab3[eps1_index,eps2_index]]
        fQs3=interp1d(p[:nrws],Qs3energy[e])

        norm = MidpointNormalize(midpoint=0)
        
        ax3.plot()
        en = ax3.scatter(fQs3(pext), pext, 5, fQs3(pext), edgecolor='None', 
                         norm=norm, cmap=cm_br,
                         vmin = -max(abs(fQs3(pext))), 
                         vmax = max(abs(fQs3(pext))))
        ax3.set_facecolor('0.8')
        #ax3.set_title('Total C(A,K): %1.1f \n' %(1/(2*pi)*simps(simps(wtemp,kx),p)), fontsize=16)
        ax3.set_xlabel('C(A,K)')#, fontsize=14)
        for label in ax3.get_xticklabels()[::2]:
            label.set_visible(False)
        plt.xlim(-max(abs(fQs3(pext)))*1.1, max(abs(fQs3(pext)))*1.1)
        ax3.set_yticklabels([])
        plt.ylim(pt,ps)
        ax3.invert_yaxis()
        ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
        
    plt.show()

# -----------------------------------------------------------------------------

### zonally integrated energetics comparison ----------------------------------------------------

def compare_energetics():

    venergy_int = (simps(lambda1[:nrws]/S[:nrws]*venergy,p[:nrws]))
    wenergy_int = (simps(wenergy,p[:nrws]))
    Efrac = (venergy_int-wenergy_int)/wenergy_int # APE/KE
    print ('v\'T\' = %.4f, w\'T\' = %.4f, dAPE/dt = %.4f for WL = %.3f' % (venergy_int[e],wenergy_int[e],venergy_int[e]-wenergy_int[e],wl[i_maxunstab[e,eps2_index]]))

    if unstab2 == True:
        v2energy_int = (simps(lambda1[:nrws]/S[:nrws]*v2energy,p[:nrws]))
        w2energy_int = (simps(w2energy,p[:nrws]))
        E2frac = (v2energy_int-w2energy_int)/w2energy_int
        print ('v\'T\' = %.4f, w\'T\' = %.4f, dAPE/dt = %.4f for WL = %.3f' % (v2energy_int[e],w2energy_int[e],v2energy_int[e]-w2energy_int[e][e],wl[i_maxunstab2[e,eps2_index]]))

    if unstab3 == True:
        v3energy_int = (simps(lambda1[:nrws]/S[:nrws]*v3energy,p[:nrws]))
        w3energy_int = (simps(w3energy,p[:nrws]))
        E3frac = (v3energy_int-w3energy_int)/w3energy_int
        print ('v\'T\' = %.6f, w\'T\' = %.6f, dAPE/dt = %.6f for WL = %.3f' % (v3energy_int[e],w3energy_int[e],v3energy_int[e]-w3energy_int[e],wl[i_maxunstab3[e,eps2_index]]))

    if stab == True:
        vsenergy_int = (simps(lambda1[:nrws]/S[:nrws]*vsenergy,p[:nrws]))
        wsenergy_int = (simps(wsenergy,p[:nrws]))
        Esfrac = (vsenergy_int-wsenergy_int)/wsenergy_int
        print ('v\'T\' = %.4f, w\'T\' = %.4f, dAPE/dt = %.4f for WL = %.3f' % (vsenergy_int[e],wsenergy_int[e],vsenergy_int[e]-wsenergy_int[e],wl[i_maxstab[e,eps2_index]]))

    if stab2 == True:
        vs2energy_int = (simps(lambda1[:nrws]/S[:nrws]*vs2energy,p[:nrws]))
        ws2energy_int = (simps(ws2energy,p[:nrws]))
        Es2frac = (vs2energy_int-ws2energy_int)/ws2energy_int
        print ('v\'T\' = %.4f, w\'T\' = %.4f, dAPE/dt = %.4f for WL = %.3f' % (vs2energy_int[e],ws2energy_int[e],vs2energy_int[e]-ws2energy_int[e],wl[i_maxstab2[e,eps2_index]]))
        
    if stab3 == True:
        vs3energy_int = (simps(lambda1[:nrws]/S[:nrws]*vs3energy,p[:nrws]))
        ws3energy_int = (simps(ws3energy,p[:nrws]))
        Es3frac = (vs3energy_int-ws3energy_int)/ws3energy_int
        print ('v\'T\' = %.4f, w\'T\' = %.4f, dAPE/dt = %.4f for WL = %.3f' % (vs3energy_int[e],ws3energy_int[e][e],vs3energy_int[e]-ws3energy_int[e],wl[i_maxstab3[e,eps2_index]]))
        
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(5,4))
    norm = MidpointNormalize(midpoint=0)
        
    Sint = interp1d(p[:nrws],S[:nrws])
    #comp = (lambda1[:nrws]*Sint(pext)*fv(pext)-fw(pext))/fw(pext)
    #comp = (lambda1[:nrws]*S[:nrws]*venergy-wenergy)/wenergy
    comp = (Sint(pext)*interp1d(p[:nrws],lambda1[:nrws])(pext)*fv(pext)-fw(pext))
    #comp = (Sint(pext)*lambda1[:nrws]*fv(pext)-fw(pext))
    comp2 = fw(pext)
        
    ax1.plot()
    en = ax1.scatter(comp, pext, 8, comp, edgecolor='None', norm=norm, cmap=cm_br)
    norm = MidpointNormalize(midpoint=0)
    en = ax2.scatter(comp2, pext, 8, comp2, edgecolor='None', norm=norm, cmap=cm_br)
    ax1.set_facecolor('0.8')
    ax2.set_facecolor('0.8')
    ax1.set_ylim(pt,ps)
    ax2.set_ylim(pt,ps)
    structureplotcustom(ax1)
    structureplotcustom(ax2)
    #plt.xlim(-max(abs(comp))*1.3, max(abs(comp))*1.3)
    ax1.set_ylabel('')
    ax2.set_ylabel('')
    ax1.set_xlabel('d(APE)/dt')
    ax2.set_xlabel('d(KE)/dt')
    ax1.set_xticks([0])
    ax1.set_xticklabels([0])
    ax2.set_xticks([0])
    ax2.set_xticklabels([0])
    fig.tight_layout()

    plt.show()

# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
