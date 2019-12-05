#120ms
#Time:O(n)   Space: O(n)
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans=[]
        def act(i,n):
            if not i:
                return
            if n==len(ans):
                ans.append([])
            ans[n].append(i.val)#第几行加对应的几个值
            if i.children:
                for j in i.children:
                    act(j,n+1)
        act(root,0)
        return ans

#120ms
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        def layer(root, ans, n_layer=0):
            if root:
                try:
                    ans[n_layer].append(root.val)
                except IndexError:
                    ans.append([root.val])
                for i in root.children:
                    layer(i, ans, n_layer+1)
        layer(root, ans)
        return ans
        
#816 ms，BFS
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root]
        while cur:#不为空
            dim = []
            next = []
            for i in cur:
                dim.append(i.val)
                next += i.children#存下一层,与上面注意区别
            res.append(dim)
            cur = next
        return res
