# -*- coding:utf-8 -*-
#双指针,原地调整
#这样相对位置会变化，所以不能通过
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) == 0:
            return []
        left = 0
        right = len(array)-1
        while left < right:
            while array[left]%2 != 0:#左奇一直右移直到偶数
                left += 1
            while array[right]%2 == 0:#右偶一直左移直到奇数
                right -= 1
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1
        return array


# -*- coding:utf-8 -*-
#双数组来存
#运行时间：25ms   占用内存：5724k
#Time:O(n)  Space: O(n)
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd,even = [],[]
        for i in array:
            odd.append(i) if i%2 == 1 else even.append(i)
        return odd+even