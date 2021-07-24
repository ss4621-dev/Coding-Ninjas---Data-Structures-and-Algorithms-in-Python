from sys import stdin
def maxfreq(arr):
    d = {}
    max = -999999999
    ans = arr[0]
    for w in arr:
        d[w] = d.get(w, 0) + 1
    for i in arr:
        if d[i] > d[ans]:
            ans=i
    return ans
   
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))
