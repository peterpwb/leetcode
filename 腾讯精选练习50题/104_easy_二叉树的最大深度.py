# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#递归，64ms,DFS（深度优先搜索）
#Time:O(n)[每个节点只访问一次]   Space:O(n)[最糟，完全不平衡],O(log(N))[最好，完全平衡]
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)
        
#迭代,BFS(广度优先算法)算法,56ms
from collections import deque

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth=1
        queue=deque([(1, root)])
        while queue:
            depth, node=queue.popleft()
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))
        return depth