class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self,root):
        if root is None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end = '')
            print(root.left.data, end=',')
        if root.right != None:
            print("R:",end = '')
            print(root.right.data, end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
        
    def printTree(self):
        self.printTreeHelper(self.root)
        
    def searchHelper(self,root,data):
        if root == None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            return self.searchHelper(root.left, data)
        else:
            return self.searchHelper(root.right, data)
        
    def search(self, data):
        return self.searchHelper(self.root, data)
    
    def insertHelper(self,root,data):
        if root is None:
            Node = BinaryTreeNode(data)
            return Node
        if data <= root.data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root
    
    def insert(self,data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)
        
    def minimum(self,root):
        if root is None:
            return 100000
        leftMin = self.minimum(root.left)
        return min(leftMin, root.data)
    
    def deleteHelper(self, root, data):
        if root is None:
            return False, None
        if data<root.data:
            isDeleted,root.left=self.deleteHelper(root.left, data)
            return isDeleted, root
        if data>root.data:
            isDeleted,root.right=self.deleteHelper(root.right, data)
            return isDeleted, root
        if data==root.data:
            if root.left==None and root.right==None:
                return True, None
            elif root.left is None:
                return True, root.right
            elif root.right is None:
                return True, root.left
            else:
                minRightNode=self.minimum(root.right)
                root.data=minRightNode
                isDeleted,root.right=self.deleteHelper(root.right, minRightNode)
                return isDeleted, root
    
    def delete(self, data):
        isDeleted,newRoot=self.deleteHelper(self.root, data)
        if isDeleted:
            self.numNodes-=1
            self.root=newRoot
        return isDeleted
    def count(self):
        return self.numNode
            
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
