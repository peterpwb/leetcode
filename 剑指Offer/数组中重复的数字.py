# -*- coding:utf-8 -*-
#运行时间：29ms   占用内存：6580k
#Time:O(n)   Space: O(n)
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        res = []
        for i in numbers:
            if i not in res:
                res.append(i)
            else:
                duplication[0] = i
                return True
        return False
        
        
#所以可以利用现有数组设置标志，当一个数字被访问过后,
#可以设置对应位上的数 + n，之后再遇到相同的数时，会发现对应位上的数已经大于等于n了，那么直接返回这个数即可
#运行时间：31ms  占用内存：5752k
#Time:O(n)   Space: O(1)
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers is None or numbers == []:
            return False
        index = 0
        while index < len(numbers):
            if numbers[index] == index:
                index += 1
            elif numbers[index] == numbers[numbers[index]]:
                duplication[0] = numbers[index]
                return True
            else:
                index_2 = numbers[index]
                numbers[index],numbers[index_2] = numbers[index_2],numbers[index]
        return False
