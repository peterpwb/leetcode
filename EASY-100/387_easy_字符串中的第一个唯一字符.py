#自己的方法1，字符串统计方法，56ms
# Time:O(n)   Space: O(n)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        set1=set(s)
        res = []
        for i in set1:
            if s.count(i) == 1:
                res.append(s.index(i))
        if res:
            return min(res)
        else:
            return -1
            
            
#自己的方法2，计数器，76 ms
# Time:O(n)   Space: O(n)
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        r1 = Counter(s).most_common()
        #返回一个列表[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
        res = []
        for i in r1:
            if i[1] == 1:
                res.append(i[0])#['c','d']
        dim = []
        for i in res:
            dim.append(s.index(i))
        if dim:
            return min(dim)
        else:
            return -1


#44 ms
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
        