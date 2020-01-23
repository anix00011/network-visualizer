import random
from queue import Queue
from MPort import Port
import multiprocessing
from Link import Link


def initializeSwitch():
	pass
localIP     = "127.0.0.1"
localPort   = random.randint(25000,30000)
bufferSize  = 1024


INITIAL_CONFIG_MESSAGE={"type":"BPDU","Root":SWITCH_ID,"Source":SWITCH_ID,"Distance":0}
FRAME_TO_Send=[];
DATA_FRAME={"type":"data","Destination":"","Source": "","Message":""}
CONFIG_FRAME={"type":"config","Root":"","SourceBridge":"","Distance":""}
TERMINATE_NETWORK = False 

PORT_CONNECTION=[]
FORWARDING_TABLE=[]


class Switch(Port):
	SWITCH_ID=random.randint(1,1000);
	Switch_Name=""
	Port_Status=["B","B","B","B","B","B","B","B"]

	a=random.randint(0,255)
	b=random.randint(0,255)
	c=random.randint(0,255)
	d=random.randint(0,255)
	e=random.randint(0,255)
	f=random.randint(0,255)
	link = Link()

	Ports=[]
	Port1=int()
	Port2=int()
	Port3=int()
	Port4=int()
	Port5=int()
	Port6=int()
	Port7=int()
	Port8=int()

	P1Q=Queue(4)
	P2Q=Queue(4)
	P3Q=Queue(4)
	P4Q=Queue(4)
	P5Q=Queue(4)
	P6Q=Queue(4)
	P7Q=Queue(4)
	P8Q=Queue(4)
	

	toPort1,fromPort1=link.createLink()
	toPort2,fromPort2=link.createLink()
	toPort3,fromPort3=link.createLink()
	toPort4,fromPort4=link.createLink()
	toPort5,fromPort5=link.createLink()
	toPort6,fromPort6=link.createLink()
	toPort7,fromPort7=link.createLink()
	toPort8,fromPort8=link.createLink()

	PortWriteQueue=Queue()
	switchQueue1=Queue()
	switchQueue2=Queue()
	switchQueue3=Queue()
	switchQueue4=Queue()
	switchQueue5=Queue()
	switchQueue6=Queue()
	switchQueue7=Queue()
	switchQueue8=Queue()

	MAC_ADDRESS=[a,b,c,d,e,f]

	def __init__(self,Switch_Queue,state,name):
		print("Switch is Live")
		self.state = state
		self.Switch_Name=name
		
		self.switchQueue=Switch_Queue
        readQueue= Queue()
        Read = multiprocessing.Process(target = Read, args =(readQueue, ))
        Write = multiprocessing.Process(target = Write, args =(readQueue, ))
        Read.start() 
        Write.start()

	
	def Write(self,in_q):
		while True:
			if in_q.empty() == 0:
				pass
			data = in_q.get()
			msgFromServer=input(":")

	def Read(self,out_q): 
		while True:
			processFrame(message)

	def toSwitchPipe(self):
		return [(self.toPort1,1),(self.toPort2,2),(self.toPort3,3),(self.toPort4,4),(self.toPort5,5),(self.toPort6,6),(self.toPort7,7)(self.toPort8,8)]

	def initializePorts(self):
		self.Port1=Port(switchQueue1,"Disabled",1,Switch_Name,toPort1)
		self.Port2=Port(switchQueue2,"Disabled",2,Switch_Name,toPort1)
		self.Port3=Port(switchQueue3,"Disabled",3,Switch_Name,toPort1)
		self.Port4=Port(switchQueue4,"Disabled",4,Switch_Name,toPort1)
		self.Port5=Port(switchQueue5,"Disabled",5,Switch_Name,toPort1)
		self.Port6=Port(switchQueue6,"Disabled",6,Switch_Name,toPort1)
		self.Port7=Port(switchQueue7,"Disabled",7,Switch_Name,toPort1)
		self.Port8=Port(switchQueue8,"Disabled",8,Switch_Name,toPort1)
		self.Ports=[self.Port1,self.Port2,self.Port3,self.Port4,self.Port5,self.Port6,self.Port7,self.Port8]