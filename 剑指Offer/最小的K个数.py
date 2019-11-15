# -*- coding:utf-8 -*-
#运行时间：26ms  占用内存：5724k
#Time:O(nlogn)   Space: O(1)
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]
        
#快速排序
#运行时间：32ms   占用内存：5624k
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            left = quick_sort([x for x in lst[1: ] if x < pivot])
            right = quick_sort([x for x in lst[1: ] if x >= pivot])
            return left + [pivot] + right
 
        if tinput == [] or k > len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[: k]
        
#归并排序
#运行时间：28ms   占用内存：5624k
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def merge_sort(lst):
            if len(lst) <= 1:
                return lst
            mid = len(lst) // 2
            left = merge_sort(lst[: mid])
            right = merge_sort(lst[mid:])
            return merge(left, right)
        def merge(left, right):
            l, r, res = 0, 0, []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            res += left[l:]
            res += right[r:]
            return res
        if tinput == [] or k > len(tinput):
            return []
        tinput = merge_sort(tinput)
        return tinput[: k]