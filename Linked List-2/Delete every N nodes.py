from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
    if N == 0:
        return head
    if  M == 0:
        return
    t1=head
    while True:
        c1=1
        c2=1
        while c1!=M and t1!=None:
            t1=t1.next
            c1=c1+1
        if t1 is None:
            return head
        t2=t1.next
        while c2!=N and t2!=None:
            t2=t2.next
            c2=c2+1
        if t2 is None:
            t1.next=None
            return head
        t2=t2.next
        t1.next=t2
        t1=t1.next
            

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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1
