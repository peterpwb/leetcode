# -*- coding:utf-8 -*-
#运行时间：33ms  占用内存：5752k
#找规律
class Solution:
    def cutRope(self, number):
        # write code here
        sum = 1
        if number == 2:
            return 1
        if number == 3:
            return 2
        #结果是2与3的组合
        x = number % 3
        y = number // 3
        if x == 0:#没有2
            return pow(3,y)
        elif x == 1:#余数为1
            return 2*2*pow(3,y-1)
        else:
            return 2*pow(3,y)