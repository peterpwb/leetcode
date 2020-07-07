# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#

#递归做法52 ms,后序：左-右-根
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dim(root):
            if not root:return None
            dim(root.left)
            dim(root.right)
            res.append(root.val)
        dim(root)
        return res

#迭代做法48ms
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]