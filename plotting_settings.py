#!/usr/bin/env python
# coding: utf-8


# -----------------------------------------------------------------------------
# plotting settings
# -----------------------------------------------------------------------------

# for centering colormaps around e.g. zero:
class MidpointNormalize(Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)
    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))

# creating colormap from blue to white to red:
lev = 50
cm_colors = [(0, 109/255., 136/255.), (1, 1, 1), (209/255., 98/255., 76/255.)]
cm_br = LinearSegmentedColormap.from_list('my_list', cm_colors, N=lev)

# creating different colormaps with white, red, blue, and grey:
cm_bgr_colors = [(0, 109/255., 136/255.), (.75, .75, .75, .7), (209/255., 98/255., 76/255.)]
cm_bgr = LinearSegmentedColormap.from_list('my_list', cm_bgr_colors, N=lev)

cm_wr_colors = [(1,1,1),(1,1,1),(209/255., 98/255., 76/255.)]#(248/255, 233/255, 230/255), 
cm_wr = LinearSegmentedColormap.from_list('my_list', cm_wr_colors, N=lev)
cm_wr.set_under('white')

cm_wrr_colors = [(1,1,1),(1,1,1),(169/255,29/255,0)]
cm_wrr = LinearSegmentedColormap.from_list('my_list', cm_wrr_colors, N=lev)
cm_wrr.set_under('white')

cm_wbr_colors = [(1,1,1),(1,1,1),(1,1,1),(0, 109/255., 136/255.),(169/255,29/255,0)]
cm_wbr = LinearSegmentedColormap.from_list('my_list', cm_wbr_colors, N=lev)
cm_wbr.set_under('white')

cm_bwrr_colors = [(0, 109/255., 136/255.),(0, 109/255., 136/255.),(0, 109/255., 136/255.),(.9,.9,.9),(169/255,29/255,0)]#(248/255, 233/255, 230/255), 
cm_bwrr = LinearSegmentedColormap.from_list('my_list', cm_bwrr_colors, N=lev)
cm_bwrr.set_under('white')

cm_wgrr_colors = [(1,1,1),(1,1,1),(1,1,1),(.6,.6,.6),(169/255,29/255,0)]
cm_wgrr = LinearSegmentedColormap.from_list('my_list', cm_wgrr_colors, N=lev)
cm_wgrr.set_under('white')

cm_gwrr_colors = [(.4,.4,.4),(.4,.4,.4),(.4,.4,.4),(.95,.95,.95),(169/255,29/255,0)] 
cm_gwrr = LinearSegmentedColormap.from_list('my_list', cm_gwrr_colors, N=lev)
cm_gwrr.set_under('white')

c = [(.9,.9,.9),(0, 109/255., 136/255.),(209/255., 98/255., 76/255.),(.3,.3,.3),(124/255,101/255,133/255),(.6,.6,.6),(163/255,209/255,219/255),(1,1,1)]
c_greys = [(.6,.6,.6),(.3,.3,.3),(0,0,0)]
c_reds = [(169/255,29/255,0),(169/255,29/255,0,.75),(169/255,29/255,0,.55),(169/255,29/255,0,.4),(169/255,29/255,0,.2),(169/255,29/255,0,.1)]
c_blues = [(0, 109/255., 136/255.),(0, 109/255., 136/255., .75),(0, 109/255., 136/255., .55),(0, 109/255., 136/255., .4),(0, 109/255., 136/255., .2),(0, 109/255., 136/255., .1),(0, 109/255., 136/255., .05)]
c_wb = LinearSegmentedColormap.from_list('my_list', [(1,1,1),(0, 109/255., 136/255.)], N=lev)
c_yb = LinearSegmentedColormap.from_list('my_list', [(1, 1, 200/255.),(0,0,0)], N=lev)
c_yg = LinearSegmentedColormap.from_list('my_list', [(1, 1, 200/255.),(.6,.6,.6)], N=lev)


# general plotting settings

ms = 3			# markersize
ls = ':'		# line style
marker = 'o'	# marker type

def sigmaplotcustom(ax):		# some settings for the growth rate plots
    ax.set_ylim(bottom=0)
    ax.set_xticks([.1,.5,1,5,10,50])
    ax.set_xticklabels([100,500,1000,5000,10000,50000])
    ax.set_xlabel('wavelength (km)')
    ax.set_ylabel('growth rate (10$\mathregular{^{-5}s^{-1}}$)')

