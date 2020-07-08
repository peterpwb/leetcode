# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#是二叉搜索树，所以一定满足左节点<=当前节点<=右节点
# Time:O(n)  Space: O(1)
#84ms
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #最近公共祖先的值一定介于p、q值之间(闭区间)
        while (root.val - p.val) * (root.val - q.val) > 0:
        #同时大于当前节点或同时小于当前节点
            root = (root.left, root.right)[p.val > root.val]
            #这样写是直接拿判断结果当索引
            #写法同root =root.left if p.val < root.val else root.right
        return root 
        
        
#92ms
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val > p.val and root.val > q.val:#比p,q都大所以root变小
                root = root.left
            elif root.val < p.val and root.val < q.val:#比p,q都小所以root变大
                root = root.right
            else:
                return root#直到在p,q之间