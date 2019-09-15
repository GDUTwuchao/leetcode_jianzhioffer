'''
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

'''


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here

        if (pRoot is None):
            return []
        queue = [pRoot]
        result = []
        while (queue):
            size = len(queue)
            row = []
            for i in queue:
                row.append(i.val)
            result.append(row)
            for i in range(size):
                node = queue.pop(0)
                if (node.left is not None):
                    queue.append(node.left)
                if (node.right is not None):
                    queue.append(node.right)
        return result