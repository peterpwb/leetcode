# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#二叉搜索树的中序遍历是递增的,	52 ms
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res == sorted(res) and len(set(res)) == len(res)#判断二叉树有没有重复元素，有的话不符合二叉搜索树定义