# -*- coding:utf-8 -*-

#利用zip函数旋转矩阵
#可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
#输出并删除第一行后，再进行一次逆时针旋转,然后重复操作
#运行时间：38ms   占用内存：5760k
# Time:O(n)   Space: O(n)
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list,zip(*matrix)))[::-1]
        return res
