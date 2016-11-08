def MCD(a,b):
	resto = 0
	while b > 0:
		resto = b
		b = a % b
		a = resto
	return a

d = 2
n = 1
m = 0

while d <= 1000000:
	if n < d:
		if n == 1 or n == d - 1:
			m = m + 1
			n = n + 1
		else:
			if MCD(n,d) == 1:
				n = n + 1
				m = m + 1
			else:
				n = n + 1
	else:
		n = 1
		d = d + 1
		
print m
		