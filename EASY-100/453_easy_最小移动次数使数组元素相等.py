#自己的方法,136 ms
# Time:O(n)  Space: O(1)
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums=sorted(nums)
        res = 0
        for i in range(1,len(nums)):
            res += nums[i]-nums[0]
        return res

#80ms，找最小就好不需要排序
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        res = 0
        for n in nums:
            res += n - minimum
        return res
        
#348 ms
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min = float("inf")
        if len(nums) == 1:
            return 0
        for i in nums:#遍历得到最大值和最小值
            if i < min:
                min = i
        res = 0
        for i in nums:
            res += i - min
        return res