## Read input as specified in the question.
## Print output as specified in the question.
def lastIndex(arr, x, si):
    l = len(arr)
    if si == l:
        return -1
    
    smallerListOutput = lastIndex(arr, x, si + 1)
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if arr[si] == x:
            return si
        else:
            return -1

from sys import setrecursionlimit
setrecursionlimit(100000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr, x, 0))
