# -*- coding: utf-8 -*-

'''
读取log文件中的数据，并画图表
'''

import matplotlib.pyplot as plt
from path_dir import *

server_path = "".join([log_dir, "serverlog.txt"])
input = open(server_path, 'r')

rangeUpdateTime = [0.0]

for line in input:
    line = line.split()
    if 'update' in line:
        rangeUpdateTime.append(float(line[-1]))

plt.figure('frame time')
plt.subplot(211)
plt.plot(rangeUpdateTime, '.r',)
plt.grid(True)
plt.subplot(212)
plt.plot(rangeUpdateTime)
plt.grid(True)
plt.show()