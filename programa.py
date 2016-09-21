# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:30:40 2016

@author: hugo
"""

linea = raw_input()
a,n, x = linea.strip().split()
a = int(a)
n = int(n)
x = float(x)
for x in range(n):
    for y in range(n):
        print '?', x, y
        b = raw_input()
        if( b == x):
            print '= x y'
            break