#!/usr/local/bin/python3

# Imports
import math
import pandas as pd
import numpy as np


def pidata(st,en,step,func,formatter=None):
    xaxis = ""
    yaxis = ""
    i = st
    while (i < en):
        if i + step < en:
            extr = ","
        else:
            extr = ""
        if formatter != None:
            xaxis += formatter(i) + extr
            yaxis += formatter(func(i)) + extr
        else:
            xaxis += i + extr
            yaxis += func(i) + extr
        i += step
    return (xaxis,yaxis)

# PI series
ax, ay = pidata(-math.pi,math.pi,0.25,lambda x: math.sin(x),lambda x:f"{x:.2f}")
print(f"[{ax}],\n[{ay}]")


# def stepFunc(steps, offset, ratio)
#     arr = []
#     for i in range(0, steps):
#         if i == 0:
#             arr.append(offset)
#         yield offset + i * ratio
# culmn = 0.0
# for i in range(0, 100):

data = pd.DataFrame()
data['X'] = pd.array(np.arange(0, 100))
data['Y'] = pd.array([(np.random.randint(0,x+1)) for x in data['X']])
                      
