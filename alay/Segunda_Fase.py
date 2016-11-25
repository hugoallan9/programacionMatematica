# -*- coding: utf-8 -*-
#!/usr/bin/python
import random, pdb, time
from Tkinter import *

global time_of_sleep;
time_of_sleep = 1; 

class visual_tower:
	def __init__(self,n,p0,p1,p2):
		self.myGui=Tk();
		self.myGui.title("Torres de Hanoi");
		self.p=[];
		self.p.append(p0);
		self.p.append(p1);
		self.p.append(p2);
		self.Frames=[];
		#self._n = self.p[0]._size+self.p[1]._size + self.p[2]._size + self.p[3]._size;
		self._n=n;
		for i in range(3):
			self.Frames.append(Frame(self.myGui,height=self._n*100,width=(self._n+1)*25));
			self.Frames[i].grid(row=0,column=i);
		self.showit();
		self.myGui.update();
		self.myGui.quit();
	def showit(self):
		w=range(self._n);
		for f in range(3):
			w_tmp = Canvas(self.Frames[f], width=(self._n)*25, height=26);
			w_tmp.grid(row=self._n,column=0,columnspan=(self._n+1));
			w_tmp.create_rectangle(0,0, self._n*25 ,10,fill="red");
			ff=[0 for i in range(self._n)];
			for i in range(0,self.p[f]._size):
				w[i] = Canvas(self.Frames[f], width=(self.p[f].stk[i])*25, height=26);
				w[i].grid(row=self._n-i-1,column=0,columnspan=(self._n-self.p[f].stk[i]+1));
				w[i].create_rectangle(0,0, self.p[f].stk[i]*25 ,25,fill="black");
			for i in range(self.p[f]._size,self._n):
				w[i] = Canvas(self.Frames[f], width=(self._n)*25, height=26);
				w[i].grid(row=self._n-i-1,column=0,columnspan=(self._n+1));
				w[i].create_rectangle(0,0, self._n*25 ,25,fill="white");
			
		self.myGui.update();
		if(self.p[2]._size == self._n and self.p[0]._size == 0 ):
			self.myGui.mainloop();

class stack:
	def __init__(self,size,name):
		self.name=name;
		self._size=size;
		self.stk=[];
		for i in range(self._size,0,-1):
			self.stk.append(i);
	def pop(self):
		if self._size > 0:
			_tmp=self.stk[ self._size-1 ];
			self.stk=self.stk[:self._size-1];
			self._size=self._size-1;
			return _tmp;
		else:
			return -1;
	def push(self,elem):
		if(self._size==0 or elem < self.stk[ self._size-1 ]):
			self.stk.append(elem);
			self._size=self._size+1;
		else :
			print "Esto no es valido"
	def printit(self):
		for i in range(self._size-1,-1,-1):
			print(self.stk[i]);

class hanoi:
	def __init__(self,n):
		self.n=n;
		self.p1=stack(self.n,name="peg1");
		self.p2=stack(self.n,name="peg2");
		self.p3=stack(self.n,name="peg3");
		self.vt=visual_tower(self.n,self.p1,self.p2,self.p3);
		while(self.p2.pop() !=-1):
			pass;
		while(self.p3.pop() !=-1):
			pass;
		self.displayit();
	def displayit(self):
		self.vt.showit();
		time.sleep(time_of_sleep);

		
def tower_of_hanoi(num_of_Disks, src,  inter1, dest):
	#pdb.set_trace();
	global H,time_of_sleep;
	time_of_sleep=1; # change it as per your convenience
	if(num_of_Disks %2 == 1 and num_of_Disks < 2):
		dest.push(src.pop());
		H.displayit();

	elif(num_of_Disks % 2==0 and num_of_Disks < 3):
		inter1.push(src.pop());
		H.displayit();
		dest.push(src.pop());
		H.displayit();
		dest.push(inter1.pop());
		H.displayit();
	else:
		tower_of_hanoi(num_of_Disks-1,src,dest,inter1);
		dest.push(src.pop());
		H.displayit();
		tower_of_hanoi(num_of_Disks-1,inter1,src,dest);



def main():
	n=input("Numero de discos: "); # no. of disks
	global H;
	H = hanoi(n);
	tower_of_hanoi(n,H.p1,H.p2,H.p3);

def TOI(N):
	global H;
	H = hanoi(N); # creating object of hanoi class :)
	tower_of_hanoi(N,H.p1,H.p2,H.p3);
	
if __name__=="__main__":main();

