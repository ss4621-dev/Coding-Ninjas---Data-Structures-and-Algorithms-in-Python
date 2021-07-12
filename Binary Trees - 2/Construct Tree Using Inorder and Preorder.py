from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTreePreorder(preorder, inorder, n) :
	#Your code goes here
     if len(preorder)==0 or len(inorder)==0:
        return 
     rootData=preorder[0]
     root=BinaryTreeNode(rootData)
     for i in range(len(inorder)):
        if inorder[i]==rootData:
            rootIndexInorder=i
            break
     lenLeftSubTree=rootIndexInorder
     leftInorder=inorder[0:lenLeftSubTree]
     rightInorder=inorder[lenLeftSubTree+1:]
     leftPreorder=preorder[1:lenLeftSubTree+1]
     rightPreorder=preorder[lenLeftSubTree+1:]
     leftSubTree=buildTreePreorder(leftPreorder, leftInorder, n)
     rightSubTree=buildTreePreorder(rightPreorder, rightInorder, n)
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

    preorder = list(map(int, stdin.readline().strip().split(" ")))
    inorder = list(map(int, stdin.readline().strip().split(" ")))

    return preorder, inorder, n


# Main
preorder, inorder, n = takeInput()
root = buildTreePreorder(preorder, inorder, n)
printLevelWise(root)
