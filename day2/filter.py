#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )

# Interate the file line by line
for line in f:
    # Split the line on whitespace
    fields = line.split()
    # Determine if the 9th column contains the spring tRNA
    if "tRNA" in fields[9]:
        print line,