from sys import stdin

def longestConsecutiveSubsequence(arr,n):
    arr.sort()
    start = arr[0]
    end = arr[0]
    count = 1
    a1 = start
    a2 = end
    flag = True
    maxCount = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            count += 1
            end = arr[i]
        else:
            flag = False
            if count >= maxCount:
                a1 = start
                a2 = end
                maxCount = count
                
            start = arr[i]
            end = arr[i]
            count = 1
    if flag == True:
        return a1,a2
    return a1,a2
            
   
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans1, ans2 = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(ans1,ans2)
