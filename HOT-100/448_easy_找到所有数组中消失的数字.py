#484 ms,计算每个数出现的次数
#Time:O(n)    Space: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic1 = [0]*len(nums)
        for i in nums:
            dic1[i-1] += 1#[1,1,2,0,1,1,1,1]
        res = []
        for i in range(len(dic1)):
            if dic1[i] == 0:
                res.append(i+1)
        return res

#160 ms
#Time:O(n)    Space: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return []
        else:
            return list(set(range(1,len(nums)+1))-set(nums))