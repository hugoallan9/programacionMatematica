import Tkinter as tk
import parser 
import threading


class gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.master.title('Calculadora')
        self.master.geometry('450x450')
        self.createWidgets()
        self.entradaRPN = ''
        
    def mandarBoton(self,texto):
        self.textoEntry.set( self.textoEntry.get() + texto)
        self.entradaRPN = self.entradaRPN + ' ' + texto

    def calcularExpresion(self):
        rp = shunting(get_input(self.entradaRPN))
        self.textoEntry.set(resultado(rp))
        self.entradaRPN = ''
        
        
    def hiloCalculo(self):
        thread = list()
        t = threading.Thread( target = self.calcularExpresion )
        thread.append(t)
        t.start()
       
        
    def createWidgets(self):
        self.textoEntry = tk.StringVar()
        entrySalida = tk.Entry(textvariable=self.textoEntry)
        entrySalida.grid(row = 3, column = 1, columnspan = 10, rowspan = 2,
                         pady = 20)
        
        boton9 = tk.Button(text='9', command = lambda: self.mandarBoton('9'))
        boton9.grid(column = 2, row = 5)

        boton8 = tk.Button(text = '8', command = lambda: self.mandarBoton('8'))
        boton8.grid(row = 5, column = 1)

        boton7 = tk.Button(text = '7', command = lambda: self.mandarBoton('7') )
        boton7.grid(row = 5, column = 0)

        boton6 = tk.Button(text = '6',  command = lambda: self.mandarBoton('6'))
        boton6.grid(row = 7, column = 2)

        boton5 = tk.Button(text = '5', command = lambda: self.mandarBoton('5'))
        boton5.grid(row = 7, column = 1)

        boton4 = tk.Button(text = '4', command = lambda: self.mandarBoton('4'))
        boton4.grid(row = 7, column = 0)

        boton3 = tk.Button(text = '3', command = lambda: self.mandarBoton('3'))
        boton3.grid(row = 9, column = 2)

        boton2 = tk.Button(text = '2', command = lambda: self.mandarBoton('2'))
        boton2.grid(row = 9, column =1)

        boton1 = tk.Button(text = '1', command = lambda: self.mandarBoton('1'))
        boton1.grid(row = 9, column = 0)

        boton0 = tk.Button(text='0', command = lambda: self.mandarBoton('0'))
        boton0.grid(row =11, column = 1)

        botonSuma = tk.Button(text = '+', command = lambda: self.mandarBoton('+'))
        botonSuma.grid(column = 3,row = 5)

        botonResta = tk.Button(text = '-', command = lambda: self.mandarBoton('-'))
        botonResta.grid(column = 3,row = 7)

        
        botonProducto = tk.Button(text = 'x', command = lambda: self.mandarBoton('*'))
        botonProducto.grid(column = 3,row = 9)

        
        botonDivision = tk.Button(text = '/', command = lambda: self.mandarBoton('/'))
        botonDivision.grid(column = 4,row = 5)

        
        botonPotencia = tk.Button(text = '^', command = lambda: self.mandarBoton('^'))
        botonPotencia.grid(column = 4,row = 7)

        
        botonIgual = tk.Button(text = '=', command = self.hiloCalculo)
        botonIgual.grid(column = 4,row = 9)


        
        botonPL = tk.Button(text = '(', command = lambda: self.mandarBoton('('))
        botonPL.grid(column = 0,row = 11)

        
        botonPR = tk.Button(text = ')', command = lambda: self.mandarBoton(')'))
        botonPR.grid(column = 2,row = 11)





        

inter = gui()
inter.mainloop()
        
