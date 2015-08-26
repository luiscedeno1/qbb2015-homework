#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
file_name1 = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(file_name1, comment='#', header=None)

df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

# Lines in BDGP6.Ensembl.81.gtf that contain "Sxl" gene.
roi = df["attributes"].str.contains("Sxl")

# X and Y axis
plt.figure()
plt.plot(df[roi]["start"])
plt.title("Plot 1: Lines in BDGP6.Ensembl.81.gtf that contain Sxl Gene")
plt.ylabel("Start Position")
plt.xlabel("Lines in BDGP6 where Sxl Gene is Located")
plt.savefig("plot1.png")
