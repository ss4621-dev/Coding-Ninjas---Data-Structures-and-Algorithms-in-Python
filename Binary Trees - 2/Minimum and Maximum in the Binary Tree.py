import sys
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 9)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#Representation of the Pair Class
class Pair :

    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum



def getMinAndMaxHelper(root) :
    #Your code goes here
    #Base Case
    if root is None:
        return 2147483647,-2147483648

    
    leftMin,leftMax = getMinAndMaxHelper(root.left)
    rightMin, rightMax = getMinAndMaxHelper(root.right)
    
    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    
    return minimum, maximum

def getMinAndMax(root):
    p = Pair(None, None)
    p.minimum, p.maximum = getMinAndMaxHelper(root)
    
    return p

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
pair = getMinAndMax(root)
print(str(str(pair.minimum) + " " + str(pair.maximum)))
