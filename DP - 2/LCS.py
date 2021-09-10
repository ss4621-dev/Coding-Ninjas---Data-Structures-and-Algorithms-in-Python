
from sys import stdin

def lcs(s, t) :
    n = len(s)
    m = len(t)
    
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
    return dp[0][0]

#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))
