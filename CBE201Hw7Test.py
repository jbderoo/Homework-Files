# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:03:14 2015
@author: jderoo
"""
from scipy.optimize import fsolve

def Joule_func(A, B, C, D, Temp_K): # where Temp_K is Temperature in Kelvin, A B C D are constants
    Joules = (A * Temp_K) + ((B / 2) * Temp_K**2) + ((C / 3) * Temp_K**3) + ((D / 4) * Temp_K**4)   
    return Joules

def Cp_func(A, B, C, D, Temp_K):  # where Temp_K is Temperature in Kelvin, A B C D are constants
    Cp = A + (B * Temp_K) + (C * Temp_K**2) + (D * Temp_K**3)
    return Cp  
    

def inv_Joule_func(Temp_C): # where Temp_C is Temperature in Celcius, A B C D are constants
    return (32.24 * Temp_C) + ((.001924 / 2) * Temp_C**2) + ((1.055e-5 / 3) * Temp_C**3) + ((-3.596e-9 / 4) * Temp_C**4) - 13173.988703326577  

def Antoines_Eq(A1, B1, C1, Temp_C1):
    Psat = 10 ** (A1 - (B1/(C1 + Temp_C1)))
    return Psat


#-----------question 1----------
print('Question 1 answers:')
Cp1 = Joule_func(32.24, .001924, 1.055e-5, -3.596e-9, 593) - Joule_func(32.24, .001924, 1.055e-5, -3.596e-9, 373)
# 20 kg water, 18 kg/kgmol water
KJoules = Cp1 * 20 / 18
print('Killajoules out = ',KJoules, 'KJ') 
print('')

#-----------question 2----------
print('Question 2 answers:')

Cp2 = Cp_func(32.24, .001924, 1.055e-5, -3.596e-9, 298)
print('the Cp of water is', Cp2, 'J/(gmol K)')

Delta_H_CO = Joule_func(30.87, -.01285, 2.789e-5, -1.272e-8, 473) - Joule_func(30.87, -.01285, 2.789e-5, -1.272e-8, 323)
print('Delta H of CO is',Delta_H_CO, 'J/gmol')

Delta_H_CO2 = Joule_func(19.8, .07344, -5.602e-5, 1.7115e-8, 473) - Joule_func(19.8, .07344, -5.602e-5, 1.7115e-8, 323)
print('Delta H of CO2 is', Delta_H_CO2, 'J/gmol') 

# 40 gmols of CO, 60 gmoles of CO2
KJoule_Work_Done = ((Delta_H_CO * 40) + (Delta_H_CO2 * 60)) / 1000
print('Killajoules heat into system = ',KJoule_Work_Done, 'KJ') 
print('')

#-----------question 3----------
print('Question 3 answers:')

Ref_energy = Joule_func(32.24, .001924, 1.055e-5, -3.596e-9, 179.88 + 273)
print('The reference energy is', Ref_energy, 'KJ')

needed_energy = Ref_energy - 1913 # 1913 is the energy in the H hat in the system total
print('The needed energy is', needed_energy, 'KJ')

Guess = 130
Soln = fsolve(inv_Joule_func, Guess)[0]
Operating_Temp_K = Soln

print('The Operating Temperature of the system is', Operating_Temp_K, 'K')

Psat_water_mmhg = Antoines_Eq(8.14019, 1810.94, 244.485, Operating_Temp_K - 273)
Psat_water_bar = Psat_water_mmhg / 750.06156 # mm Hg in 1 bar
print('The Partial Pressure of the water is',  Psat_water_bar, 'bar')

Prc_water_vapor = (Psat_water_bar / 10)
Prc_water_liq = 1 - Prc_water_vapor
print('The Perecent water vapor at equalibrium is', Prc_water_vapor * 100, '%')
print('The Perecent water liquid at equalibrium is', Prc_water_liq * 100, '%')

Weight_vapor_out = (Psat_water_bar/10) * 200
Weight_liq_out =  (1 - Prc_water_vapor) * 200
print('The weight of vapor out is', Weight_vapor_out, 'kg')
print('The weight of Liquid out is', Weight_liq_out, 'kg')

Energy_Vapor = 2777.1 * Weight_vapor_out
Energy_Liq = .0754 * (121.5 + 273) * Weight_liq_out * 1000 / 18
Sum_energy = Energy_Vapor + Energy_Liq
print('')
print('The energy from vapor is', Energy_Vapor, 'KJ')
print('The energy from liquid is', Energy_Liq, 'KJ')
print('The total energy is', Sum_energy, 'KJ')

#-------Question 4------------
print('')
print('Question 4 answers:')

Cp_Benzene_vap = Cp_func(-33.92, .4739, -3.107e-4, 7.13e-8, 500+273)
Cp_Benzene_liq_in = Cp_func(-6.2106, .5650, -3.141e-4, 0, 25+273)
Cp_Benzene_liq_out = Cp_func(-6.2106, .5650, -3.141e-4, 0, 200+273)
Cp_Benzene_vap_80 = Cp_func(-33.92, .4739, -3.107e-4, 7.13e-8, 80.1+273)

print('The Cp for Benzene Vapor phase is', Cp_Benzene_vap, 'J/(gmol K)')
print('The Cp for Benzene Liquid 25 C phase is', Cp_Benzene_liq_in, 'J/(gmol K)')
print('The Cp for Benzene Liquid 200 C phase is', Cp_Benzene_liq_out, 'J/(gmol K)')
print('The Cp for Benzene Vapor 80.1 C phase is', Cp_Benzene_vap_80, 'J/(gmol K)')

#Killajoules out =  8615.892832559139 KJ
#
#Question 2 answers:
#the Cp of water is 33.655071123168 J/(gmol K)
#Delta H of CO is 4409.321198363999 J/gmol
#Delta H of CO2 is 6175.142736199503 J/gmol
#Killajoules heat into system =  546.8814121065302 KJ
#
#Question 3 answers:
#The reference energy is 15086.988703326577 KJ
#The needed energy is 13173.988703326577 KJ
#The Operating Temperature of the system is 397.736831501 K
#The Partial Pressure of the water is 2.29268927014 bar
#The Perecent water vapor at equalibrium is 22.9268927014 %
#The Perecent water liquid at equalibrium is 77.0731072986 %
#The weight of vapor out is 45.8537854028 kg
#The weight of Liquid out is 154.146214597 kg
#
#The energy from vapor is 127340.547442 KJ
#The energy from liquid is 254729.188725 KJ
#The total energy is 382069.736168 KJ
#
#Question 4 answers:
#The Cp for Benzene Vapor phase is 179.68519078209997 J/(gmol K)
#The Cp for Benzene Liquid 25 C phase is 134.26606359999997 J/(gmol K)
#The Cp for Benzene Liquid 200 C phase is 190.76112109999997 J/(gmol K)
#The Cp for Benzene Vapor 80.1 C phase is 97.81507277474827 J/(gmol K)