import threading
import time
import random
import operator
Mailboxes=[]
NodeList=[]
Number_of_election=0
##conset
class ConSet:
    def __init__(self):
        self.set={}
        self.lock=threading.Lock()
    
    def insert(self,elt,vote):
        self.lock.acquire(blocking=True)
        
        if elt in self.set:
            self.set[elt]=vote
            self.lock.release()
        else:
            self.set[elt]=vote
            self.lock.release()

    def printConSet(self):
        self.lock.acquire(blocking=True)
        print(self.set)
        self.lock.release()

class Election:
    def __init__(self,Votes):
        self.lock=threading.Lock()
        self.post=Votes
        global Number_of_election
        self.id=Number_of_election
    
    def getVotes(self):
        self.lock.acquire(blocking=True)
        self.post.printConSet()
        self.lock.release()
        






##Nodes
number_of_nodes=1

class Node:
    def __init__(self):
        global number_of_nodes
        global NodeList
        self.mail=[]
        self.identifier=0
        self.Leader=0
        global Mailboxes
        Mailboxes.append(self.mail)
        number_of_nodes+=1
        NodeList.append(self)
        self.lock=threading.Lock()

    def who_is_leader(self):          ### Function that shows who is the president of that spesific node
        self.lock.acquire(blocking=True)
        print("Im "+str(self.identifier)+" My president is "+str(self.Leader))
        self.lock.release()


    def LeaderCheck(self): ##Function that ask everybody for leader
        self.lock.acquire(blocking=True)
        for z in range(len(NodeList)):
            print("Im "+str(NodeList[z].identifier)+" My president is "+str(NodeList[z].Leader))
        self.lock.release()




    

    
    def nodeWork(self,identifier,number_of_nodes):
        
        self.lock.acquire(blocking=True)
        self.identifier=identifier
        global Mailboxes
        global Number_of_election
        winner=False
        while winner==False:
            Biggest_Vote=0
            Biggest_Key=0
            Tie_breaker=0
            Number_of_election+=1
            election_votes=ConSet()
            
            for x in range(len(NodeList)):
                vote=random.randint(1,(number_of_nodes*number_of_nodes))
                election_votes.insert(NodeList[x].identifier,vote)
                if vote>Biggest_Vote:
                    Tie_breaker=0
                    Biggest_Key=NodeList[x].identifier
                    Biggest_Vote=vote
                elif vote==Biggest_Vote:
                    Tie_breaker+=1
            total_election=Election(election_votes)
            print("This Election Votes is below")
            total_election.getVotes()
            if Tie_breaker==0:
                 for y in range(len(Mailboxes)):
                     Mailboxes[y].append(total_election)
                 for z in range(len(NodeList)):
                     NodeList[z].Leader=Biggest_Key
                 winner=True
                     
            else:
                print("ReElection Time!!!")    
        time.sleep(0.5)
        self.lock.release()










##Test 



new_node=Node()


t1 = threading.Thread(target=new_node.nodeWork,args=(2,2,))
new_node2=Node()
t1.start()
t2 = threading.Thread(target=new_node2.nodeWork,args=(4,3,))
t2.start()


t1.join()

t2.join()

t2 = threading.Thread(target=new_node2.LeaderCheck,args=())
t2.start()
t2.join()





###



#




