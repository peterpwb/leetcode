# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归做法,60ms
#Time:O(n)  Space:O(h)(h为树的高度)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMorror(root.left,root.right)
        
    def isMorror(self,left,right):
        if not left and not right:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isMorror(left.left,right.right) and self.isMorror(left.right,right.left)
        
#迭代做法,用栈,60ms
#Time:O(n)  Space:O(h)(h为树的高度)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack=[(root.left,root.right)]
        while stack:
            cur = stack.pop()
            l,r = cur[0],cur[1]
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            stack.append((l.right,r.left))
            stack.append((l.left,r.right))
        return True
        
        
#迭代做法2，队列层序遍历，检查是否是回文，56ms
#Time:O(n)  Space:O(n)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root]
        while queue:
            next_queue = list()
            layer = []
            for i in queue:
                if not i:
                    layer.append(None)
                    continue
                next_queue.append(i.left)
                next_queue.append(i.right)
                layer.append(i.val)
            if layer != layer[::-1]:
                return False
            queue = next_queue
        return True