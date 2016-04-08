# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:12:59 2016

@author: jderoo
"""

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
    lower_limit = A1 + B1 + C1 + D1
    upper_limit = A2 + B2 + C2 + D2
    net_joules  = upper_limit - lower_limit
    return net_joules * 8.3145 
test = joule(3.28, .593, 0, .04, 800-273, 300-273)
print('Does', test, '= -15060? Your answer is in J/mol')
print(joule(3.47, 1.45, 0, .121, 250, 650))