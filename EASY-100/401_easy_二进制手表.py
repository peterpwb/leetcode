#56ms
#Time:O(1)   Space: O(1)
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        dec=[]
        for i in range(12):
            for j in range(60):
                if self.count1(i)+self.count1(j)==num:
                    dec.append('%d:%02d'%(i,j))
        return dec
    
    #计算二进制中1的个数
    def count1(self,n:int):
        res=0
        while n!=0:
            n= n&(n-1)#常用方法
            res+=1
        return res
        
        
#48ms,直接统计每个数字对应的二进制有多少个1
class Solution:
    def readBinaryWatch(self, num):
        bins = [str(bin(i))[2:].count('1') for i in range(60)]
        results = []
        for hour in range(12):
            for minute in range(60):
                if bins[hour] + bins[minute] == num:
                    results.append('%d:%02d'%(hour, minute))
        return results