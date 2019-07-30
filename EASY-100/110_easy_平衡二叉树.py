# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#88ms，递归
# Time:  O(n), Space: O(h), h is height of binary tree
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        ld = self.maxdepth(root.left)
        rd = self.maxdepth(root.right)
        if abs(ld-rd) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    
    def maxdepth(self,root: TreeNode):
        if root is None:
            return 0
        return max(self.maxdepth(root.left),self.maxdepth(root.right))+1