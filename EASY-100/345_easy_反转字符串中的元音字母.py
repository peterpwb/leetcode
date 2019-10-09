#双指针,72 ms
#Time:O(n)   Space: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        set1 = {"a","e","i","o","u","A","E","I","O","U"}
        left = 0
        right = len(s)-1
        res = list(s)
        while left<right:
            if res[left] in set1 and res[right] in set1:
                temp = res[left]
                res[left] = res[right]
                res[right] = temp
                left += 1
                right -= 1
            if res[left] not in set1:
                left += 1
            if res[right] not in set1:
                right -= 1
        return "".join(res)
        
 