# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#两次遍历，第一次取长度，第二次取一半,44 ms
#Time:O(L)[链表长度]   Space: O(1)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        n //= 2
        while n > 0:
            head = head.next
            n -= 1
        return head
        
#一次遍历，快慢指针，48 ms
#Time:O(L)[链表长度]   Space: O(1)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow