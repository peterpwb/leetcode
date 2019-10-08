#84ms，自己的方法
#Time:O(n)   Space:O(n)
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        res=str.split()#["dog","cat","cat","dog"]
        if len(res) != len(pattern) or len(set(res)) != len(set(pattern)):
            return False
        dic={}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]]=res[i]
            else:
                if dic[pattern[i]]!=res[i]:
                    return False
        return True
        
        
        
#44ms,zip方法的使用
#Time:O(n)   Space:O(n)
class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

#64ms
#Time:O(n)   Space:O(n)
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        split_str=str.split(" ")
        
        if len(split_str) != len(pattern):
            return False
        
        map1={}
        map2={}
        
        for i in range(len(pattern)):
            key=pattern[i]
            value=split_str[i]
            
            if key not in map1:
                map1[key] = value
                
            if value not in map2:
                map2[value]=key
            
            if key in map1 and map1[key] != value or value in map2 and map2[value]!=key:
                return False    
            else:
                pass
            
        return True


