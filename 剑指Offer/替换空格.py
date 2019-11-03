# -*- coding:utf-8 -*-

#这题需要问清楚是在原字符串上修改还是创建新的来替换
#如果是原地修改需要从后往前，这样移动的次数少

#新建，用函数切分，然后再组合
#27 ms  5676K
#Time:O(n)   Space:O(n) 
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = []
        for i in s:
            if i != " ":
                res.append(i)
            else:
                res.append("%20")
        return "".join(res)
        
#内置函数
# -*- coding:utf-8 
-*-class Solution:    
# s 源字符串    
    def replaceSpace(self, s):
        return "%20".join(list(s.split(" ")))