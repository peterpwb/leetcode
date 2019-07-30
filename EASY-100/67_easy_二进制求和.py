#自己之前的做法，56ms
# Time:  O(n)   Space: O(1)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=str(int(a)+int(b))
        res=list(map(int,c))#如[1,1,2]
        if len(res)==1:
            if res==[0]:
                return "0"
            elif res==[1]:
                return "1"
            else:
                return "10"
        for i in reversed(range(1,len(res))):
            if res[i]==2:
                res[i]=0
                res[i-1]+=1
            elif res[i]==3:
                res[i]=1
                res[i-1]+=1
            else:
                continue
        if res[0]==1:
            return ("".join('%s' %id for id in res))
        elif res[0]==2:
            res[0]=0
            res=[1]+res
            return ("".join('%s' %id for id in res))
        else:
            res[0]=1
            res=[1]+res
            return ("".join('%s' %id for id in res))

#二进制转十进制再转二进制,52ms
# Time:  O(1)   Space: O(1)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = int(a, 2)
        j = int(b, 2)
        return "{:b}".format(i + j)
        
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]