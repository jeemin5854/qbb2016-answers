#!/bin/bash/env python

import sys

file = open("sys.stdin(1)", 'r')
string_list = file.read().split(">")
length= []
f = open("listoflengths", 'w')

for i in range(1, leng(string_list)):
	length.append(string_list[i].split("_")[3])
	

sortedlist = length.sort()
f.write(sortedlist)


f.close()
file.close()
