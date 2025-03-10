#!/usr/local/bin/python3

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

data = pd.DataFrame()
data['X'] = pd.array(np.arange(-3.14, 3.14, 0.1))
data['Y'] = pd.array([(math.sin(x)) for x in np.arange(-3.14, 3.14, 0.1)])

# Create the Figure and Axes
sns.set_theme()
sns.relplot(data, x="X", y="Y", kind="line")
plt.savefig("data/sns_pi_chart.png")