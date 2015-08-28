#!/usr/bin/env python

import numpy as NUMPY
import pandas as pd
import matplotlib.pyplot as plt

file_name1 = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

#  Hay que eliminar los ceros
df = file_name1[file_name1["FPKM"] > 0]
df2 = NUMPY.log(df["FPKM"])

#  Esto se usa para contruir la grafica
plt.figure()
#plt.hist(np.log(df["FPKM"].values))
df2.plot(kind='kde', color="purple")
plt.title("FPKM values in SRR072893")
plt.ylabel("Density (FPKM) in SRR072893")
plt.xlabel("log FPKM Values")
plt.savefig("question3density.png")

#  RECUERDA colocar los labels para la grafica ANTES de colocar el plt.savefig