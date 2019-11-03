# -*- coding:utf-8 -*-
#找规律，其实还是斐波那契数列
#运行时间：24ms  占用内存：5856k
#Time:O(n)  Space: O(1)

class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 1:
            return number
        elif number == 2:
            return 2
        a1,a2,a3 = 1,2,0
        while number > 2:
            a3 = a1 + a2
            a1 =a2
            a2 =a3
            number -= 1
        return a3