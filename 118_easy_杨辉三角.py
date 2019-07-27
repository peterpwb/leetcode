#52ms,动态规划方法,基于上一行得到当前行
#Time:  O(n^2),Space: O(1)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1]*(i+1)
            if i>1:
                for n in range(1,i):
                    row[n] = pre[n-1]+pre[n]
            res.append(row)
            pre = row
        return res
            
#类似但是只算一半(对称),44ms
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, (i+3)//2):
                res[i][j] = res[i][i-j] = res[i-1][j] + res[i-1][j-1]  #res[i][j]与res[i][i-j]相等
        return res


            
#40ms,匿名函数的运用
#Time:  O(n^2),Space: O(1)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1,numRows):
            res.append(list(map(lambda x,y:x+y,[0]+res[-1],res[-1]+[0])))
        return res