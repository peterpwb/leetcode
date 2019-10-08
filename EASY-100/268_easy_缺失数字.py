#Time:O(n)   Space:O(1)
#64ms,全部数相加，再对比等差数列求和差的值就是少的数
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        for i in nums:
            sum+=i
        res=((len(nums)+1)*len(nums))//2
        return res-sum

#Time:O(n)   Space:O(n)
#64ms，全部排列然后找差的,集合可以直接相减，也可以做交并
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums)+1)) - set(nums)).pop()


#64ms,异或计算，不必考虑溢出
#Time:O(n)   Space:O(1)
#0^4 = 4,   4^4 = 0,   1^1^2^2^3 = 3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)
        for i in range(res):
            res^=nums[i]
            res^=i
        return res