# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归，前序遍历首位为根节点，中序遍历根节点左侧为左子树，右侧为右子树
#268 ms
#Time:O(n)   Space:O(n) 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # write code here
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root