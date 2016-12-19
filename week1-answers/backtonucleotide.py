#!/usr/bin/env python

import sys, fasta, itertools
import matplotlib.pyplot as plt
from scipy import stats


nucfile = fasta.FASTAReader(open(sys.argv[1]))
profile = fasta.FASTAReader(open(sys.argv[2]))


codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}



nuclist = []
prolist = []

for seq in nucfile:
    nuclist.append(seq[1])
    
for seq in profile:
    prolist.append(seq[1])
  
alignednuc = []
    
for pro, dna in itertools.izip(prolist, nuclist):
    tempseq = []
    temppos = 0
    for letter in pro:
        if letter == "-":
            tempseq.append("---")
        else:
            tempseq.append(dna[temppos: temppos+3])
            temppos += 3
    alignednuc.append("".join(tempseq))

dslist= []
dnlist = []

for i, seq in enumerate(alignednuc):
    if i == 0:
        refseq = seq
        for num in range(0, len(seq) / 3):
            dnlist.append(0)
            dslist.append(0)
        continue
    nucpos = 0
    for codon in range(0, len(seq) / 3 ):
        if seq[nucpos:nucpos + 3] != refseq[nucpos:nucpos + 3]:
            try:
                if codontable[seq[nucpos:nucpos + 3]] == codontable[refseq[nucpos:nucpos + 3]]:
                    dslist[codon] += 1
                    nucpos += 3
                    continue
                elif seq[nucpos:nucpos + 3] == "---":
                    nucpos += 3
                    continue
                else:
                    dnlist[codon] += 1
                    nucpos += 3
            except KeyError:
                nucpos += 3
                continue
        nucpos += 3

calclist=[]
for i in range(0,len(dslist)):
    calclist.append(dnlist[i] - dslist[i])

zmin =stats.zscore(calclist)

plt.figure()
for i, z in enumerate(zmin):
    if z > 3:
        plt.scatter(i,z, color ='orange')
    else:
        plt.scatter(i, z, color='blue')
plt.ylabel("zscore")
plt.xlabel("codon num")

    
    
plt.savefig("scatter.png")
plt.close()




