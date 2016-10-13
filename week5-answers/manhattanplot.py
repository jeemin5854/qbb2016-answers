#!/bin/bash/env python

import sys 
import math
import matplotlib.pyplot as plt
import os 

xlist = []
ylist = []
file = open(sys.argv[1], 'r')

for f in file:
	if f.startswith(" CHR"):
		continue
	else:
		x = f.strip().split(" ")[1]
		xlist.append(x)
		y = f.split(" ")[9]
		y = -1 * math.log(float(y))
		ylist.append(y)

plt.scatter(xlist, ylist)
plt.ylim(0)
plt.savefig('46.png')
plt.close()