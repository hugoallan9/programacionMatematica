#!/usr/bin/env python2.7
from tkinter import *
from turtle import *

setup(900, 800, 0, 0)
title("TORRES DE HANOI")


class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) 
        self.fillcolor(n/7., 0, 1-n/7.)
        self.st()

class Tower(list):
    
    def __init__(self, x):
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(250)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"enter")
    clear()
    try:
        hanoi(7, t1, t2, t3)
        write(" ",
              align="center", font=("Courier", 17, "bold"))
    except Terminator:
        pass  

def main():
    global t1, t2, t3
    ht(); penup(); goto(0, -225)   
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    
    for i in range(7,0,-1):
        t1.push(Disc(i))
    
    write("Barra espaciadora para iniciar el juego",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")
    listen()
    return "En proceso"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()
