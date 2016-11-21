# -*- coding: utf-8 -*-

while True:
	n = input ('Ingresar anio: ')
	if 2100>= n>= 1900:
		a = n % 19
		b = n % 4
		c = n % 7
		d = ((19*a) + 24) % 30
		e = (2*b + 4*c + 6*d + 5) % 7
		marzo = 22 + d + e
		abril = d + e - 9
	
		if d + e < 10:
			print 'Domingo de pascua:',marzo,'de marzo'
		else:
			if abril == 25:
				print 'Domingo de pascua: 18 de abril'
			if abril == 26:
				print 'Domingo de pascua: 19 de abril'
			else:
				print 'Domingo de pascua:',d + e - 9,'de abril'
	else: 
		print 'El año ingresado debe estar entre 1900 y 2100'

