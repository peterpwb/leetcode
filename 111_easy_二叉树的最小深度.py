# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time:  O(n), Space: O(h), h is height of binary tree
#递归1,72ms
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            if root.left and root.right:
                return min(self.minDepth(root.left),self.minDepth(root.right))+1
            elif root.left:
                return self.minDepth(root.left)+1
            elif root.right:
                return self.minDepth(root.right)+1
            else:
                return 1
        else:
            return 0
            
            
#递归2,68ms
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0 
        if root.left and root.right:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        else:
            return max(self.minDepth(root.left),self.minDepth(root.right))+1