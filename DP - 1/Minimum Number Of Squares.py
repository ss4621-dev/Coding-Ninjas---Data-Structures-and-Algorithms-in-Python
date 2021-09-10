import sys, math
from sys import setrecursionlimit
setrecursionlimit(10**4)
def minSquares(n):
    dp = [None]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4,n+1):
        root = int(math.sqrt(i))
        ans = sys.maxsize
        for j in range(1,root+1):
            ans = min(ans,dp[i-(j**2)])
        dp[i] = 1 + ans
    return dp[n]
        
            

        

    
n = int(input())
ans = minSquares(n)
print(ans)
