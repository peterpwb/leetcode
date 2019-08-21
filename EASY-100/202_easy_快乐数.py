#最终肯定会变成循环，不是1就是 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 
# Time : O(n)  Space: O(n)
class Solution:
    def isHappy(self, n: int) -> bool:
        res = {1}
        while n not in res:
            res.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n==1