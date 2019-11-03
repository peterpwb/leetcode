
# -*- coding:utf-8 -*-
#找规律，最后递归
#f(n)=f(0)+f(1)+f(2)+f(3)+ ... +f(n-1)
#得到f(n) = 2*f(n-1) 

#运行时间：28ms  占用内存：5856k
#Time:O(n)  Space: O(1)

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return 2*self.jumpFloorII(number-1)