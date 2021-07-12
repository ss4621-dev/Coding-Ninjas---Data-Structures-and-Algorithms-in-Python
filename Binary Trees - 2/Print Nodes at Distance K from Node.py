from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printAtDepthK(root,k):
    if root is None:
        return
    if k==0:
        print(root.data)
        return
    printAtDepthK(root.left,k-1)
    printAtDepthK(root.right,k-1)
    
    
def nodesAtDistanceK(root, node, k) :
	#Your code goes here
    if root is None:
        return -1
    if root.data==node:
        printAtDepthK(root,k)
        return 0
    lD=nodesAtDistanceK(root.left,node,k)
    if lD!=-1:
        distanceLeft=lD+1
        if k==distanceLeft:
            print(root.data)
            return distanceLeft
        else:
            rightDepth=k-distanceLeft-1
            printAtDepthK(root.right,rightDepth)
            return distanceLeft
    rD=nodesAtDistanceK(root.right,node,k)
    if rD != -1:
        distanceRight = rD + 1
        if k == distanceRight:
            print(root.data)
            return distanceRight
        else:
            leftDepth = k - distanceRight - 1
            printAtDepthK(root.left, leftDepth)
            return distanceRight
    if lD==-1 and rD==-1:
        return -1


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k)
