# Time:(logn)   Space: O(1)
#自己的做法，44 ms
#任何该进制的都可以这么做

class Solution:
    def toHex(self, num: int) -> str:
        dic1 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 
    	8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        res = ""
        if num == 0:
            return '0'
        else:
            if num<0:#补码
                num+=2**32
            while num>0:
                res += dic1[num%16]
                num//=16
            return res[::-1]