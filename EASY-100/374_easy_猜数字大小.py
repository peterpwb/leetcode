# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

#二分查找,24 ms
#Time:O(logn) Space: O(1)
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=1,n
        while l<=r:
            mid=l+(r-l)//2
            if guess(mid)==1:
                l=mid+1
            elif guess(mid)==-1:
                r=mid-1
            else:
                return mid
        return -1