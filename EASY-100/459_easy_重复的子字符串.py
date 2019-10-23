1.一个字符串如果符合要求，则该字符串至少由2个子串组成。例：b b / abc abc【4个子串可以视为2个更长一点的子串】


2.s+s。以后，则该字符串至少由4个子串组成 bb+bb / abcabc+abcabc


3.截去首尾各一个字符s[1:-1] （注：只截一个是为了判断类似本例，重复子串长度为1的情况。当重复子串长度大于1时，任意截去首尾小于等于重复子字符串长度都可）


4.由于s+s组成的4个重复子串被破坏了首尾2个，则只剩下中间两个 b bb b。此时在判断中间两个子串组成是否等于s，若是，则成立。

#48 ms
# Time:O(n)  Space: O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1: -1].find(s) != -1

   