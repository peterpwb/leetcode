#Time:O(n)  Space:O(1)
#80ms,用set-list转换删除多余项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums=sorted（list(set(nums))）
        return len(nums)

#92ms,双指针的做法
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        i=0
        for j in range(len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
        
#96ms,直接删除
class Solution3：
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]:
                del nums[i+1]
            else:
                i += 1
        return len(nums)
