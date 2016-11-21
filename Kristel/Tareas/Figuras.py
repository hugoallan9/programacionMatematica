


#Figuras

#TrianguloRelleno
print("Triangulo")
x = int(eval(input("Tamaño del triangulo:"))) 
ult = (x * 2) - 1 
for imp in range(1, ult, 2): 
        linea = '*' * imp
        linea = linea.center(ult, ' ') 
        print(linea)



        
#TrianguloHueco




#CuadradodRelleno
print("Cuadrado")
b = int(eval(input("Tamaño del cuadrado: ")))
for i in range(b):
    for j in range(b):
        print("*", end="")
    print("")

#CuadradoHueco


#RectanguloRelleno
print("Rectangulo")
b = int(eval(input("Tamaño de altura: ")))
a = int(eval(input("Tamaño de base: ")))
for i in range(b):
    if i % 2 ==0:
        print(a*"*")
    else:
        print((b)*"*")
    

#RectanguloHueco
