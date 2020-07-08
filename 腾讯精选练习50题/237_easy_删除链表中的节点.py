# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#36 ms
#Time:O(1)  Space: O(1)
#node这个节点就是需要删除的节点，直接在上面进行操作。
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next