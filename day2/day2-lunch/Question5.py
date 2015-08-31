#!/usr/bin/env python

# Calculate how many alignments are on chromosome 2L 2R 3L 3R 4 X (keep track separately)

file_name1 = "/Users/cmdb/qbb2015/day1/BDGP6.sam"
Z = open(file_name1)

dictionary = {}

for line in Z:
    field = line.split()
    if "@" not in field[0]:
        if field[2] not in dictionary:
            dictionary[field[2]] = 1
        else:
            dictionary[field[2]] +=1
            
for alignments in ["2L", "2R", "3L", "3R", "4", "X"]:
    print alignments, dictionary[alignments]