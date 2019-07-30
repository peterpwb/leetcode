# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Time:O(n)  Space:O(1)
#80ms,递归,理解每层需要做什么
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        next = head.next
        head.next =self.swapPairs(next.next)
        next.next = head
        return next
        
#迭代1,56ms
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        if head is None or head.next is None:
            return head
        while head and head.next:
            curr.next=head.next
            head.next=head.next.next
            curr.next.next=head
            curr=curr.next.next#要类似于前一次，前面多一项
            head=head.next
        return dummy.next
        
        
        
#迭代2,52ms
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while head:
            if head and head.next:
                tmp = head.next
                p.next = tmp
                # 交换 位置
                head.next = head.next.next
                tmp.next = head
                head = head.next
                p = p.next.next
            else:
                p.next = h
                h = h.next
        return dummy.next
