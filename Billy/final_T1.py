def EsPrimo(n):
	if n < 2:
		return False
	else:
		m = 2
		while m >= 2 and m < n:
			if n % m == 0:
				return False
				break
			else:
				m = m + 1

p = 1
m = 0
n = 0

while n < 10001:
	if EsPrimo(p) == False:
		p = p + 1
	else:
		m = p
		p = p + 1
		n = n + 1
		
print m