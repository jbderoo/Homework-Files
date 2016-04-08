# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:56:55 2015

@author: jderoo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

D       = np.linspace(0,3,100)
U       = np.linspace(0,3,100)
R       = np.zeros(shape=(100,100))
rmax    = 0

for i in range(1,100,1):
        for j in range(0,100,1):
                divadend    = ((3 * D[i]) * (U[j] ** .7))
                sor1        = D[i] ** .95
                sor2        = 1 + sor1 + U[j]
                sor3        = sor2 ** 3
                R[i][j]     = divadend / sor3
#This is where things fall apart I think.         
                if R[i][j] > rmax:
                    rmax            = R[i][j]
                    D_optimum_input = D[i]
                    U_optimum_input = U[j]

#I pulled line 32 from the internet. I understand what it does,
#But I don't understand how it does what it does.
#R_min, R_max = -np.abs(R).max(), np.abs(R).max()

fig          = plt.figure()
ax           = fig.add_subplot(111, projection='3d')
surf         = ax.plot_surface(D, U, R, cmap=cm.hsv, vmax = rmax)
ax.set_xlabel('D Conc Label')
ax.set_ylabel('U Conc Label')
ax.set_zlabel('Dmab Conc Label')
ax.set_title('3D Surface Plot finding best Concentrations in')
fig.colorbar(surf, shrink=0.5, aspect=5)

print()
print('The optimum D Conc in is', D_optimum_input)
print('The optimum U Conc in is', U_optimum_input)
print('The highest Dmab Conc out is', rmax)
print()
print('Ignore warning below')
print()