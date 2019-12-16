#递归，二叉树的中序遍历
#运行时间：31ms   占用内存：5756k

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)# 将左子树构建成双链表，返回链表头
        p = left
        
        while left and p.right:# 定位至左子树的最右的一个结点
            p = p.right
        
        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p
        
        right = self.Convert(pRootOfTree.right)
        if right:# 如果右子树不为空，将该链表追加到root结点之后
            right.left = pRootOfTree
            pRootOfTree.right = right
        
        return left if left else pRootOfTree
            
           
            