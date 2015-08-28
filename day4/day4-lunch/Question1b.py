#!/usr/bin/env python

#  Overlap region

""""
Count intersection to three BED files
"""

from __future__ import division
import numpy
import sys
import matplotlib.pyplot as plt

def arrays_from_len_file(fname):
    arrays = {}
    for line in open(fname):
        fields = line.split()
        name = fields[0]
        size = int(fields[1])
        arrays[name] = numpy.zeros(size, dtype=bool)
    return arrays

def set_bits_from_file(arrays, fname): # Just one time
    for line in open(fname):
        fields = line.split()
        #  Parse fields
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        arrays[chrom][start:end] = 1


CTCF = arrays_from_len_file(sys.argv[1])  #  como no va a funcionar sin el sys, por eso se anade el sys arriba
set_bits_from_file(CTCF, sys.argv[2])
BEAF = arrays_from_len_file(sys.argv[1])  #  como no va a funcionar sin el sys, por eso se anade el sys arriba
set_bits_from_file(BEAF, sys.argv[3])
SuHW = arrays_from_len_file(sys.argv[1])  #  como no va a funcionar sin el sys, por eso se anade el sys arriba
set_bits_from_file(SuHW, sys.argv[4])


def OVERLAP(file, arrays):
    total = 0
    any_overlap = 0
    all_overlap = 0
    overlap = 0
    for line in open(file):
        fields = line.split()
        #  parse fields
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        # get slice
        sl = arrays[chrom][start:end]
        #  aggregate
        total += 1
        any_overlap += sl.any()
        all_overlap += sl.all()
        # overlap
        if len(sl) > 0:
            overlap += (numpy.sum(sl)/len(sl)<=1.00)
    print "Total: %d, Any overlap: %d, All overlap: %d, overlap: %d" % (total, any_overlap, all_overlap, overlap)
        
# como hay 3 tipos para escoger, y se eligen 2, para calcular el numero de permutaciones es el 3 a la 2 y da 9
OVERLAP(sys.argv[2], CTCF) # CTCF vs CTCF
OVERLAP(sys.argv[2], BEAF) # CTCF vs BEAF
OVERLAP(sys.argv[2], SuHW) # CTCF vs SuHW
OVERLAP(sys.argv[3], CTCF) # BEAF vs CTCF
OVERLAP(sys.argv[3], BEAF) # BEAF vs BEAF
OVERLAP(sys.argv[3], SuHW) # BEAF vs SuHW
OVERLAP(sys.argv[4], CTCF) # SuHW vs CTCF
OVERLAP(sys.argv[4], BEAF) # SuHW vs BEAF
OVERLAP(sys.argv[4], SuHW) # SuHW vs SuHW


def OVERLAP(file, arrays2, arrays3):
    total = 0
    any_overlap = 0
    all_overlap = 0
    overlap = 0
    for line in open(file):
        fields = line.split()
        #  parse fields
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        # get slice
        sl = arrays2[chrom][start:end]
        sl2 = arrays3[chrom][start:end]
        #  aggregate
        total += 1
        any_overlap += sl.any() & sl2.any()
        all_overlap += sl.all() & sl2.all()
        # overlap
        if len(sl) > 0 and len(sl2) > 0:
            overlap += (numpy.sum(sl)/len(sl)<=1.00) & (numpy.sum(sl2)/len(sl2)<=1.00)
    print "Total: %d, Any overlap: %d, All overlap: %d, overlap: %d" % (total, any_overlap, all_overlap, overlap)

# como hay 3 tipos para escoger, y se eligen 3, para calcular el numero de permutaciones es el 3 a la 3 y da 27
OVERLAP(sys.argv[2], CTCF, CTCF) # CTCF vs CTCF vs CTCF
OVERLAP(sys.argv[2], CTCF, BEAF) # CTCF vs CTCF vs BEAF
OVERLAP(sys.argv[2], CTCF, SuHW) # CTCF vs CTCF vs SuHW
OVERLAP(sys.argv[2], BEAF, CTCF) # CTCF vs BEAF vs CTCF
OVERLAP(sys.argv[2], BEAF, BEAF) # CTCF vs BEAF vs BEAF
OVERLAP(sys.argv[2], BEAF, SuHW) # CTCF vs BEAF vs SuHW
OVERLAP(sys.argv[2], SuHW, CTCF) # CTCF vs SuHW vs CTCF
OVERLAP(sys.argv[2], SuHW, BEAF) # CTCF vs SuHW vs BEAF
OVERLAP(sys.argv[2], SuHW, SuHW) # CTCF vs SuHW vs SuHW

OVERLAP(sys.argv[3], CTCF, CTCF) # BEAF vs CTCF vs CTCF
OVERLAP(sys.argv[3], CTCF, BEAF) # BEAF vs CTCF vs BEAF
OVERLAP(sys.argv[3], CTCF, SuHW) # BEAF vs CTCF vs SuHW
OVERLAP(sys.argv[3], BEAF, CTCF) # BEAF vs BEAF vs CTCF
OVERLAP(sys.argv[3], BEAF, BEAF) # BEAF vs BEAF vs BEAF
OVERLAP(sys.argv[3], BEAF, SuHW) # BEAF vs BEAF vs SuHW
OVERLAP(sys.argv[3], SuHW, CTCF) # BEAF vs SuHW vs CTCF
OVERLAP(sys.argv[3], SuHW, BEAF) # BEAF vs SuHW vs BEAF
OVERLAP(sys.argv[3], SuHW, SuHW) # BEAF vs SuHW vs SuHW

OVERLAP(sys.argv[4], CTCF, CTCF) # SuHW vs CTCF vs CTCF
OVERLAP(sys.argv[4], CTCF, BEAF) # SuHW vs CTCF vs BEAF
OVERLAP(sys.argv[4], CTCF, SuHW) # SuHW vs CTCF vs SuHW
OVERLAP(sys.argv[4], BEAF, CTCF) # SuHW vs BEAF vs CTCF
OVERLAP(sys.argv[4], BEAF, BEAF) # SuHW vs BEAF vs BEAF
OVERLAP(sys.argv[4], BEAF, SuHW) # SuHW vs BEAF vs SuHW
OVERLAP(sys.argv[4], SuHW, CTCF) # SuHW vs SuHW vs CTCF
OVERLAP(sys.argv[4], SuHW, BEAF) # SuHW vs SuHW vs BEAF
OVERLAP(sys.argv[4], SuHW, SuHW) # SuHW vs SuHW vs SuHW

#hasta aqui el codigo de arriba funciona
#esto se hace ahora para el ven diagram
#from matplotlib_venn import venn3
#venn3(subsets = (2578, 1715, 1, 2, 1, 2, 2), set_labels = ('CTCF', 'BEAF', 'SuHW'))

#from matplotlib_venn import venn3
#CTCF = set(['5600', '3192', '2231', '2578'])
#BEAF = set(['5600', '2354', '1158', '1715'])
#SuHW = set(['6135', '1782',' 246', '516'])

#venn3([CTCF, BEAF, SuHW], ('CTCF', 'BEAF', 'SuHW'))

#plt.show()

from matplotlib_venn import venn3
venn3(subsets = (2143, 1268, 3412, 1852, 3996, 3121, 5264), set_labels = ('CTCF', 'BEAF', 'SuHW'))
#plt.show()
plt.savefig("question1b.png")
