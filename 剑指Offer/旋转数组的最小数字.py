# -*- coding:utf-8 -*-
#题意需要充分利用两个有序数组

#分为前后两个有序数组，遍历出现小值即为最小值
#Time:O(n)  Space:O(1) 
#688 ms  5856K

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        for i in range(length-1):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
                
# -*- coding:utf-8 -*-
#二分查找寻找最小值
#Time:O(logn) Space: O(1)
#652 ms  5984K
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        left = 0
        right = length -1
        while left < right:
            mid = left + (right - left)//2
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:#如[1,0,1,1,1]，只能一个个试
                right -= 1
        return rotateArray[left]