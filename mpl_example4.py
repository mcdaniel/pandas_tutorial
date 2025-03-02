#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sctrx = np.random.randint(0, 100, 100)
sctry = np.random.randint(0, 100, 100)

errbarx = np.arange(0,100,5)
errbary = np.random.randint(0, 100, 20)
errbar_error = np.random.randint(10, 25, 20)

fix, axes = plt.subplots(2, 1)
axes[0].scatter(sctrx, sctry, color="red")
axes[0].set_title("Scatter Plot")
axes[0].grid(True)
axes[1].errorbar(errbarx, errbary, yerr=errbar_error, fmt='o')
axes[1].set_title("Error Bar Plot")
axes[1].grid(True)
plt.tight_layout()
plt.savefig("data/complex.png")