# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#100 ms，一次遍历
#Time:O(max(m,n))   Space:O(max(m,n))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = dim = ListNode(0)#头一位好处理
        addone = 0
        while l1 and l2:
            dim.next = ListNode((l1.val + l2.val +addone)%10)
            addone = (l1.val + l2.val +addone)//10
            l1 = l1.next
            l2 = l2.next
            dim = dim.next
        #处理最后多处理的进1,可能一直进1
        l1 = l1 if l1 else l2
        while addone:
            if l1:#确定不为空才能加值
                dim.next = ListNode((l1.val + addone)%10)
                addone = (l1.val + addone)//10
                l1 = l1.next
                dim = dim.next
            else:#l1为空就剩一个加1
                dim.next = ListNode(1)
                dim = dim.next
                #addone = 0这样写也可以
                break#始终是1，跳出少一次循环节约时间
        dim.next = l1
        return res.next
        
