from sys import stdin


def intersection(arr1, arr2, n, m) :
    arr1.sort()
    arr2.sort()
    
    n = 0
    m = 0
    
    while n < len(arr1) and m < len(arr2):
        if arr1[n] == arr2[m]:
            print(arr1[n], end = ' ')
            n = n + 1
            m = m + 1
        
        elif arr1[n] > arr2[m]:
            m = m + 1
        
        elif arr1[n] < arr2[m]:
            n = n + 1
            
        




























# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1
