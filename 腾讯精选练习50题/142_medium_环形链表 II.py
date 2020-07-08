# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#44 ms,双指针，找到相遇点（题目141），然后一个起点出发，一个相遇点出发，相同步长，相遇点的地方就是入口
#Time:O(n)  Space:O(1)
class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
        
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = self.hasCycle(head)
        if res == None:
            return None
        part1 = head
        part2 = res
        while part1 and part2:
            if part1 == part2:
                return part1
            else:
                part1 = part1.next
                part2 = part2.next
        