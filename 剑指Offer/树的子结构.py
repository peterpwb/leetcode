# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#运行时间：30ms   占用内存：5756k
# Time:O(n)  Space:O(1)
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.same(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
        #注意第一个是判断是否相等
    def same(self, A, B):#判断是否相等
        if not B:
            return True
        if not A:
            return False
        return A.val == B.val and self.same(A.left,B.left) and self.same(A.right,B.right)
        
#需要注意的是  DoesTree1HasTree2函数中，如果Tree2为空，则说明第二棵树遍历完了，即是第一颗树的子树，返回TRUE
#如果tree1为空而tree2不为空说明tree2结构超大，tree1中不存在 