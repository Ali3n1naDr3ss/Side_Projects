import numpy as np
import matplotlib.pyplot as plt

HI_spectrum = '/Users/user/Desktop/spectrum.csv'

with open(HI_spectrum, 'r') as f:
    headers = f.readline().split(',')
    lines = f.readlines()[2:]
    print(lines)

    frequency = []
    power = []
    unknown = []
    rad_vel = []
    for line in lines:
        cols = line.split(',')
        frequency.append(float(cols[0]))
        power.append(float(cols[1]))
        unknown.append(float(cols[2]))
        rad_vel.append(float(cols[3]))
    
    plt.plot(frequency, power)
    plt.xlabel(headers[0])
    plt.ylabel(headers[1])
    plt.show()