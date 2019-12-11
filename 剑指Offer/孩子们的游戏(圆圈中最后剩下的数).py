#约瑟夫环，递归
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        if n == 1:
            return 0
        else:
            return (self.LastRemaining_Solution(n-1,m)+m)%n
            
            
#运行时间：30ms  占用内存：5752k
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n <1 or m <1:
            return -1 
        last = 0
        for i in range(2,n+1):
            last = (last+m)%i
        return last