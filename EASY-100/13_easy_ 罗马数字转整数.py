#76 ms,两位做比较
#Time:O(n)  Space:O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        res,i=0,0
        dic1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        dic2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        while i < len(s):
            if i < len(s)-1 and s[i:i+2] in dic2:#确保剩两位
                res += dic2[s[i:i+2]]
                i += 2
            else:
                res += dic1[s[i]]
                i += 1
        return res