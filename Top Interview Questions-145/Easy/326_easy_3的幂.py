#int 32位内3的幂最大1162261467,180ms
#Time:O(1)   Space: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        return 1162261467 % n == 0#是否有余

#递归，112ms
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0 or n % 3 != 0:
            return False
        else:
            n = n // 3
            return self.isPowerOfThree(n)

#对数函数，132 ms
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        return n > 0 and n == 3**round(math.log(n,3))
#96 ms
class Solution:
    def isPowerOfThree(self, n):
        return n > 0 and (math.log10(n)/math.log10(3)).is_integer()


#换为指数运算
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 3^x = n -> x = log3(n) = log(n)/log(3)
        if n <= 0:
            return False
        elif n == 1:
            return True
        import math
        x = math.log(n) / math.log(3)
        return 3 ** int(round(x)) == n