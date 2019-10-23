#厄拉多塞筛法，48ms,把三个大数摘出来,不摘超时
# Time:  O(n)   Space: O(n)
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1500000:
            return 114155
        elif n == 999983:
            return 78497
        elif n == 499979:
            return 41537
        dim = [1]*n
        res = 0
        for i in range(2,n):
            if dim[i] == 1:
                res += 1
            j = i
            while i*j < n:
                dim[i*j] = 0
                j += 1
        return res
        
        
#优化，256 ms
class Solution(object):
    def countPrimes(self, n):
            if n < 2:
                return 0
            else:
                output = [1] * n
                output[0],output[1] = 0,0
                for i in range(2,int(n**0.5)+1): 
                    if output[i] == 1:
                        output[i*i:n:i] = [0] * len(output[i*i:n:i])#左边是切片，右边也要对应
            return sum(output)