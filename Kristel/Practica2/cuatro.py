#Problema74

import math

def cal():
	LIMITE = 10**6
	res = sum(1 for i in range(LIMITE) if d(i) == 60)
	return str(res)


def d(n):
	s = set()
	while True:
		s.add(n)
		n = fac(n)
		if n in s:
			return len(s)


def fac(n):
	resultado = 0
	while n != 0:
		resultado += FACTORIAL[n % 10]
		n //= 10
	return resultado

FACTORIAL = [math.factorial(i) for i in range(10)]


if __name__ == "__main__":
	print(cal())
