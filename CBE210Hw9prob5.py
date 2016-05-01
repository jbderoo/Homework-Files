import os
import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf_filename 		= os.path.expanduser('~') + '/Desktop/Spring_2016/CBE_210_Hw9_prob5.pdf'

#---Critical Data---
tempc_eth   		= 282.3 # K
pressc_eth  		= 50.4  # bar
Z_eth       		= .281  # compressibilty  
volc_eth    		= 131   # critical volume
omega_eth   		= .087  # omega for eth
tempc_prop  		= 365.6 # K
pressc_prop 		= 46.65 # bar
Z_prop      		= .289  # compressibility
volc_prop   		= 188.4 # critical volume
omega_prop  		= .14   # omega prop

#--Given Data--
press     		= 30           # bar
R         		= 83.14        # gas constant
mol_eth   		= .35          # mol % ethylene
mol_prop  		= .65          # mol % propylene
temp      		= 150 + 273.15 # K

#---Calculations---
tempr_eth  		= temp / tempc_eth 
tempr_prop 		= temp / tempc_prop
Bo_eth  		= .083 - (.422 / (tempr_eth ** 1.6))
Bo_prop 		= .083 - (.422 / (tempr_prop ** 1.6))
B1_eth  		= .139 - (.172 / (tempr_eth ** 4.2))
B1_prop 		= .139 - (.172 / (tempr_prop ** 4.2))
omega   		= (omega_eth + omega_prop) / 2
Zc      		= (Z_eth + Z_prop) / 2
volc    		= (((volc_eth ** (1.0/3.0)) + ( volc_prop **  (1.0/3.0))) / 2.0) ** 3
tempc   		= (tempc_eth * tempc_prop) ** .5
pressc_eth   		= (Z_eth * R * tempc_eth) / volc_eth
pressc_50eth 		= (Zc * R * tempc) / volc 
pressc_prop  		= (Z_prop * R * tempc_prop) / volc_prop
tempr_50eth  		= temp / tempc
Bo_50eth     		= .083 - (.422 / (tempr_50eth ** 1.6))
B1_50eth     		= .139 - (.172 / (tempr_50eth ** 4.2))
B_hat_50eth  		= Bo_50eth + (omega * B1_50eth) # -----
B_hat_eth    		= Bo_eth +  (omega_eth  * B1_eth)
B_hat_prop   		= Bo_prop + (omega_prop * B1_prop)
B_eth           	= B_hat_eth * R * tempc_eth / pressc_eth
B_prop                  = B_hat_prop * R * tempc_prop / pressc_prop
B_50eth   	        = B_hat_50eth * R * tempc / pressc_50eth
delta     	        = (2 * B_50eth) - B_eth - B_prop
phi_eth   	        = m.exp((press * (B_eth  + ((mol_prop ** 2) * delta))) / (R * temp))
phi_prop  	        = m.exp((press * (B_prop + ((mol_eth ** 2)  * delta))) / (R * temp))
fugacity_eth		= press * phi_eth  * mol_eth
fugacity_prop		= press * phi_prop * mol_prop
pressr_eth  		= press / pressc_eth
pressr_prop 		= press / pressc_prop
phi_eth_real  		= (1.0496 ** omega_eth) * .9462
phi_prop_real 		= (1.019 ** omega_prop) * .8713  

print(fugacity_eth,	'Fugacity ethylene')            # 10.05
print(fugacity_prop,    'Fugacity propylene')		# 17.06
print(phi_eth,		'Phi ethylene')		        # .957
print(phi_prop,		'Phi propylene')		# .875
print(tempr_eth,	'Reduced temp ethylene')	# 1.5
print(pressr_eth,	'Reduced pres ethylene')	# .6
print(tempr_prop,	'Reduced temp propylene')	# 1.15
print(pressr_prop,	'Reduced pres propylene')	# .64
print(phi_eth_real,	'phi ethylene interpolated')	# .950
print(phi_prop_real,	"phi propylene interpolated")   # .873
