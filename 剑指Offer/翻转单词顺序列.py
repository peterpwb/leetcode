# -*- coding:utf-8 -*-
#运行时间：25ms  占用内存：5624k
#Time:O(n), Space: O(n)
class Solution:
    def ReverseSentence(self, s):
        # write code here
        res = s.split(" ")[::-1]
        return " ".join(res) if res else ""