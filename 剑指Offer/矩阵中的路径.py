#运行时间：26ms  占用内存：5840k
# -*- coding:utf-8 -*-
#回溯法
#遍历矩阵中的每一个位置
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.exist_helper(x, i, j, path):
                    return True
        return False
    def exist_helper(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            if not p[1:]:
                return True
            matrix[i][j] = ''
            if i > 0 and self.exist_helper(matrix, i-1, j, p[1:]):
                return True
            if i < len(matrix)-1 and self.exist_helper(matrix, i+1, j ,p[1:]):
                return True
            if j > 0 and self.exist_helper(matrix, i, j-1, p[1:]):
                return True
            if j < len(matrix[0])-1 and self.exist_helper(matrix, i, j+1, p[1:]):
                return True
            matrix[i][j] = p[0]
            return False
        else:
            return False