#动态规划，40ms
#Time:O(n)  Space: O(1)
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