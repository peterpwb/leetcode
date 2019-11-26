#运行时间：35ms  占用内存：5740k
#Time:O(n)   Space:O(l)
#动态规划，同力扣53

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        for i in range(1,len(array)):
            array[i] = array[i] + max(array[i-1],0)
        return max(array)