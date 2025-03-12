#!/usr/local/bin/python3

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

words = [['Uno', 'Dos', 'Tres', 'Quarto'], ['Un', 'Duex', 'Trois', 'Quatre']]
data = pd.DataFrame()
data['index'] = pd.Series(words[0])
data.set_index('index', inplace=True)
for i in range(0, len(words[1])):
    data[words[1][i]] = np.random.randint(0, (i+1)*25, len(words[0]))

sns.heatmap(data, annot=True, fmt='.2f')
plt.title('Heatmap')
plt.savefig('data/sns_heatmap.png')