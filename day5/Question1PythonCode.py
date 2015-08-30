#! /usr/bin/env python

import sys

file_name1 = open("Bothfblast2.txt")


dictionary = {}

for line in file_name1:
    if line.startswith(">"):
        hit = line
    elif "Identities" in line:
        fields = line.split()
        identities = fields [2]
        gaps = fields [6]
        dictionary[hit]=(identities, gaps)
    else:
        pass

print dictionary 