import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from matplotlib import cm


# load the data
fin = np.loadtxt('./inter/fes.dat')
x = fin[:,0]
y = fin[:,1]
z = fin[:,2]
xnew, ynew = np.meshgrid(np.unique(x), np.unique(y))
Z = z.reshape((len(np.unique(y)), len(np.unique(x))))
znew = Z - np.min(Z)

fin = np.loadtxt('./mfeps/mep_inter.dat')
cv1 = fin[:,0]
cv2 = fin[:,1]
nrg = fin[:,2]






# plot the data 
fig, ax1 = plt.subplots(figsize=(4, 3))

max_val = 28
levels = np.linspace(0, max_val, int((max_val+1)))
clevels = np.linspace(0, max_val, 10)

cs = ax1.contourf(xnew,ynew,znew,
                  vmin=0,vmax=max_val,
                  levels=levels,
                  cmap=cm.plasma)
cbar = fig.colorbar(cs, ax=ax1)
cbar.ax.set_ylabel('Free Energy  (kcal/mol)', size=10,
                   labelpad=8)
cbar.ax.tick_params(axis='both', which='major', labelsize=10)
ax1.tick_params(axis='both', which='major', labelsize=10)
ax1.set_xticks([2, 2.2, 2.4, 2.6, 2.8, 3])
ax1.contour(xnew, ynew, znew, levels=clevels, colors='black', linewidths=0.5, linestyles='solid', alpha=0.5)
ax1.plot(cv1, cv2, 'x-', label='Optimized Path', color='white', linewidth=2, ms=6)
ax1.set_xlabel(r'$s_\mathrm{CO}$', size=11)
ax1.set_ylabel(r'$s_\mathrm{(OH)_{aq}}$', size=11)
ax1.set_xlim(1.9, 3.1)
ax1.set_ylim(0, 2)
ax1.set_yticks([0,0.25,0.5,0.75,1,1.25,1.5,1.75,2])

plt.tight_layout()
plt.subplots_adjust(wspace=0.2)
#plt.savefig('fep_inter.png', dpi=400, bbox_inches='tight', transparent=False, edgecolor='none')
plt.show()