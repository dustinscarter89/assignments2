#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:20:37 2017

@author: dustinscarter
"""
import matplotlib.pyplot as plt
from math import sin
from random import random
import numpy as np

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')

x1 = np.linspace(0,2,100)
y1 = np.sqrt(1-(x1-1)**2)
ax1.plot(x1,y1,'k')

y2 = 2-np.sqrt(4-x1**2)
ax1.plot(x1,y2,'k')

ax1.set_xlim(0,2)
ax1.set_ylim(0,2)
ax1.fill_between(x1, y1, y2, where=y1>y2, facecolor='green')

plt.show()
#plt.savefig('MC1.png')
# MC intergral


def f(x):
    return 2-np.sqrt(4-x**2)
def g(x):
    return np.sqrt(1-(x-1)**2)

def MC(N):
    count = 0
    for i in range(N):
        x = 2*random()
        y = random()
        if f(x)<=y<=g(x):
            count += 1
    I = 2*count/N
    return I
print(MC(10))
print(MC(100))
print(MC(1000))
print(MC(10000))

p1=MC(10)/4
p2=MC(100)/4
p3=MC(1000)/4
p4=MC(10000)/4


var1=p1*(1-p1)
var2=p2*(1-p2)
var3=p3*(1-p3)
var4=p4*(1-p4)

std1=np.sqrt(var1)
std2=np.sqrt(var2)
std3=np.sqrt(var3)
std4=np.sqrt(var4)

print(std1)
print(std2)
print(std3)
print(std4)