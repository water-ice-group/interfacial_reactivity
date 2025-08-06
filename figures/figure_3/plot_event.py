import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

plt.rcParams['lines.linewidth']                 = 2                      # Linewidth
plt.rcParams['axes.linewidth']                  = 1.2                    # Axes linewidth
plt.rcParams['font.family']                     = 'DejaVu Sans'                # Font family
plt.rcParams['mathtext.fontset']                = 'dejavusans'           # Math font






# load data and calculate runing averages
# -------------------------------------------------------------
fin = np.loadtxt('data/OXY_dens.dat')
ox_x = fin[:,0]
ox_y = fin[:,1]

result = np.loadtxt(f'data/colvar/colvar_walker_1.dat')
result = np.loadtxt(f'data/colvar/colvar_walker_3.dat')
data = (result[:,0]/(10**6), result[:,1],result[:,2])
cv_x = data[0]
cv_y = data[1]
block_size = 100
cv_y_running_avg_w3 = np.convolve(cv_y, np.ones(block_size)/block_size, mode='valid')
cv_x_filtered_w3 = cv_x[:len(cv_y_running_avg_w3)]
dist = np.loadtxt('data/dist_time/dens_time_walker_3.dat')
dist_x = np.linspace(0,len(dist),len(dist))/(10**4)
dist_y = dist
dist_y_running_avg_3 = np.convolve(dist_y, np.ones(block_size)/block_size, mode='valid')
dist_x_filtered_3 = dist_x[:len(dist_y_running_avg_3)]

event_2_w3 = np.where((cv_x_filtered_w3 > 0.78) & (cv_x_filtered_w3 < 0.98))[0] # location of the reactive event
# -------------------------------------------------------------







# plot the data
# -------------------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(5, 2), gridspec_kw={'width_ratios': [4, 1]})

ymin, ymax = 2, 3.15
min_val, max_val = min(cv_x_filtered_w3[event_2_w3]), max(cv_x_filtered_w3[event_2_w3]) 
min_dist_ref, max_dist_ref = -1.5, 1
a = (max_dist_ref - min_dist_ref) / (ymax - ymin)
b = min_dist_ref - a * ymin
def s_to_d(s):
    return ((s-2.75) * 4 )
def d_to_s(d):
    return (d / 4) + 2.75

# Primary y-axis plot
ax[0].plot(cv_x_filtered_w3[event_2_w3], cv_y_running_avg_w3[event_2_w3],
           label=r'$s_\mathrm{CO}$', color='#417e8c',lw=2.5)
ax[0].set_xlim(min_val, max_val)
ax[0].set_ylim(ymin, ymax)
ax[0].set_xlabel('Time  (ns)', size=10)
ax[0].set_ylabel(r'$s_\mathrm{CO}$', size=12)
ax[0].axes.yaxis.set_minor_locator(AutoMinorLocator())
ax[0].axes.xaxis.set_minor_locator(AutoMinorLocator())
ax[0].tick_params(which='both', direction='in')
ax[0].grid(ls='--')
ax[0].set_yticks([2.0, 2.25, 2.5, 2.75, 3.0])
ax[0].set_xticks([0.8, 0.85, 0.9, 0.95])

secax = ax[0].twinx()
secax.plot(dist_x_filtered_3[event_2_w3], dist_y_running_avg_3[event_2_w3], '--',
           label=r'$d_\mathrm{int}$', color='black', lw=2)
secax.set_ylim(s_to_d(ymin), s_to_d(ymax))
secax.axes.yaxis.set_ticklabels([])
secax.set_yticks(s_to_d(np.array([2.0, 2.25, 2.5, 2.75, 3.0])))  # Example alignment
lines, labels = ax[0].get_legend_handles_labels()
lines2, labels2 = secax.get_legend_handles_labels()
secax.legend(lines + lines2, labels + labels2, loc='lower right')

# Secondary axis plot
ax[1].plot(ox_y, ox_x, label='Density', color='maroon',lw=2)
zeros = np.zeros(len(ox_x))
ax[1].fill_betweenx(ox_x, ox_y, where=ox_y > zeros, color='red', alpha=0.2)
ax[1].set_ylim(s_to_d(ymin), s_to_d(ymax))
ax[1].set_xlim(0, 1.7)
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_ylabel(r'$d_\mathrm{int}$  (Å)', fontsize=10)
ax[1].set_xlabel(r'$\rho$  (Å)',size=10)
ax[1].set_yticks(s_to_d(np.array([2.0, 2.25, 2.5, 2.75, 3.0])))
ax[1].tick_params(axis='x', direction='in')

# inset axis
ax_inset = fig.add_axes([0.77, 0.68, 0.12, 0.18])
ax_inset.plot(-ox_x, ox_y, label='Density', color='maroon')
shaded_region = np.where((-ox_x > -1) & (-ox_x < 3))

ax_inset.fill_between(-ox_x[shaded_region], [-0.5]*len(ox_x[shaded_region]),  [1.8]*len(ox_x[shaded_region]), color='red', alpha=0.2)
ax_inset.set_ylim(-0.1,1.6)
ax_inset.set_xticks([])
ax_inset.set_yticks([])
plt.subplots_adjust(wspace=0.0)
#plt.savefig('./figures/test.png', dpi=800, bbox_inches='tight', edgecolor='none', transparent=False)
plt.show()