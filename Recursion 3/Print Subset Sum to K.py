## Read input as specified in the question.
## Print output as specified in the question.
def subsetSum(arr,k,n,op):
    #base case
    if len(arr)==0:
        if k==0:
            print(*op)
        return
    
    newOp=[]
    newOp=newOp+op
    newOp.append(arr[0])
    subsetSum(arr[1:n],k-arr[0],n,newOp)
    subsetSum(arr[1:n],k,n,op)
    return
    
    
#main
n=int(input())
arr=[int(i) for i in input().split()]
k=int(input())
subsetSum(arr,k,n,[])
