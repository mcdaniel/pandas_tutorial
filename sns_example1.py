#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

3 # Set theme to default and load data
sns.set_theme()
df = pd.read_csv("data/wordle_freq.csv", index_col='bigram')

# Load the data