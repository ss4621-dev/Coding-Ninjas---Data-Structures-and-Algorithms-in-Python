class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele= ele
        self.priority=priority
class PriorityQueue:
    def __init__(self):
        self.pq=[]
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty() is True:
            return None
        return self.pq[0].ele
    def __percolateUp(self):
        CI = self.getSize() -1
        while CI > 0:
            PI = (CI-1)//2
            if self.pq[CI].priority > self.pq[PI].priority:
                self.pq[PI],self.pq[CI] = self.pq[CI],self.pq[PI]
                CI = PI
            else:
                break
    def insert(self,ele,priority):
        pqn=PriorityQueueNode(ele,priority)
        self.pq.append(pqn)
        self.__percolateUp()
    def __percolateDown(self):
        PI= 0
        MI=PI
        while MI < self.getSize():
            LI = 2*MI+1
            RI=2*MI+2
            if LI < self.getSize() and RI < self.getSize():
                if self.pq[MI].priority < self.pq[LI].priority > self.pq[RI].priority:
                    self.pq[MI],self.pq[LI] = self.pq[LI],self.pq[MI]
                    MI=LI
                else:
                    self.pq[MI],self.pq[RI] = self.pq[RI],self.pq[MI]
                    MI=RI
            elif LI < self.getSize() and  self.pq[MI].priority < self.pq[LI].priority:
                self.pq[MI],self.pq[LI] = self.pq[LI],self.pq[MI]
                MI=LI
            else:
                break
                
                    
        
    def removeMax(self):
        temp=self.pq[0].ele
        self.pq[0]= self.pq[self.getSize() -1]
        self.pq.pop()
        self.__percolateDown()
        return temp
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
        
    
