def checkNumber(arr, x):
    if x in arr:
        return True
    else:
        return False
    
    smallernumber = arr[1:]
    checksmallernumber = checkNumber(smallernumber)
    return checksmallernumber
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
