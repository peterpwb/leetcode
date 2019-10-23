#短的可以，长的超时,计数器为0也不会消失
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        for i in range(len(s)-len(p)+1):
            if collections.Counter(s[i:i+len(p)])==collections.Counter(p):
                res.append(i)
        return res


#136ms
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if s == "":
            return []
        output  = []
        correctdict = dict()
        tempdict = dict()
        for i in s+p:
            if i not in correctdict:
                correctdict[i] = 0
                tempdict[i] = 0
            
        for i in p:
            correctdict[i] += 1
                
        for i in s[0:len(p)]:
            tempdict[i] += 1
        if tempdict == correctdict:
            output.append(0)  
            
        for i in range(len(s) - len(p)):
            tempdict[s[i]] -= 1
            tempdict[s[i + len(p)]] += 1
            if tempdict == correctdict:
                output.append(i + 1)
        return output
        
        
#164ms，这个比较好理解一点
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        dic1 = [0]*26
        dic2 = [0]*26
        res = []
        for i in range(len(p)):#p长度中26个字母分别出现了几次
            dic1[ord(p[i])-ord('a')] += 1
            dic2[ord(s[i])-ord('a')] += 1
        if dic1 == dic2:#出现的一样就加0，因为是无序排列
            res.append(0)
        for i in range(1, len(s)-len(p)+1):#向右移动一位
            dic2[ord(s[i-1])-ord('a')] -= 1
            dic2[ord(s[i+len(p)-1])-ord('a')] += 1
            if dic1 == dic2:
                res.append(i)
        return res
        
#204ms
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_p = {}
        for i in p:
            dict_p[i] = dict_p.get(i,0) + 1#get方法取键对应的值，有则返回没有则返回0
        dict_s = {}
        list_n = []
        len_p = len(p)
        for i ,val in enumerate(s):
            dict_s[val] = dict_s.get(val,0) + 1
            if dict_s == dict_p:
                list_n.append(i - len_p + 1)
            if i - len_p + 1 >= 0:
                dict_s[s[i - len_p + 1]] = dict_s.get(s[i - len_p + 1]) - 1
                if dict_s[s[i - len_p + 1]] == 0:
                    del dict_s[s[i - len_p + 1]]
        return list_n

#滑动窗口，96 ms
class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        res = []
        window = {}     # 记录窗口中各个字符数量的字典
        needs = {}      # 记录目标字符串中各个字符数量的字典
        for c in p: needs[c] = needs.get(c, 0) + 1  # 统计目标字符串的信息

        length, limit = len(p), len(s)
        left = right = 0                    # 定理两个指针，分别表示窗口的左、右界限

        while right < limit:
            c = s[right]
            if c not in needs:              # 当遇到不需要的字符时
                window.clear()              # 将之前统计的信息全部放弃
                left = right = right + 1    # 从下一位置开始重新统计，右移一位
            else:
                window[c] = window.get(c, 0) + 1            # 统计窗口内各种字符出现的次数
                if right-left+1 == length:                  # 当窗口大小与目标字符串长度一致时
                    if window == needs: res.append(left)    # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                    window[s[left]] -= 1                    # 并将移除的字符数量减一
                    left += 1                               # left右移
                right += 1                                  # right右移
        return res

