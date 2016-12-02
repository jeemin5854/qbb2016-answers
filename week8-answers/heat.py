#!/bin/bash/env python

import sys
import numpy as np
from math import log
import h5py

file = h5py.File('/Users/cmdb/qbb2016-answers/week8-answers/Out.heat', 'r')
ctcffile = open('/Users/cmdb/qbb2016-answers/week8-answers/ctcf_peaks.tsv', 'r')


counts = file['0.counts'][...]
expected = file['0.expected'][...]
position = file['0.positions'][...]
region= file['regions'][...]

start = region[0][4]
end = region[0][5]
chrlist=[]

for line in ctcffile:
	if line.startswith("chrX") and int(line.split("\t")[1]) > start and int(line.split("\t")[1]) < end:
		chrlist.append(line.split("\t")[1])

for line in chrlist:
	enrich = 0
	for b, a in enumerate(position):
		if int(line) > a[0] and int(line) < a[1]:
	 		for i in range(0,len(position)):
	 			if np.log( ( counts[b][i] + 1 ) / ( expected[b][i] + 1 ) ) > enrich:
	 				enrich = np.log( ( counts[b][i] + 1 ) / ( expected[b][i] + 1 ) )
	 				col = position[i]
			print enrich, col, b









# results = np.zeros((459, 459))

# for i in range(counts.shape[0]):
#     for j in range(counts.shape[1]):
#         if np.where([i, j]):
#             results[i, j]=log((counts[i, j])/ (expected([i, j]))


# ctcfsites== line.strip().split("\t")[1]
# ctcfpeak== line.strip().split("\t")[2]
    
