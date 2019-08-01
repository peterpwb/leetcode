# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#100 ms，一次遍历
#Time:O(max(m,n))   Space:O(max(m,n))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = dim = ListNode(0)
        next = 0
        while l1 and l2:
            dim.next = ListNode((l1.val + l2.val+next)%10)
            next = (l1.val + l2.val+next)//10
            l1 = l1.next
            l2 = l2.next
            dim =dim.next
        l1 = l1 if l1 else l2
        while next:#处理首位多出来的1
            if l1:
                dim.next = ListNode((l1.val+next)%10)
                next = (l1.val+next)//10
                l1 = l1.next
                dim = dim.next
            else:#l1,l2都为空
                dim.next = ListNode(next)
                dim  = dim.next
                break#始终是1,需跳出
        dim.next = l1
        return res.next
        