#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

print LIST[0]
SCORES, E_VAL in LIST

a = np.log10(SCORES)
b = -np.log10(E_VAL)

plt.figure()
plt.scatter(b, a, color="green")
plt.title("Scatterplot of Scores and E-Values")
plt.xlabel("log of E_VAL")
plt.ylabel("log of SCORES")

plt.savefig("SCORESEVALUESscatter.png")