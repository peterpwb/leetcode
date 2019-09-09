# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time:  O(n)  Space: O(1)
#自己的方法，64 ms，内存大
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        return res==res[::-1]
        
#步骤：92 ms
设置快慢指针
每次快指针增加两个，慢指针增加一个
这样当快指针结尾时，慢指针指向了链表的中间
用慢指针逆序链表的后半部分，利用Python交换的特性，不需要额外的tmp结点
一个从头开始，一个从中间开始，判断两者是否相同

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:return True
        # 取中位数的上边界，比如[1, 2, 2, 3] 取到是第二个2
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 奇数时候，中点位置下一个，（这样翻转才一样）
        if fast:
            slow = slow.next
        # 翻转操作
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # 对比
        p1 = head
        p2 = prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

#报错，原因因为反转的时候head就改变了
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dim = head
        prev = self.reverseList(head)
        while dim and prev:
            if dim.val != prev.val:
                return False
            else:
                dim = dim.next
                prev = prev.next
        return True
        

    def reverseList(self, head):
        prev = None
        curr = head
        while curr != None:
            temp = prev
            prev = curr
            curr = curr.next
            prev.next = temp
            
        return prev
