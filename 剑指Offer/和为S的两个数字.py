# -*- coding:utf-8 -*-
#运行时间：25ms   占用内存：5728k
#Time:O(n2), Space: O(1)

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        for i in range(len(array)):
            for j in array[i:]:
                if array[i]+j == tsum:
                    return [array[i],j]
        return []