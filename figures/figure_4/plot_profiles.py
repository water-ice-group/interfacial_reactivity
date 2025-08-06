import matplotlib.pyplot as plt 
from matplotlib.ticker import AutoMinorLocator
import numpy as np
from scipy import stats

# load the data 
# -------------------------------------------------------------
# densities
fin = np.loadtxt('data/density/co2_density.dat')
co2_dens_x = fin[:,0]
co2_dens_y = fin[:,1]
fin = np.loadtxt('data/density/bic_density.dat')
bic_dens_x = fin[:,0]
bic_dens_y = fin[:,1]
fin = np.loadtxt('data/density/ca_density.dat')
ca_dens_x = fin[:,0]
ca_dens_y = fin[:,1]
fin = np.loadtxt('data/density/ts_density.dat')
ts_dens_x = fin[:,0]
ts_dens_y = fin[:,1]

# coordination numbers
fin = np.loadtxt('data/cn/co2_coord.dat')
co2_coord_x = fin[:,0]
co2_coord_y = fin[:,1]
fin = np.loadtxt('data/cn/bic_coord.dat')
bic_coord_x = fin[:,0]
bic_coord_y = fin[:,1]
fin = np.loadtxt('data/cn/ca_coord.dat')
ca_coord_x = fin[:,0]
ca_coord_y = fin[:,1]
fin = np.loadtxt('data/cn/ts_coord.dat')
ts_coord_x = fin[:,0]
ts_coord_y = fin[:,1]

# hbonding 
fin = np.loadtxt('data/hbonds/co2_hbonds.dat')
co2_hbond_x = fin[:,0]
co2_hbond_y = fin[:,1]
fin = np.loadtxt('data/hbonds/bic_hbonds.dat')
bic_hbond_x = fin[:,0]
bic_hbond_y = fin[:,1]
fin = np.loadtxt('data/hbonds/ca_hbonds.dat')
ca_hbond_x = fin[:,0]
ca_hbond_y = fin[:,1]
fin = np.loadtxt('data/hbonds/ts_hbonds.dat')
ts_hbond_x = fin[:,0]
ts_hbond_y = fin[:,1]


# water density
fin = np.loadtxt(f'./data/OXY_dens.dat')
x_h2o = fin[:,0]
y_h2o = fin[:,1]
# -------------------------------------------------------------







# plot the profiles
# -------------------------------------------------------------
fig,ax=plt.subplots(3,1,figsize=(3,6))

# -------------------------------------------------------------------------------------
ax[0].plot(co2_dens_x,co2_dens_y,label='CO$_2$',color='darkgreen')
ax[0].plot(ca_dens_x,ca_dens_y,label=r'H$_2$CO$_3$',color='orange')
ax[0].plot(bic_dens_x,bic_dens_y,label=r'HCO$_3^{-}$',color='#003399')
ax[0].plot(ts_dens_x,ts_dens_y,label=r'TS$^{\ddag}$',color='black')
ax[0].set_yticks([])
ax[0].set_ylabel(r'$\rho \mathrm{(C)}$',size=10)
ax[0].set_ylim(0,0.8)
ax[0].axes.xaxis.set_minor_locator(AutoMinorLocator())
ax[0].tick_params(which='both', direction='in')
ax[0].grid(ls='--')

secax = ax[0].twinx()
secax.plot(x_h2o,y_h2o,
           color='maroon',lw=1.8,
           label=r'H$_2$O')
zeros = np.zeros(len(x_h2o))
secax.fill_between(x_h2o,y_h2o,zeros,color='red',alpha=0.2)
secax.set_xlim(-8,4)
secax.set_ylim(0,1.7)
secax.set_ylabel(r'$\rho \mathrm{(H_2O)}$  (g/ml)',size=10)
secax.axes.xaxis.set_ticklabels([])
secax.axes.yaxis.set_minor_locator(AutoMinorLocator())
secax.grid(ls='--')
secax.tick_params(labelsize=9)

