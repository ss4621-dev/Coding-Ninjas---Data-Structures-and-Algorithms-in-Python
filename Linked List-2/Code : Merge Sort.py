from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
def llength(head):
    i = 0
    while head is not None:
        head = head.next
        i+=1  
    return i
        
def midPoint(head) :
    if head is None:
        return
    fast = head
    slow = head
    while slow.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast.next is None:
            break
    return slow

def split(head):
    l = llength(head)
    m = l//2
    i = 0
    h1 = head
    prev = None
    while i < m:
        prev = head
        head = head.next
        i+=1
    prev.next = None
    h2 = head
    return h1,h2
        

def merge(head1, head2):
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    # Write your code here
    fh = None
    ft = None
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:

            if fh is None:
                fh = head1
                ft = head1
            else:
                ft.next = head1
                ft = ft.next
            head1 = head1.next

        else:
            if fh is None:
                fh = head2
                ft = head2
            else:
                ft.next = head2
                ft = ft.next
            head2 = head2.next

    if head1 is not None:
        ft.next = head1
    else:
        ft.next = head2

    return fh

def mergeSort(head):
    #base case
    if head is None or head.next is None:
        return head
    
    l1,l2 = split(head)
    sl1 = mergeSort(l1)
    sl2 = mergeSort(l2)
    ul = merge(sl1,sl2)
    return ul
    




























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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
