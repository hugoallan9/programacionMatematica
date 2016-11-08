x=1
y=2
suma = 0
total = 0

while suma <=4000000:
    suma = y
    if suma % 2 == 0:
        total = total+ suma
    suma = x+y
    x=y
    y=suma

print total
