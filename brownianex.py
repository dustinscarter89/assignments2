#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:07:30 2017

@author: dustinscarter
"""

# Brownian Motion
import numpy as np
import matplotlib.pyplot as plt

# init
L1 = 101
L2 = 101
N = 1000

position = np.empty([N,2])
position[0,0] = int(L1/2)
position[0,1] = int(L2/2)
direction = np.array([[0,1],[0,-1],[1,0],[-1,0]])

# random walk
for i in range(1,N):
    position1 = [-1,-1]
    
    while min(position1)<0 or position1[0] >L1 or position1[1] >L2:
        move = np.random.randint(len(direction))
        position1 = position[i-1,:] + direction[move]
        
    position[i,:] = position1
plt.xlim(0,101)
plt.ylim(0,101)
plt.title('Brownian motion')
plt.plot(position[:,0], position[:,1], '-o')        
plt.show()