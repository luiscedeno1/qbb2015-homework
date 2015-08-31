#!/usr/bin/env python

# Count number of alignments

file_name1 = "/Users/cmdb/qbb2015/day1/BDGP6.sam"
Z = open(file_name1)

count = 0

for line in Z:
    field = line.split()
    if "@" not in field[0]:
        count += 1
    
print "Number of alignments is %s" %count