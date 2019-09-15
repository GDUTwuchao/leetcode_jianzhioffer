'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

思路：
首先根节点以及其左右子树，
左子树的左子树和右子树的右子树相同
左子树的右子树和右子树的左子树相同即可，采用递归
非递归也可，采用栈或队列存取各级子树根节点
'''
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymBT(pRoot, pRoot)

    def isSymBT(self, tree1, tree2):
        if tree1 == None and tree2 == None:
            return True
        if tree1 == None or tree2 == None:
            return False
        if tree1.val != tree2.val:
            return False
        return self.isSymBT(tree1.left, tree2.right) and self.isSymBT(tree1.right, tree2.left)
