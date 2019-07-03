#按位取反
class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x>0:
            while x!=0:
                rev=rev*10+x%10
                x=x//10
        else:
            x=x*-1
            while x!=0:
                rev=rev*10+x%10
                x=x//10
            rev=rev*-1

        if rev>(2**31)-1 or rev<-(2**31):
            return 0
        else:
            return rev

#转字符串直接转
class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=int(str(x)[::-1])
            if x>(2**31)-1:
                return 0
            else:
                return x
        else:
            x=x*-1
            x=int(str(x)[::-1])
            if -x<-2**31:
                return 0
            else:
                return -x
            
