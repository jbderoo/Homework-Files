
from math import log

def entropy(A, B, C, D, inputT, outputT, inputP, outputP): 
    tempk1 = inputT + 273
    tempk2 = outputT + 273
    A1 = (A * log(tempk1)) 
    B1 = ((((B / 1) * 1e-3) * (tempk1 ** 1)))
    C1 = ((((C / 2) * 1e-6) * (tempk1 ** 2)))
    D1 = ((((-D / 2) * 1e5) * (tempk1 ** -2)))
    A2 = (A * log(tempk2)) 
    B2 = ((((B / 1) * 1e-3) * (tempk2 ** 1)))
    C2 = ((((C / 2) * 1e-6) * (tempk2 ** 2)))
    D2 = ((((-D / 2) * 1e5) * (tempk2 ** -2)))
    upper_limit = A1 + B1 + C1 + D1
    lower_limit = A2 + B2 + C2 + D1
    net_joule   = -upper_limit + lower_limit
    net_joules  = net_joule * 8.3145
    pressure = log(outputP / inputP) * 8.3145
    delta_s = net_joules - pressure
    return delta_s 

# print(entropy(3.280, .593, 0, .040, 800-273, 300-273, 50, 1.0133))
print(entropy(1.702, 9.081, -2.164, 0, 600-273, 400-273, 10, 2), 'J/mol K')
# -5.657 J/mol K
