from Tkinter import *


def Sumar():
    suma = float(caja1.get()) + float(caja2.get())
    etiquetaResultado = Label(gui, text = suma)
    etiquetaResultado.pack()

def Restar():
    resta = float(caja1.get()) - float(caja2.get())
    etiquetaResultado = Label(gui, text = resta)
    etiquetaResultado.pack()

def Multiplicar():
    producto =  float(caja1.get()) * float(caja2.get())
    etiquetaResultado = Label(gui, text = producto)
    etiquetaResultado.pack()

def Dividir():
    producto =  float(caja1.get()) / float(caja2.get())
    etiquetaResultado = Label(gui, text = producto)
    etiquetaResultado.pack()




gui = Tk()
gui.title('Calculadora simple')
gui.geometry('400x200')

#Haciendo el primer label
etiqueta1 = Label(gui, text= 'Ingresa el primer numero')
etiqueta1.pack()

#Haciendo la primera caja de entrada para el primer numero
caja1 = Entry(gui)
caja1.pack()

#Haciendo el primer label
etiqueta2 = Label(gui, text= 'Ingresa el segundo numero')
etiqueta2.pack()

#Haciendo la primera caja de entrada para el primer numero
caja2 = Entry(gui)
caja2.pack()

#Boton de suma
botonSuma = Button(gui, text= 'Sumar', command = Sumar)
botonSuma.pack()

#Boton de Resta
botonResta = Button(gui, text= 'Restar', command = Restar)
botonResta.pack()

#Boton de Multiplicar
botonMultiplicar = Button(gui, text= 'Multiplicar', command = Multiplicar)
botonMultiplicar.pack()

#Boton de Division
botonDividir = Button(gui, text= 'Dividir', command = Dividir)
botonDividir.pack()


gui.mainloop()
