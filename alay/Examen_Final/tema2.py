primos=[]
primos=[2,3,5,7]
for i in range(2, 55):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        primos.append(i)

def mayor(n):
    k=1
    for p in primos:
        if k*p>n:
            return k
        k=k*p
print "Respuesta: ", mayor(1000000)

