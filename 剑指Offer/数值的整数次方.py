#运行时间：22ms   占用内存：5732k
# -*- coding:utf-8 -*-
#Time:O(n)  Space: O(1)
class Solution:
    def Power(self, base, exponent):
        result = 1        
        if base == 0:
            return 0        
        if exponent == 0:
            return 1        
        if exponent < 0:
            for i in range(-exponent):
                result = result * base
            return 1/result
        for i in range(exponent):
            result = result * base
        return result


#运行时间：28ms   占用内存：5856k
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base**exponent