# -*- coding:utf-8 -*-
#题意考察用"先进后出的"栈实现"先进先出的"队列

#1入列，2出列
#运行时间：25ms  占用内存：5852k
#Time: O(1)   Space: O(1)
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
         
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if not self.stack2:#2为空
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                #将1中的元素都倒序导入2，这样出来的第一个就为1里面的第一个
        return self.stack2.pop()
