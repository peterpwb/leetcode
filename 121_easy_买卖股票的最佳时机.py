#一次遍历，原始方法，96ms
# Time:  O(n)  Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        ming == min(prices[0],prices[1])
        if prices[0]>prices[1]:
            res= 0
        else:
            res = prices[1]-prices[0]
        for i in range(2,len(prices)):
            if prices[i] < ming:
                ming = prices[i]
            if prices[i]-ming > res:
                res = prices[i]-ming
        return res

#动态规划，104ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        minPrice=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            maxprofit=max(maxprofit,prices[i]-minPrice)
            minPrice=min(minPrice,prices[i])
        return maxprofit
