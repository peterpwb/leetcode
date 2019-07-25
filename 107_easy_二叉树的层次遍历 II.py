# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#层序遍历BFS，最后倒转，52ms
#Time:O(n)  Space:O(n)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        target = []
        while queue:
            next_queue = []
            res=[]
            for i in queue:
                if not i:
                    continue
                next_queue.append(i.left)
                next_queue.append(i.right)
                res.append(i.val)
            queue = next_queue
            target.append(res)
        return target[::-1][1:]#最后一次[None,None...]导出的[]