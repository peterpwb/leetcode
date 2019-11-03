# -*- coding:utf-8 -*-
#从左下开始找，大于target上移，小于target右移
#285 ms  5632K
#Time:O(n)[rows,cols长的那个]   Space:O(1) 
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        #row是行，column是列
        rows = len(array)-1
        cols = len(array[0])-1
        i = rows
        j = 0
        while j <= cols and i >= 0:
                if array[i][j] > target:
                    i -= 1
                elif array[i][j] < target:
                    j += 1
                else:
                    return True
        return False