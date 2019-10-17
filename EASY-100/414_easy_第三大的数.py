#88ms,遍历一次取出最大，第二大，第三大
#Time:O(n)  Space: O(1)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
            if len(nums)<3:
                return max(nums)
            first,second,third=float('-inf'),float('-inf'),float('-inf')
            for i in nums:
                if i in [first,second,third]:#已有
                    continue
                if i > first:
                    first,second,third=i,first,second#出现最大
                elif i > second:
                    second,third=i,second#第二大
                elif i >third:
                    third=i
                else:
                    continue
            if third == float('-inf'):
                return first
            return third

#复杂度O(nlgn),48ms
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res=list(sorted(set(nums)))
        if len(res)<3:
            return res[-1]
        else:
            return res[-3]