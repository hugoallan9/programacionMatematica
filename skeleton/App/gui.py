#-*- coding:utf-8 -*-
import Tkinter as tk
import tkMessageBox
from logica import *
class Interfaz(tk.Frame):
    calc = Calculadora()
    
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master.geometry('350x150+100+100')
        self.master.title('Calculadora simple')
        self.createWidgets()

    def createWidgets(self):
        self.etiquetaNum1 = tk.Label(text= 'Ingresa el primer número')
        self.etiquetaNum1.grid(row=0, stick=tk.W)

        self.caja1 = tk.Entry()
        self.caja1.grid(row=0, column=1)

        self.etiquetaNum2 = tk.Label(text = 'Ingresa el segundo número')
        self.etiquetaNum2.grid(row=1, stick = tk.W)

        self.caja2 = tk.Entry()
        self.caja2.grid(row = 1, column = 1)
        
        self.btSuma = tk.Button(text= 'Sumar', command = self.procesarSuma ) 
        self.btSuma.grid(stick=tk.N+tk.S+tk.E+tk.W,row=3, column=0, columnspan=2)
        
    def procesarSuma(self):
        self.num1 = float(self.caja1.get() )
        self.num2 = float( self.caja2.get() )
        tkMessageBox.showinfo('Resultado de suma', 'La suma es: %.2f'%self.calc.sumar(self.num1,self.num2))
