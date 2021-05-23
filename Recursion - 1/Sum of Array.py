def sumArray(arr,n):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        return arr[0] + sumArray(arr[1:], n)
    
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr,n))
