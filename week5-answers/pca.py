#!/bin/bash/env python

import sys
import matplotlib.pyplot as plt


file = open(sys.argv[1], 'r')
#string_list = file.read().split("/r/n")
xaxis= []
yaxis = []

#for i in range(1, len(string_list)):
for line in file:
	xaxis.append(float(line.split(" ")[2]))
	yaxis.append(float(line.split(" ")[3]))

plt.scatter(xaxis, yaxis)
plt.show()
