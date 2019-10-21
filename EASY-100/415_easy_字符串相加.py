#双指针，每一位的数相加，56 ms
#Time:O(n)[两个字符串较长的那个]   Space: O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i,j,dim = len(num1)-1,len(num2)-1,0
        #从尾部开始，dim0/1判断是否进1
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0#到头了就用0填充
            n2 = int(num2[j]) if j >= 0 else 0
            temp = n1 + n2 +dim
            dim = temp//10
            res = str(temp%10) + res
            i -= 1
            j -= 1
        return "1"+res if dim else res#首位是否有进位
            
