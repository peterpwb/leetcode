#字典
# Time:  O(logn)  Space: O(1)
class Solution:
    def convertToTitle(self, n: int) -> str:
        check = {}
        for i in range(26):
            check[i+1] = chr(i+65)
        #{1: 'A', 2: 'B', 3: 'C', 4: 'D',...}
        res = []
        while n!= 0:
            if n-(n//26)*26 != 0:
                res.append(n-(n//26)*26)
                n = n//26
            else:
                res.append(26)
                n = int((n/26)-1)
        pop= ""
        for i in res[::-1]:
            pop += check[i]
        return pop

#40ms
#26进制的问题，映射关系却是从[1, 26] 因此,重新建立一个映射从[0, 25]
class Solution(object):
    def convertToTitle(self, n):
        ans = ''
        while n > 0:
            n -= 1#核心
            ans += chr((n)%26+ord('A'))
            #(n - 1) % 26得到的就是[0, 25]之间的数字
            n //= 26
        return ans[::-1]