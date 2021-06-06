from sys import stdin


def findDuplicate(arr, n) :
    s = sum(arr)
    p = 0
    for i in range(0, n-1):
        p = p + i
    
    return s-p
    



#main
t = int(input())
while t > 0:
    n = int(input())
    arr = [ int(i) for i in input().split()]
    ans = findDuplicate(arr, n)
    print(ans)
    t -= 1
