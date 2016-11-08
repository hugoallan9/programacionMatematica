tope=1000001
Fracciones=range(tope)
for i in range(2,tope):
    if Fracciones[i]==i:
        for j in range(i,tope,i):
            Fracciones[j]-=Fracciones[j]//i
resultado= sum(Fracciones)-1

print resultado
