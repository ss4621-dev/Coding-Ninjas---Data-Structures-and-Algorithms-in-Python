from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

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

def reverse(head):
    if head is None or head.next is None:
        smallhead = head
        tail = head
        return smallhead, tail
    smallhead, tail = reverse(head.next)
    tail.next = head
    tail = tail.next
    tail.next = None
    
    return smallhead, tail

    

def kReverse(head, k) :
	#Your code goes here
    #base case
    if k < 1:
        return head
    
    if k == llength(head):
        bh,bt = reverse(head)
        return bh
    
    if llength(head) < k:
        bh, bt = reverse(head)
        return bh
    
    i = 1
    h1 = head
    t1 = head
    while i < k:
        t1 = t1.next
        i+=1
        
    h2 = kReverse(t1.next, k)
    t1.next = None
    h3,t3 = reverse(h1)
    t3.next = h2
    
    return h3
    

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
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1
