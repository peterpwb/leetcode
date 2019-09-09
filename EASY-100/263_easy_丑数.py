#36 ms，不断整除看结果是否为1
# Time:O(logn) = O(1)   Space: O(1)
class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        while True:
            if num % 2 == 0: num =// 2
            if num % 3 == 0: num =// 3
            if num % 5 == 0: num =// 5
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0: break
        return num == 1