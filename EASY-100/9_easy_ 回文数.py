#88 ms,数字转字符
#Time:O(1)   Space:O(1) 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

#同84 ms，按位取反
#Time:O(1)   Space:O(1) 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or  x % 10 == 0 and x != 0: return False#尾带0不行
        r = 0
        res = x
        while res:
            r = r*10 + res % 10
            res = res // 10
        return x == r




