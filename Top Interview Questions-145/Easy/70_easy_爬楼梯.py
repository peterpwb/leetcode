#动态规划，40ms
#Time:O(n)  Space: O(1)[只用了常量级]
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a1,a2,a3 = 1,2,0
        while n>2:
            a3 = a1+a2
            a1 = a2
            a2 = a3
            n -= 1
        return a3

#递归，超时
from functools import lru_cache#装饰器，缓存已经计算过的内容
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)