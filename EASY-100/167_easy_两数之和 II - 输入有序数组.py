#函数运用，92 ms，同第一题
#Time:O(n)   Space:O(n) 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for ind,val in enumerate(numbers,start = 1):
            if target - val in res:
                return [res[target - val],ind]
            else:
                res[val] = ind
                
#双指针,116 ms
#Time:  O(n) Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end = 0,len(numbers)-1
        while start != end:
            if numbers[start]+numbers[end] > target:
                end -= 1
            elif numbers[start]+numbers[end] < target:
                start += 1
            else:
                return [start+1,end+1]