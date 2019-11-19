# -*- coding:utf-8 -*-
#运行时间：30ms  占用内存：5752k
#计数器做法

from collections import Counter
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        res = len(numbers)//2
        dim = Counter(numbers).most_common()
        return dim[0][0] if dim[0][1] > res else 0
    
    
#方法2,遍历一遍数组，存数字和次数，相同加1，不同减1
#运行时间：31ms    占用内存：6368k
#Time:O(n), Space: O(1)
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        len_num = len(numbers)
        if len_num == 0:
            return 0
        i = numbers[0]
        j = 1
        for k in range(1,len_num):
            if j == 0:
                i = numbers[k]
                j = 1
            else:
                if numbers[k] == i:
                    j += 1
                else:
                    j -= 1
        #最后得到的数就是可能最大的数
        time = 0
        for m in range(len_num):
            if numbers[m] == i:
                time += 1
        return i if time*2 > len_num else 0
