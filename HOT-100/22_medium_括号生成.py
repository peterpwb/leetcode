#超时
import itertools
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dim = ["()"]*n  #['()', '()', '()']
        curr = list(map("".join,itertools.product(*dim)))
        res = []
        #['(((', '(()', '()(', '())', ')((', ')()', '))(', ')))']#按左右对称分布
        for i in curr:
            guo = 0
            for j in range(n):
                if i[j] == "(":
                    guo += 1
                else:
                    guo -= 1
            res.append(guo)#[3, 1, 1, -1, 1, -1, -1, -3]
        result = []
        for i in range(len(res)):
            j = i+1
            while j < len(res) :
                if res[i] + res[j] == 0:
                    result.append(curr[i]+curr[j])
                else:
                    j += 1
        return list(set(result))
        
#递归，40 ms
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

#动态规划,48 ms  "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】 
#其中 p + q = n-1，且 p q 均为非负整数
# Time:  O(4^n / n^(3/2)) ~= Catalan numbers    Space: O(n)
class Solution(object):
    def generateParenthesis(self, n):
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        for i in range(1,n+1):
            for p in range(i):
                l1 = dp[p]
                l2 = dp[i-1-p]
                for k1 in l1:
                    for k2 in l2:
                        dp[i].append("({0}){1}".format(k1,k2))
        return dp[n]