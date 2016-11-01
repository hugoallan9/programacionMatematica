from Tkinter import *

def hanoi(n,a,b,c,report):
	if n <= 0: return
	hanoi(n-1,a,c,b,report)
	report(n,a,b)
	hanoi(n-1,c,b,a,report)
	
class Tkhanoi:
	def __init__(self,n, bitmap = None):
		self.n = n
		self.tk = tk = Tk()
		self.tk.title("animacion")
		self.canvas = c = Canvas(tk)
		c.pack()
		width, height = tk.getint(c["width"]), tk.getint(c["height"])
		if bitmap:
			self.bitmap = c.create_bitmap(width // 2,height // 2,bitmap = bitmap,foreground = "blue")
		pegwidth = 10
		pegheight = height // 2
		pegdist = width // 3
		x1, y1 = (pegdist-pegwidth) // 2, height // 3
		x2, y2 = x1 + pegwidth, y1 + pegheight
		self.pegs = []
		p = c.create_rectangle(x1,y1,x2,y2,fill = "black")
		self.pegs.append(p)
		x1, x2 = x1 + pegdist, x2 + pegdist
		p = c.create_rectangle(x1, y1, x2, y2, fill = "black")
		self.pegs. append(p)
		x1, x2 = x1 + pegdist, x2 + pegdist
		p = c.create_rectangle(x1,y1,x2,y2,fill = "black")
		self.pegs.append(p)
		self.tk.update()
		pieceheight = pegheight // 16
		maxpiecewidth = pegdist * 2 // 3
		minpiecewidth = 2 * pegwidth
		self.pegstate = [[],[],[]]
		self.pieces = {}
		x1, y1 = (pegdist - maxpiecewidth) // 2, y2 - pieceheight - 2
		x2, y2 = x1 + maxpiecewidth, y1 + pieceheight
		dx = (maxpiecewidth - minpiecewidth) // (2 * max(1, n-1))
		for i in range(n, 0 , -1):
			p = c.create_rectangle(x1,y1,x2,y2,fill = "red")
			self.pieces[i] = p
			self.pegstate[0].append(i)
			x1, x2 = x1 + dx, x2 - dx
			y1, y2 = y1 - pieceheight - 2, y2 - pieceheight - 2
			self.tk.update()
			self.tk.after(25)
			
	def run(self):
		hanoi(self.n,0,2,1,self.report)
		
	def report(self,i,a,b):
		if self.pegstate[a][-1] != i: raise RuntimeError
		del self.pegstate[a][-1]
		p = self.pieces[i]
		c = self.canvas
		ax1, ay1, ax2, ay2 = c.bbox(self.pegs[a])
		while 1:
			x1, y1, x2, y2 = c.bbox(p)
			if y2 < ay1: break
			c.move(p,0,-1)
			self.tk.update()
		bx1, by1, bx2, by2 = c.bbox(self.pegs[b])
		newcenter = (bx1 + bx2) // 2
		while 1:
			x1, y1, x2, y2 = c.bbox(p)
			center = (x1 + x2) // 2
			if center == newcenter: break
			if center > newcenter: c.move(p,-1,0)
			else: c.move(p,1,0)
			self.tk.update()
		pieceheight = y2 - y1
		newbottom = by2 - pieceheight * len(self.pegstate[b]) - 2
		while 1:
			x1, y1, x2, y2 = c.bbox(p)
			if y2>= newbottom: break
			c.move(p,0,1)
			self.tk.update()
		self.pegstate[b].append(i)
		
class interfaz:
	def __init__(self):
		self.hola= hola = Tk()
		self.hola.title("Menu")
		Mensaje = Label(hola, text= "Elija el numero de discos: ")
		Mensaje.grid(row = 0, column = 0)
		boton1 = Button(hola,text = '1', command = lambda: self.mandarBoton('1'))
		boton1.grid(row = 0, column = 1)
		boton2 = Button(hola,text = '2', command = lambda: self.mandarBoton('2'))
		boton2.grid(row = 0, column = 2)
		boton3 = Button(hola,text = '3', command = lambda: self.mandarBoton('3'))
		boton3.grid(row = 0, column = 3)
		boton4 = Button(hola,text = '4', command = lambda: self.mandarBoton('4'))
		boton4.grid(row = 1, column = 1)
		boton5 = Button(hola,text = '5', command = lambda: self.mandarBoton('5'))
		boton5.grid(row = 1, column = 2)
		boton6 = Button(hola,text = '6', command = lambda: self.mandarBoton('6'))
		boton6.grid(row = 1, column =3)
		boton7 = Button(hola,text = '7', command = lambda: self.mandarBoton('7'))
		boton7.grid(row = 2, column = 1)	
		hola.mainloop()
		
	def mandarBoton(self,texto):
		n= int(texto)
		bitmap = None
		m = Tkhanoi(n,bitmap)
		m.run()
		
h = interfaz()