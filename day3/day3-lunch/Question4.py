#!/usr/bin/env python

import numpy as NUMPY
import pandas as pd
import matplotlib.pyplot as plt

# RECUERDA usar df para eliminar los ceros
file = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
file2 = file["FPKM"] > 0

#  Hay que eliminar los ceros.  Como es un MAplot se necesita comparar y anadir otro archivo o file
file3 = pd.read_table("~/qbb2015/stringtie/SRR072894/t_data.ctab")
file4 = file3["FPKM"] > 0

sumatoria = file4 & file2

file5 = file[sumatoria]["FPKM"]
file6 = file3[sumatoria]["FPKM"]


mate = NUMPY.log2(file5)
mate2 = NUMPY.log2(file6)

#The MA-plot is a plot of the distribution of the red/green intensity ratio ('M') plotted by the average intensity ('A')
m = mate - mate2
a = (mate + mate2)/2

#df2 = NUMPY.log(df["FPKM"])

#  Esto se usa para contruir la grafica
plt.figure()
plt.scatter(a, m, color="grey")
#plt.hist(np.log(df["FPKM"].values))
#df2.plot(kind='kde', color="purple")
plt.title("FPKM MA-Plot")
plt.ylabel("Distribution of the z/r intensity ratio")
plt.xlabel("Average intensity")
plt.savefig("question4maplot.png")

#  RECUERDA colocar los labels para la grafica ANTES de colocar el plt.savefig
