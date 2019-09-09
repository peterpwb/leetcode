#32ms，循环
# Time:O(n)  Space: O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(int(i) for i in str(num))#列表生成式
        return num
        
 
#找规律
# Time:O(1)  Space: O(1)
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
            
        return 9 if num%9==0 else num%9