#自己的方法1，直接求和加一,76 ms
# Time:  O(n)   Space: O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=0
        for i in range(len(digits)):
            s=s+digits[i]*(10**(len(digits)-i-1))
        s+=1
        res=list(map(int,str(s)))
        return res
        
        
#一行解决,类似方法1,56 ms
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int,str(int(''.join(map(str,digits)))+1)))

#自己的方法2，将数倒过来,40ms
# Time:  O(n)   Space: O(n)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1]
        digits[0] += 1
        i = 0
        while i < len(digits)-1:
            if digits[i] == 10:
                digits[i] = 0
                digits[i+1] += 1
                i += 1
            else:
                return digits[::-1]
        if digits[-1] == 10:
            digits[-1] =0
            digits.append(1)
        return digits[::-1]