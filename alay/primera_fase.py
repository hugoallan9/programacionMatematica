
def Torres(n, inc='A', temp='B', fin='C'):
    
    if n>0:
        Torres(n-1, inc, fin, temp)
        print 'Mueve el disco en', inc, 'hacia', fin
        Torres(n-1, temp, inc, fin)

discos = int(input("Ingresa el numero de discos:"))

while True:
    if discos <= 0:
        discos=input('Ingresa un numero positivo de discos: ')
    else:
        Torres(discos)
        pasos=2**discos-1
        print ''
        print 'Menor numero de pasos para ganar: '+str(pasos)
        break
            
        
