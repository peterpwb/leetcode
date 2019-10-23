#36 ms,用列表模仿栈
#Time:O(n)  Space:O(n)
#双set更快
class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        set1 = {"{","[","("}
        set2 = {"{}","[]","()"}
        if s[0] not in set1:
            return False
        for i in s:
            if i in set1:
                res.append(i)
            else:
                if len(res) == 0:#当前面匹配完，如右括号报错
                    return False
                elif res[-1]+i in set2:
                    res.pop()
                else:
                    return False
        return res == []

#52 ms，使用字典
#Time:O(n)  Space:O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        dict1={'(':')','[':']','{':'}'}
        res=[]#定义一个列表做栈
        for i in range(len(s)):
            if s[i] in dict1:#键在其中
                res+=[s[i]]
            else:
                if len(res)==0:
                    return False
                elif dict1[res[-1]] != s[i]:
                    return False
                else:
                    del res[-1]
        return len(res)==0