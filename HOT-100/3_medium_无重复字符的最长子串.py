#滑动窗口,76ms
# Time: O(n)  Space: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        maxlen = 0
        length = len(s)
        res = set()#用来存无重复字母
        while end < length:
            if s[end] not in res:#没有该字母
                res.add(s[end])
                end += 1
                maxlen = max(maxlen,end-start)#取两者中长的那个
            else:
                res.remove(s[start])#如果没删到重复元素会一直删
                start += 1
        return maxlen
