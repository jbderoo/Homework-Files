import os
import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf_filename = os.path.expanduser('~') + '/Desktop/Spring_2016/CBE_210_last_prob.pdf'

# Finds saturation pressures for a given species at temperatures
def Psat(A, B, C, temp):
	Psat = A - ( B / (C + temp))
	return Psat

# Data input
press_data = np.array([12.71000, 19.00,  20.83, 21.87, 23.1, 23.92, 24.34, 24.43, 24.43, 24.25, 23.85, 23.1, 21.81, 19.83, 16.92])
# Data input
methanolx  = np.array([.001,  .0248, .0457, .0663, .1247, .2292, .3887, .4974, .5910, .6868, .7676, .8343, .8981, .9512, .9999])
# Data input
methanoly  = np.array([.001, .3275, .3970, .4311, .4747, .5042, .5272, .5414, .5563, .578,  .6066, .6451, .7088, .8084, .9999])
# benzene liquid mol %
benzenex   = 1.000 - np.array(methanolx)
# benzene vapor  mol %
benzeney   = 1.000 - np.array(methanoly)
# Psat methanol 
Psat_meth  = Psat(16.5785, 3638.27, 239.5, 298-273.00)
# Psat benzene
Psat_ben   = Psat(13.7819, 2726.81, 217.572, 298-273.00)
# ---- All storage ----
meth_corr  = np.zeros(shape=(len(press_data),1))
ben_corr   = np.zeros(shape=(len(press_data),1)) 
total_Ge   = np.zeros(shape=(len(press_data),1)) 
Gibbs_mol  = np.zeros(shape=(len(press_data),1)) 
term1      = np.zeros(shape=(len(press_data),1))
term2      = np.zeros(shape=(len(press_data),1))

for i in range(len(press_data)):
# Making the math easy, splitting terms up
	term1[i]     = methanoly[i] * press_data[i] / (methanolx[i] * 16.92)
# Correction factor for methanol
	meth_corr[i] = m.log(term1[i]) 
# Making the math easy, splitting terms up
	term2[i]     = benzeney[i]  * press_data[i] / (benzenex[i]  * 12.71)
# Correction factor for benzene 
	ben_corr[i]  = m.log(term2[i])
# Total excess Gibbs
	total_Ge[i]  = (methanolx[i] * meth_corr[i]) + (benzenex[i] * ben_corr[i])
# Gibbs / mol
	Gibbs_mol[i] = total_Ge[i] * (1.000 / (methanolx[i] * benzenex[i])) 

# Approximation for line fit
fit	 = np.polyfit(np.transpose(methanolx[3:12]), Gibbs_mol[3:12], 5)
plotfit  = np.polyval(fit, methanolx)

# Assign values A12 and A21 
A12 = plotfit[0]
A21 = plotfit[len(plotfit) - 1]
print("The first value of Margule's is", A12)  # 2.73
print("The second value of Margule's is", A21) # 1.61

#---- Below is all plotting-----
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

pp  = PdfPages(pdf_filename)
plotter(1,
        'Pxy for methanol and benzene at 298 K',
        [methanolx, methanoly],
        'Mol % methanol',
        [press_data, press_data],
        'Pressure KPa',
        ['b', 'r'],
        ['vapor line', 'liquid line'],
        'lower right',
        )

plotter(2,
        'ln(gamma) for methanol and benzene vs methanol mol % at 298 K',
        [methanolx, methanolx],
        'Mol % methanol',
        [meth_corr, ben_corr], 
        'gamma',
        ['b', 'r'],
        ['methanol correction', 'benzene correction'],
        'upper right',
        )

plotter(3,
	'Ge/RT vs Methanol mol %',
        [methanolx],
        'Mol % methanol',
        [total_Ge], 
        'Ge/RT',
        ['b'],
        ['Ge/RT total'],
        'upper right',
        )

plotter(4,
        'Graph 4',
        [methanolx, methanolx, methanolx, methanolx], #, methanolx],
        'Mol % methanol',
        [meth_corr, ben_corr, total_Ge, Gibbs_mol], #, Gibbs_mol],
        'Pressure',
        ['b', 'r', 'k', 'g'],
        ['methanol correction', 'benzene correction', 'total Gibbs Energy', 'Gibbs Energy per mole'],
        'upper right',
        )

pp.close()


