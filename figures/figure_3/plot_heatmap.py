import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
import scipy.stats as stats

plt.rcParams['lines.linewidth']                 = 2                      # Linewidth
plt.rcParams['axes.linewidth']                  = 1.2                    # Axes linewidth
plt.rcParams['font.family']                     = 'DejaVu Sans'                # Font family
plt.rcParams['mathtext.fontset']                = 'dejavusans'           # Math font


## load the data
# -------------------------------------------------------------
result = np.loadtxt(f'data/colvar/colvar_walker_1.dat')
data = (result[:,0]/(10**6), result[:,1],result[:,2])
cv_x  = data[0][1:]
cv_y  = data[1][1:]
cv_y2 = data[2][1:]
dist = np.loadtxt('data/dist_time/dens_time_walker_1.dat')
dist_x = np.linspace(0,len(dist),len(dist))/(10**4)
dist_y = dist 
result2 = np.loadtxt('data/colvar/colvar_walker_2.dat')
data2 = (result2[:,0]/(10**6), result2[:,1], result2[:,2])
cv_x = np.append(cv_x, data2[0][1:])
cv_y = np.append(cv_y, data2[1][1:])
cv_y2 = np.append(cv_y2, data2[2][1:])
dist2 = np.loadtxt('data/dist_time/dens_time_walker_2.dat')
dist_y = np.append(dist_y, dist2)
dist_x = np.linspace(0, len(dist_y), len(dist_y)) / (10**4)
result3 = np.loadtxt('data/colvar/colvar_walker_3.dat')
data3 = (result3[:,0]/(10**6), result3[:,1], result3[:,2])
cv_x = np.append(cv_x, data3[0][1:])
cv_y = np.append(cv_y, data3[1][1:])
cv_y2 = np.append(cv_y2, data3[2][1:])
dist3 = np.loadtxt('data/dist_time/dens_time_walker_3.dat')
dist_y = np.append(dist_y, dist3)
result4 = np.loadtxt('data/colvar/colvar_walker_4.dat')
data4 = (result4[:,0]/(10**6), result4[:,1], result4[:,2])
cv_x = np.append(cv_x, data4[0][1:])
cv_y = np.append(cv_y, data4[1][1:])
cv_y2 = np.append(cv_y2, data4[2][1:])
dist4 = np.loadtxt('data/dist_time/dens_time_walker_4.dat')
dist_y = np.append(dist_y, dist4)
result5 = np.loadtxt('data/colvar/colvar_walker_5.dat')
data5 = (result5[:,0]/(10**6), result5[:,1], result5[:,2])
cv_x = np.append(cv_x, data5[0][1:])
cv_y = np.append(cv_y, data5[1][1:])
cv_y2 = np.append(cv_y2, data5[2][1:])
dist5 = np.loadtxt('data/dist_time/dens_time_walker_5.dat')
dist_y = np.append(dist_y, dist5)
# -------------------------------------------------------------






# Perform 2D histogram
# -------------------------------------------------------------
minval = -1.5
maxval = 1.5
hist, xedges, yedges = np.histogram2d(cv_y, dist_y, bins=100,
                                      range=[[2.0, 3], [minval,maxval]],
                                      density=False)
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
X, Y = np.meshgrid(xcenters, ycenters)

# Calculate the mean distance for each CV bin
selected = np.where((dist_y > minval) & (dist_y < maxval)) # restrict to the interfacial region
dens,xedges,*_ = stats.binned_statistic(cv_y[selected], dist_y[selected], statistic='mean', 
                                   bins=50, range=[(2, 3)])
xval = (xedges[:-1] + xedges[1:]) / 2
# -------------------------------------------------------------







# Plot the 2D histogram 
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4,3))
c = ax.pcolormesh(X, Y, hist.T, cmap='viridis')
c.set_clim(vmin=5, vmax=50) # cap at 50 to prevent saturation from reactant/product states
fig.colorbar(c, ax=ax)
ax.set_xlim(2.0,3)
ax.tick_params(which='both', direction='out',labelsize=10)

plt.plot(xval, dens, '--',
         color='white', linewidth=2.5)
plt.xlabel(r'$s_\mathrm{CO}$',fontsize=12)
plt.ylabel(r'$d_\mathrm{int}$  (Å)',fontsize=12)
#plt.savefig(f'./figures/heatmap_final.png',dpi=800,bbox_inches='tight', edgecolor='none',transparent=False)
plt.show()
