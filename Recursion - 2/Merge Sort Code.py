def merge(a, a1, a2):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            k = k + 1
            i = i + 1
        else:
            a[k] = a2[j]
            k = k + 1
            j = j + 1
        
    while i < len(a1):
        a[k] = a1[i]
        k = k + 1
        i = i + 1
            
    while j < len(a2):
        a[k] = a2[j]
        k = k + 1
        j = j + 1
            
def mergeSort(a):
    if len(a) == 0 or len(a) == 1:
        return
    mid = len(a) // 2
    
    a1 = a[:mid]
    a2 = a[mid:]
    
    mergeSort(a1)
    mergeSort(a2)
    
    merge(a, a1, a2)

n = int(input())
a = [int(i) for i in input().split()]
mergeSort(a)
print(*a)          
