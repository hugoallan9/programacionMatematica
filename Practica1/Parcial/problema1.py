# -*- coding: utf-8 -*-
fib1 = 1
fib2 = 2
suma = 0

if (fib2 % 2) == 0:
    suma = suma + fib2

while fib2 < 4000000:
    aux = fib2
    fib2 = fib2 + fib1
    fib1 = aux
    if (fib2 % 2) == 0:
        suma = suma + fib2

print 'La suma de los números pares de la sucesión de Fibonacci menores a 4000000 es: ', suma
