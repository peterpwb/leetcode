#solution1,按位取反,52 ms
#Time:O(log(n)) = O(1)  Space:O(1)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        result = 0
        while x:
            result = result * 10 + x % 10#10^x=n-->x=log10(n)-->Time:O(log(n))
            x //= 10
        return result if result <= 0x7fffffff else 0 


#solution2,转字符串直接转,56 ms
#0x7FFFFFFF是最大的整数型int
#Time:O(1)  Space:O(1)
class Solution:
    def reverse(self, x: int) -> int:
        int_max = 0x7FFFFFFF - 1
        int_min = -0x7FFFFFFF
        if x >= 0:
            if int_min < int(str(x)[::-1]) < int_max:
                return int(str(x)[::-1])  
            else:
                return 0
        else:
            if int_min < int(str(x)[1:][::-1]) < int_max:
                return -int(str(x)[1:][::-1])
            else:
                return 0
            
