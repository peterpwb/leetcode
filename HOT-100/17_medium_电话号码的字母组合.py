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
    
#迭代器的运用，28ms
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        res = []
        if digits is "":
            return res
        for i in range(len(digits)):
            res.append(dic[digits[i]])#["abc","def"]
        return list(map("".join,itertools.product(*res)))#*的使用
