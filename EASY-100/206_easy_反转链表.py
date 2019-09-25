# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#数组来存,常规,64 ms
#Time:  O(n)  Space: O(n)
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        dim = ListNode(0)
        cur = dim
        while res != []:
            cur.next = ListNode(res.pop())
            cur = cur.next#指向下一个指针
        return dim.next
        
#多元赋值   36ms
#Time:O(n)  Space: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p,res = head,None
        while p:
            res,res.next,p = p,res,p.next
        return res
        
        p:1->2->3->4->5
        res,res.next,p = p,res,p.next
        res:1->2->3->4->5   => 1->None
        p:2->3->4->5
        res:2->3->4->5      => 2->1->None
        p:3->4->5 
        res:3->4->5         => 3->2->1->None
        ...
       
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
    
    
#递归,40 ms
#Time:O(n)  Space: O(n)
class Solution(object):
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)#p为尾结点
        head.next.next = head#指向下一个后再指会本身实现倒转
        head.next = None#必须为None,否则可能会出现循环，这样就直接倒转前面的剩余部分
        return p
    

