# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归,题目类似力扣437
#运行时间：30ms    占用内存：5860k

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        else:
            left = self.FindPath(root.left,expectNumber-root.val)
            right = self.FindPath(root.right,expectNumber-root.val)
            for i in left+right:
                res.append([root.val]+i)
        return res