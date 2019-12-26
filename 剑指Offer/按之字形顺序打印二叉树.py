#运行时间：29ms   占用内存：5752k

#将每层的数据存进ArrayList中，偶数层时进行reverse操作
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        # 1.迭代 ，层遍历  左到右， 右到左
        if not pRoot :
            return []
        result=[]
        result_tmp=[pRoot]
        flag=0
        while result_tmp:
            tmp_list=[]
            r=[]
            for tmp in result_tmp:
                r.append(tmp.val)
                if tmp.left:
                    tmp_list.append(tmp.left)
                if tmp.right:
                    tmp_list.append(tmp.right)
            result_tmp=tmp_list
            if r and  flag :
                result.append(r[::-1])
                flag=0
            elif r:
                result.append(r)
                flag=1
 
        return result
        

            
            
            