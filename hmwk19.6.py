#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:46:32 2017

@author: dustinscarter
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:22:53 2017

@author: dustinscarter
"""

#Write a program to find the ground state of 
#LJ potential for N=3 (assuming $\epsilon$ = $\sigma$ = 1)

import numpy as np
import matplotlib.pyplot as plt

n = 6

def LJ(r1,r2,r3):
    r16 = r1**n
    r112 = r16*r16
    r26 = r2**n
    r212 = r26*r26
    r36 = r3**n
    r312 = r36*r36
    
    return 4*((1/r112 - 1/r16)+(1/r212 - 1/r26)+(1/r312 - 1/r36))


m=10000
r1 = np.linspace(1.0,3.0,m)
r2 = np.linspace(1.0,3.0,m)
r3 = np.linspace(1.0,3.0,m)



print('minimum value:   ', min(LJ(r1,r2,r3)))

x = abs(min(LJ(r1,r2,r3)))
y = (-4/(3*x)+(16/(9*x**2)+16/(3*x))**(1/2))/2
w =(-4/(3*x)-(16/(9*x**2)+16/(3*x))**(1/2))/2
z = y**(1/n)

print("minimum coordinate:   ",z)
print("minimum coordinate:   ",w)



