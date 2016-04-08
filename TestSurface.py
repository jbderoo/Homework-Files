# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:56:55 2015

@author: jderoo
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#D is a vector from 0 to 3, 100 spaces in between
D = np.linspace(0,3,100)
#U is a vector from 0 to 3, 100 spaces in between
U = np.linspace(0,3,100)
#A is a blank matrix/list
A = []

#for loop that ranges i from 0 to 100 steps of 1
for i in range(0,100,1):
    #for loop that ranges j from 0 to 100 steps of 1
    for j in range(0,100,1):
#The base equation we were given in the homework
      r = ((3*D[i]*(U[j])^.7)/(1 + D[i]^.95 + U[j])^.3)
 #in cell location i,j place the calced value of r     
      A[i,j] = r
#3D plot D, U, and the now filled matrix A
Axes3D.plot_surface(D,U,A)