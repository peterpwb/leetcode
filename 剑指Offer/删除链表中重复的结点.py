# -*- coding:utf-8 -*-
#运行时间：43ms占用内存：5744k

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        if pHead.val == pHead.next.val:
            pNode = pHead.next
            while pNode and pNode.val == pHead.val:
                pNode = pNode.next
            return self.deleteDuplication(pNode)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead


#运行时间：33ms  占用内存：5864k
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        pNode = ListNode(0)
        pNode.next = pHead
        pre = pNode
        p = pHead
        while p and p.next:
            nex = p.next
            if p.val == nex.val:
                while nex and nex.val == p.val:
                    nex = nex.next
                pre.next = nex
                p = nex
            else:
                pre = p
                p = p.next
        return pNode.next
        