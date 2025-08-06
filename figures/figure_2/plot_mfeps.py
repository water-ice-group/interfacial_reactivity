import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.transforms import Bbox

plt.rcParams['lines.linewidth']                 = 2                      # Linewidth
plt.rcParams['axes.linewidth']                  = 1.2                    # Axes linewidth
plt.rcParams['font.family']                     = 'DejaVu Sans'                # Font family
plt.rcParams['mathtext.fontset']                = 'dejavusans'           # Math font





# load the data
fin_gas = np.loadtxt('./mfeps/mep_gas.dat')
fin_nrg = fin_gas[:,2]
xrange_gas = np.linspace(0,1,len(fin_nrg))
fin_bulk = np.loadtxt('./mfeps/mep_bulk.dat')
fin_nrg_bulk = fin_bulk[:,2]
xrange_bulk = np.linspace(0,1,len(fin_nrg_bulk))
fin_inter = np.loadtxt('./mfeps/mep_inter.dat')
fin_nrg_inter = fin_inter[:,2]
xrange_inter = np.linspace(0,1,len(fin_nrg_inter))







# plot the data
fig, ax2 = plt.subplots(figsize=(3,4))
line_gas, = ax2.plot(xrange_gas, fin_nrg, 'o-', color='darkgreen', label='Gas', ms=7, markeredgewidth=1.5, markeredgecolor='darkgreen')
line_gas.set_markerfacecolor((0.56, 0.93, 0.56, 0.7))  # lightgreen with alpha 0.7
line_bulk, = ax2.plot(xrange_bulk, fin_nrg_bulk, '^-', color='blue', label='Bulk', ms=7, markeredgewidth=1.5, markeredgecolor='blue')
line_bulk.set_markerfacecolor((0.68, 0.85, 0.9, 0.7))  # lightblue with alpha 0.7
ax2.plot(xrange_inter, fin_nrg_inter, 'x-', color='red', label='Inter', ms=7)
print(fin_nrg[-1])
print(fin_nrg_bulk[-1])
print(fin_nrg_inter[-1])
ax2.set_xlabel('Extent of reaction', size=11)
ax2.axes.yaxis.set_minor_locator(AutoMinorLocator())
ax2.axes.xaxis.set_minor_locator(AutoMinorLocator())
ax2.tick_params(which='both', direction='in')
ax2.legend(bbox_to_anchor=(0.58, 1.5), loc='upper left', 
           ncol=1, frameon=True, columnspacing=1.5, handletextpad=0.8,
           handlelength=2)
ax2.grid(ls='--')

insetx_min = 0.65
insetx_max = 1.05
insety_min = 7.5
insety_max = 17
rect = plt.Rectangle((insetx_min, insety_min), insetx_max - insetx_min, insety_max - insety_min, linewidth=1, edgecolor='black', facecolor='none', linestyle='--')
ax2.add_patch(rect)
bbox = Bbox.from_bounds(0.031, 1.07, 0.45, 0.4)
ax_inset = inset_axes(ax2, width="100%", height="100%", bbox_transform=ax2.transAxes, bbox_to_anchor=bbox)
line_gas, = ax_inset.plot(xrange_gas, fin_nrg, 'o-', color='darkgreen', ms=7, markeredgewidth=1.5, markeredgecolor='darkgreen')
line_gas.set_markerfacecolor((0.56, 0.93, 0.56, 0.7))  # lightgreen with alpha 0.7
line_bulk, = ax_inset.plot(xrange_bulk, fin_nrg_bulk, '^-', color='blue', ms=7, markeredgewidth=1.5, markeredgecolor='blue')
line_bulk.set_markerfacecolor((0.68, 0.85, 0.9, 0.7))  # lightblue with alpha 0.7
ax_inset.plot(xrange_inter, fin_nrg_inter, 'x-', color='red', ms=7)
ax_inset.set_xlim(insetx_min, insetx_max)
ax_inset.set_ylim(insety_min, insety_max)
ax_inset.tick_params(which='both', direction='in')
ax_inset.axes.yaxis.set_minor_locator(AutoMinorLocator())
ax_inset.axes.xaxis.set_minor_locator(AutoMinorLocator())
ax_inset.grid(ls='--')
ax_inset.yaxis.set_label_position("right")
ax_inset.yaxis.tick_right()
ax_inset.xaxis.set_label_position("top")
ax_inset.xaxis.tick_top()

plt.tight_layout()
plt.subplots_adjust(wspace=0.2)
#plt.savefig('mfeps.png', dpi=400, bbox_inches='tight', transparent=False, edgecolor='none')
plt.show()