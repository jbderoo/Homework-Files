# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:25:53 2015

@author: jderoo
"""

#%Jacob DeRoo
#%Pxy and Txy diagrams for Ethylene glycol (EG) and Ethanolamine (E)
#clear
#clc
#
#Mol_Conc_EG = linspace(0,1,100); %Varying Molar fractions of EG
#Mol_Conc_E = 1 - Mol_Conc_EG; %Varying Molar fraction of E with respect to EG
#
#Temp_C = 140; %Temperature = 140 C
#
#%Antoine's Constants
#Aeg = 8.0908; Beg = 2088.9; Ceg = 203.5; %Constants for Ethylene Glycol
#Ae = 7.4568; Be = 1577.67; Ce = 173.37; %Constants for Ethanolamine
#
#%Antoine's Equations
#Psat_EG = 10^(Aeg - (Beg/(Temp_C + Ceg))); %Saturation Pressure for EG
#Psat_E = 10^(Ae - (Be/(Temp_C + Ce))); %Saturation Pressure for E
#
#for i = 1:length(Mol_Conc_EG);
#    %Calculating Boiling Point Pressure
#    BP_Pressure(i) = Psat_EG.*Mol_Conc_EG(i) + Psat_E.*Mol_Conc_E(i);
#    %Calculating Vapor Mole Fraction of EG
#    Vapor_MF_EG(i) = (Psat_EG./BP_Pressure(i)).*Mol_Conc_EG(i);
#end
#
#figure;
#plot(Mol_Conc_EG, BP_Pressure, Vapor_MF_EG, BP_Pressure)
#xlabel('Molar Concentration Ethylene Glycol')
#ylabel('Pressure')
#title('Pxy for Ethylene Glycol and Ethanolamine')
#legend('Liquid Line', 'Vapor Line')
########
########
#Pressure = 760*.25; %Pressure = mm Hg
#
#for i = 1:length(Mol_Conc_EG);
#    %build a matrix solving 3 equations, 3 unknowns
#    %x = Y_EG Y_E Temperature
#               %Raoult's equation for EG
#    F = @ (x) [x(1)*Pressure - 10^(Aeg - Beg/(Ceg + x(3))).*Mol_Conc_EG(i);
#               %Raoult's equation for E
#               x(2)*Pressure - 10^(Ae - Be/(Ce + x(3))).*Mol_Conc_E(i);
#               %Vapor Pressure percents must add to 1
#               x(1) + x(2) - 1];
#           %initial guess
#           x0 = [Mol_Conc_EG(i), Mol_Conc_E(i), 50];
#           options = optimset('display','off');
#            
#           x = fsolve(F,x0, options);
#          
#           Vapor_Pressure_EG(i) = x(1);    
#           Vapor_Pressure_E(i) = x(2);
#           Temperature_BP(i) = x(3);
#           
#end
#
#figure;
#   plot(Mol_Conc_EG, Temperature_BP, Vapor_Pressure_EG, Temperature_BP)
#   xlabel('Molar Concentration')
#   ylabel('Temperature')
#   title('Txy for Ethylene Glycol and Ethanolamine')
#   legend('Liquid line', 'Vapor line') 

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#EG = Ethylene Glycol
Mol_Conc_EG  = np.linspace(0,1,100)
#E = Ethanolamine
Mol_Conc_E   = 1 - Mol_Conc_EG #Varying Molar fraction of E with respect to EG

#Temperature = 140 C
#Temp_C       = 140
#
#Antoine's Constants
#
#Constants for Ethylene Glycol
Aeg = 8.0908
Beg = 2088.9
Ceg = 203.5
#
#Constants for Ethanolamine
Ae  = 7.4568
Be  = 1577.67
Ce  = 173.37
#
##Antoine's Equations
#Psat_EG = 10 ** (Aeg - (Beg / (Temp_C + Ceg) ))   #Saturation Pressure for EG
#Psat_E  = 10 ** (Ae  - (Be  / (Temp_C + Ce ) ))   #Saturation Pressure for E
#
##Storage for Boiling Point and Vapor Mole Fraction of EG
#BP_Pressure = np.zeros(shape = (len(Mol_Conc_EG),1))
#Vapor_MF_EG = np.zeros(shape = (len(Mol_Conc_EG),1))
#
#MCE_cnt = len(Mol_Conc_EG)
#for i in range(0, MCE_cnt):    #= 1:length(Mol_Conc_EG);
#    #Calculating Boiling Point Pressure
#    BP_Pressure[i] = ((Psat_EG * Mol_Conc_EG[i]) + (Psat_E * Mol_Conc_E[i]))
#    #Calculating Vapor Mole Fraction of EG
#    Vapor_MF_EG[i] = ((Psat_EG / BP_Pressure[i]) * Mol_Conc_EG[i])
#
fig = plt.figure()
ax  = fig.add_subplot(111)
#plt.figure(1)
#plt.plot(Mol_Conc_EG, BP_Pressure, 'r', label='Liquid Line')
#plt.plot(Vapor_MF_EG, BP_Pressure, 'b', label='Vapor Line')
#ax.set_xlabel('Molar Concentration Ethylene Glycol')
#ax.set_ylabel('Pressure')
#ax.set_title('Pxy for Ethylene Glycol and Ethanolamine')
#plt.legend(loc='upper right')

#---------Start Plot 2---------------
Pressure = 760*.25 #Pressure = mm Hg

Vapor_Pressure_EG = np.zeros(shape = (len(Mol_Conc_EG),1))
Vapor_Pressure_E  = np.zeros(shape = (len(Mol_Conc_E),1))
Temperature_BP    = np.zeros(shape = (len(Mol_Conc_EG),1))

def saturation_pressure(x, y):
    eg  = ((x[0] * Pressure) -  ((10 ** ( (Aeg - Beg) / (Ceg + x[2])) ) * y[0]))
    e   = ((x[1] * Pressure) -  ((10 ** ( (Ae  - Be)  / (Ce + x[2]))  ) * y[1]))
    vp  = x[0] + x[1] - 1
    return [ eg, e, vp ]

for i in range(0,len(Mol_Conc_EG)):
       x0   = [Mol_Conc_EG[i], Mol_Conc_E[i], 50]
       Soln = fsolve(saturation_pressure,x0, [Mol_Conc_EG[i], Mol_Conc_E[i]])

       Vapor_Pressure_EG[i] = Soln[0]    
       Vapor_Pressure_E[i]  = Soln[1]
       Temperature_BP[i]    = Soln[2]

#end for loop

plt.figure(2)
plt.plot(Mol_Conc_EG, Temperature_BP, 'r', label='Vapor Line')
plt.plot(Vapor_Pressure_EG, Temperature_BP, 'b', label='Liquid Line')
ax.set_xlabel('Molar Concentration')
ax.set_ylabel('Temperature')
ax.set_title('Txy for Ethylene Glycol and Ethanolamine')
plt.legend(loc='upper right') 