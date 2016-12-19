#!/bin/bash/env python

import sys


for i, line in enumerate( sys.argv[1].readlines() ):
    line = line.rstrip( "\r\n" )
    if line.startswith( ">" ): # Same as if line[0] == ">"
        continue
    # Must be a sequence line
    print i, line[10:30]

