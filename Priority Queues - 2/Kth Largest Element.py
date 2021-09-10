import heapq
def kthLargest(lst, k):
    i = 0
    ans = 0
    heapq._heapify_max(lst)
    while i < k:
        ans = heapq._heappop_max(lst)
        i = i + 1
    return ans


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
