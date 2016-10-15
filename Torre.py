# -*- coding: utf-8 -*-
#!/usr/bin/python
 
def torres(N, inc='1', temp='2', fin='3'):
 
    if N > 0: 
        torres(N-1, inc, fin, temp)
        print ('Mover torre', inc, 'a torre', fin)
        torres(N-1, temp, inc, fin)
        
discos = int(input("Ingresa el numero de discos:"))
torres(discos)
print ('La cantidad de movimientos mínimos es:',2**(discos)-1)
    
