
from queue import Queue
import heapq

def buyTicket(arr, k):
    count=0
    d={}           
    q=Queue()
    for i in range(0, len(arr)):
        q.put(i)
        d[i]=arr[i]
        
    heapq._heapify_max(arr)
    pq=arr
    while q.empty()==False:
        curr=q.get()
        if curr==k:
            if d[curr]== pq[0]:
                count+=1
                return count
            q.put(curr)
        else:
            if d[curr]==pq[0]:
                count+=1
                heapq._heappop_max(pq)
            else:
                q.put(curr)
                
    return count

#main
n=int(input())
arr = [int(i) for i in input().split()]
k=int(input())
print(buyTicket(arr, k))
