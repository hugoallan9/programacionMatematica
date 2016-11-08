# -*- coding: utf-8 -*-
def P(L):
    phi = range(L+1)
    for n in range(2, L+1):
        if phi[n] == n:
            for k in range(n, L+1, n):
                phi[k] -= phi[k] // n
    return sum(phi) - 1

print P(1000000)
