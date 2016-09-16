#!/bin/bash/env python

file = open("alignblastresult", 'r')
string_list= file.read().split(">")
result = ""
f = open("output2", 'w')

for i in range (1, len(string_list)):
    gene_name= string_list[i].split("\n")[0]
    result += ">" + gene_name + '\n'
    sequences = string_list[i].split("Query")
    for j in range (1, len(sequences)):
        result += sequences[j].split("\n")[2].split()[-2] + '\n'
    f.write(result)
    result = ""

f.close()
file.close()