from Tkinter import * 

class Disco:
    def __init__(self,cv,pos,length,height,colour):
        x0, y0 = pos
        x1, x2 = x0-length/2.0, x0+length/2.0
        y1, y2 = y0-height, y0
        self.cv = cv
        self.item = cv.create_rectangle(x1,y1,x2,y2,
                                        fill = "#%02x%02x%02x" % colour)       
    def move_to(self, x, y):
        x1,y1,x2,y2 = self.cv.coords(self.item)
        x0, y0 = (x1 + x2)/2, y2
        dx, dy = x-x0, y-y0
        d = (dx**2+dy**2)**0.5

class Torre(list):
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h
    def top(self):
        return self.x, self.y - len(self)*self.h
    
class HanoiEngine:
    def __init__(self, canvas, nrOfDiscs, speed, moveCntDisplay=None):
        self.cv = canvas
        self.nrOfDiscs = nrOfDiscs
        self.moveDisplay = moveCntDisplay
        self.running = False
        self.moveCnt = 0
        self.discs = []
        self.towerA = Tower( 80, 190, 15)
        self.towerB = Tower(220, 190, 15)
        self.towerC = Tower(360, 190, 15)
        
    def hanoi(self, n, src, dest, temp):
        if n > 0:
            for x in self.hanoi(n-1, src, temp, dest): yield None
            yield self.move(src, dest)
            for x in self.hanoi(n-1, temp, dest, src): yield None

    def move(self, src_tower, dest_tower):
        self.moveCnt += 1
        self.moveDisplay(self.moveCnt)
        disc = src_tower.pop()
        x1, y1 = src_tower.top()
        x2, y2 = dest_tower.top()
        disc.move_to(x1,20, self.speed)
        disc.move_to(x2,20, self.speed)
        disc.move_to(x2,y2, self.speed)
        dest_tower.append(disc)
        
    def run(self):
        self.running = True
        try:
            while self.running:
                result = self.step()
            return result  # True iff done
        except StopIteration:  # game over
            return True

class Hanoi:
    def displayMove(self, move):   
        self.moveCntLbl.configure(text = "move:\n%d" % move)
    
    def adjust_nr_of_discs(self, e):
        self.hEngine.nrOfDiscs = self.discs.get()
        self.reset()

    def setState(self, STATE):
        self.state = STATE
        try:
            if STATE == "START":
                self.discs.configure(state=NORMAL)
                self.discs.configure(fg="black")
                self.discsLbl.configure(fg="black")
            elif STATE == "RUNNING":
                self.discs.configure(state=DISABLED)
                self.discs.configure(fg="gray70")
                self.discsLbl.configure(fg="gray70")
        except TclError:
            pass
                   
    def start(self):

        if self.state in ["START", "PAUSE"]:
            self.setState("RUNNING")            
            if self.hEngine.run():
                self.setState("DONE")
            else:
                self.setState("PAUSE")
        elif self.state == "RUNNING":
            self.setState("TIMEOUT")
            self.hEngine.stop()              
    def __init__(self, nrOfDiscs):
        root = Tk()                            
        root.title("")
        #root.protocol("WM_DELETE_WINDOW",root.quit) #counter productive here!?
        cv = Canvas(root,width=440,height=210, bg="gray90") 
        cv.pack()        
        fnt = ("Arial", 12, "bold")
        attrFrame = Frame(root) #contains scales to adjust game's attributes
        self.discsLbl = Label(attrFrame, width=7, height=2, font=fnt,
                              text="discs:\n")
        self.discs = Scale(attrFrame, from_=1, to_=10, orient=HORIZONTAL,
                           font=fnt, length=75, showvalue=1, repeatinterval=10,
                           command=self.adjust_nr_of_discs)
        self.discs.set(nrOfDiscs)
        self.tempoLbl = Label(attrFrame, width=8,  height=2, font=fnt,
                              text = "   speed:\n")
        self.tempo = Scale(attrFrame, from_=1, to_=10, orient=HORIZONTAL,
                           font=fnt, length=100, showvalue=1,repeatinterval=10,
                           command = self.adjust_speed)
        self.tempo.set(speed)
        self.moveCntLbl= Label(attrFrame, width=5, height=2, font=fnt,
                               padx=20, text=" move:\n0", anchor=CENTER)                        
        for widget in ( self.discsLbl, self.discs, self.tempoLbl, self.tempo,
                                                             self.moveCntLbl ):
            widget.pack(side=LEFT)
        attrFrame.pack(side=TOP)
        ctrlFrame = Frame(root)  
        self.startBtn = Button(ctrlFrame, width=11, text="start", font=fnt,
                               state = NORMAL,  padx=15, command = self.start)
        for widget in self.startBtn:
            widget.pack(side=LEFT)
        ctrlFrame.pack(side=TOP)
        peg1 = cv.create_rectangle(  75,  40,  85, 190, fill='black')
        peg2 = cv.create_rectangle( 215,  40, 225, 190, fill='black')
        peg3 = cv.create_rectangle( 355,  40, 365, 190, fill='black')
        floor = cv.create_rectangle( 10, 191, 430, 200, fill='black')
        self.hEngine = HanoiEngine(cv, nrOfDiscs, speed, self.displayMove)
        self.state = "START"
        root.mainloop()

if __name__  == "__main__":
    Hanoi(4,5)

