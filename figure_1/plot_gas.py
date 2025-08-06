# plot of the free energy 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import random
from scipy import interpolate
from scipy.ndimage.filters import gaussian_filter

# load the data
# results in eV. 1eV = 23.0609 kcal/mol
fin = np.loadtxt('./gas_data/fes.dat')
x = fin[:,0]
y = fin[:,1]
z = fin[:,2]
z = np.array([i*23.0609 for i in z])
xnew, ynew = np.meshgrid(np.unique(x), np.unique(y))
Z = z.reshape((len(np.unique(y)), len(np.unique(x))))
znew = Z - np.min(Z)

fin = np.loadtxt('./gas_data/mep.dat')
cv1 = fin[:,0]
cv2 = fin[:,1]
nrg = fin[:,2]




# plot the data
max_val = 56
fig, ax = plt.subplots(figsize=(4,3))

# reverse the plots 
cv2 = (1 - cv2)
ynew = (1 - ynew)

levels = np.linspace(0, max_val, int((max_val+1)))
cs = ax.contourf(xnew,ynew,znew,
                  vmin=0,vmax=max_val,
                  levels=levels,
                  cmap=cm.plasma)
cbar = fig.colorbar(cs)
cbar.ax.set_ylabel('Free Energy  (kcal/mol)',size=10)
cbar.ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)
clevels = np.linspace(0, max_val, 10)
ax.contour(xnew, ynew, znew, levels=clevels, colors='black', linewidths=0.5,# gray color
                  linestyles='solid', alpha=0.5)
ax.plot(cv1, cv2, 'ro-', label='Optimized Path',
        color='white', linewidth=2,
        ms=5)
ax.set_xlabel(r'$s_\mathrm{CO}$',size=12)
ax.set_ylabel(r'$1 - s_\mathrm{(OH)_{g}}$',size=12)
ax.set_xlim(1.75,2.9)
ax.set_ylim(0.05,1)

#plt.savefig('final_plot_reverse.png',dpi=400,bbox_inches='tight',transparent=False, edgecolor='none')
plt.show()