import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

temp_k    = 30 + 273.15 # K
temp_c    = 30          # C
propanol  = np.linspace(0,1,100) # mol %
water     = 1 - propanol           # mol %
def P_sat(A, B, C, temp_c):
    P_sat = m.exp(A - (B / (temp_c + C)))
    return P_sat
Aw = 16.3872
Bw = 3885.70
Cw = 230.17 # Water constants
A2 = 16.6796
B2 = 3640.20
C2 = 219.61 # 2-Propanol " "

P_sat_h2o    = P_sat(Aw, Bw, Cw, temp_c)
P_sat_2p     = P_sat(A2, B2, C2, temp_c)
BP_press     = np.zeros(shape=(len(water),1))
vap_mol_2p   = np.zeros(shape=(len(water),1))
correct1     = np.zeros(shape=(len(water),1))
correct2     = np.zeros(shape=(len(water),1))
BP_press2    = np.zeros(shape=(len(water),1))
vap_mol_2P   = np.zeros(shape=(len(water),1))

for x in range(len(propanol)):
    BP_press[x] = (P_sat_2p * propanol[x]) + (P_sat_h2o * water[x])
    vap_mol_2p[x] = (P_sat_2p / BP_press[x]) * propanol[x]
    correct2[x] = m.exp(1.42 * (water[x]    ** 2))   
    correct1[x] = m.exp(1.42 * (propanol[x] ** 2))
    BP_press2[x] = (P_sat_2p * propanol[x] * correct2[x]) + (P_sat_h2o * water[x] * correct1[x])
    vap_mol_2P[x] = P_sat_2p * propanol[x] * correct2[x] / BP_press2[x]


pp  = PdfPages('Desktop/CBE_210_Hw8_Prob5.pdf')
fig = plt.figure(1)
ax  = fig.add_subplot(111)
plt.figure(1)
plt.plot(propanol, BP_press, 'r', label= 'liquid line')
plt.plot(vap_mol_2p, BP_press, 'b', label= 'vapor line')
plt.xlim([0,1])
ax.set_xlabel('Mole Fraction')
ax.set_ylabel('Pressure KPa')
ax.set_title('P-x-y curve for traditional Raoult')
pp.savefig()

fig = plt.figure(2)
ax  = fig.add_subplot(111)
plt.figure(2)
plt.plot(propanol, BP_press2, 'r', label= 'liquid line')
plt.plot(vap_mol_2P, BP_press2, 'b', label= 'vapor line')
ax.set_xlabel('Mole Fraction')
ax.set_ylabel('Pressure KPa')
ax.set_title('P-x-y curve for modified Raoult')
pp.savefig()
pp.close()
