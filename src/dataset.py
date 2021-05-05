'''Formatting the data'''
from . import io
import numpy as np

class Vta1Dataset():
    def __init__(self, treatment, task):
        self.spikes = io.load_spikes()
        self.times = io.load_trial_data()
        self.treatment = treatment
        self.task = task
        self.window = 1.2
        self.isi_map = {float(trial_type): 1.2 + (trial_type) * 0.2 for trial_type in range(10)}
        self.isi_map[10.0] = 1.2
        self.isi_map[11.0] = 2.8
        self.trial_type_map = {"A": list(range(0, 10)), "B": [10], "C": [11]}

    def spike_times_per_trial(self, odor):
        '''Returns spikes_trial, a list for each trial which is a dataframe of all spikes during that trial.
        Returns isi_list, a list of interstimulus interval times for each trial.
        '''
        time_index = self.times.reset_index()
        sessionarray = time_index[
            (time_index["task"] == self.task)
            & (time_index["treatment"] == self.treatment)
        ]["session"].unique()
        spikes_trial = []
        isi_list = []
        for session in sessionarray:
            odor_times = self.times.loc[self.treatment, self.task, session]
            spike_times = self.spikes.loc[self.treatment, self.task, session]
            odor_table = odor_times[odor_times["trial_type"].isin(self.trial_type_map[odor])]
            for _, row in odor_table.iterrows():
                start = row["odor_onsets"]
                end = start + self.window * 1000
                isi = self.isi_map[row["trial_type"]]
                trial_isi = spike_times[
                    (spike_times["spiketimes"] >= start)
                    & (spike_times["spiketimes"] <= end)
                ]
                assert len(trial_isi) >= 0
                spikes_trial.append(trial_isi - start)
                isi_list.append(isi)
        return spikes_trial, isi_list

    def binned_spike_counts_per_trial(self, odor, bin_count=50):
        '''Returns binned spike count for use in PSTH graph.
           It accepts odor (A,B,C) and bin count (integer) as an input'''
        hist_odor = []
        spikes_trial, _ = self.spike_times_per_trial(odor)
        for interval_spikes in spikes_trial:
            T = self.window * 1000
            bin_size = T / bin_count
            bins = np.arange(0, T + bin_size, bin_size)
            spikes_t = interval_spikes.to_numpy()
            r_est, _ = np.histogram(spikes_t, bins=bins)
            hist_odor.append(r_est)
        return hist_odor

    def linreg_X_Y(self, odors, bin_count=50):
        ''' X is a matrix with a rows for each trial and column for each bin.
            Y is also a matrix with a row for each trial, and one column representing interstimulus intervals.
            This function takes different odors (A, B, C) as a list and creates X and Y from trials with the selected odors.
        '''
        odor_hist = []
        odor_time = []
        for odor in odors:
            odor_hist.append(np.array(self.binned_spike_counts_per_trial(odor, bin_count)))
            odor_time.append(np.array(self.spike_times_per_trial(odor)[1]))
        X = np.vstack(odor_hist)
        Y = np.hstack(odor_time)
        return (X, Y)
