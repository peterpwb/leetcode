# -*- coding:utf-8 -*-
#类似力扣155
#运行时间：27ms  占用内存：5716k
#Time:O(1)   Space: O(1)
class Solution:
    def __init__(self):
        self.stack1 = []
        self.minstack = []
        
    def push(self, node):#小于最小值才压入
        # write code here
        self.stack1.append(node)
        if not self.minstack or node <= self.minstack[-1]: 
            self.minstack.append(node)
            
    def pop(self):#注意区别
        # write code here
        if self.stack1.pop() == self.minstack[-1]:
            self.minstack.pop()
        
    def top(self):
        # write code here
        return self.stack1[-1]
        
    def min(self):
        # write code here
        return self.minstack[-1]
        
#运行时间：31ms    占用内存：5720k
class Solution:
    def __init__(self):
        self.stack1 = []
        self.minstack = []
        
    def push(self, node):#每次都把最小元素压入最小值栈，而且栈顶一直都是最小值
        # write code here
        self.stack1.append(node)
        if not self.minstack or node <= self.minstack[-1]: 
            self.minstack.append(node)
        else:
            self.minstack.append(self.minstack[-1])
            
    def pop(self):#出的时候同时出
        # write code here
        self.minstack.pop()
        self.stack1.pop()
        
    def top(self):
        # write code here
        return self.stack1[-1]
        
    def min(self):
        # write code here
        return self.minstack[-1]