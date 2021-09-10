def checkMaxHeap(lst):
    parent = 0
    leftChild = 2*parent+1
    rightChild = 2*parent+2
    while leftChild < n:
        if lst[parent] < lst[leftChild]:
            return False
        elif rightChild < n and lst[parent] < lst[rightChild]:
            return False
        parent = parent + 1
        leftChild = 2*parent+1
        rightChild = 2*parent+2
    return True
    
    

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
