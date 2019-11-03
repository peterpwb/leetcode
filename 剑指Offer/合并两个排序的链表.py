# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        res = []
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                res.append(pHead1.val)
                pHead1 = pHead1.next
            else:
                res.append(pHead2.val)
                pHead2 = pHead2.next
        pHead1 = pHead1 if pHead1 else pHead2
        while pHead1:
            res.append(pHead1.val)
            pHead1 = pHead1.next
        return res

#运行时间：33ms  占用内存：8636k
#Time:O(n)  Space:O(1)
#力扣21
class Solution:
    def Merge(self,pHead1,pHead2):
        dim = ListNode(0)
        p = dim
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                p.next = pHead1
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                pHead2 = pHead2.next
            p = p.next
        p.next = pHead1 if pHead1 else pHead2
        return dim.next
                
            