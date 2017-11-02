#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:11:01 2017

@author: dustinscarter
"""

## Decay process
import numpy as np
import matplotlib.pyplot as plt


# Initial parameters
NTl = 1000
NPb = 0
tau = 3.053*60
dt = 1 
p = 1 - 2**(-dt/tau)
tmax = 1000

t_points = np.arange(0.0, tmax, dt)
Tl = []
Pb = []

for t in t_points:
    Tl.append(NTl)
    Pb.append(NPb)
    
    # Calculate the decayed atoms
    decay = 0
    for i in range(NTl):
        if np.random.random()<p:
            decay += 1
    NTl -= decay
    NPb += decay

plt.plot(t_points, Tl, label='Tl')
plt.plot(t_points, Pb, label='Pb')
plt.xlabel("Time")
plt.ylabel("Number of atoms")
plt.legend()
plt.show()