'''
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。

'''
class Solution:
    def Print(self, pRoot):
        if pRoot == None:
            return []
        result = []
        nodeStack = [pRoot]
        while nodeStack:
            res = []
            nextStack = []
            for i in nodeStack:
                res.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                nodeStack = nextStack
            result.append(res)
        final_result = []
        for i,v in enumerate(result):
            if i % 2 ==0:
                final_result.append(v)
            else:
                final_result.append(v[::-1])
        return final_result


'''
[0,[1,[3],[4]],[2,[5],[6]]]
-->[[1,[3],[4]],[2,[5],[6]]]
-->[[3],[4],[5],[6]]
'''