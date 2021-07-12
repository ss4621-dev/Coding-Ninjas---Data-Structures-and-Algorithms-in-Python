from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    # Your code goes here
    q=queue.Queue()
    q.put(root)
    while q.empty() is False:
        currNode=q.get()
        if currNode.left is None and currNode.right is None:
            print(currNode.data,':','L',':','-1',',','R',':','-1',sep='')
        elif currNode.left is None:
            print(currNode.data,':','L',':','-1',',','R',':',currNode.right.data,sep='')
            q.put(currNode.right)
        elif currNode.right is None:
            print(currNode.data,':','L',':',currNode.left.data,',','R',':','-1',sep='')
            q.put(currNode.left)
        else:
            print(currNode.data,':','L',':',currNode.left.data,',','R',':',currNode.right.data,sep='')
            q.put(currNode.left)
            q.put(currNode.right)
            


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


# Main
root = takeInput()
printLevelWise(root)
