def SumaDigitos(n):
	return sum(map(int,list(str(n))))
	
n = 0

for i in xrange(0,10 ** 9,9):
	s1 = SumaDigitos(i)
	s2 = SumaDigitos(137*i)
	if s1 == s2:
		n = n + 1
		
print n