# -*- coding: utf-8 -*-
def menu():
    print '='*20
    print '(179) Problema 179'
    print '(216) Problema 216'
    print '(357) Problema 357'
    print '(4) Salir'
    print '='*20,'\n'
def primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    for i in range(2,numero):
        if (numero % i) == 0:
            return False
    return True
def criba(n):
  l=[]
  multiplos = set()
  for i in range(2, n+1):
    if i not in multiplos:
      l.append(i)
      multiplos.update(range(i*i, n+1, i))
  return l[-1]
def problema357():
    n = 1
    suma = 0
    divisores = []
    primos = []
    while n < 100000000:
        for i in range(1,n+1):
            if (n % i) == 0:
                divisores.append(i)
        for d in divisores:
            c = d + n/d
            if primo(c) == True:
                primos.append(c)
        if len(divisores) == len(primos):
            suma = suma + n
        #print n, suma
        #print divisores, primos
        divisores = []
        primos = []
        n = n + 1
    print suma
def problema179():
    n = 2
    divisores1 = []
    divisores2 = []
    number = 0
    while n < 10000000:
        for i in range(1,n+1):
            if (n % i) == 0:
                divisores1.append(i)
        aux = n + 1
        for j in range(1, aux+1):
            if (aux % j) == 0:
                divisores2.append(j)
        if len(divisores1) == len(divisores2):
            number = number + 1
        n = n + 1
        divisores1, divisores2 = [], []
    print number
def problema216():
    n = 2
    primes = 0
    while n <= 50000000:
        t_n = 2 * (n ** 2) -1
        if criba(t_n + 1) == t_n:
            primes = primes + 1
        n = n + 1
    print primes


op = ''
while op != '4':
    menu()
    op = raw_input('Ingrese el número del problema a realizar: ')
    print '\n'
    if op == '179':
        problema179()
    elif op == '216':
        problema216()
    elif op == '357'
        problema357()
