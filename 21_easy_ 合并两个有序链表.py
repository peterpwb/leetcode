# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#40ms,新建一个链表操作
#Time:O(n)  Space:O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)#链表的常用技巧，新建一个表头这样好操作，回头再去掉
        p = dummy
        while (l1 and l2):
            if (l1.val <= l2.val):
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        #有一个已经到tail
        if (l1): p.next = l1
        elif (l2): p.next = l2
        return dummy.next
        

#48ms,直接返回列表也能通过
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=[]
        while l1:
            res.append(l1.val)
            l1 = l1.next
        while l2:
            res.append(l2.val)
            l2 = l2.next
        return sorted(res)
