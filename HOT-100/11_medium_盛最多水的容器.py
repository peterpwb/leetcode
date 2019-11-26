#双指针，左右遍历
#Time:O(n)   Space:O(l)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height)-1
        while i < j:
            res=max(res,min(height[i],height[j])*(j-i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return res