
# Computational Neuroscience Project

This project is to explore dataset vta-1 from crcns.org.

Information about the dataset can be found at: https://crcns.org/data-sets/bst/vta-1/about-vta-1


## Overview

When animals are unsure of the consequences of their environment(impending reward or punishment), the state of the environment is understood as "hidden". The brain acts as a function of probabilty distribution.

Using spike time data from a hidden states paradigm, can we create a model that will predict at what time point an animal is expecting a reward given a conditioned stimulus?  

## Hypothesis

In situations in which timing of reward is uncertain, an animal's expectation of the timing will be the mean of the distribution.

## Methods

Using the code in this repository, we created a peri-stimulus time histograms and raster plots to inititally compare spiking differences of dopaminergic neurons in ventral tegmental area of the brain in response to alternate reward times (1.2 or 2.8 seconds). We then performed a linear regression using these data, and used this model to predict reward expectancy for a novel stimulus and reward pair with randomly determined reward times that varied between 1.2 and 2.8 seconds. We then computed summary statistics on the resulting predictions. 

## Setting up

Follow instructions at [data/README.md](./data/README.md) to download dataset.


Create a virtual environment and install the dependencies as follows:

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Install the project in development mode by running `pip install -e .`.

Start a Jupyter Notebook server by running `jupyter notebook` and following the instructions that it outputs. Navigate to `Plots.ipynb` and run the cells to recreate the graphs. A wrapper class for the dataset can be found in the `src/` directory.
