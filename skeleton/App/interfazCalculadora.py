import Tkinter as tk

class gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.master.title('Calculadora')
        self.master.geometry('450x450')
        self.createWidgets()

    def createWidgets(self):
        boton9 = tk.Button(text='9')
        boton9.grid(column = 2, row = 5)

        boton8 = tk.Button(text = '8')
        boton8.grid(row = 5, column = 1)

        boton7 = tk.Button(text = '7')
        boton7.grid(row = 5, column = 0)

        boton6 = tk.Button(text = '6')
        boton6.grid(row = 7, column = 2)

        boton5 = tk.Button(text = '5')
        boton5.grid(row = 7, column = 1)

        boton4 = tk.Button(text = '4')
        boton4.grid(row = 7, column = 0)

        boton3 = tk.Button(text = '3')
        boton3.grid(row = 9, column = 2)

        boton2 = tk.Button(text = '2')
        boton2.grid(row = 9, column =1)

        boton1 = tk.Button(text = '1')
        boton1.grid(row = 9, column = 0)

        boton0 = tk.Button(text='0')
        boton0.grid(row =11, column = 1)


inter = gui()
inter.mainloop()
        
