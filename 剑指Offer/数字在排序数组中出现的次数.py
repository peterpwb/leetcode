#运行时间：25ms  占用内存：5732k
#Time:O(n)   Space: O(1)
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        res = 0
        for i in data:
            if i == k:
                res += 1
        return res

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)