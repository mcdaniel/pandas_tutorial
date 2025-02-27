#!/usr/local/bin/python3

import pandas as pd

# Load files
letfreq = pd.read_csv("data/wordle_freq.csv", index_col='letter')
print(letfreq)

# Show the frequency column
print(letfreq['frequency'])
print(letfreq['frequency'].tolist())

# Show a row of the table by index reference and integer row number
print(letfreq.loc['b'])
print(letfreq.iloc[1])

# Show a cell of the table referenced
print(letfreq.loc['b', 'frequency'])
print(letfreq.iloc[1, 1])
print(letfreq.at['b', 'frequency'])

# Show a range of values in a series
print(letfreq.iloc[1, 0:2])

# lastly, you can filter by a condition or conditions
print(letfreq[letfreq['frequency'] > 0.05])
print(letfreq[(letfreq['frequency'] > 0.05) & (letfreq['count'] > 3000)])