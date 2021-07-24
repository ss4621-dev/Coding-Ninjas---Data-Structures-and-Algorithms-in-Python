def subsetSum(l):
    d = {0:0}
    sum = 0
    maxSize = 0
    for i in range(len(l)):
        sum = sum + l[i]
        if sum not in d:
            d[sum] = i+1
        
        else:
            size = i - d[sum] + 1
            if size > maxSize:
                maxSize = size
    return maxSize


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))
