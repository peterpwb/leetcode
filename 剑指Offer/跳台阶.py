# -*- coding:utf-8 -*-

#运行时间：22ms   占用内存：5736k
#存储前F(n-1)与F(n-2)的值
#Time:O(n)  Space: O(1)

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        a1,a2,a3 = 1,2,0
        while number > 2:
            a3 = a1 + a2
            a1 = a2
            a2 = a3
            number -= 1
        return a3