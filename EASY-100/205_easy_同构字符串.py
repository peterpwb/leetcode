#自己的做法，36ms，单向只能确定A对B键值一一对应，不能查到值是否有重复
# Time:  O(n)  Space: O(1)
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        return self.check(s,t) and self.check(t,s)#正反查
        
    def check(self,a,b):
        res={}
        for i in range(len(a)):
            if a[i] == b[i]:#必须换值
                return False
            if a[i] not in res:
                res[a[i]]=b[i]
            else:
                if res[a[i]]!=b[i]:
                    return False
        return True
#方法2,40ms
# Time:  O(n)  Space: O(1)
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] != t[i]:
                return False
            if s[i] not in d and t[i] in d.values():#可以检查值是否在字典内
                return False
            d[s[i]] = t[i]
        return True