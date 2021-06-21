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
        

def bubbleSort(head) :
	#Your code goes here
     l=llength(head)
     for i in range(l-1):
        p=None
        i=head
        j=head.next
        while j is not None:
            if i.data<j.data:
                p=i
                i=i.next
                j=j.next
            else:
                if p is None:
                    i.next=j.next
                    j.next=i
                    head=j
                    p=j
                    j=i.next
                else:    
                    p.next=j
                    i.next=j.next
                    j.next=i
                    j=i.next
                    p=p.next
     return head



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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
