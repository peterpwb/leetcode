#运行时间：22ms  占用内存：5740k
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        self.res=[]
        self.dfs(pRoot)
        return self.res[k-1] if 0<k<=len(self.res) else None
    def dfs(self,root):
        if not root:return
        self.dfs(root.left)
        self.res.append(root)
        self.dfs(root.right)