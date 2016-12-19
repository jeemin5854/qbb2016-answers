#!/bin/bash/env python

import itertools
nucfile = open ("alignment.fa", 'r')
aafile = open ("aaalign", 'r')
nuc_gene= nucfile.read().split(">")
aa_gene=aafile.read().split(">")
result = ""

out = open("backtonuc", 'w')

for i in range(1, len(nuc_gene)):
	gene_name= nuc_gene[i].split("\n")[0]
	result += ">" + gene_name + '\n'
	sequences = nuc_gene[i].split("\n")
	for j in range (1,len(sequences)):
		result += sequences[j]
	result = str(result)
	out.write(result)
	


"""
for i, j in itertools.izip(nuc_gene, aa_gene):
	gene_name= nuc_gene[i].split("\n")[0]
    #result += ">" + gene_name + '\n'
	nucsequence = nuc_gene[i].split("\n")
	aasequence = aa_gene[j].split("\n")
	for x, y in itertools.izip(nucsequence*3, aasequence):
		if y == "-":
			print "---"
		else:
			print x"""
"""
result = str(result)
out.write(result)
"""

"""
for i in itertools.izip(nuc_gene, aa_gene):
	nucsequence = nuc_gene[i].split("\n")[1]
	aasequence = aa_gene[i].split("\n")[1]
	for seq1, seq2 in itertools.izip(nucsequence * 3, aasequence):
		if sequence == "-":
			result += "---"
		else:
			result += seq1
			out.write(result)
			break
"""
nucfile.close()
aafile.close()
out.close()