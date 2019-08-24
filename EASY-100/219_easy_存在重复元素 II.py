#132 ms,查索引
# Time:  O(n)   Space: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k== 0 or nums==[]:
            return False
        res = {}
        for key,val in enumerate(nums):
            if val in res:
                if key-res[val]<= k:
                    return True#存在
                else:
                    res[val]=key#替换
                
            else:#没有就将对应值的索引存入
                res[val] = key
        return False
                

