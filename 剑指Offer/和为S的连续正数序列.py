#双指针
#运行时间：25ms   占用内存：5752k
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        left,right,sum,res = 1,2,3,[]
        while left < (1+tsum)//2:
            if sum > tsum:
                sum -= left
                left += 1
            else:
                if sum == tsum:
                    res.append([i for i in range(left,right+1)])
                right += 1
                sum += right
        return res