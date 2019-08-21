#滑动窗口,116 ms
# Time : O(n)  Space: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        res = 0
        dim = set()
        while i < len(s) and j <len(s):
            if s[j] not in dim:
                dim.add(s[j])
                j += 1
                res = max(res,j-i)
            else:
                dim.remove(s[i])
                i += 1
        return res