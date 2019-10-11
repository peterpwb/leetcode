#计数器1，64 ms
# Time:O(n)   Space: O(1)
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r1 = Counter(ransomNote).most_common()
        #返回一个列表[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
        m1 = Counter(magazine).most_common()
        #列表变字典
        dic1 = {}
        for i in m1:
            dic1[i[0]] = i[1]#{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
        for j in r1:
            if j[0] in dic1:
                if dic1[j[0]] >= j[1]:#数量够多
                    continue
                else:
                    return False
            else:
                return False
        return True


#计数器2，24 ms【直接是集合所以最小最快】
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        set1 = set(ransomNote)
        set2 = set(magazine)
        if set1 <= set2:
            for val in set1:
                if magazine.count(val)>=ransomNote.count(val):#直接统计每个数对应的个数
                    continue
                else: return False
            return True
            
        return False

#计数器3，56 ms
class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        #小减大为空，大减小还有东西
        #Counter(magazine) - Counter(ransomNote)--->Counter({'f': 1, 'd': 1})
        #Counter(ransomNote) - Counter(magazine)--->Counter()
