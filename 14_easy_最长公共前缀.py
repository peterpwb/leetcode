#方法1,56ms
#Time:  O(n * k), k is the length of the common prefix  Space:O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        if len(strs)==0:
            return res
            
        if len(strs)==1:
            return strs[0]
            
        minlen=len(strs[0])
        #取字符串中的最小长度
        for i in range(1,len(strs)):
            if minlen>len(strs[i]):
                minlen=len(strs[i])
                
        for i in range(minlen):
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    return res
            res+=strs[0][i]
        return res
        

#方法2,zip()函数,*的使用
class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for chars in zip(*strs):
            if all(c == chars[0] for c in chars):
                prefix += chars[0]
            else:
                return prefix
        return prefix

