
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    # Your code goes here
    if inputQueue.qsize() == 1:
        return inputQueue
    
    temp = inputQueue.get()
    
    reverseQueue(inputQueue)
    inputQueue.put(temp)
    return inputQueue





'''-------------- Utility Functions --------------'''



def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1
