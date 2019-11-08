# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归，类似力扣110
#运行时间：34ms   占用内存：5752k
#Time:O(n), Space: O(h), h is height of binary tree
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        leftdepth = self.maxDepth(pRoot.left)
        rightdepth = self.maxDepth(pRoot.right)
        if abs(leftdepth-rightdepth)<=1:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        else:
            return False
        
    def maxDepth(self,root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
