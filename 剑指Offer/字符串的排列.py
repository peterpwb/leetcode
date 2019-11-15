#运行时间：35ms   占用内存：5752k
#迭代器的使用
# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))
        
