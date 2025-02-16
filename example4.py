#!/usr/local/bin/python3

import pandas as pd

# Load files
letfreq = pd.read_csv("data/wordle_freq.csv")
print(letfreq)

# Show the frequency column
print(letfreq['frequency'])
print(letfreq['frequency'].tolist())

