#代码所基于的想法是，将两个链表L1和L2进行拼接，
#得到L1+L2和L2+L1两个拼接结果。这两个拼接后的链表长度是一致的，那么逐个判断即可
#长度相同有公共结点，第一次就遍历到；没有公共结点，走到尾部NULL相遇，返回NULL
#长度不同有公共结点，第一遍差值就出来了，第二遍一起到公共结点；没有公共，一起到结尾NUL

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#运行时间：31ms   占用内存：5756k
#Time:O(n+m)  Space:O(1)

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = pHead2 if p1 == None else p1.next
            p2 = pHead1 if p2 == None else p2.next
        return p1