def printPairDiffK(l, k):
    d ={}
    for i in l:
        d[i] = d.get(i, 0) + 1
        
    count = 0
    for i in d.keys():
        if i == i+k:
            n = len(l)
            return (n*(n-1))//2
            
        else:
            if i+k in d:
                m = d[i]
                n = d[i+k]
                count += m*n
                d[i] = 0
    return count
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))
