import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitBotton = tk.Button(self, text = 'Quit',
                                    command = self.quit)
        self.quitBotton.grid()

app = Application()
app.master.title('Mi primer ventana')
app.mainloop()

        
    
