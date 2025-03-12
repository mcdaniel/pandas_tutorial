#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

maxval = 15
numbers = np.arange(maxval)
squares = np.fromfunction(lambda x: x**2, (maxval,))
cubes = np.fromfunction(lambda x: x**3, (maxval,))

fig, ax = plt.subplots()
ax.set_title('Squares, Cubes, and Fourths')
ax.set_xlabel('$x$')
ax.set_xticks(numbers)
ax.set_ylabel('$y = x^2$', color='blue')
ax.set_ylim(0, maxval**2)
ax.set_yticks(squares[3:])
ax.plot(numbers, squares)
ax.plot(numbers, cubes, 'yp')
ax.plot(numbers, [x**4 for x in range(maxval)], 'g--')
ax.legend(['Squares', 'Cubes', 'Fourths'], loc='upper left')
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.savefig('data/mpl_numbers.png')