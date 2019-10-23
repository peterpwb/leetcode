#直接运用统计函数，56ms
# Time:  O(n)Space: O(n)
class Solution3(object):
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    import collections
    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
        
        

        
#字典的做法，判断每个字符出现的次数 36ms
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = {}
        tMap = {}
        
        for i in s:
            if i in sMap:
                sMap[i] += 1
            else:
                sMap[i] = 1
        
        for i in t:
            if i in tMap:
                tMap[i] += 1
            else:
                tMap[i] = 1
        
        return sMap == tMap
        
        
#56ms，利用sorted()可以给字母排序
# Time:  O(nlogn)  Space: O(n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s)==sorted(t)
        #例如sorted('dscdv')=['c', 'd', 'd', 's', 'v']返回数组