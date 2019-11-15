# -*- coding:utf-8 -*-
#运行时间：31ms  占用内存：5740k

class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(1,n+1)))
        
#逻辑与的短路特性实现递归终止
#逻辑与有个短路特点，前面为假，后面不计算
#1.需利用逻辑与的短路特性实现递归终止。 
#2.当n==0时，(n>0)&&((sum+=Sum_Solution(n-1))>0)只执行前面的判断，为false，然后直接返回0；
#3.当n>0时，执行sum+=Sum_Solution(n-1)，实现递归计算Sum_Solution(n)。
class Solution:
    def Sum_Solution(self, n):
        sum = n
        sum += Sum_Solution(n-1)
        ans = (n>0) && (sum>0)
        return sum
