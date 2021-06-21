from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(Head, i, j) :
    #Your code goes here
    m = 0
    n = 0
    p1 = None
    p2 = None
    c1 = Head
    c2 = Head
    
    while m < i:
        p1 = c1
        c1 = c1.next
        m+=1
        
    while n < j:
        p2 = c2
        c2 = c2.next
        n+=1
        
    if (j - i)**2 == 1:
        p1.next = c2
        temp = c2.next
        c2.next = c1
        c1.next = temp
    else:
        t1 = c1.next
        t2 = c2.next
        p1.next = c2
        c2.next = t1
        p2.next = c1
        c1.next = t2
    
    
    
    return head
    
        






























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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
