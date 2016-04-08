# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:33:14 2016

@author: jderoo
"""

# Problem 4, CBE 210 Hw #7

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

tempc_h2o      = 647.1 # k
pressc_bar_h2o = 220.55 # bar
pressc_h2o     = pressc_bar_h2o * 100 # kPa
pressr_h2o     = 3300 / pressc_h2o
compress       = .345
temp_h2o       = np.linspace(523, 923, 1000)
Hr_RTc         = np.zeros(shape = (len(temp_h2o),1))

for i in range(len(temp_h2o)):    
    tempr_h2o = temp_h2o[i] / tempc_h2o    
    B_o  = .083 - (.422 / (tempr_h2o ** 1.6))
    B_1  = .139 - (.172 / (tempr_h2o ** 4.2)) 
    dB_o = .675 / (tempr_h2o ** 2.6)
    dB_1 = .722 / (tempr_h2o ** 5.2)
    term1 = B_o - (tempr_h2o * dB_o)
    term2 = B_1 - (tempr_h2o * dB_1)    
    Hr_RTc[i] = pressr_h2o * (term1 + (compress * term2))
    #print(tempr_h2o, Hr_RTc)

def joule(A, B, C, D, input_stream, output_stream):
    tempk1 = input_stream  + 273
    tempk2 = output_stream + 273
    A1 = A * tempk1
    B1 = (((B / 2) * 1e-3) * (tempk1 ** 2))
    C1 = (((C / 3) * 1e-6) * (tempk1 ** 3))
    D1 = (((-D) * 1e5) * (tempk1 ** -1))
    A2 = A * tempk2
    B2 = (((B / 2) * 1e-3) * (tempk2 ** 2))
    C2 = (((C / 3) * 1e-6) * (tempk2 ** 3))
    D2 = (((-D) * 1e5) * (tempk2 ** -1))
    upper_limit = A1 + B1 + C1 + D1
    lower_limit = A2 + B2 + C2 + D2
    net_joules = - upper_limit + lower_limit
    return net_joules * 8.3145     

delta_Hr = ( max(Hr_RTc) - min(Hr_RTc) ) * 8.3145 * tempc_h2o
delta_Hr_real = (3792.9 - 2839) * 18.02
dH_ideal = joule(3.47, 1.45, 0, .121, 250, 650)
Hr_real = delta_Hr_real - dH_ideal
error = 100 * ((Hr_real - delta_Hr) / Hr_real)
print('The error is %2.3f%%.' % (error))

x = np.linspace(0,10,100)
y = x ** 2

pp = PdfPages('Desktop/multipage.pdf') #**
fig = plt.figure(1)
ax  = fig.add_subplot(111)
plt.figure(1)
plt.plot(temp_h2o, Hr_RTc, 'r', label= 'Hr_RTc values')
ax.set_xlabel('Temperatures')
ax.set_ylabel('Hr_RTc')
ax.set_title('Hr_RTc for steam at 3300 kPa')
plt.legend(loc='upper left')
pp.savefig()                           #**


fig = plt.figure(2)
ax  = fig.add_subplot(111)
plt.figure(2)
plt.plot(x, y, 'b', label= 'x squared')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Hr_RTc for steam at 3300 kPa')
plt.legend(loc='upper left')
pp.savefig()                          #**
pp.close()                            #**
