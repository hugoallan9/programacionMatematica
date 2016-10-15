def hanoi(N, inc='A', temp='B', fin='C'):

    if N > 0:
        hanoi(N-1, inc, fin, temp)
        print 'Se mueve el disco en torre', inc, 'a torre', fin
        hanoi(N-1, temp, inc, fin)

discos = int(input("Ingresa el numero de discos:"))
pasos = 2**discos - 1

hanoi(discos)

print 'Se necesitaron ', pasos, ' pasos para resolver el juego.'
