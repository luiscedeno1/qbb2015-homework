#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

# esto se anadio luego que se hizo la grafica de scatter3
metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
Sxl = [] #este es el list
for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    Sxl.append(df[roi]["FPKM"].values) #hay que definir un list
    
Sxl2 = []
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df2 = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi2 = df["t_name"].str.contains("FBtr0331261")
    Sxl2.append(df2[roi2]["FPKM"].values) #hay que definir un list
    
plt.figure()
plt.plot(Sxl, label = 'female')
plt.plot(Sxl2, label = 'male')
plt.legend()
plt.axis([0, 8, 0, 160])
plt.savefig("timecourse1.png")