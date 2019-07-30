#56ms,内置函数的应用
#Time:O(n)  Space:O(k)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
            
            
#48ms,遍历
#Time:O(n)  Space:O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        if len(nums) == 1:
            return 0 if  target <= nums[0] else 1
        while i <len(nums)-1:
            if target <= nums[i]:
                return i
            elif target <= nums[i+1]:
                return i+1
            else:
                i += 1
        return len(nums)
        
#二分法，52ms
#Time:  O(logn)  Space: O(1)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left