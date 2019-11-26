#2004 ms，双指针
#Time:O(N2)[头指针k的循环O(n),双指针O(n),乘法法则]   Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()#先排序O(nlog(n))
        for k in range(len(nums)-2):#到倒数第三位
            if nums[k] > 0:
                break#最左边的数都大于0,三数之和必大于0
            if k > 0 and nums[k] == nums[k - 1]:continue#开头一样的话直接进入下一个数,因为结果一致
            i, j = k+1, len(nums)-1 #双指针，一个在开头的后一位，一个在结尾
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1#左边前进一位
                    while i < j and nums[i] == nums[i - 1]: i += 1#左右一样的话，多进一位，因为结果相同
                elif s > 0:
                    j -= 1#右边退回一位
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res