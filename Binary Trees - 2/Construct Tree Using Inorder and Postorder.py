from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTreePostOrder(postOrder, inOrder, n) :
	#Your code goes here
     if len(postOrder)==0 or len(inOrder)==0:
        return 
     rootData=postOrder[-1]
     root=BinaryTreeNode(rootData)
     for i in range(len(inOrder)):
        if inOrder[i]==rootData:
            rootIndexInOrder=i
            break
     lenLeftSubTree=rootIndexInOrder
     leftInOrder=inOrder[0:lenLeftSubTree]
     rightInOrder=inOrder[lenLeftSubTree+1:]
     leftPostOrder=postOrder[0:lenLeftSubTree]
     rightPostOrder=postOrder[lenLeftSubTree:-1]
     leftSubTree=buildTreePostOrder(leftPostOrder, leftInOrder, n)
     rightSubTree=buildTreePostOrder(rightPostOrder, rightInOrder, n)
     root.left=leftSubTree
     root.right=rightSubTree
     return root




'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTreePostOrder(postOrder, inOrder, n)
printLevelWise(root)
