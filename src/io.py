# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import
import glob
from scipy.io import loadmat
from os import path
import parse
import pandas as pd

def _load_data(columns):
    times = []
    for file in glob.glob(path.join("data","vta1","data","*")):
        fileinfo = parse.parse(
            path.join("data","vta1", "data","{treatment}_{task}_{session}.mat"),
            file,
        ).named
        mat = loadmat(file)
        event_categories = {c: mat[c][:, 0] for c in columns}
        df = pd.DataFrame(event_categories)
        for key, value in fileinfo.items():
            df[key] = value
        df = df.set_index(["treatment", "task", "session"])
        
        times.append(df)

    if len(times) == 0:
        raise ValueError("Data not found. See data/README.md file"
                         " on instructions for downloading the data")
    # combine DataFrame for each file into a single DataFrame
    times_df = times[0].append(times[1:] if len(times) > 1 else [])
    return times_df.sort_index()

def load_spikes():
    """ returns spike times from vta-1 dataset
    
    # DataFrame columns:
    - spiketimes: time of spiking of optogenetically-identified dopamine
                  neurons in the mouse ventral tegmental area in milliseconds
    """
    return _load_data(["spiketimes"])


def load_trial_data():
    """ returns odor and reward onsets from vta-1 dataset
    
    # DataFrame columns:
    - odor_onsets: time of odor onset in milliseconds
    - reward_onsets: time of reward onset in milliseconds
    - trial_type:
        - 1-9 correspond to Odor A Trials, with ISIs of 1.2s (1) to 2.8s (9).
        - 10 and 11 correspond to Odor B and Odor C trials, respectively
        - 16 corresponds to Odor D trials
        - 13 corresponds to Odor A omission trials
        - 14 corresponds to Odor B omission trials
        - 15 corresponds to Odor C omission trials
    """
    return _load_data(["odor_onsets", "reward_onsets", "trial_type"])