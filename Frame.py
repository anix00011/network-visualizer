import sys
from datetime import datetime

class Frame:
    def __init__(self):
        pass

    def TCPSend(self,framex):
        #Swap destination and source address
        framex["frame"][4]=framex["frame"]["Destination"]
        framex["frame"]["Destination"]=framex["frame"]["Source"]
        framex["frame"]["Source"]=framex["frame"][4]
        del framex["frame"][4]
        return framex["frame"]
        f = open("SentMsg.txt","w")
        f.write(str(framex["frame"]))

    def TCPRecv(self,framex):
        f = open("log.txt","w")
        f.write(str(framex))
        f.close()
        f = open("")
        f = open("RecvdMsg.txt","w")
        f.write(str(framex["frame"]))
        f.close()
        TCPSend(framex)
        return framex

    def UDPRecv(self,framex):
        f = open("log.txt","w")
        f.write(str(framex))
        f.close()

    def STPRecv(self,framex):
        f = open("log.txt","w")
        f.write(str(framex))
        f.close()
        f = open("RecvdMsg.txt","w")
        f.write(str(framex["frame"]))
        f.close()

    def ICMPSend(self,framex):
        framex["frame"][4]=framex["frame"]["Destination"]
        framex["frame"]["Destination"]=framex["frame"]["Source"]
        framex["frame"]["Source"]=framex["frame"][4]
        del framex["frame"][4]
        return framex["frame"]
        f = open("SentMsg.txt","w")
        f.write(str(framex["frame"]))

    def ICMPRecv(self,framex):
        f = open("log.txt","w")
        f.write(str(framex))
        f.close()
        f = open("RecvdMsg.txt","w")
        f.write(str(framex["frame"]))
        f.close()
        ICMPSend(framex)

    def processFrame(self):
        """Frame=[{"Protocol":{"TCP":1,"UDP":0,"STP":0,"ICMP":0},"frame":{"Destination":"","Source": "","Message":""}},
        {"Protocol":{"TCP":0,"UDP":1,"STP":0,"ICMP":0},"Destination":"","Source": "","Message":""},
        {"Protocol":{"TCP":0,"UDP":0,"STP":1,"ICMP":0},"Root":"","SourceBridge":"","Distance":""},
        {"Protocol":{"TCP":0,"UDP":0,"STP":0,"ICMP":1},"Destination":"","Source": "","Hop":""}]"""

        fname=""
        for j,k in Frame["Protocol"].items():
            if k==1:
                fname=j
                break
        getattr(sys.modules[__name__], "%sFunc"%fname)(i["frame"])

    FRAME_TO_Send=[]
    
    DATA_FRAME={"type":"data","Destination":"","Source": "","Message":""}
    CONFIG_FRAME={"type":"config","Root":"","SourceBridge":"","Distance":""}
    PING_FRAME={"type":"ICMP","Destination":"","Source": "","Hop":""}
    TERMINATE_NETWORK = False 

    def SwitchSend(self,framex):
        f = open("RoutingTable"+str(i)+".txt\n","r+")
        linestoken=f.readlines()
        token=1
        result=[]
        for x in linestoken:
            result.append(x.split()[token])
        if framex["frame"]["Destination"] not in result:
            f.write=framex["frame"]["Destination"]
        f.close()
        return framex

    def SwitchRecv(self,framex):
        hop,a =int();
        hop = hop +1
        framex["frame"]["hop"]=hop
        f = open("RoutingTable"+str(i)+".txt\n","r+")
        #First bit will be host name followed by hop count
        linestoken=f.readlines()
        token=1
        result=[]
        for x in linestoken:
            result.append(x.split()[token])
        if framex["frame"]["Source"] not in result:
            f.write=framex["frame"]["Source"]
            f.write=framex["frame"]["hop"]
        f.close()
        SwitchSend(framex)
        return framex


    DATA_FRAME={"Protcol":{"TCP":1, "UDP":0, "ICMP":0, "STP":0},"Destination":"","Source": "","Message":""}
    STP_FRAME={"Protcol":{"TCP":0, "UDP":0, "ICMP":0, "STP":1},"Root":"","SourceBridge":"","Distance":""}
    PING_FRAME={"Protcol":{"TCP":0, "UDP":0, "ICMP":1, "STP":0},"Destination":"","Source": "","Hop":""}
    UDP_FRAME={"Protocol":{"TCP":0, "UDP":1, "ICMP":0, "STP":0}, "Desination":"", "Source": "", "Message":""}
    TERMINATE_NETWORK = False 

    fname=""
    for j,k in Frame["Protocol"].items():
        if k==1:
            fname=j
            break
    getattr(sys.modules[__name__], "%sRecv"%fname)(i["frame"])
