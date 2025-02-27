#!/usr/local/bin/python3

# Imports
import math

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
