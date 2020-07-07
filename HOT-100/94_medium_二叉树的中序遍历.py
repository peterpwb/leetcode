# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#递归做法，28ms
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        def helper(root):
            if not root:
                return None
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res
        
#迭代做法,52 ms,用一个指针模拟过程
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        
#颜色标记法，44 ms
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


#优化40 ms
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack,rst = [root],[]
        while stack:
            i = stack.pop()
            if isinstance(i,TreeNode):
                stack.extend([i.right,i.val,i.left])
            elif isinstance(i,int):
                rst.append(i)
        return rst