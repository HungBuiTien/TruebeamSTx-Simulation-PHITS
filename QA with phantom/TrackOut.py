# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

track_file = open("track-xy.out",'r')
lines = track_file.readlines()

data = []
for i in range(147, 4188):
    tmp = lines[i].split()
    for j in range(len(tmp)):
        data.append(float(tmp[j]))

data = np.array(data)
data = data.reshape(201, 201)
ox = data[100,:]



# read FFF experiment data
exFile = open("6FFF_Depth10_Size10.txt", 'r')
exdat = exFile.readlines()
exData = []

for line in exdat:
    tmp = line.split()
    exData.append(float(tmp[0]))

exData = np.array(exData)


# plotting
# pos  = np.linspace(-10,10,201)
# plt.plot(pos, 100*ox/ox[100], label='FFF-Simulation')
# plt.scatter(pos,exData, marker='s', color='red', label='FFF-Experiment')
# plt.xlabel('xlabel')
# plt.ylabel('ylabel')
# plt.legend()
# plt.grid()
plt.imshow(data,'jet',extent=(-10.05,10.05,-10.05,10.05))
# plt.plot(ox)