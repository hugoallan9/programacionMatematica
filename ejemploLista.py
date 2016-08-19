# -*- coding: utf8 -*-


# Lista de meses

meses = ['January', 
	'February', 
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'Octuber',
	'November',
	'December']

terminaciones = ['st', 'nd', 'rd'] + 17*['th'] + ['st', 'nd', 'rd'] +7*['th'] + ['st']

fecha = raw_input('Ingresa la fecha (MM/DD/AAAA)')

mes = fecha[0:2]
dia = fecha[3:5]
year = fecha[-4:]

print mes, dia, year

