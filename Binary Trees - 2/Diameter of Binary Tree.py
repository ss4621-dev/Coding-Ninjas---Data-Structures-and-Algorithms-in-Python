from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def diameterOfBinaryTree(root) :
    # Your code goes here
    ''''if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    ldiameter = diameterOfBinaryTree(root.left)
    rdiameter = diameterOfBinaryTree(root.right)
    
    return max((lheight + rheight + 1), ldiameter, rdiameter)'''

    if root is None:
        return 0,0
    LH, LD = diameterOfBinaryTree(root.left)
    RH, RD = diameterOfBinaryTree(root.right)
    H = max(LH,RH) + 1
    D = max((LH + RH + 1),LD,RD)
    
    return H,D





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
    if root==None:
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

print(diameterOfBinaryTree(root)[1])
