import random
from queue import Queue 
from threading import Thread
from Port import Port 
import multiprocessing
from Link import Link
from Frame import Frame


class Host():
	Host_name=""
	A=192
	B=168
	C=random.randint(0,255)
	D=random.randint(1,254)

	a=random.randint(0,255)
	b=random.randint(0,255)
	c=random.randint(0,255)
	d=random.randint(0,255)
	e=random.randint(0,255)
	f=random.randint(0,255)

	frame=Frame()

	IP_ADDRESS=[A,B,C,D]
	MAC_ADDRESS=[a,b,c,d,e,f]
	link=Link("FE")
	toPort,fromPort = link.createLink();

	def __init__(self):
		pass

	def __init__(self,Host_Queue,state,name):
		self.Host_name=name
		self.state = state
		self.hostQueue = Host_Queue
		self.readQueue= Queue()
		self.Port0=Port(hostQueue,"Blocked",0,self.name,self.toPort)
		readThread = Thread(target = Read, args =(self.hostQueue, ))
		readThread.start()
		

	def __del__(self):
		self.Read.join()
		self.Write.join()
		self.HostThread.join()

	def Write(self,in_q):
		while True:
			if in_q.empty() == 0:
				pass
			data = in_q.get()


	def Read(self,out_q): 
		while True:

			P.processFrame(message)
	
	def toHostPipe(self):
		return (self.toPort,0)

	def Ping(self,IP_ADDRESS):
		self.HostThread.start()
		for i in range(4):
			createICMP_frame(IP_ADDRESS)


