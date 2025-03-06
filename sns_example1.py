#!/usr/local/bin/python3

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = (
    {
        "X": [-3.14,-2.89,-2.64,-2.39,-2.14,-1.89,-1.64,-1.39,-1.14,-0.89,-0.64,-0.39,-0.14,0.11,0.36,0.61,0.86,1.11,1.36,1.61,1.86,2.11,2.36,2.61,2.86,3.11],
        "Y": [-0.00,-0.25,-0.48,-0.68,-0.84,-0.95,-1.00,-0.98,-0.91,-0.78,-0.60,-0.38,-0.14,0.11,0.35,0.57,0.76,0.89,0.98,1.00,0.96,0.86,0.71,0.51,0.28,0.03]
    }
)

# Create the Figure and Axes
sns.set_theme()
df = pd.DataFrame(data)
sns.relplot(df, x="X", y="Y", kind="line")
plt.savefig("data/sns_pi_chart.png")