# -*- coding: utf-8 -*-

data = []
with open('prueba3.txt','r') as myfile:
    for line in myfile:
        data.extend(map(int, line.split(',')))
print ( min(data))

