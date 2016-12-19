#!/usr/bin/env python

import sys


file = open(sys.argv[1])

for line in file:
    line = line.rstrip('\r\n').split('\t')
    if int(line[2]) == 10293 and int(line[1]) == 1:
        print ">" + line[0]
        print line[3].replace("-", "")


