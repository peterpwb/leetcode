#48 ms,注意是否为空即可s.isspace():#只为空格组成
# Time:  O(n)   Space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(s.split())[-1]) if list(s.split())!=[] else 0