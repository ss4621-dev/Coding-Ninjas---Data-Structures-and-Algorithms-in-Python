## Read input as specified in the question.
## Print output as specified in the question.
def subSets(arr,op,n):
    if len(arr) == 0:
        print(op)
        return

    subSets(arr[1:], op,n)
    subSets(arr[1:], op+str(arr[0])+" "  ,n)


#main
n = int(input())
arr = [i for i in input().split()]
subSets(arr, '', n)
