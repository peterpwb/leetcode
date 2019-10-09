#原始方法，88ms
#Time:O(^2)   Space:O(1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in nums1:
            if i in nums2:
                a.append(i)
                nums2.remove(i)
        return a
        
#计数器方法,88ms
#Time:O(^2)   Space:O(n)[min(m, n)]
class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		from collections import Counter
		if not nums1 or not nums2:
			return []
		a=Counter(nums1)
		b=Counter(nums2)
		res=a&b#可做交集
		return list(res.elements())#有多少个，就返回多少个
        
        
#类似方法,60ms
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        output = []
        for key in c1:
            if key in c2:
                output += [key]* min(c1[key], c2[key])
                
        return output
        
        
Q1: What if the given array is already sorted? How would you optimize your algorithm?
如果已经排好序的话，肯定使用双指针来解决问题了。譬如说是从小到大排序的两个list——nums1和nums2，
那么指针a和b分别指向nums1和nums2的起始位置，然后分三种情况处理：

    若data(a) == data(b)，则两个指针分别右移a++; b++
    若data(a) < data(b)，则 a++
    若data(a) > data(b)，则 b++
    以此规则，直到有一个指针指到list的结束位置

Q2: What if nums1's size is small compared to nums2's size? Which algorithm is better?
如果知道nums1长度更短这个条件的话，那就是先统计nums1中的元素个数，再统计nums2的元素个数


