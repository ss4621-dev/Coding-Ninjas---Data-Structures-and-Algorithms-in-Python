import queue
from sys import setrecursionlimit
setrecursionlimit(10**6)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    if len(lst) == 0:
        return
    if len(lst)%2 == 0:
        mid = len(lst)//2 - 1
    else:
        mid = (len(lst)//2)
    root = BinaryTreeNode(lst[mid])
    leftSubTree = constructBST(lst[0:mid])
    rightSubTree = constructBST(lst[mid+1:])
    root.left = leftSubTree
    root.right = rightSubTree
    return root
    

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)
