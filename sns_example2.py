#!/usr/local/bin/python3

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

data = pd.DataFrame()
data['X'] = pd.array(np.arange(0, 100))
data['Y'] = pd.array([(np.random.randint(0,x+1)) for x in data['X']])
data['Depth'] = pd.array([(np.random.randint(0,5)) for x in range(0,100)])

sns.scatterplot(data, x="X", y="Y", hue="Depth")
plt.savefig("data/sns_scatter.png") 