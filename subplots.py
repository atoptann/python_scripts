# This document is prepared by Aysenur Toptan
# for

import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
import os

import matplotlib as mpl
from matplotlib import cm


plt.rc("font", size=14)
mpl.rcParams['legend.fontsize'] = 9

fig = plt.figure(figsize=(8,7))
xlist = np.linspace(0.0, 20.0, 50)
ylist = np.linspace(0.0, 20.0, 50)
X, Y = np.meshgrid(xlist, ylist)
Z= np.sqrt(X**2+Y**2)

plt.subplot(2,2,1)
plt.title('Default')
plt.contourf(X, Y, Z, 10)
plt.colorbar()

plt.subplot(2,2,2)
plt.title('Coolwarm')
plt.contourf(X, Y, Z, 10, cmap=cm.coolwarm) # 20 : number of levels
plt.colorbar()

plt.subplot(2,2,3)
plt.title('RdBu')
plt.contourf(X, Y, Z, 10, cmap=cm.RdBu) # 20 : number of levels
plt.colorbar()

plt.subplot(2,2,4)
plt.title('Rainbow')
plt.contourf(X, Y, Z, 10, cmap=cm.rainbow) # 20 : number of levels
plt.colorbar()

plt.savefig('subplot_contourf_2d.png');
plt.close(fig)
