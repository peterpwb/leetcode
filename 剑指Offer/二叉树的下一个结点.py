# -*- coding:utf-8 -*-
#运行时间：30ms  占用内存：5752k

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right != None:#如果有右子树，则找右子树的最左节点
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        while pNode.next:#没右子树，则找第一个当前节点是父节点左孩子的节点
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return None#退到了根节点仍没找到，则返回null