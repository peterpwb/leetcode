# -*- coding:utf-8 -*-
#运行时间：28ms  占用内存：5624k
#常规做法
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = []
        for i in array:
            if i in res:
                res.remove(i)
            else:
                res.append(i)
        return res
