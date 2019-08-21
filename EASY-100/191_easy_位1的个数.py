#n&(n-1)方法统计1的个数，16ms
#Time:O(1)   Space:O(1)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n>0:
            n=n&(n-1)
            ans+=1
        return ans
        
#计算过程
        00000000000000000000000000001011
        00000000000000000000000000001010
        00000000000000000000000000001010  ans=1
        
        00000000000000000000000000001010
        00000000000000000000000000001001
        00000000000000000000000000001000  ans=2
        
        00000000000000000000000000001000
        00000000000000000000000000000111
        00000000000000000000000000000000  ans=3
        
#直接统计,20ms
#Time:O(n)   Space:O(1)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
        
#直接每一位检查是不是1,28ms
#Time:O(1)   Space:O(1)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n>0:
            if n&1==1:
                ans+=1
            n>>=1
        return ans