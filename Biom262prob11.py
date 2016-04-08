# Problem 11, Biomechanics Hw 3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.integrate import simps
from numpy import trapz
from shapely.geometry import LineString

length = 12 # mm
area   = 4 # mm
strain = np.array( [0, .012, .0276, .0492, .06, .0804, .0948, .1068, .1212, .1356, .1584, .1872, .204, .24]) # mm
force  = np.array([0, 80, 184, 328, 400, 496, 576, 628, 688, 736, 764, 788, 796, 804])
stress = force/area # Mega Pascal

simps_area = simps(stress, dx = len(strain))
print('simpsons area =', simps_area)
# simps_area = 24052
volume = length * area # mm
energy = simps_area / volume # megajoule / mm
print('The strain energy density is', energy, 'MPa / mm^3')
# energy = 501.083 Mpa / mm^3

youngs_mod = (stress[9] - stress[0]) / (strain[9] - strain[0])
mod_test = youngs_mod * strain
mod_test1 = mod_test - 20
print("The Elastic Modulus is", youngs_mod, "MPa")
# youngs_mod = 1356.93 Mpa

print('The ultimate strain is', max(strain)) # .024
print('The ultimate stress is', max(stress), 'MPa') # 201

pp  = PdfPages('Desktop/Stress_Strain_Curve.pdf')
fig = plt.figure(1)
ax  = fig.add_subplot(111)
plt.figure(1)
plt.plot(strain, stress, 'r', label= 'Behavior Line')
plt.plot(strain, mod_test - 20 , 'b', label= 'test')
plt.plot(.155, 190, 'ks')
plt.ylim([0,250])
ax.set_xlabel('Strain')
ax.set_ylabel('Stress (Mega Pascal)')
ax.set_title('Problem 11 Stress Strain Curve')
ax.annotate('Yield Point .15, 190', xy=(.15, 190), xytext=(.10, 200))
pp.savefig()
pp.close()
