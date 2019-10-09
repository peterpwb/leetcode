#将前N项和存入target，最后直接从target里面找，76ms
#Time:O(n)   Space: O(n)
class NumArray:
    def __init__(self, nums: List[int]): 
        self.nums = nums
        sum_=0
        n = len(nums)
        target =[]
        for i in range(n):
            sum_ += nums[i]
            target.append(sum_)
        self.target = target
    def sumRange(self, i: int, j: int) -> int:            
        return self.target[j]-self.target[i]+self.nums[i]
        



#把前i个数求和放在nums[i-1]位置,92ms
#Time:O(n)   Space: O(1)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(len(self.nums)):
            if i > 0:
                self.nums[i] = self.nums[i]+self.nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if i>0:
            return self.nums[j]-self.nums[i-1]
        else:
            return self.nums[j]




#原始方法，时间久,1432ms
#Time:O(n)   Space: O(1)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j + 1])