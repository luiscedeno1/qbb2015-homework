#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
file_name1 = "/Users/cmdb/qbb2015/rawdata/samples.csv"

df = pd.read_table(file_name1, sep=',')

# Remember to include roi: region of interest
roi = df["sample"]

for z in roi:
    file_name2 = "/Users/cmdb/qbb2015/stringtie/" + z + "/t_data.ctab"
    df2 = pd.read_table(file_name2)
    # Add another roi with the specific transcript
    roi2 = df2["t_name"].str.contains("FBtr0331261")
    print df2[roi2]
