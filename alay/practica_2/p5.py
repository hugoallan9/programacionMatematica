n = 5
f = 1
primos=[]
 
while True:
    if all(n % p for p in primos):
        primos.append(n)
    else:
        if not any((n-2*i*i) in primos for i in range(1, n)):
            break
    n =n+(3-f)
    f = -f

print "Respuesta:", n
