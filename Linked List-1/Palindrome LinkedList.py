
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def llength(head):
    c = 0
    while head is not None:
        head=head.next
        c+=1
        
    return c

def reversell(head):
    if head is None or head.next is None:
        return head
    newHead = reversell(head.next)
    head.next.next = head
    head.next = None
    return newHead

def isPalindrome(head) :
    if head is None or llength(head) == 1:
        return True
    #Your code goes here
    l = llength(head)
    m = l//2
    firstHead = head
    
    if l %2 == 0:
        i = 0
        while i < m-1:
            head = head.next
            i+=1
        secondHead = head.next
        head.next = None
        
            
    else:
        j = 0
        while j < m:
            head = head.next
            j+=1
        secondHead = head.next.next
        head.next = None
        
    newHead = reversell(secondHead)  
    
    while firstHead is not None and newHead is not None:
        if firstHead.data == newHead.data:
            firstHead = firstHead.next
            newHead = newHead.next
        else:
            return False
    
    return True
        
    

































#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1
