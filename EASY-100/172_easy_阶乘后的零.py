#有一个5就有一个0,56 ms
# Time:  O(logn) = O(1),Space: O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            count += n//5
            n //= 5
        return count
        
        
#递归,44 ms
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        return n//5 + self.trailingZeroes(n//5)