from eulerlib import *

p = numtheory.Divisors(1000000)
n = 1
m = 0
l = 0.0

while n <= 1000000:
	k = float(p.phi(n))
	s = float(n)
	t = s / k
	if t > l:
		l = t
		m = n
		n = n + 1
	else:
		n = n + 1

print m
		