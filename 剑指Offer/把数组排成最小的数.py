# -*- coding:utf-8 -*-
#迭代器的使用
#运行时间：29ms   占用内存：5736k

import itertools
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        nums = []
        list_num = list(itertools.permutations(numbers,len(numbers)))#第2个参数是元组长度
        #全排列，[3,32,321]--->[(3, 32, 321), (3, 321, 32), (32, 3, 321), (32, 321, 3), (321, 3, 32), (321, 32, 3)]
        for item in list_num:
            num = ''.join(map(str,item))
            nums.append(num)
        return min(map(int,nums))

# -*- coding:utf-8 -*-
#pyhton2做法，python3移除cmp函数【有两个参数】，key只有一个参数
#运行时间：30ms  占用内存：7340k
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        num=map(str,numbers)
        num.sort(lambda x,y:cmp(x+y,y+x))
        return ''.join(num)
        
#python3做法
#运行时间：33ms   占用内存：5752k
import sys
from functools import cmp_to_key
class Solution:
    def PrintMinNumber(self, numbers):
        def cmp_new(x,y):
            if x+y > y+x:
                return 1
            elif x+y <y+x:
                return -1
            else:
                return 0
        num=list(map(str,numbers))
        num.sort(key=cmp_to_key(cmp_new))#key只能有一个参数
        return ''.join(num)