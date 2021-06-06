#function definition

def equilibrium(n,arr):
    ls = 0
    rs = sum(arr[1:])
    ans = 0
    for i in range(1,n):
        ls = ls + arr[i-1]
        rs = rs - arr[i]
        if ls == rs:
            return i
    return -1
        

    

#main
t = int(input())
while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    ans = equilibrium(n,arr)
    print(ans)
    t=t-1
    
    
