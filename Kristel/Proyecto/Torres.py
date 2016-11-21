# -*- coding: utf-8 -*-
#!/usr/bin/python
 
def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)
        
discos = int(input("Ingresa el numero de discos:"))
hanoi(discos)
print ('La cantidad de movimientos mínimos es:',2**(discos)-1)
    
