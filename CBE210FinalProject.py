import os
import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf_filename = os.path.expanduser('~') + '/Desktop/Spring_2016/CBE_210_FP.pdf'

#----creates a function for easy plotting, ignore 9-43 ------
def plotter(plot_id, title, x_axis, x_label, y_axis, y_label, color, legend, location, x_lower_bound = 0, x_upper_bound = 1):
    """ plot graph
    Args:
        param1 int: plot_id           Unique numeric idenifer for plot
        param2 string: title          Title for graph
        param3 array: x_axis          Data points for x axis
        param4 string: x_label        Label for x axis
        param5 array: y_axis          Data points for y axis
        param6 string: y_label        Label for y axis
        param7 array: color           Graph line color
        param8 string: legend         Title of legend
    Returns:
        bool: always true, because we don't bother to test. :)
    """

    # Verify that all arrays have the same number of elements
    plot_lines = len(x_axis)
    if (len(y_axis) != plot_lines):
        print("y-axis count not equal to x-axis")
        exit
    if (len(color) != plot_lines):
        print("color count not equal to x-axis")
        exit
    #
    fig = plt.figure(plot_id)
    ax  = fig.add_subplot(111)
    plt.figure(plot_id)
    for idx in range(len(x_axis)):
        plt.plot(x_axis[idx], y_axis[idx], color[idx], label = legend[idx])
    legend = ax.legend(loc=location)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    pp.savefig()
    return True
#-------------

# import data found on web
yourFileName  = 'CBE210_FP_data2.txt'
master_array  = np.loadtxt(yourFileName,skiprows=1)

yourFileName  = 'Entropy_input.txt'
entropy_array = np.loadtxt(yourFileName,skiprows=0)
#-------------

# 55 - 61 & 69 + 70 assigns data found on web, 62-68 creates 0s arrays for For loop  
temp      = master_array[0:21,  0]
ethanol_x = master_array[0:21,  1]
ethanol_g = master_array[0:21,  2]
water_x   = master_array[0:21,  4]
water_g   = master_array[0:21,  5]
ethanol_y = master_array[0:21,  8]
water_y   = master_array[0:21,  9]
GeRT      = np.zeros(shape=(len(temp))) 
HeRT      = np.zeros(shape=(len(temp))) 
Ge        = np.zeros(shape=(len(temp))) 
He        = np.zeros(shape=(len(temp))) 
He2       = np.zeros(shape=(len(temp))) 
s_real_13 = np.zeros(shape=(len(temp))) 
s_real_7  = np.zeros(shape=(len(temp))) 
H_real_7  = np.zeros(shape=(len(temp))) 
H_real_13 = np.zeros(shape=(len(temp))) 
A12       = 1.6022
A21       = 0.7947
R         = 8.314 # J / mol K
#-----------

# updated x1 values
x1     = np.zeros(shape=(len(temp) - 1)) 
for i in range(len(temp) - 1):
	x1[i]  = (ethanol_x[i] + ethanol_x[i + 1]) / 2
#------

# Begin Calculations
for i in range(len(temp)):
    GeRT[i]  = ((A21 * ethanol_x[i]) + (A12 * water_x[i])) * (ethanol_x[i] * water_x[i])  #eq 12.9b
    Ge[i]    = GeRT[i] * R * temp[i]							  # times T and R
    HeRT     = -temp[i] * np.diff(GeRT) / np.diff(temp)					  # eq 11.58	
delta_G = np.diff(Ge)

for i in range(len(temp)):
	Se = -np.diff(Ge) / np.diff(temp)        # calc S^E, table 11.1 page 415 
	term1 = (np.diff(GeRT) / np.diff(temp))  # used later in lne 88, table 11.1 page 415
Se.resize(21,1)    # resizes Se, puts a 0 in the 20th cell (removed during graphing) 
term1.resize(21,1) # resizes Se, puts a 0 in the 20th cell (removed during graphing) 

for i in range(len(temp)):
	He[i]  = Ge[i] + (temp[i] * Se[i])       # calcs He table 11.1
	He2[i] = (-R * (temp[i]**2)) * term1[i]  # calcs He table 11.1 a different way
He.resize(21,1)  # resizes He, puts a 0 in the 20th cell (removed during graphing) 
He2.resize(21,1) # resizes He, puts a 0 in the 20th cell (removed during graphing) 

#Entropy balances over our distillation column assuming Se is correct (they aren't)
s_ideal_13 = (.35 * 1.217) + (.65 * .507) - R *(.35 * m.log(.35) + .65 * m.log(.65))
s_ideal_7  = (.6  * 1.217) + (.4  * .507) - R *(.6  * m.log(.6)  + .4  * m.log(.4))
s_real = entropy_array[0,:] 

for i in range(len(temp)):
	s_real_13[i] = s_ideal_13 + Se[i]
	s_real_7[i]  = s_ideal_7 + Se[i]

# entropy balance of the distillation column
delta_s = (2.7 * s_real) + (2.35 * s_real_13) - (5 * s_real_7)
print('The entropy of our distillation column is %5.3f J/ K ' % delta_s[14]) # index 14 corresponds to temp input of distillation.
print('The temperature of the distillation is %5.3f C.' % temp[14])

#Enthalpy balances over our distillation column assuming He is correct (they aren't)

enthalpy_eth = 4670.86 # J / mol
enthalpy_h2o = -1331   # J / mol 

H_ideal_13 = (.35 * enthalpy_eth) + (.65 * enthalpy_h2o)
H_ideal_7  = (.6 * enthalpy_eth)  + (.4 * enthalpy_h2o)
H_real     = entropy_array[1,:]

for i in range(len(temp)):
	H_real_13[i] = H_ideal_13 + He[i]
	H_real_7[i]  = H_ideal_7  + He[i]

delta_H = (2.7 * H_real) + (2.35 * H_real_13) - (5 * H_real_7)
print('The enthalpy of our distillation column is %5.3f J / K ' % delta_H[14])

#---- Below is all plotting-----

pp  = PdfPages(pdf_filename)
plotter(1,
        'Txy for water and ethanol at 1 bar',
        [ethanol_x, ethanol_y],
        'Mol % ethanol',
        [temp, temp],
        'temperature C',
        ['b', 'r'],
        ['dew line', 'bubble line'],
        'upper right',
        )
plotter(2,
        'Ge and Se', 
        [ethanol_x, x1], # ending 1 before
        'Mol % ethanol', 
        [Ge, Se[0:20]],		    # ending 1 before
        'J / mol',
        ['b', 'r'],
        ['Ge', 'Se'],
        'upper right',
        )
plotter(3,
        'Ge He TSe for distillation column',
        [x1, x1, x1, x1], # ending 1 before
        'Mol % ethanol', 
        [Ge[0:20], Se[0:20], He[0:20], He2[0:20]],			      # ending 1 before
        'J / mol',
        ['b', 'r', 'g', 'k--'], 
        ['Ge', 'Se', 'He', 'He2'],
        'lower left',
        )
pp.close()
