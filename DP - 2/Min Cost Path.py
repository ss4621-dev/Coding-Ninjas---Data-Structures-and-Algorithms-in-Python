from sys import stdin

def lis(li,n): 
    dp = [[0 for j in range(2)] for i in range(n+1)]
    
    for i in range(n-1, -1, -1):
        
        including_max = 1
        for j in range(i+1, n):
            if li[j] > li[i]:
                including_max = max(including_max, 1+dp[j][0])
        dp[i][0] = including_max
        excluding_max = dp[i+1][1]
        overallMax = max(including_max,excluding_max)
        dp[i][1] = overallMax
        
    return dp[0][1]

 

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    li=list(map(int,stdin.readline().strip().split( )))
    return li,n
    

li,n=takeInput()
print(lis(li,n))
