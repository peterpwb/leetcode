#运行时间：29ms   占用内存：5656k
#Time:O(n)  Space: O(1)
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()#排序
        zero = numbers.count(0)#统计有多少个大小王
        small = zero
        gap = 0
        while small < 4:
            if numbers[small] == numbers[small+1]:#出现对子
                return False
            gap += numbers[small+1] - numbers[small] - 1
            if gap > zero:#差距无法弥补
                return False
            small += 1
        return True