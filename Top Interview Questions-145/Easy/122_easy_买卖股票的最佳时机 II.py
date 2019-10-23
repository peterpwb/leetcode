#60ms,贪心算法
# Time:  O(n)  Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        target = 0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1] > 0:
                target += prices[i]-prices[i-1]
        return target