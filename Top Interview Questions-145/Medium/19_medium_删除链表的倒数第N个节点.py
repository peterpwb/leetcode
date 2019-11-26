# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#两次遍历,52 ms
#Time:O(L)[链表长度]  Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        num = 0
        while cur:#统计有几个数
            num += 1
            cur = cur.next
        p = ListNode(0)
        p.next = head#创建一个头，以处理第一个结点的删除或者单节点的链表
        dim = p
        num -= n
        while num > 0:
            num -= 1
            dim = dim.next
        dim.next=dim.next.next
        return p.next
        
#一次遍历，两个指针，保持两个结点相差N个结点，当一个到结尾时，另一个正好到指定位置,64 ms
#Time:O(L)  Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = ListNode(0)
        p.next = head
        slow = fast = p
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return p.next
        