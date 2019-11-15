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