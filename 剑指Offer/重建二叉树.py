# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归，前序遍历首位为根节点，中序遍历根节点左侧为左子树，右侧为右子树
#运行时间：65ms   占用内存：5624k
#Time:O(n)   Space:O(n) 

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        mid = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:mid+1],tin[:mid])
        root.right = self.reConstructBinaryTree(pre[mid+1:],tin[mid+1:])
        return root