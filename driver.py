from Host import Host
from Switch import Switch

from queue import Queue 
from threading import Thread 

VISUALIZER = True

HOSTS=[]
SWITCHES=[]
NETWORK=[]
LINKS=[]
NETWORK_Connection_Register = [[],[]]

while VISUALIZER == True:
    print("Welcome to Network Visualizer")
    print("Please follow the instruction for Visualizer to work properly")
    while True:
        print("Enter \n1 to Add new component to the network")
        print("2 to Modify Network")
        print("3 to Run Simulation ")
        print("4 to save and Terminate the Simulation")
        Input = int(input())
        if Input == 1:
            AddComponent()
        elif Input == 2:
            ModifyNetwork()
        elif Input == 3:
            Simulate()
        elif Input == 4:
            Save()
            break;
        else:
            print("Enter the correct choice");

def AddComponent():
    while True:
        print("Enter 1 to add Host to the Network")
        print("Enter 2 to add Switch to the network")
        print("Enter 3 to add connection")
        print("Enter 4 to return to the previous menu")
        Input=int(input())
        if Input == 1:
            addHost()
        elif Input == 2:
            addSwitch()
        elif Input == 3:
            addConnection()
        elif Input == 4:
            return
        else:
            print("Enter the correct choice")

def ModifyNetwork():
    while True:
        print("Enter 1 to Modify Host to the Network")
        print("Enter 2 to Modify Switch to the network")
        print("Enter 3 to Modify connection")
        print("Enter 4 to return to the previous menu")
        Input=int(input())
        if Input == 1:
            ModifyHost()
        elif Input == 2:
            ModifySwitch()
        elif Input == 3:
            ModifyConnection()
        elif Input == 4:
            return
        else:
            print("Enter the correct choice")

def Simulate():
    while True:
        print("Enter 1 to Ping in the Network")
        print("Enter 2 to see forwarding table of the Switch in the network")
        print("Enter 3 send message from one host to another")
        print("Enter 4 to return to the previous menu")
        Input=int(input())
        if Input == 1:
            Ping()
        elif Input == 2:
            FTable()
        elif Input == 3:
            Message()
        elif Input == 4:
            return
        else:
            print("Enter the correct choice")

def Save():
    pass

def addHost():
    hostQueue = Queue()
    name=input("Enter the name of the host in Single Capital Letter");
    host = Host(hostQueue,"Active",name)
    toHostConnectionObject , portNo =host.toHostPipe()
    NETWORK_Connection_Register[0].append((name,host,toHostConnectionObject))

def addSwitch():
    SwitchQueue = Queue()
    name=input("Enter the name of the Switch in Single small Letter");
    switch = Switch(SwitchQueue,"Active",name)
    toSwitchConnectionObjects =switch.toHostPipe()
    NETWORK_Connection_Register[1].append((name,switch,toSwitchConnectionObjects))

def addConnection():
    while True:
        M1,M2=None
        M1Connection,M2Connection=None
        flag=0
        Machine1 = input("Enter name of Host machine : ")
        Machine2 = input("Enter name of Switch machine : ")
        for i in NETWORK_Connection_Register[0]:
            if i[0] == Machine1:
                M1 = i[1]
                M1Connection= i[2]
                flag=1
        if flag == 0:
            print("Enter the correct Host name ")
            continue;
        Machine2 = input("Enter name of Switch machine : ")
        Machine2Port= int(input("Enter the port number : "))
        for i in NETWORK_Connection_Register[1]:
            if i[0] == Machine2:
                M2 = i[1]
                M2Connection=i[2][Machine2Port]
                flag=0
        if flag == 1:
            print("Enter the correct Switch name or port Number ")
            continue;
        
        #Connect pass the connection object to each other
        M1.Port0.connectSendLink(M2Connection)
        Port="Port"+Machine2Port;
        M2.Port.connectSendLink(M1Connection)

        

def Ping():
    A,B,C,D = map(int,input.split("Enter the Destination  IP Address"))
    sender=input("Enter the name of the host : ")

