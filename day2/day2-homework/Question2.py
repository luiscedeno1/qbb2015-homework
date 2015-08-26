#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
file_name1 = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(file_name1, comment='#', header=None)

df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

# Lines in BDGP6.Ensembl.81.gtf that contain "Sxl" gene AND are of type "transcript".
roi = df["attributes"].str.contains("Sxl")
# Add another roi for the "transcripts"
roi2 = df["type"].str.contains("transcript")

# X and Y axis
plt.figure()
# Add roi2 in the plt.plot
plt.plot(df[roi][roi2]["start"])
plt.title("Plot 2: Lines in BDGP6.Ensembl.81.gtf that contain Sxl Gene and are transcribed")
plt.ylabel("Start Position")
plt.xlabel("Lines in BDGP6 where Sxl Gene is Located and Transcribed")
plt.savefig("plot2.png")