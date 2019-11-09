# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#运行时间：34ms，占用内存：5720k
#递归，类似力扣101
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return self.check(pRoot.left,pRoot.right)
    
    def check(self,left,right):
        if not left and not right:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.check(left.left,right.right) and self.check(left.right,right.left)