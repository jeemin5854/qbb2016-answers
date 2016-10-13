#!/bin/bash/env python

import sys 
import codecs

f = open("newphenotype", 'w')

contents = codecs.open(sys.argv[1], encoding='utf-8').read()

newcontents= contents.replace('_','\t')

f.write(newcontents)

f.close()
