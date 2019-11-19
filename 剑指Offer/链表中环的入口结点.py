#运行时间：29ms   占用内存：5696k
#1、设置快慢指针，假如有环，他们最后一定相遇。
#2、两个指针分别从链表头和相遇点继续出发，每次走一步，最后一定相遇与环入口。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None or pHead.next is None or pHead.next.next is None:
            return None
        fast = pHead
        slow = pHead
        while fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow