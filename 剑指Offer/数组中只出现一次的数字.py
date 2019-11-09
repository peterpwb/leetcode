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
        
#位运算，首先异或一次得到结果，结果是两个不同的数所以不为0，计算1所在的位置
#然后按着1位置的不同，将结果分到两组再次异或，得到结果
#运行时间：27ms    占用内存：5624k
class Solution:
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        temp = 0
        for i in array:
            temp ^= i
        index = 0
        while (temp&1) == 0:
            temp >>= 1
            index += 1
        a = b = 0
        for i in array:
            if self.check(i,index):
                a ^= i
            else:
                b ^= i
        return [a,b]
    def check(self,num,index):
        num = num >> index
        return num&1
        
#运行时间：31ms  占用内存：5752k
#统计1的方法一致就行
class Solution:
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        temp = 0
        for i in array:
            temp ^= i
        index = bin(temp)[2:][::-1].index("1")
        a = b = 0
        for i in array:
            if self.check(i,index):
                a ^= i
            else:
                b ^= i
        return [a,b]
    def check(self,num,index):
        return index == bin(num)[2:][::-1].index("1")
