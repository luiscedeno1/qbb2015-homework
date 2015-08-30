#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

file = open ("Bothfblast2.txt")

LIST = []

for line in file:
    if "Nu" in line:
        pass
    elif "  N" in line:
        fields = line.split()
        scores = float(fields [2])
        e_val = float(fields [3])
        LIST.append((scores,e_val))
    else:
        pass

SCORES = [x[0] for x in LIST]  
E_VAL = [x[1] for x in LIST]

plt.figure()
plt.title("Plot 1: Scores")
plt.axis([30, 300, 0, 8200])
plt.hist(SCORES , bins = 100, color="red")
plt.xlabel("Scores Alignment")
plt.savefig("SCORESHist.png")

plt.figure()
plt.title("Plot 2: E Values")
plt.axis([-0.1, 10.5, 0, 1200])
plt.hist(E_VAL , bins = 100, color="orange")
plt.xlabel("E Values Alignment")
plt.savefig("EVALUESHist.png")      
    