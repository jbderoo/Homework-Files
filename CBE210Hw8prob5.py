import os
import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def plotter(plot_id, title, x_axis, x_label, y_axis, y_label, color, legend, location, x_lower_bound = 0, x_upper_bound = 1):
    """ plot grap

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
    plt.xlim([x_lower_bound,x_upper_bound])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    pp.savefig()
    return True


def P_sat(A, B, C, temp_c):
    """ calculates saturation pressure

    Args:
        param1 (float): A       Antoine's Constant A for species i
        param2 (float): B       Antoine's Constant B for species i
        param3 (float): C       Antoine's Constant C for species i
        param4 (float): temp_c  Temperature in Celcius of system

    Returns:
        float: Gives saturation pressure for species i

    """
    P_sat = m.exp(A - (B / (temp_c + C)))
    return P_sat

temp_c      = 30                     # Temp in C of system 
Aw          = 16.3872                # Water constants
Bw          = 3885.70                # Water constants
Cw          = 230.17                 # Water constants
A2          = 16.6796                # 2-Propanol constants 
B2          = 3640.20                # 2-Propanol constants
C2          = 219.61                 # 2-Propanol constants
correct_w   = 0.0
correct_p   = 0.0
propanol    = np.linspace(0,1,100)   # mol % of 2-Propanol
water       = 1 - propanol           # mol % of Water

pdf_filename = os.path.expanduser('~') + '/Desktop/Spring_2016/CBE_210_Hw8_Prob5.pdf'

BP_press    = np.zeros(shape=(len(water),1)) # storage for the for loop
vap_mol_2p  = np.zeros(shape=(len(water),1)) # storage for the for loop 
BP_press2   = np.zeros(shape=(len(water),1)) # storage for the for loop
vap_mol_2P  = np.zeros(shape=(len(water),1)) # storage for the for loop
P_sat_h2o   = P_sat(Aw, Bw, Cw, temp_c) # saturation pressure for water
P_sat_2p    = P_sat(A2, B2, C2, temp_c) # saturation pressure for 2-Propanol

"""
Typically written as one single line formula, broken into smaller/logical
bits to improve readablity and debugging mis-typed segments. :)
"""
for x in range(len(propanol)):
    BP_press[x]     = (P_sat_2p  * propanol[x]) + (P_sat_h2o * water[x]) # total boiling point pressure (BP)
    vap_mol_2p[x]   = (P_sat_2p  / BP_press[x]) * propanol[x] # mole fraction of 2-Propanol in vapor phase 
    correct_p       = m.exp(1.42 * (water[x]    ** 2)) # corrective factor (CF) for propanol
    correct_w       = m.exp(1.42 * (propanol[x] ** 2)) # corrective factor (CF) for water 
    BP_press2[x]    = (P_sat_2p  * propanol[x] * correct_p) + (P_sat_h2o * water[x] * correct_w) # BP with CF
    vap_mol_2P[x]   = P_sat_2p   * propanol[x]  * correct_p / BP_press2[x] # mole fraction of 2-Propanol in vapor phase with CF


pp  = PdfPages(pdf_filename)

plotter(1, 
        'P-x-y curve for traditional Raoult',
        [propanol, vap_mol_2p],
        'Mole Fraction 2-Propanol',
        [BP_press, BP_press],
        'Pressure KPa',
        ['r', 'b'],
        ['Bubble Point', 'Dew Point'],
        'lower right',
       )

plotter(2, 'P-x-y curve for modified Raoult', [propanol, vap_mol_2P], 'Mole Fraction 2-Propanol', [BP_press2, BP_press2], 'Pressure KPa', ['r', 'b'], ['Bubble Point', 'Dew Point'], 'lower right',)

pp.close()

