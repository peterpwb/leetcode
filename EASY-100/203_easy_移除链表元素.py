#64 ms,添加表头
# Time:  O(n)   Space: O(1)
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy=ListNode(0)
        dummy.next=head#新建一个开头这样处理链表的第一个元素
        cur=dummy#要复制一个，要不然dummy直接循环完指针就到最后了
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next
        

