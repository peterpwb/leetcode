# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#60ms,将一个值设的非常古怪，遍历如果有重复则说明是环
#Time:O(n)  Space:O(1)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == 'bjfuvth':
                return True
            else:
                head.val = 'bjfuvth'
            head = head.next
        return False
        
#双指针的做法，步长不一样，一个追上另一个则说明有环
class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False