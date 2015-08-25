#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header=None)

#print df
#print df.head()it is only for the first 10 lines

#print df.describe()
#print df.info()

#print "\nthis is what happens with [1:5]"
#print df[1:5]

#print "\nthis is what happens with [0:5]"
#print df[0:5]

# Show rows 10 through 15 (1-based, inclusive)
#print df[9:15]

#print df.info()
#how you update the columns
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]
#print df.info()

#print df.sort("type", ascending=False)

#print df["chromosome"]
#extract subset "chromosome", "start" and "end" columns
#print df[["chromosome", "start", "end"]]
#print df["start"][9:15]

#print df.shape
#df2 = df["start"]
#print df2.shape
#how to eliminate commas
#df2.to_csv("startColumn.txt", sep='\t', index=False)

#df es lo mismo que decir dataframe.  "algo" se refiere a las columnas.
#roi es igual a region of interest.
roi = df["start"] < 10
#print type(roi)
#print df[roi]













