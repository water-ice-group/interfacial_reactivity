# plot of the free energy 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import random
from scipy import interpolate
from scipy.ndimage.filters import gaussian_filter

plt.rcParams['lines.linewidth']                 = 2                      # Linewidth
plt.rcParams['axes.linewidth']                  = 1.2                    # Axes linewidth
plt.rcParams['font.family']                     = 'DejaVu Sans'                # Font family
plt.rcParams['mathtext.fontset']                = 'dejavusans'           # Math font

# load the data
fin = np.loadtxt('./bulk_data/fes.dat')
x = fin[:,0]
y = fin[:,1]
z = fin[:,2]
xnew, ynew = np.meshgrid(np.unique(x), np.unique(y))
Z = z.reshape((len(np.unique(y)), len(np.unique(x))))
znew = Z - np.min(Z)

fin = np.loadtxt('./bulk_data/mep.dat')
cv1 = fin[:,0]
cv2 = fin[:,1]
nrg = fin[:,2]




# plot the data
max_val = 28
fig, ax = plt.subplots(figsize=(4,3))

levels = np.linspace(0, max_val, int((max_val+1)))
cs = ax.contourf(xnew,ynew,znew,
                  vmin=0,vmax=max_val,
                  levels=levels,
                  cmap=cm.plasma
                  )
cbar = fig.colorbar(cs)
cbar.ax.set_ylabel('Free Energy  (kcal/mol)',size=10)
cbar.ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set_xticks([2,2.2,2.4,2.6,2.8,3])
clevels = np.linspace(0, max_val, 10)
ax.contour(xnew, ynew, znew, levels=clevels, colors='black', linewidths=0.5,
           linestyles='solid',alpha=0.5)
ax.plot(cv1, cv2, '^-', label='Optimized Path',
        color='white', linewidth=2,
        ms=4)

ax.set_xlabel(r'$s_\mathrm{CO}$',size=12)
ax.set_ylabel(r'$s_\mathrm{(OH)_{aq}}$',size=12)
ax.set_xlim(1.9,3.1)
ax.set_ylim(0,2)

#plt.savefig('final_plot.png',dpi=400,bbox_inches='tight',transparent=False, edgecolor='none')
plt.show()