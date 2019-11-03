# -*- coding:utf-8 -*-
#F(n)=F(n-1)+F(n-2)

#常规思路，递归
#系统会让一个超大的n来让Stack Overflow,通过不了
from functools import lru_cache#缓存已经计算过的F(n-1)等
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)


#动态规划，类似力扣70
#记录F(n-1)+F(n-2)的值
#运行时间：23ms  占用内存：5856k
#Time:O(n)  Space: O(1)
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a1,a2,a3 = 0,1,0
        while n >= 2:#注意区别，这个有等号，可以代入检查一下
            a3 = a1+a2
            a1 = a2
            a2 = a3
            n -= 1
        return a3
