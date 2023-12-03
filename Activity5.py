#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:39:28 2023

@author: Koichiro Takahashi
"""

import numpy as np

from scipy.special import factorial

# Problem.0
print("")
print("Problem. 0:")
print("Hello World")

# Problem.1
print("")
print("Problem. 1:")

def time(h):
    
    g = 9.8 
    t = np.sqrt(2*h/g)
    
    return t

h = 100 #[m]
print(time(h))

# Problem.2
print("")
print("Problem. 2:")


C = [1]
i = 0

def Catalan(n):
    if n == 0:
        return 1
    else:
        return ((4*n - 2)/(n + 1))*Catalan(n-1)
    
while  C[i] <= 1000000000: 
    a = Catalan(i+1)
    C.append(a)
    print(int(C[i]))
    i += 1

# Problem.3
print("")
print("Problem. 3a:")

def binomial(n,k):
    
    n = int(n)
    k = int(k)
    if k == 0:
        return 1
        
    else:
        Integer = factorial(n)/(factorial(k)*factorial(n-k))
        return int(Integer)

print(binomial(5,0))
print("")
print("Problem. 3b:")

def Pascal(n):
    for i in range(0,n+1):
        for j in range(0,i):
            print(binomial(i,j), end = " ")
        print(" ")
    
print(Pascal(20))

# Problem.4
print("")
print("Problem. 4a:")

print(Catalan(100))

print("")
print("Problem. 4b:")
def divisor(m, n):
    if n == 0:
        return m
    else:
        return divisor(n, m%n)
print(divisor(192, 108))
        


    