import fractions

def ListaPhi(n):
	resultado = list(range(n + 1))
	for i in range(2, len(resultado)):
		if resultado[i] == i:  # i is prime
			for j in range(i, len(resultado), i):
				resultado[j] = resultado[j] // i * (i - 1)
	return resultado

Phis = ListaPhi(1000000)
ans = max(range(2,len(Phis)), key = (lambda i: fractions.Fraction(i,Phis[i])))
print str(ans)
