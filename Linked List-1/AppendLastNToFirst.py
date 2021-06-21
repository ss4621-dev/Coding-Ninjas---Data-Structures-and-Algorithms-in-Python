
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def llength(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count

def appendLastNToFirst(head, n) :
    #Your code goes here
    if n == 0:
        return head
    if head is None:
        return
    prevHead = head
    len = llength(head)
    rem = len - n
    curr = head
    prev = None
    i = 0
    
    while i < rem:
        prev = curr
        curr=curr.next
        i=i+1
        
    prev.next=None
    newHead=curr
    
    while curr.next is not None:
        curr=curr.next
        
    curr.next=prevHead
    
    return newHead














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
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 
