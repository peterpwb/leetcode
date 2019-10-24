#1412 ms，把每个字母当成回文串的中心
#马拉车算法，不管回文是奇数还是偶数，前后和间隔都加上#就肯定变偶数了，最后再去掉
#Time:O(n)  Space: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        def helper(i,j):
            while i >= 0 and j < n and s[i] == s[j]:#注意是大于等于0
                i -= 1
                j += 1
            if len(self.res) < j - i -1 :
                #如果长度更长就更新，注意减一
                #检查的时候可以就按只有一个元素检查是否正确，左右都移一位但是不对所以只留一个值
                self.res = s[i+1:j]
        for i in range(n):#从每个元素开始遍历一次，每个元素中心扩展
            helper(i,i)
        return self.res.replace('#',"")
