# -*- coding: utf-8 -*-
print '*Nota: Esta fórmula es válida de 1900 hasta 2100.*\n'
#Este programa sólo le dejará hacer cinco consultas.
a = 0 
while a < 5:
	a = a +1
	n = input ('>>>Ingrese el año que desea saber su domingo de pascua. \n')
	if 2100>= n>= 1900:
		a = n % 19
		b = n % 4
		c = n % 7
		d = ((19*a) + 24) % 30
		e = (2*b + 4*c + 6*d + 5) % 7
		marzo = 22 + d + e
		abril = d + e - 9
	
		if d + e < 10:
			print 'El domingo de Pascua del año', n, 'es el', marzo, 'de marzo.\n'
		else:
			if abril == 26:
				print 'El domingo de Pascua del año', n, 'es el 19 de abril.\n'
			if abril == 25:
				print 'El domingo de Pascua del año', n, 'es el 18 de abril.\n'
			else:
				print 'El domingo de Pascua del año', n, 'es el', d + e - 9, 'de abril.\n'
	else: 
		print '*El número que ingresó no está dentro del rango permitido*\n'