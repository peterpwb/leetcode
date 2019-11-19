# -*- coding:utf-8 -*-
#运行时间：31ms  占用内存：5740k

class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(1,n+1)))
        
#运行时间：30ms   占用内存：5752k

class Solution:
    def __init__(self):
        self.sum = 0
        
    def Sum_Solution(self, n):
        def qiuhe(n):
            self.sum += n
            n -= 1
            return n >0 and self.Sum_Solution(n)
        qiuhe(n)
        return self.sum
