#!/bin/bash/env python

import sys

file = open(sys.argv[1], 'r')
string_list = file.read().split(">")
length= []
f = open("listoflengths", 'w')

for i in range(1, len(string_list)):
	length.append(float(string_list[i].split("_")[3]))

halfG = str(sum(length)/float(2))
halfG= float(halfG)

for item in length:
    item=int(item)

sortedlist = sorted(length)
#f.writelines(["%s\n" % item  for item in sortedlist])

counter =0
for item in sortedlist:
	if counter <  halfG:
		counter +=item
	else:
		print "N50 is "
		print item
		break

f.close()
file.close()
