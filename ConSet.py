
import threading
import time

class ConSet:
    def __init__(self):
        self.set={}
        self.lock=threading.Lock()
    
    def insert(self,elt):
        self.lock.acquire(blocking=True)
        if elt in self.set:
            print("Adding")
            self.set[elt]=True
            self.lock.release()
        else:
            print("Adding")
            self.set[elt]=True
            self.lock.release()

    def printDictionary(self):
        self.lock.acquire(blocking=True)
        print(self.set)
        self.lock.release()

    def pop(self):
        check=False
        while check==False:
            for key in self.set:
                print("Searching")
                if self.set[key]==True:
                    self.lock.acquire(blocking=True)
                    print("Found One")
                    check=True
        for key, value in self.set.items():
            if(value==True):
                print("Realeasing from search")
                self.set[key]=False
                self.lock.release()
                return key





###Test
ch=ConSet()   
t1 = threading.Thread(target=ch.pop)
t1.start()


t2 = threading.Thread(target=ch.insert, args=(3,))

t2.start()

t1.join()

t2.join()

ch.printDictionary()





        