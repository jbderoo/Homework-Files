import os
import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf_filename = os.path.expanduser('~') + '/Desktop/Spring_2016/CBE_210_Hw9_prob4.pdf'
# CBE 210 Hw set 9, problem 4 (11.24b in book)

#----Critical Data-----
temp_crit  = 408.1 # Kelvin
press_crit = 36.48 # bar
omega      = .181  # unitless corrective factor
Z          = .282  # compressibility factor
vol_crit   = 262.7 # mL / mol

#----Given Data----
temp_c    = 40                   # degree Celcius 
temp_k    = temp_c + 273.15      # Kelvin
press     = np.linspace(0,10,20) # Bar
vap_press = 5.28                 # Bar
phi       = np.zeros(shape=(len(press),1)) # storage for the for loop 
R         = 83.14                # gas constant in mL bar / mol Kelvin
fugacity  = np.zeros(shape=(len(press),1)) # storage for the for loop 

#---start calcs----
temp_r = temp_k / temp_crit # finds reduced temperature 
press_r_sat = vap_press/press_crit # reduced saturation pressure 
vol_sat = vol_crit * (Z ** ((1 - temp_r) ** 2/7)) # finds liquid mL/mol 

for i in range(len(press)):
#---Graph 1---
    press_r = press[i] / press_crit # finds new reduced pressure
    term1   = press_r / temp_r # making math easy
    term2   = .083 - (.422 / (temp_r ** 1.6)) # making math easy
    term3   = .139 - (.172 / (temp_r ** 4.2))  # making math easy
    term4   = term3 * omega # making math easy
    term5   = term2 + term4 # making math easy
    phi[i]  = m.exp(term1 * term5) # calculates fugacity coefficent 
#---Graph 2---
    phi_sat     = m.exp(press_r_sat * term5) # finds phi for saturation pressure
    poynting    = (vol_sat * (press[i] - vap_press)) / (R * temp_k) # Poynting correction	 
    fugacity[i] = phi_sat * vap_press * m.exp(poynting) # stores fugacity calcs

#----Below me is just plotting-------

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
    #plt.xlim([0,x_upper_bound])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    pp.savefig()
    return True

pp  = PdfPages(pdf_filename)
plotter(1,
	'Fugacity coefficent vs Pressure',
	[press],
	'Pressure (bar)',
	[phi],
	'Fugacity coefficent (Phi)',
	['r'],
	[''],
	'upper right',
	)

plotter(2,
	'Fugacity vs Pressure',
        [press],
	'Pressure (bar)',
	[fugacity],
	'Fugacity (f)',
	['b'],
	[''],
	'lower right',
	)
pp.close()
