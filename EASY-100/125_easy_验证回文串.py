#56ms，filter返回的是迭代对象
# Time:  O(n) Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        res = "".join(filter(str.isalnum,s)).lower()
        return res == res[::-1]

#52ms,maketrans()的运用
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        import string
        res = str.maketrans("","",string.punctuation+" ")
        #这里没有替换，但是用到了maketrans()函数的删除功能
        s = s.translate(res).lower()
        return s == s[::-1]