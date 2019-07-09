#Time:O(n)  Space:O(1)
#用set-list转换删除多余项，最快时间复杂度O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums=sorted（list(set(nums))）
        return len(nums)

#直接对数组进行操作
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        i=0
        for j in range(len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
        
#直接删除
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]:
                del nums[i+1]
            else:
                i += 1
        return len(nums)
