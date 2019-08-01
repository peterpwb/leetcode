#Counter类的运用，132ms
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        import collections
        return collections.Counter(nums).most_common()[-1][0]
        
#set的运用,124ms
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return res.pop()
        
#异或运算,120ms，相同的数异或为0
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res^i
        return res