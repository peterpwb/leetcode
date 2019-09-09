 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time:  O(n)  Space: O(h)
#递归1,16ms
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        temp=root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(temp)
        return root
        
#递归2,20ms
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        root.left,root.right=root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
#递归3,84ms
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        else:
            tem = root.left
            root.left = root.right
            root.right = tem
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        return root