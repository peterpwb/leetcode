# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#运行时间：29ms  占用内存：5752k
#力扣226，递归
# Time:  O(n)  Space: O(h)
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        temp = root.left
        root.left = self.Mirror(root.right)
        root.right = self.Mirror(temp)
        return root