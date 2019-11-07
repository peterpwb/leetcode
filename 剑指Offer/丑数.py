# -*- coding:utf-8 -*-
#Time:O(n),Space: O(1)
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0：
            return 0
        res = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        #p2，p3，p5分别为三个队列的指针
        for i in range(index-1):
            new = min(res[p2]*2,res[p3]*3,res[p5]*5)
            res.append(new)
            if new % 2 == 0:
                p2 += 1
            if new % 3 == 0:
                p3 += 1
            if new % 5 == 0:
                p5 += 1
        return res[-1]