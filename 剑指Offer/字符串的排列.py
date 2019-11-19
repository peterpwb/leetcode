#运行时间：35ms   占用内存：5752k
#迭代器的使用
# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))
 
#运行时间：32ms   占用内存：5628k
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                res.add(ss[i]+j)
        return sorted(res) # sorted()能对可迭代对象进行排序,结果返回一个新的list
