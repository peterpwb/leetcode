# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Time:O(n)   Space:O(n)
#自己的做法，84ms
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        sev=[]
        while head:
            if head.val not in sev:
                sev+=[head.val]
                head=head.next
            else:
                head=head.next
        return sev
        
#直接在该链表内修改,64ms
#Time:O(n)   Space:O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dim = cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur =cur.next
        return dim

#递归，100ms
#Time:O(n)   Space:O(1)
class Solution:
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        if head.next:
            if head.val == head.next.val:
                head = self.deleteDuplicates2(head.next)
            else:
                head.next = self.deleteDuplicates2(head.next)
        return head