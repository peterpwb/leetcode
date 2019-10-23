#44 ms  enumerate()函数（索引，值）字典模仿哈希表
#Time:O(n)   Space:O(n)  (遍历)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        dic_index = {}
        for key,val in enumerate(nums):
            if target-val in dic_index:
                return [dic_index[target-val],key]
            else:
                dic_index[val]=key
