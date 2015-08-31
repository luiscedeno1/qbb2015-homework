#!/usr/bin/env python

# Calculate average MAPQ score

file_name1 = "/Users/cmdb/qbb2015/day1/BDGP6.sam"
Z = open(file_name1)

count = 0
MAPQ = 0

for line in Z:
    field = line.split()
    if "@" not in field[0]:
        MAPQ = MAPQ + int(field[4])
        count += 1

        
print "Calculate average MAPQ score is %s" %(MAPQ/count)