from sys import setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(tree):
    if tree==None:
        return 
    node=tree
    maxSum=tree.data
    for child in  tree.children:
        maxSum=maxSum+child.data
    for child in tree.children:
        childMaxSum,childNode=maxSumNode(child)
        if childMaxSum>maxSum:
            maxSum=childMaxSum
            node=childNode
    return maxSum, node

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
tempsum, temp = maxSumNode(tree)
print(temp.data)
