#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
file_name1 = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(file_name1)

arrangement = df.sort(columns="FPKM", ascending=True)
roi = arrangement["FPKM"] > 0
# Remember the FPKM
z = 0
for i in df["FPKM"]:
    if i > 0:
        z += 1
        print z
        print arrangement[roi]["FPKM"]
        
top = arrangement[roi]["FPKM"][0:11572]
middle = arrangement[roi]["FPKM"][11572:23145]
bottom = arrangement[roi]["FPKM"][23145:34717]

# X and Y axis
plt.figure()
plt.boxplot([top, middle, bottom])
plt.title("Plot 4: FPKM Values in SRR072893")
plt.ylabel("FPKM Values")
plt.xlabel("SRR072893")
plt.savefig("plot4.png")
