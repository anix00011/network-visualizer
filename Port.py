import multiprocessing
from threading import Thread
from queue import Queue
from Link import Link

class Port:
	Machine_name= ""
	WriteQueue=Queue()

	def __init__(self,Machine_Queue,state,portNo,name,link):
		self.portNo= portNo
		self.Machine_name = name
		self.recieveLink=link
		self.state = state
		self.M_Queue = Machine_Queue
		self.readQueue=Queue();

		Read = multiprocessing.Process(target = Read, args =(self.M_Queue,self.recieveLink))		
		Read.start()
	
	def __del__(self):
		self.Read.join()
		self.Write.join()
	
	def frameFromMachine(self,frame):
		self.readQueue.put(frame)


	def Write(self,in_q,writeLink):
		while True:
			if in_q.empty() == 0:
				continue
			data = in_q.get()
			writeLink.send(data)

	def Read(self,out_q,recieveLink): 
		while True: 
			frame = recieveLink.recv()
			processFrame(frame)
	

	def connectSendLink(self,link):
		Write = Thread(target = Write, args =(readQueue,link,))
		Write.start()


