import os
import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pdf_filename = os.path.expanduser('~') + '/Desktop/Spring_2016/CBE_210_last_prob3.pdf'

# Data input
H2SO4x = np.array([.1, .2, .3, .4, .5, .6, .7, .8, .85, .9, .95])
# moele % for water
H2Ox = H2SO4x - 1
# data input for enthalpies
mixed_H = -1*np.array([-73.27, -144.21, -208.64, -262.83, -302.84, -323.31, -320.98, -279.58, -237.58, -178.87, -100.71])


He_mix = mixed_H / (H2SO4x * H2Ox)         # Enthalpy / mixture
fit = np.polyfit(H2SO4x, He_mix, 3)        # line of best fit
vector_approx = np.polyval(fit, H2SO4x)	   # approximation vector
H_bar_1e = np.zeros(shape=(len(H2SO4x),1)) # storage for loop
H_bar_2e = np.zeros(shape=(len(H2SO4x),1)) # storage for loop 

for i in range(len(H2SO4x)):
# excess enthalpy H2SO4
	H_bar_1e[i] = (H2Ox[i] ** 2)  * (He_mix[i] + (H2SO4x[i] * vector_approx[i]))
# excess enthalpy H2O 
	H_bar_2e[i] = (H2SO4x[i] ** 2) * (He_mix[i] - (H2Ox[i]  * vector_approx[i]))

#---Below me is plotting---
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
         'Question 3',
         [H2SO4x, H2SO4x, H2SO4x],
         'Mol % H2SO4',
         [He_mix,H_bar_1e, H_bar_2e],
         'Kj / Kg',
         ['b', 'r', 'k'],
         ['mixture excess enthalpies', 'H bar excess H2SO4', 'H bar excess H2O'],
         'lower left',
         )
pp.close()

