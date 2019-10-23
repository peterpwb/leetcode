# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#1236 ms,双递归
#Time:O(n)  Space: O(h)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        return self.pathSum(root.left,sum)+self.pathSum(root.right,sum)+self.dfs(root,sum)
    
    def dfs(self,node: TreeNode, sum: int):
        if node == None:
            return 0
        count = 0
        if node.val == sum:
            count = 1
        return count + self.dfs(node.left,sum-node.val)+self.dfs(node.right,sum-node.val)
        
#1068 ms
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def find(root,sum):
            if root and root.val== sum:
                return 1+find(root.left,0)+find(root.right,0)
            if not root:
                return 0
            return find(root.left, sum-root.val)+find(root.right,sum-root.val)        
        if not root:
            return 0
        if root:
            left = self.pathSum(root.left,sum)
            right = self.pathSum(root.right,sum)
            l = find(root.left,sum-root.val)
            r = find(root.right,sum-root.val)
            if sum == root.val:
                return 1+left+right+l+r
            else:
                return left+right+l+r
                
#1740 ms,dfs2,1的简约版
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node, sum):
            return dfs(node.left, sum-node.val) + dfs(node.right, sum-node.val) + (sum == node.val) if node else 0
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum) if root else 0

