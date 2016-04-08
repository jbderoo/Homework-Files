# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:54:00 2016

@author: jderoo
"""


from scipy.optimize import fsolve

def F(x):
    return -(((4.14e-4) * x[0]**3) - x[0]**2 + 152.5*(x[0]) + 5800)
    
guess = 2250
soln  = fsolve(F, guess)

volume = soln[0]
print(volume, 'cm^3')
# 2248.89391411 cm^3

Z = (1800 * volume) / (8314 * 523)
print('Z is', Z)
# Z is 0.930957307471