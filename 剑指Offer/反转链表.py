# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#测试用例1.输入的是None,2.输入的链表只有一个结点，3.输入的链表有多个结点

#运行时间：28ms  占用内存：5752k
#Time:O(n)  Space: O(1)
#力扣206里面的迭代方法
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        cur,pre = pHead,None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur 
            cur = temp
        return pre
        
#迭代方法[类似多元赋值]  28ms
#Time: O(n)  Space: O(1)
class Solution(object):
    def reverseList(self, head):
        prev = None#初始化前一个节点，为空
        curr = head#当前节点指向头结点
        while curr:
            temp = prev#记录前一个节点。
            prev = curr#前结点指向当前
            curr = curr.next#当前结点指向下一个
            prev.next = temp#当前结点指向前一个结点
            
        return prev
#解释：
head=1->2->3->4->5
prev=None
curr=1->2->3->4->5
while curr!=None:            while curr!=None:     while curr!=None:
    temp=None                  temp=1->None          temp=2->1->None
    prev=1->2->3->4->5         prev=2->3->4->5       prev=3->4->5
    cur=2->3->4->5             curr=3->4->5          curr=4->5
    prev=1->None               prev=2->1->None       prev=3->2->1->None