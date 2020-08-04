class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        a = list(permutations(nums,len(nums)))
        res = []
        for i in a:
            if i in res:
                continue
            else:
                res.append(i)
        return res