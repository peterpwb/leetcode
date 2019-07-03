'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range (len(nums)):
            if (target-nums[i]) in nums=='true':
                b=nums.index(target-nums[i])
                list2=[]
                list2.append(i)
                list2.append(b)
                return list2
        return null
'''
#0:2,1：7,3:15,4:27    2+7=9    输出[0,1]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums)==0:#空的话输出空
            return []
        index_of_value={}#定义一个空的字典
        for key,value in enumerate(nums):#该内置函数生成数据和数据下标的枚举
            if (target-value) in index_of_value:#如果该键存在
                return[index_of_value[target-value],key]
            index_of_value[value]=key#将该键值存入字典
