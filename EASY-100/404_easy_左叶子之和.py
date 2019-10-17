#递归1,56ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time:O(n)   Space: O(h)
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
            
            
#100ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:#为空返回
            return 0
        elif root.left is None and root.right is None:#无分支返回
            return 0
        elif root.left and root.left.left is None and root.left.right is None:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
