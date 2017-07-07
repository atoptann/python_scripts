# This document is prepared by Aysenur Toptan
# for

import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
import csv
import os

import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d


plt.rc("font", size=14)
mpl.rcParams['legend.fontsize'] = 9

fig = plt.figure(figsize=(8,7))
xlist = np.linspace(0.0, 20.0, 50)
ylist = np.linspace(0.0, 20.0, 50)
X, Y = np.meshgrid(xlist, ylist)
Z= np.sqrt(X**2+Y**2)
plt.contourf(X, Y, Z, 20, cmap=cm.coolwarm) # 20 : number of levels
plt.colorbar()
plt.xlabel('$X_{1}$')
plt.ylabel('$X_{2}$')
plt.title('$X_{3}$')
plt.grid(True)
plt.savefig('contourf_2d.png');
plt.close(fig)
