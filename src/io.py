# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import
import glob
from scipy.io import loadmat 
from os import path
import parse
import pandas as pd

def _load_data(column):
    spikes = []
    for file in glob.glob(path.join("data","vta1","data","*")):
        fileinfo = parse.parse(path.join("data","vta1", "data","{treatment}_{task}_{trial}.mat"), file).named
        mat = loadmat(file)
        for spike in mat[column]:
            d = {
                 "time": spike[0] 
                 }
            d.update(fileinfo)
            spikes.append(d) 
    if len(spikes) == 0:
        raise ValueError("Missing data. See data/README.md file on instructions for downloading the data")
        
    spiket = pd.DataFrame(spikes)        
    spiket = spiket.set_index(["treatment", "task", "trial"])
    return spiket

def load_spikes():
    """ return spike_train derived from crcns vta-1 dataset"""
    return _load_data("spiketimes")
    

        
def load_odor():
    """ return odor onsets derived from crcns vta-1 dataset"""
    return _load_data("odor_onsets")
    


    
    