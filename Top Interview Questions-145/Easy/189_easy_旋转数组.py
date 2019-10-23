#方法1，切片，60 ms
# Time:  O(n)  Space: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        step=k%len(nums)
        nums[:]=nums[-step:]+nums[:-step]
        
        
#方法2，先加再去头，72 ms
# Time:  O(n)  Space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        step=k%len(nums)
        res=len(nums)-step
        for i in range(res):
            nums.append(nums[i])
        nums[:]=nums[res:]
        
#方法3，在新的列表里面取数
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        step=k%len(nums)
        if step==0:
            nums=nums
        else:
            nums = self.rotate_x(nums, step)
        
    def rotate_x(self,x,n):
        b = x.copy()
        b.reverse()
        i = 0
        while i <= n:
            x[i] = b[n - i - 1]
            i += 1
        j = 0
        while j < len(x) - n:
            x[n + j] = b[len(x) - j - 1]
            j += 1
        return x
        
        
