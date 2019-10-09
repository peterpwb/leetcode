#Time:O(1)   Space: O(1)
#类似326,48m
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num == 1:
            return True
        import math
        x=math.log(num)/math.log(4)
        return 4**int(round(x))==num

#56ms
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (math.log10(num)/math.log10(4)).is_integer()