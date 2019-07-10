import numpy as np
import matplotlib.pyplot as plt
import mdtraj.io as io
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rcParams['axes.linewidth'] = 2
rcParams.update({'font.size': 18})
import matplotlib
matplotlib.rcParams['axes.formatter.useoffset'] = False

# These are the "Tableau 20" colors as RGB.
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)


def plot_macros():
    for i in range(15):
        a = io.loadh('../macros_on_tica/on_tica_macro_%d.h5' %i)['arr_0']
        print i, a.shape
        plt.plot(a[:,0],a[:,1],'o',alpha=0.8,markersize=8,label=i,color=tableau20[i])
    plt.grid(True)
    leg = plt.legend(ncol=3,numpoints=1,scatterpoints=1,handletextpad=0.2,labelspacing=None,columnspacing=None,shadow=True,fancybox=True,bbox_to_anchor=(0.4,1.05)\
    ,prop={'family':'serif', 'size':'20', 'weight':'light'})
    for lh in leg.legendHandles: 
        lh._legmarker.set_alpha(1)


def project_plot_data():
    data = np.load('raw_data.npy')
    tica = io.loadh('original_SREP_tica.h5')
    print "raw_data.shape, vecs.shape:", data.shape, tica['vecs'].shape
    proj = np.dot(data,tica['components'].T)
    print "projected.shape:", proj.shape
    for i in range(len(proj)):
        plt.plot(proj[i][0],proj[i][1],'r*',markersize=18)
        plt.text(proj[i][0],proj[i][1],i,fontsize=18)

plt.figure(figsize=(10,8))
plot_macros()
project_plot_data()
plt.savefig('img_center_macro_location_on_tica.png')
#plt.show()
    

