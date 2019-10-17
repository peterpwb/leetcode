#自己的做法1，计数器,36ms
# Time:O(n)  Space: O(1)
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = Counter(s).most_common()
        #返回一个列表[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
        dim = 0
        count1 = 0
        if len(res) == 1:#只有一种字母
            return res[0][1]
        for i in res:
            if i[1]%2 == 0:
                dim += i[1]
            else:
                if i[1] == 1:
                    count1 += 1
                else:
                    dim += i[1]-1
                    count1 += 1#奇数项里面多的那个也可以做回文中间的那个
        return dim+1 if count1 != 0 else dim

#自己的方法2，68ms
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res=[]
        for i in s:
            if i not in res:
                res.append(i)
            else:
                res.remove(i)
        if len(res)!=0:
            return len(s)-len(res)+1
        else:
            return len(s)
            
#48ms,自己针对别人计数法的改进
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        #"soooosczzzcccdds"---({'o': 4, 'c': 4, 's': 3, 'z': 3, 'd': 2})
        res = 0
        res_odd=0
        for key,n in c.items():
            if n&1:
                res_odd+=1
                res+=(n//2)*2
            else:
                res+=n
        return res+1 if res_odd!=0 else res
        