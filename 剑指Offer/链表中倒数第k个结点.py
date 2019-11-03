# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
 
#运行时间：26ms   占用内存：5856k
#Time:O(n)  Space: O(n)
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l=[]
        while head!=None:
            l.append(head)#python2是加head,python3 是加head.val
            head=head.next
        if k>len(l) or k<1:
            return
        return l[-k]
        



#快慢指针，快比慢多K步，这样快到头，慢正好到指定位置
#类似的题目有力扣876，判断是否有环。
#运行时间：32ms   占用内存：5756k
class Solution:
    def FindKthToTail(self,head,k):
        if head == None or k <= 0:#特殊情况需要判定
            return None
        fast = slow = head
        while k > 1:
            if fast.next:
                fast = fast.next
                k -= 1
            else:
                return None
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow
