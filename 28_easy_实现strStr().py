#Time:O(n+k)  Space:O(k)
#方法一，内置函数
#52ms，index()函数，不在会抛异常
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='':
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1
            
#find()函数，52ms
#Time:O(n+k)  Space:O(k)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        return haystack.find(needle)


#方法二，切片,40ms
# Time:  O(n*k)  Space: O(k)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
#方法三，KMP算法，76ms
# Time:  O(n+k)  Space: O(k)
#匹配过程的时间复杂度为O(n)+计算next的O(m)时间=O(m + n)
class Solution:
    def strStr(self, s: str, p: str) -> int:
        if not p:
            return 0
        def get_next(p):
            next=[-1]
            j=0
            k=-1
            while j<=len(p)-1:
                if k==-1 or p[j]==p[k]:#p[k]表示前缀，p[j]表示后缀
                    k+=1
                    j+=1
                    next.append(k)
                else:
                    k=next[k]
            return next
        next=get_next(p)
        i=0
        j=0
        while j<=len(p)-1 and i<=len(s)-1:
            if s[i]==p[j] or j==-1:
                i+=1
                j+=1
            else:
                j=next[j]
        if j==len(p):
            return i-j
        else:
            return -1

