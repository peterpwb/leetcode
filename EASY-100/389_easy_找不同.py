#计数器的应用,40ms
# Time:O(n)   Space: O(1)
import collections
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list(collections.Counter(t) - collections.Counter(s))[0]

#异或做法
#Time:O(n)   Space: O(1)
class Solution(object):
    def findTheDifference(self, s, t):
        res=0
        for i in s:
            res=res^ord(i)
        for i in t:
            res=res^ord(i)
        return chr(res)