#set检查有无重复,172 ms
# Time : O(n)  Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
#哈希表,188 ms
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for i in nums:
            if i in res:
                return True
            else:
                res.add(i)
        return False