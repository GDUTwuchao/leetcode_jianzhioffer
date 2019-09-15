'''
二叉搜索树(BST)是一棵树，其所有节点都遵循下述属性 - 节点的左子树的键小于或等于其父节点的键。
节点的右子树的键大于其父节点的键。 因此，BST将其所有子树分成两部分; 左边的子树和右边的子树，可以定义为
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)

'''

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(8)
root.insert(4)
root.insert(2)
root.insert(5)
root.insert(10)
root.insert(17)
root.insert(25)
root.insert(20)
root.insert(21)
root.insert(13)
root.PrintTree()
print(root.findval(21))
print(root.findval(14))

