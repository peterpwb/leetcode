'''
递归:就是依次输出根,左,右,递归下去
迭代:使用栈来完成,我们先将根节点放入栈中,然后将其弹出,依次将该弹出的节点的右节点,
和左节点,注意顺序,是右,左,为什么?因为栈是先入后出的,我们要先输出右节点,所以让它先进栈.
'''
#前序遍历：根-左-右
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归做法  60 ms
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dim(root):
            if not root:return None
            res.append(root.val)
            dim(root.left)
            dim(root.right)
        dim(root)
        return res

#迭代做法  非递归--栈  40 ms
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:stack.append(node.right)
            if node.left:stack.append(node.left)
        return res
        
#颜色标记法,36ms
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
                stack.append((WHITE, node.right))
            else:
                res.append(node.val)
        return res[::-1]