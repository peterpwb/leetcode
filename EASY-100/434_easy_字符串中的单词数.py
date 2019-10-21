#40ms
#Time:O(n)  Space: O(1)
class Solution:
    def countSegments(self, s: str) -> int:
        res=s.split(' ')
        conv=0
        for i in range(len(res)):
            if res[i]!='':
                conv+=1
        return conv
        
#40 ms
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())