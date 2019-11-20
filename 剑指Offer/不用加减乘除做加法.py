#运行时间：28ms  占用内存：5736k
# -*- coding:utf-8 -*-
#同力扣371

class Solution: 
    def Add(self, a, b):
        while(b): 
            a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)
