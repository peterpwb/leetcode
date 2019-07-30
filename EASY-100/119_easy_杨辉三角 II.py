#Time:  O(n^2),Space: O(1)，同118
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [[1]]
        for i in range(1,rowIndex+1):
            r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
        return r[-1]


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        
        while 1<=rowIndex:
            result.append([1 for i in range(len(result[0])+1)])
            for i in range(1,len(result[1])-1):
                result[1][i] = result[0][i] + result[0][i-1]
            result.pop(0)
            rowIndex -= 1
        return result[0]
       
       
       
       
class Solution(object):
    def getRow(self, rowIndex):
        for r in range(rowIndex+1) :
            res = [1] * (r+1)
            for c in range(1, r) :
                res[c] = above[c-1] + above[c]
            above = res
        return res