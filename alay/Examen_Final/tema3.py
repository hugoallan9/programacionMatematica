# -*- coding: utf-8 -*-

contador = 0

for i in range(0, (10**8)-1):
    if i % 9 == 0:
        result1 = list(str(i))
        result2 = list(str(137 * i))
        sum1 = 0
        for j in result1:
            sum1 =sum1+int(j)
        sum2 = 0
        for j in result2:
            sum2 =sum2+int(j)
        if sum1 == sum2:
            contador =contador+1
print "Respuesta:", contador
