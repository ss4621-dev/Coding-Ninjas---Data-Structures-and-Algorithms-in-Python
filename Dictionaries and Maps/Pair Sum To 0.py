from sys import stdin

def pairSum0(l,n):
    # Write your code here
    d = {}
    for i in l:
        d[i] = d.get(i,0) + 1
        
    
    count = 0
    for j in d:
        if j == 0:
            k = d[j]
            count = count+(k*(k-1)//2)
            
        else:
            if -j in d:
                p = d[j]
                q = d[-j]
                count = count + (p*q)
                d[j] = 0
                d[-j] = 0
            
    return count
        
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))
