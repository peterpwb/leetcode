#遍历，64 ms
#Time:O(n)  Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


#直接一次，二分查找
1.直接等于target
2.在左半边的递增区域
a. target 在 left 和 mid 之间
b. 不在之间
3.在右半边的递增区域
a. target 在 mid 和 right 之间
b. 不在之间
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if nums[left] == target else -1


#先找二分查找找到分割点，然后再判断，52 ms
#Time:O(logn)  Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        n = len(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) //2
            if nums[mid] > nums[right]:#直接与右边点对比
                left = mid + 1
            else:
                right = mid
        t = left
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) //2
            realmid = (mid + t) % n
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

