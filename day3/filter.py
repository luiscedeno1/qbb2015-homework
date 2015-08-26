#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

import sys 

print sys.argv
#filename = sys.argv[1]

#f = open( filename )



f = sys.stdin

# Interate the file line by line
#for line in f:
    # Split the line on whitespace
    #fields = line.split()
    # Determine if the 9th column contains the spring tRNA
    #if "tRNA" in fields[9]:
        #print line,
        
#line_count = 0
#for data in f:
    #if line_count <= 10:
        #pass
    #elif line_count <= 15:
        #print data,
    #else:
        #break
    #line_count += 1
    
#for line_count, data in enumerate( f ):
    #if line_count <= 10:
        #pass
    #elif line_count <= 15:
        #print data,
    #else:
        #break     

name_counts = {}
for line_count, data in enumerate( f ):
    fields = data.split()
    gene_name = fields [9]
    if gene_name not in name_counts:
        name_counts[gene_name] = 1
    else:
        name_counts[gene_name] += 1

# Iterate key, value pairs from the name counts dictionary
for key, value in name_counts.iteritems():
    print key, value
           