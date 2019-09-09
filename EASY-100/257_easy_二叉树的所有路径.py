# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归1,72ms
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths

        
#递归2
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:#终止条件
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + "->" + i)
        if root.right:
            for j in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + "->" + j)
        return paths