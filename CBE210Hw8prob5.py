import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

"""
calculates saturation pressure

A       Antoine's Constant A for species i
B       Antoine's Constant B for species i
C       Antoine's Constant C for species i
temp_c  Temperature in Celcius of system
return  Gives saturation pressure for species i

"""

def P_sat(A, B, C, temp_c):
    P_sat = m.exp(A - (B / (temp_c + C)))
    return P_sat

temp_c    = 30                     # Temp in C of system 
propanol  = np.linspace(0,1,100)   # mol % of 2-Propanol
water     = 1 - propanol           # mol % of Water
Aw = 16.3872                       # Water constants
Bw = 3885.70                       # Water constants
Cw = 230.17                        # Water constants
A2 = 16.6796                       # 2-Propanol constants 
B2 = 3640.20                       # 2-Propanol constants
C2 = 219.61                        # 2-Propanol constants
pdf_filename = '/Users/jderoo/Desktop/Spring_2016/CBE_210_Hw8_Prob5.pdf'

P_sat_h2o    = P_sat(Aw, Bw, Cw, temp_c) # saturation pressure for water
P_sat_2p     = P_sat(A2, B2, C2, temp_c) # "           "  for 2-Propanol
BP_press     = np.zeros(shape=(len(water),1)) # storage for the for loop
vap_mol_2p   = np.zeros(shape=(len(water),1)) # storage for the for loop 
correct1     = np.zeros(shape=(len(water),1)) # storage for the for loop
correct2     = np.zeros(shape=(len(water),1)) # storage for the for loop
BP_press2    = np.zeros(shape=(len(water),1)) # storage for the for loop
vap_mol_2P   = np.zeros(shape=(len(water),1)) # storage for the for loop

for x in range(len(propanol)):
# finds and stores total boiling point pressure
    BP_press[x] = (P_sat_2p * propanol[x]) + (P_sat_h2o * water[x])
# finds and stores mole fraction of 2-Propanol in vapor phase 
    vap_mol_2p[x] = (P_sat_2p / BP_press[x]) * propanol[x]
# finds corrective factor for propanol
    correct2[x] = m.exp(1.42 * (water[x]    ** 2))   
# finds and stores corrective factor for water 
    correct1[x] = m.exp(1.42 * (propanol[x] ** 2))
# finds and stores total boiling point pressure with corrective factor
    BP_press2[x] = (P_sat_2p * propanol[x] * correct2[x]) + (P_sat_h2o * water[x] * correct1[x])
# finds and stores mole fraction of 2-Propanol in vapor phase with corrective factor
    vap_mol_2P[x] = P_sat_2p * propanol[x] * correct2[x] / BP_press2[x]

# plot 1
pp  = PdfPages(pdf_filename)
fig = plt.figure(1)
ax  = fig.add_subplot(111)
plt.figure(1)
plt.plot(propanol, BP_press, 'r', label= 'Bubble Point')
plt.plot(vap_mol_2p, BP_press, 'b', label= 'Dew Point')
legend = ax.legend(loc='lower right')
plt.xlim([0,1])
ax.set_xlabel('Mole Fraction 2-Propanol')
ax.set_ylabel('Pressure KPa')
ax.set_title('P-x-y curve for traditional Raoult')
pp.savefig()

# plot 2
fig = plt.figure(2)
ax  = fig.add_subplot(111)
plt.figure(2)
plt.plot(propanol, BP_press2, 'r', label= 'Bubble Point')
plt.plot(vap_mol_2P, BP_press2, 'b', label= 'Dew Point')
legend = ax.legend(loc='lower right')
ax.set_xlabel('Mole Fraction 2-Propanol')
ax.set_ylabel('Pressure KPa')
ax.set_title('P-x-y curve for modified Raoult')
pp.savefig()
pp.close()
