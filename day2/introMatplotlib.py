#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None)

df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

# que columna contiene el cromosoma 2L
#roi = df["chromosome"].str.contains("2L")
#print df[roi]

#eje de y es la posicion donde se encuentra el cromosoma, y el de x es el numero de filas (rows) 2L en centromere
#plt.figure()
#plt.plot(df[roi]["start"])
#plt.savefig("starts2L.png")

for chromosome in ("2L", "2R", "Y"):
    roi = df["chromosome"].str.contains(chromosome)

#print df[roi]

    plt.figure()
    plt.plot(df[roi]["start"])
    plt.title(chromosome)
    plt.ylabel("start position")
    plt.xlabel("gene")
    plt.savefig("starts" + chromosome + ".png")