lines, labels = ax[0].get_legend_handles_labels()
lines2, labels2 = secax.get_legend_handles_labels()
secax.legend(lines + lines2, labels + labels2, 
             loc=[-0.01,1.04], ncol=3,
             handlelength=1.2,  # Reduced handle length
             frameon=True,
             fontsize=10,
             labelspacing=0.1,  # Reduced spacing between labels
             columnspacing=1)  # Reduced spacing between columns



# -------------------------------------------------------------------------------------
ax[1].plot(co2_coord_x,co2_coord_y,label='CO$_2$',color='darkgreen')
# CA
ax[1].plot(ca_coord_x,ca_coord_y,label=r'H$_2$CO$_3$',color='orange')
last_dig = np.where(~np.isnan(ca_coord_y))[0][-1]
ax[1].vlines(x=ca_coord_x[last_dig],ymin=0,ymax=ca_coord_y[last_dig],color='orange',ls=':',lw=1.5)
# BiC
ax[1].plot(bic_coord_x,bic_coord_y,label=r'HCO$_3^{-}$',color='#003399')
last_dig = np.where(~np.isnan(bic_coord_y))[0][-1]
ax[1].vlines(x=bic_coord_x[last_dig],ymin=0,ymax=bic_coord_y[last_dig],color='#003399',ls=':',lw=1.5)
# TS
ax[1].plot(ts_coord_x,ts_coord_y,label=r'TS$^{\ddag}$',color='black')
last_dig = np.where(~np.isnan(ts_coord_y))[0][-1]
ax[1].vlines(x=ts_coord_x[last_dig],ymin=0,ymax=ts_coord_y[last_dig],color='black',ls=':',lw=1.5)

ax[1].set_xlim(-8,4)
ax[1].set_ylabel(r'$\langle q_\mathrm{sol} \rangle$',size=11)
ax[1].axes.xaxis.set_ticklabels([])
ax[1].axes.yaxis.set_minor_locator(AutoMinorLocator())
ax[1].axes.xaxis.set_minor_locator(AutoMinorLocator())
ax[1].tick_params(which='both', direction='in')
ax[1].grid(ls='--')
ax[1].set_yticks([0,1,2,3,4,5])
ax[1].set_ylim(0,5.8)
# -------------------------------------------------------------------------------------
ax[2].plot(co2_hbond_x,co2_hbond_y,label='CO$_2$',color='darkgreen')
# CA
ax[2].plot(ca_hbond_x,ca_hbond_y,label='CA',color='orange')
last_digit = np.where(~np.isnan(ca_hbond_y))[0][-1]
ax[2].vlines(x=ca_hbond_x[last_digit],ymin=0,ymax=ca_hbond_y[last_digit],color='orange',ls=':',lw=1.5)
# BiC
ax[2].plot(bic_hbond_x,bic_hbond_y,label='BiC',color='#003399')
last_digit = np.where(~np.isnan(bic_hbond_y))[0][-1]
ax[2].vlines(x=bic_hbond_x[last_digit],ymin=0,ymax=bic_hbond_y[last_digit],color='black',ls=':',lw=1.5)
# TS
ax[2].plot(ts_hbond_x,ts_hbond_y,label=r'TS$^{\ddag}$',color='black')
last_digit = np.where(~np.isnan(ts_hbond_y))[0][-1]
#ax[2].vlines(x=ts_hbond_x[last_digit],ymin=0,ymax=ts_hbond_y[last_digit],color='black',ls=':',lw=1.5)

ax[2].set_xlim(-8,4)
ax[2].axes.yaxis.set_minor_locator(AutoMinorLocator())
ax[2].axes.xaxis.set_minor_locator(AutoMinorLocator())
ax[2].tick_params(which='both', direction='in')
ax[2].set_ylabel(r'$\langle n_\mathrm{HB} \rangle$',size=11)
ax[2].set_xlabel(r'$d_\mathrm{int}$  (Å)',size=11)
ax[2].grid(ls='--')
ax[2].set_yticks([0,1,2,3,4,5])
ax[2].set_ylim(0,6)


plt.subplots_adjust(hspace=0.05)
#plt.savefig(f'./profile.pdf',dpi=800,bbox_inches='tight',facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()
