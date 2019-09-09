#自己的做法，速度偏慢因为在除2，44ms
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        while n%2==0:
            n=n//2
        return n == 1

# Time:  O(1)  Space: O(1)
#位运算符，28ms
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        return (n & (n - 1)) == 0
#2的幂次方在二进制下，只有1位是1，其余全是0。
所以减1的二进制，按位与运算符不会出现同一个位置的1

#位运算符，20ms
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        elif n==1:
            return True
        else:
            return (n & (-n)) == n
            
#2的幂次方在二进制下，只有1位是1，其余全是0。
例如:8---00001000。负数的在计算机中二进制表示为补码
(原码->正常二进制表示，原码按位取反(0-1,1-0)，最后再+1。
然后两者进行与操作，得到的肯定是原码中最后一个二进制的1。
例如8&(-8)->00001000 & 11111000 得 00001000，即8。 
建议自己动手算一下，按照这个流程来一遍，加深印象。