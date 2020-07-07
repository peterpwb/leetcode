"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#递归  64 ms
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        def helper(root):
            if root:
                for i in root.children:
                    helper(i)
                res.append(root.val)
        helper(root)
        return res

#迭代方法
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            for i in node.children:
                stack.append(i)
            res.append(node.val)
        return res[::-1]