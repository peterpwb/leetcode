#168题的镜像，56ms
#Time:O(n)   Space:O(n)
class Solution:
    def titleToNumber(self, s: str) -> int:
        check = {}
        for i in range(26):
            check[chr(i+65)] = i+1
            #{'A': 1, 'B': 2, 'C': 3...}
            
        res = []
        for i in s[::-1]:
            res.append(check[i])
        dim = 0
        for i in range(len(res)):
            dim += res[i]*(26**(i))
        return dim
        
        
#pow(x,y)==x**y,52ms
#Time:O(n)   Space:O(1)
class Solution:
    def titleToNumber(self, s: str) -> int:
        num=0
        le=len(s)
        for i in range(l):
            num+=pow(26,(le-i-1))*(ord(s[i])-64)
        return num


#26进制转10进制
#Time:O(n)   Space:O(1)
class Solution(object):
    def titleToNumber(self, s):
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x)-ord('A')+1
        return ans