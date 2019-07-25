# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归，112ms
# Time:  O(n),Space: O(logn)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
        mid = len(nums)//2#或者int mid = l + (r-l)/2
        res = TreeNode(nums[mid])
        res.left = self.sortedArrayToBST(nums[0:mid])
        res.right = self.sortedArrayToBST(nums[mid+1:])
        return res
        
