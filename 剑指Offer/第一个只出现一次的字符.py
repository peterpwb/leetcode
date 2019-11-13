# -*- coding:utf-8 -*-
#自己的做法：计数器做法。当多个元素计数值相同时，排列是无确定顺序的
#运行时间：41ms   占用内存：5752k
#Time:O(n)   Space: O(1)
#用于统计各元素个数的数组长度固定，所以视该算法的空间复杂度为O(1)
from collections import Counter
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dim = Counter(s).most_common()
        res = []
        #返回一个列表[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
        for i in dim:
            if i[1]==1:
                res.append(i[0])
        if len(res) == 0:
            return -1
        return min(list(map(lambda x:s.index(x),res)))#函数运用
        
        
#运行时间：35ms  占用内存：5752k
class Solution:
    def FirstNotRepeatingChar(self, s):
        tmp = list(filter(lambda x:s.count(x)==1,s))
        return -1 if len(tmp)==0 else s.index(tmp[0])