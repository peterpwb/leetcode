# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#后进先出，题意希望用栈做
#递归本质也是一种栈结构，所以也可以用递归

#遍历链表，反转列表
#46 ms  5752K
#Time:O(n)   Space:O(n) 
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]
        
        
        
#递归
#运行时间：24ms    占用内存：5728k
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        return self.printListFromTailToHead(listNode.next)+[listNode.val]
