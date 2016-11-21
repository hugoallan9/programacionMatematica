#problema 9 Euler

a=0
b=0
c=0
e=False
for i in range(1,1000/3):
    for j in range(i,1000/2):
        c=1000-i-j
        if (i*i+j*j)==c*c:
            e=True
            break
    if e:
        break
resultado=i*j*c

print "Respuesta:", resultado
            
            
