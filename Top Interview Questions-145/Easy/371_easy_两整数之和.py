#运用函数，48ms
# Time:O(1)  Space: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([b, a])
        
#44ms
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a.__add__(b)



a + b 的问题拆分为 (a 和 b 的无进位结果) + (a 和 b 的进位结果)
无进位加法使用异或运算计算得出
进位结果使用与运算和移位运算计算得出
循环此过程，直到进位为 0

PS:在 Python 中，整数不是 32 位的，也就是说你一直循环左移并不会存在溢出的现象，
这就需要手动对 Python 中的整数进行处理，手动模拟32位INT整型。

#位运算，68 ms
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 2^32
        MASK = 0x100000000#将整数对 0x100000000 取模，保证该数从 32 位开始到最高位都是 0
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1#0x80000000
        while b:
            # 计算进位
            carry = (a & b) << 1 
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)#取余再异或再取反
