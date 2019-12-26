#运行时间：29ms  占用内存：5712k
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        numlist=['0','1','2','3','4','5','6','7','8','9','+','-']
        sum=0
        label=1#正负数标记
        if s=='':
            return 0
        for string in s:
            if string in numlist:#如果是合法字符
                if string=='+':
                    label=1
                    continue
                if string=='-':
                    label=-1
                    continue
                else:
                    sum=sum*10+numlist.index(string)
            if string not in numlist:#非合法字符
                sum=0
                break#跳出循环
        if label == 1:#判断溢出
            return sum if sum <= 2147483647 else 0
        if label == -1:
            return -sum if sum <= 2147483648 else 0

        
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        try:
            return int(s)
        except Exception as e:
            return 0
