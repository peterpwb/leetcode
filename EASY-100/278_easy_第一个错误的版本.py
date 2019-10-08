# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#双指针
#Time:O(logn) 二分查找   Space:O(1)
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left+(right-left)//2 #防止溢出
            if isBadVersion(mid):#错误版本
                right = mid
            else:
                left = mid + 1
        return left