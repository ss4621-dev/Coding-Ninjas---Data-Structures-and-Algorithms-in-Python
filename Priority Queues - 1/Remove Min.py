class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
        
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
    def __percolateDown(self):
        parentIndex=0
        while 2*parentIndex+1 <self.getSize() or 2*parentIndex+2<self.getSize():
            lChild=2*parentIndex+1
            rChild=2*parentIndex+2
            if lChild>=self.getSize():
                min=rChild
            elif rChild>=self.getSize():
                min=lChild
            else:
                min=lChild if self.pq[lChild].priority<self.pq[rChild].priority else rChild
            if self.pq[min].priority<self.pq[parentIndex].priority:
                self.pq[min],self.pq[parentIndex]=self.pq[parentIndex],self.pq[min]
                parentIndex=min
            else:
                break
                
        
    def removeMin(self):
        removed=self.pq[0].ele
        self.pq[0]=self.pq[-1]
        self.pq.pop()
        self.__percolateDown()
        return removed
        
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
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
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
        
    
