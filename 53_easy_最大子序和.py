#动态规划
'''
分治法与动态规划主要区别:
① 分治法将分解后的子问题看成相互独立的.通过用递归来做。
② 动态规划将分解后的子问题理解为相互间有联系,有重叠部分,通常用迭代来做.
'''
#60ms
#Time:O(n)   Space:O(l)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+max(nums[i-1],0)
        return max(nums)
        
#56ms
# Time:  O(n)   Space: O(l)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tem = nums[0]
        max_ = tem
        for i in range(1,len(nums)):
            if tem > 0:
                max_ = max(max_,tem+nums[i])
                tem = tem + nums[i]
            else:
                max_ = max(max_,nums[i])
                tem = nums[i]
        return max_
        
        
#96ms
#Time:O(n)   Space: O(l)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nums = max(nums)
        if max_nums < 0:
            return max_nums
        global_max, local_max = 0, 0
        for x in nums:
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max