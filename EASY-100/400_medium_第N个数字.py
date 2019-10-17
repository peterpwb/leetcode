#44 ms
# Time:  O(logn)   Space: O(1)
#1-9有9个数，10-99有209个数字，100-999有3009个数字，1000-9999有4000*9个数字
#即 9 * pow(10, i - 1) * i， i为数值位数

class Solution:
    def findNthDigit(self, n: int) -> int:
    	num = 0
    	i = 1
    	while(n > num + i * 9 * 10 ** (i - 1)):
    		num += i * 9 * 10 ** (i - 1)
    		i += 1#得到i和num
    	a = 10 ** (i - 1) - 1 + (n - num) // i
    	b = (n - num) % i
    	if b == 0:
    		return a % 10
    	else:
    		a += 1
    		return (a // 10 ** (i - b)) % 10