#自带函数
#运行时间：29ms  占用内存：5692k

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            ss=float(s)
            return True
        except:
            return False
            
            
#正则化
# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        return re.match(r"^[\+|\-]?[0-9]*(\.[0-9]*)?([e|E][\+\-]?[0-9]+)?$",s)