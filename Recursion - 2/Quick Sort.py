def partition(arr, start, end):
    pivot = arr[start]
    c = 0
    for i in range(start, end + 1):
        if arr[i] < pivot:
            c = c + 1
    arr[start + c], arr[start] = arr[start], arr[start + c]
    pivot_index = start + c
    i = start
    j = end
    while i < j:
        if arr[i] < pivot:
            i = i + 1
        elif arr[j] >= pivot:
            j = j - 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1
    return pivot_index



def quickSort(arr, start, end):
    if start >= end:
        return
    pivot_index = partition(arr, start, end)
    quickSort(arr, start, pivot_index - 1)
    quickSort(arr, pivot_index + 1, end)


            

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, len(arr) - 1)
print(*arr)
