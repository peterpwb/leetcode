#双指针
#Time:O(n)   Space:O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0
            
#Time:O(n)   Space:O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        k=0
        while i<len(nums)-k:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                k=k+1
            else:
                i=i+1

#双指针，自己的做法，948 ms
#Time:O(n)   Space:O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        while a < len(nums):
            b = a+1#第二指针
            if nums[a] != 0:
                a += 1
            else:#a为0
                while not nums[b] and b<len(nums)-1:#为0
                    b += 1
                temp = nums[a]
                nums[a] = nums[b]
                nums[b] = temp
                a += 1
