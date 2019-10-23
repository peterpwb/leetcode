#44ms，数学公式
# Time:O(logn)[sqrt is O(logn) time]   Space: O(1)

import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(2*(n+1/8))-0.5)#向下取整
       