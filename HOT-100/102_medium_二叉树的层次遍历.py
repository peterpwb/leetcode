# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Time:O(n)  Space:O(n)
#BFS,类似107，做法相同
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        temp = [root]
        target = []
        while temp:
            next_temp = []
            res = []
            for i in temp:
                if not i:
                    continue
                next_temp.append(i.left)
                next_temp.append(i.right)
                res.append(i.val)
            temp = next_temp
            target.append(res)
        return target[:-1]#注意去掉最后一层空的层