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
    #plt.xlim([0,x_upper_bound])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    pp.savefig()
    return True

pp  = PdfPages(pdf_filename)
pp.close()
