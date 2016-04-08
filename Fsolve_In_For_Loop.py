# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:25:53 2015

@author: jderoo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#------Start Plot P-x-y Diagram---------

# EG = Ethylene Glycol
Mol_Conc_EG   = np.linspace(0,1,100)
# E = Ethanolamine
Mol_Conc_E    = 1 - Mol_Conc_EG # Varying Molar fraction of E with respect to EG

# Temperature = 140 C
Temp_C        = 140

# Antoine's Constants

# Constants for Ethylene Glycol
Aeg = 8.0908
Beg = 2088.9
Ceg = 203.5

# Constants for Ethanolamine
Ae  = 7.4568
Be  = 1577.67
Ce  = 173.37

# Antoine's Equations
Psat_EG = 10 ** (Aeg - (Beg / (Temp_C + Ceg) ))   # Saturation Pressure for EG
Psat_E  = 10 ** (Ae  - (Be  / (Temp_C + Ce ) ))   # Saturation Pressure for E

# Storage for Boiling Point and Vapor Mole Fraction of EG
BP_Pressure = np.zeros(shape = (len(Mol_Conc_EG),1))
Vapor_MF_EG = np.zeros(shape = (len(Mol_Conc_EG),1))

# Less Calculations in for loop
MCE_cnt = len(Mol_Conc_EG)

for i in range(0, MCE_cnt):
    # Calculating Boiling Point Pressure
    BP_Pressure[i] = ((Psat_EG * Mol_Conc_EG[i]) + (Psat_E * Mol_Conc_E[i]))
    # Calculating Vapor Mole Fraction of EG
    Vapor_MF_EG[i] = ((Psat_EG / BP_Pressure[i]) * Mol_Conc_EG[i])

# end for loop

fig = plt.figure(1)
ax  = fig.add_subplot(111)
plt.figure(1)
plt.plot(Mol_Conc_EG, BP_Pressure, 'r', label='Liquid Line')
plt.plot(Vapor_MF_EG, BP_Pressure, 'b', label='Vapor Line')
ax.set_xlabel('Molar Concentration Ethylene Glycol')
ax.set_ylabel('Pressure')
ax.set_title('Pxy for Ethylene Glycol and Ethanolamine')
plt.legend(loc='upper right')

#---------Start Plot T-x-y Diagram---------------

Pressure = 760*.25 # Pressure = mm Hg

Vapor_Pressure_EG = np.zeros(shape = (len(Mol_Conc_EG),1))
Vapor_Pressure_E  = np.zeros(shape = (len(Mol_Conc_E),1))
Temperature_BP    = np.zeros(shape = (len(Mol_Conc_EG),1))

for i in range(0, MCE_cnt):
    # build a matrix solving 3 equations, 3 unknowns
    # x[0] = Partial Pressure (Vapor) EG 
    # x[1] = Partial Pressure (Vapor) E
    # x[2] = Boiling Point Temperature Celcius
              
    def Dumby_Function(x):        # Raoult's equation for EG
        return [(x[0] * Pressure) - ((10 ** (Aeg - (Beg / (Ceg + x[2])))) * Mol_Conc_EG[i]),
                     # Raoult's equation for E
                (x[1] * Pressure) - ((10 ** (Ae -  (Be  /  (Ce + x[2])))) * Mol_Conc_E[i]),
                     # Vapor Pressure percents must add to 1
                x[0] + x[1] - 1,
                ] # end function call
           # initial guess
    guess = [Mol_Conc_EG[i], Mol_Conc_E[i], 90]
        
    Soln = fsolve(Dumby_Function,guess)
          
    Vapor_Pressure_EG[i] = Soln[0] # build vapor pressure EG vector 
    Vapor_Pressure_E[i] = Soln[1]  # build vapor pressure E vector
    Temperature_BP[i] = Soln[2]    # build temperature vector

# end for loop

fig = plt.figure(2)
ax  = fig.add_subplot(111)
plt.figure(2)
plt.plot(Mol_Conc_EG, Temperature_BP, 'r', label='Vapor Line')
plt.plot(Vapor_Pressure_EG, Temperature_BP, 'b', label='Liquid Line')
ax.set_xlabel('Molar Concentration')
ax.set_ylabel('Temperature')
ax.set_title('Txy for Ethylene Glycol and Ethanolamine')
plt.legend(loc='upper left') 