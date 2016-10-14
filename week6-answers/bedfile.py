#!/bin/bash/env python

import sys 

file = open(sys.argv[1], 'r')
xlist = []

for f in file:
	print f.strip().split("\t")[0] + "\t" + f.strip().split("\t")[1] + "\t" + f.strip().split("\t")[2] +"\t" + f.strip().split("\t")[3] + "\t" + f.strip().split("\t")[4] + "\t" + f.strip().split("\t")[5]

	



