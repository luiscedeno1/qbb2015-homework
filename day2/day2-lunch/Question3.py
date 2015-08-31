#!/usr/bin/env python

# Count number of reads that map to exactly one location in the genome

file_name1 = "/Users/cmdb/qbb2015/day1/BDGP6.sam"
Z = open(file_name1)

count = 0

for line in Z:
    if "NM:i:1" in line:
        count += 1
    
print "Count number of reads that map to exactly one location in the genome is %s" %count