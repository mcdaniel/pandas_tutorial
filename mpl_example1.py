#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

# Load the data
letfreq = pd.read_csv("data/wordle_freq.csv", index_col='letter')
print(letfreq.head())
barser = letfreq['frequency'].transform(lambda x: x*100)

# Plot the data using steps #1 (create), #2 (add style), and #3 (output)
barchart = barser.plot.bar(column='frequency', color='red', ylabel='Percentage (%)')
barchart.grid(axis='y', zorder=0)
plt.savefig("data/wordle_freq_bar.png")

