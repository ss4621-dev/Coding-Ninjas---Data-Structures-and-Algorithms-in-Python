
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
    
def lengthLL(head):
    if head is None:
        return 0
    count = 1
    while head is not None:
        head = head.next
        count = count + 1
    return count




def printIthNode(head, i):
    if head is None:
        return ''
    if i >= lengthLL(head) or i < 0:
        return ''
    count = 0
    while count != i:
        count += 1
        head = head.next
        
    return head.data
    
        
    


























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
    i = int(stdin.readline().rstrip())
    print(printIthNode(head, i))

    t -= 1
