from queue import Queue
import multiprocessing
class Link:
    def __init__(self,type):
        self.type = type
        if(self.type == "FE"):
            self.delay = 1;
        elif(self.type == "NE"):
            self.delay = 10;
        
    def createLink(self):
        End1,End2 = multiprocessing.Pipe(True);
        return (End1,End2);
