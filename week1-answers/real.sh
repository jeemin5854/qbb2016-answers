#!/bin/bash/env python

import itertools
nucfile = open ("alignment.fa", 'r')
aafile = open ("aaalign", 'r')
nuc_gene= nucfile.read().split(">")
aa_gene=aafile.read().split(">")
result = ""

out = open("backtonuc", 'w')

for i in range(1, len(nuc_gene)):
	nucsequence = nuc_gene[i].split("\n")[1]
	aasequence = aa_gene[i].split("\n")[1]
	for seq1, seq2 in itertools.izip(nucsequence * 3, aasequence):
		if seq2 == "-":
			result += "---"
		else:
			result += seq1
			
print result			

nucfile.close()
aafile.close()
out.close()