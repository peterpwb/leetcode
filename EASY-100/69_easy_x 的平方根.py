#二分法，公式(a+b)/2 >=√ab
#68 ms, Time:O(logn)  Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r**2>x:
            r= (r+x/r)//2
        return int(r)