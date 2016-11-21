#Menor numero ingresado

Lista = []
s = input("Ingreso los numeros, solo dejando espacio: ")
items = s.split() 
Lista = [eval(x) for x in items]
print("El menos de los numeros es",min(Lista))
