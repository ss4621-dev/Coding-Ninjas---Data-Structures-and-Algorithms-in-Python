import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def elementsInRangeK1K2(root, k1, k2, l):
    if root==None:
        return
    if k2<root.data:
        elementsInRangeK1K2(root.left, k1, k2, l)
    elif k1>root.data:
        elementsInRangeK1K2(root.right, k1, k2, l)
    else:
        l.append(root.data)
        elementsInRangeK1K2(root.left, k1, k2, l)
        elementsInRangeK1K2(root.right, k1, k2, l) 
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k1, k2 = (int(i) for i in input().strip().split())
l=[]
elementsInRangeK1K2(root, k1, k2, l)
l=sorted(l)
print(*l)
