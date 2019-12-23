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
        if sum == 2147483649 or sum == 2147483648:
            return 0
        return sum*label


# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s)==0:
            return 0
        else:
            if s[0]>'9' or s[0]<'0':
                a=0
            else:
                a=int(s[0])*10**(len(s)-1)
            if len(s)>1:
                for i in range(1,len(s)):
                        if s[i]>='0' and s[i]<='9':
                            a=a+int(s[i])*10**(len(s)-1-i)
                        else:
                            return 0
        if s[0]=='+':
            return a
        if s[0]=='-':
            return -a
        return a
        
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        try:
            return int(s)
        except Exception as e:
            return 0