"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        def helper(root):
            if root:
                res.append(root.val)
                for i in root.children:
                    helper(i)
        helper(root)
        return res
#迭代，开栈方法80 ms
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            for i in node.children[::-1]:#先进后出
                stack.append(i)
        return res