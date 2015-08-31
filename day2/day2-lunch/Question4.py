#!/usr/bin/env python

# For the first 10 alignments, print just the column indicating which chromosome a given read aligns to

file_name1 = "/Users/cmdb/qbb2015/day1/BDGP6.sam"
Z = open(file_name1)

count = 0

for line in Z:
    field = line.split()
    if "@" not in field[0] and count < 10:
        print field[2]
        count += 1
    elif count == 10:
        break
        
print "For the first 10 alignments, print just the column indicating which chromosome a given read aligns to is %s" %count