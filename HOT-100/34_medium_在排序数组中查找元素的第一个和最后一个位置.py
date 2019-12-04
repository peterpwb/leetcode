#分两次二分查找确定起始点和终止点,92 ms
#Time:O(logn)  Space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        #取起始下标
        while left < right:
            mid =(right + left)//2
            if nums[mid] >= target:
                right = mid 
            else:
                left = mid + 1
        if not nums or nums[left] != target:#没找到
            return [-1,-1]
        a,b = left,len(nums)-1
        while a < b:
            mid = (a+b+1)//2#其实就是左右的中点，只是是偶数的时候选右节点。
            if nums[mid] <= target:
                a = mid
            else:
                b = mid - 1
        return [left,a]