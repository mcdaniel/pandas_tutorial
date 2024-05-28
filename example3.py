#!/usr/local/bin/python3

import pandas as pd

# Load files
letfreq = pd.read_csv("data/wordle_freq.csv")
print(letfreq)
bigrams = pd.read_csv("data/wordle_bigram.csv")
print(bigrams)
trigrams = pd.read_csv("data/wordle_trigram.csv")
print(trigrams)

# Export files
letfreq.to_json("data/frequencies.json")