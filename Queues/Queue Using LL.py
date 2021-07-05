
from sys import stdin


#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.__LL = []
        self.__count = 0
        self.__head = None
        self.__tail = None
        
    



    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self) :
        #Implement the getSize() function
        return self.__count



    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.__count == 0



    def enqueue(self, data) :
        #Implement the enqueue(element) function
        if self.__head is None:
            newNode = Node(data)
            self.__head = newNode
            self.__tail = newNode
            self.__count += 1
        
        else:
            newNode = Node(data)
            self.__tail.next = newNode
            self.__count += 1
            self.__tail = self.__tail.next
            



    def dequeue(self) :
        #Implement the dequeue() function
        if self.__count == 0:
            return -1
        
        element = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return element



    def front(self) :
        #Implement the front() function
        if self.__count == 0:
            return -1
        
        return self.__head.data
        




#main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
