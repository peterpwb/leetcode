#列表生成式,44ms
#Time:O(n*4^n)  Space: O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        if digits == "":
            return []
        res = [""]
        for i in digits:
            res = [m+n for m in res for n in dic[i]]
        return res