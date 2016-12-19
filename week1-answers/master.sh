#!/bin/bash

#blastn -db nr -remote -evalue 0.0001 -max_target_seqs 1000 -outfmt "6 sseqid qstart qend sseq" -query week1_query.fa >> seq.txt
rm fastaformat.txt
cat week1_query.fa > fastaformat.txt
./blastfasta.py seq.txt >> fastaformat.txt
rm transeq.txt
transeq -sequence fastaformat.txt -outseq transeq.txt
rm align
mafft transeq.txt > align.txt
