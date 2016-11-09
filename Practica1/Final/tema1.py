# -*- coding: utf-8 -*-
def primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    for i in range(2,numero):
        if (numero % i) == 0:
            return False
    return True

n = 0
aux = 0
while aux < 10001:
    if primo(n) == True:
        aux = aux + 1
    n = n + 1
print n-1
