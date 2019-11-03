# -*- coding:utf-8 -*-
#公式运用
    * 该解法如果输入时负数会陷入死循环，
    * 因为负数右移时，要保证移位后仍然是个负数，在最高位补得是1
    * 而本题最终目的是求1的个数，那么会有无数个1了。
class Solution:
    def NumberOf1(self, n):
        # write code here
        res = 0
        while n != 0：
            n = n&(n-1)
            res += 1
        return res
        
#改进1
#运行时间：24ms   占用内存：5736k
# -*- coding:utf-8 -*-
class Solution:    
    def NumberOf1(self, n):        
        # write code here        
        count = 0        
        if n < 0:            
            n = n & 0xffffffff        
        while n:            
            count += 1            
            n = (n - 1) & n        
        return count
