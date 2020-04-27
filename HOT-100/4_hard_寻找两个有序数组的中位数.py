#56 ms 
#https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/shuang-zhi-zhen-by-powcai/
#https://blog.csdn.net/chen_xinjia/article/details/69258706
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)#确保nums1短
        k = (n1 + n2 + 1)//2
        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left)//2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"),nums2[m2-1] if m2 >0 else float("-inf"))
        if (n1+n2)%2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"),nums2[m2] if m2 < n2 else float("inf"))
        return (c1+c2)/2
        
#76 ms
class Solution:
    def get_kth(self, nums1, nums2, k):
        # print(nums1, nums2, 'k=', k)
        m, n = len(nums1), len(nums2)
        if m == 0: return nums2[k-1]
        if n == 0: return nums1[k-1]
        if k == 1: return min(nums1[0], nums2[0])
        drop1, drop2 = min(k//2, m), min(k//2, n)   # 丢弃个数
        # print('m={},n={},k/2={},drop1={},drop2={}'.format(m,n,k//2,drop1,drop2))
        if nums1[drop1-1] <= nums2[drop2-1]:  # 丢弃nums1部分
            return self.get_kth(nums1[drop1:m], nums2, k-drop1)
        else:
            return self.get_kth(nums1, nums2[drop2:n], k-drop2)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # 整合奇偶数情况
        mid_left = self.get_kth(nums1, nums2, (m+n+1)//2)
        mid_right = self.get_kth(nums1, nums2, (m+n+2)//2)
        return (mid_left+mid_right)/2