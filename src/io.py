# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import
import glob
from scipy.io import loadmat 
from os import path
import parse
import pandas as pd

def load_spikes():
    spikes = []
    for file in glob.glob(path.join("data","vta1","data","*")):
        fileinfo = parse.parse(path.join("data","vta1", "data","{treatment}_{task}_{trial}.mat"), file).named
        mat = loadmat(file)
        for spike in mat["spiketimes"]:
            d = {
                 "time": spike[0] 
                 }
            d.update(fileinfo)
            spikes.append(d) 

    spiket = pd.DataFrame(spikes)        
    spiket = spiket.set_index(["treatment", "task", "trial"])
    return spiket
        
def load_odor():        
    odor_onsets = []
    for file in glob.glob(path.join("data","vta1","data","*")):
        fileinfo = parse.parse(path.join("data","vta1", "data","{treatment}_{task}_{trial}.mat"), file).named
        mat = loadmat(file)
        for odor in mat["odor_onsets"]:
            d = {
                 "time": odor[0] 
                 }
            d.update(fileinfo)
            odor_onsets.append(d)


    odor_onsets = pd.DataFrame(odor_onsets)
    odor_onsets = odor_onsets.set_index(["treatment", "task", "trial"])
    return odor_onsets