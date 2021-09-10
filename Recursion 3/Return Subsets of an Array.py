## Read input as specified in the question.
## Print output as specified in the question.
def subset(arr):
    #base case
    if len(arr)==0:
        return ['']
    
    ans=subset(arr[1:])
    l=len(ans)
    for i in range(0,l):
        ans.append(arr[0]+' '+ans[i])
    return ans


#main
n=int(input())
arr=[i for i in input().split()]
result=subset(arr)
for j in result:
    print(j)
