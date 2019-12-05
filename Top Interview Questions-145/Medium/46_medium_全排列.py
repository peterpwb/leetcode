#迭代器的使用，40ms
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        return list(itertools.permutations(nums))
        
        
#回溯法1,40 ms
# Time:  O(n * n!)   Space: O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums,tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],tmp+[nums[i]])
        backtrack(nums,[])
        return res
        
#回溯法2,44ms
class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []

        used = [False] * len(nums)
        res = []
        self.__dfs(nums, 0, [], used, res)
        return res
        
    def __dfs(self, nums, index, pre, used, res):
        # 先写递归终止条件
        if index == len(nums):
            res.append(pre.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                # 如果没有用过，就用它
                used[i] = True
                pre.append(nums[i])

                # 在 dfs 前后，代码是对称的
                self.__dfs(nums, index + 1, pre, used, res)

                used[i] = False
                pre.pop()