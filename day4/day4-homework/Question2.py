#!/usr/bin/env python

import numpy as np
import copy as cp

# Venn diagrams are in the day4-lunch folder
# Extend the chrombits package we made in class to create the set of intervals corresponding to a ChromosomeLocationsBitArrays instance

class ChromosomeLocationBitArrays (object):
    def __init__ (self, dicts = None, file_name1 = None, tup = None):
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        if tup is not None:
            tpl_list = tup
        if file_name1 is not None:
            for line in open (file_name1):
                field = line.split()
                name = field[0]
                size = int(field[1])
                arrays[name] = np.zeros(size, dtype = bool)
        self.arrays = arrays
        self.tpl_list = tpl_list
        
    def set_bits_from_file (self, file_name1):
        for line in open (file_name1):
            field = line.split()
            chrom = field[0]
            start = int(field[1])
            end = int(field[2])
            self.arrays[chrom][start:end] = 1
    
    def create_tups (self, file_name1):
        for line in open (file_name1):
            field = line.split()
            chrom = field[0]
            start = int(field[1])
            end = int(field[2])
            self.tpl_list.append[chrom][start:end] = 1
            
    def intersect (self, other):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays (dicts = rval)
    
    def union (self, other):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays (dicts = rval)
        
    def complement (self):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~self.arrays[chrom]
        return ChromosomeLocationBitArrays (dicts = rval)
        
    def copy (self):
        return ChromosomeLocationBitArrays(
            dicts = cp.deepcopy (self.arrays)
            tup = cp.deepcopy (self.tpl_list)
        )
    
