#递归，利用递归的方法进行先序遍历，传递深度，
#递归深入一层扩容一层数组，先序遍历又保证了同层节点按从左到右入数组
#运行时间：32ms  占用内存：5652k

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        res = []
        def dep(root,depth):
            if root:
                if len(res) < depth:
                    res.append([])
                res[depth-1].append(root.val)
                dep(root.left,depth+1)
                dep(root.right,depth+1)
        dep(pRoot,1)
        return res
