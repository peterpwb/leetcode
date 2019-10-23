#python进制转换,40ms
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1],2)
        
#'{0:032b}'.format(n)将n格式化为32位无符号数,16 ms
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{0:032b}'.format(n)[::-1], 2)
        


#位运算，取出n的最低位，加入结果ans中。然后n右移，res左移。32 ms
#0左移是不变的
# Time : O(logn) = O(32)  Space: O(1)
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans=0
        i=32
        while i:
            i -= 1
            ans <<= 1
            ans += n&1
            n >>= 1
        return ans