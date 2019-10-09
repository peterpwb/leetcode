#调用函数，48 ms
#Time:O(n)   Space: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))#集合可以做交，并的操作