# -*- coding: utf-8 -*-
import Tkinter as tk

class InterfazFase2(tk.Frame):
    def __init__ (self, master = None):
        tk.Frame.__init__(self, master)
        self.master.title('Torres de Hanoi')
        self.master.geometry('500x500')
        self.createWidgets()

    def mandarBoton(self, texto):
        discos = int(texto)
        torres = hanoi(discos)

        lienzo = tk.Canvas(background = '#000000')
        lienzo.grid(row = 3, column = 1, columnspan = 9)



    #def dibujo(self, texto):
    #    discos = int(texto)
    #    lienzo = tk.Canvas(background = 'pale violet red')
    #    lienzo.grid(row = 3, rowspan = discos, column = 1, columnspan = 9)

    def createWidgets(self):
        etiqueta = tk.Label(text = 'Número de Discos:')
        etiqueta.grid(row = 1, column = 1, columnspan = 7)

        boton1 = tk.Button(text = '1', command = lambda: self.mandarBoton('1'))
        boton1.grid(row = 2, column = 1)

        boton2 = tk.Button(text = '2', command = lambda: self.mandarBoton('2'))
        boton2.grid(row = 2, column = 2)

        boton3 = tk.Button(text = '3', command = lambda: self.mandarBoton('3'))
        boton3.grid(row = 2, column = 3)

        boton4 = tk.Button(text = '4', command = lambda: self.mandarBoton('4'))
        boton4.grid(row = 2, column = 4)

        boton5 = tk.Button(text = '5', command = lambda: self.mandarBoton('5'))
        boton5.grid(row = 2, column = 5)

        boton6 = tk.Button(text = '6', command = lambda: self.mandarBoton('6'))
        boton6.grid(row = 2, column = 6)

        boton7 = tk.Button(text = '7', command = lambda: self.mandarBoton('7'))
        boton7.grid(row = 2, column = 7)

def hanoi(N, inc='A', temp='B', fin='C'):
    if N > 0:
        hanoi(N-1, inc, fin, temp)
        print 'Se mueve el disco en torre', inc, 'a torre', fin
        hanoi(N-1, temp, inc, fin)

fase2 = InterfazFase2()
fase2.mainloop()
