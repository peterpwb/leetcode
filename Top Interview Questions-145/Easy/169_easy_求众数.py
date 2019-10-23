#直接去中位数（题目要求可以达到），做算法题最好不要用现成的api，244 ms
#Time:O(nlgn) Space:O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==0:
            return None
        return sorted(nums)[len(nums)//2]

#分治，352 ms
#Time:O(nlgn) Space:O(nlgn)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums[0]
        a=self.majorityElement(nums[:len(nums)//2])
        b=self.majorityElement(nums[len(nums)//2:])
        if a==b:
            return a
        if nums.count(a)>len(nums)//2:
            return a
        else:
            return b
            

#284ms，Counter类
#Time:O(n) nums迭代一次 Space:O(n)哈希表最多包含n-n/2个关系，所以占用的空间为 O(n)
class Solution:
    def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
        return collections.Counter(nums).most_common(1)[0][0]
        
#摩尔投票，252ms
#Time:O(n) Space:O(1)
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

