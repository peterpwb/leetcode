# -*- coding:utf-8 -*-
#运行时间：43ms  占用内存：5752k
#Time:O(n)  Space: O(1)
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        sum = 0
        for i in range(1,n+1):
            sum += str(i).count("1")
        return sum
        
        
#运行时间：39ms   占用内存：5740k
# -*- coding:utf-8 -*-
#Time:O(logn)一个数字有O(logn)位  Space: O(1)
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        count = 0
        i = 1
        while i <= n:
            dim = i*10
            count += (n//dim)*i + min(max(n%dim-i+1,0),i)
            i *= 10
        return count