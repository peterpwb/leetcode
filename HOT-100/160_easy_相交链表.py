# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#240 ms,计算a.b的长度，然后移动到相同的长度然后开始看有没有相同的
#Time:O(n+m)  Space:O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        headA_check,headB_check = headA,headB
        len_a,len_b = 0,0
        while headA_check:
            len_a += 1
            headA_check = headA_check.next
        while headB_check:
            len_b +=1
            headB_check = headB_check.next
        if len_a > len_b:
            while len_a > len_b:
                headA = headA.next
                len_a -=1
        elif len_b > len_a:
            while len_b >len_a:
                headB = headB.next
                len_b -=1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        
        
#228 ms,双指针，相当于A+B与B+A对比，如果有相交则尾巴部分是相交，没有就None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        r1,r2 = headA,headB
        while r1 != r2:
            if r1:
                r1 = r1.next
            else:
                r1 = headB
                
            if r2:
                r2 = r2.next
            else:
                r2 = headA
                
        return r1