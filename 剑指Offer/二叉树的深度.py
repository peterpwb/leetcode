# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#运行时间：29ms   占用内存：5728k
#递归，64ms,DFS（深度优先搜索）类似力扣104
#Time:O(n)[每个节点只访问一次]   Space:O(n)[最糟，完全不平衡],O(log(N))[最好，完全平衡]
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1
