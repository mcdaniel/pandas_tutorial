#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

letfreq = pd.read_csv("data/wordle_freq.csv")
print(letfreq.head())
hist = letfreq.hist(column='frequency', bins=26)
hist.savefig("data/wordle_freq_hist.png")

# TODO: PROBLEM - I dont really understand what this is 
# doing or what the paramters are.  Need to slow down 
# and look at this carefully.