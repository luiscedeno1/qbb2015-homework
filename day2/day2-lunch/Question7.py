#!/usr/bin/env python

# Count number of reads that start their alignment on chromosome 2L between base 10000 and 20000 (inclusive)

file_name1 = "/Users/cmdb/qbb2015/day1/BDGP6.sam"
Z = open(file_name1)

count = 0

for line in Z:
    field = line.split()
    if "@" not in field[0] and field[2] == "2L":
        if 10000 <= int(field[3]) <= 20000:
            count += 1
            
print count