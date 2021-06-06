from sys import stdin

def findUnique(arr, n) :
    op = 0
    for i in arr:
        op = op ^ i
    return op
 
#main
t = int(input())
while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    ans = findUnique(arr, n)
    print(ans)
    
    t -= 1
