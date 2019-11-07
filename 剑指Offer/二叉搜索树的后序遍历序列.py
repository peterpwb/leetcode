# -*- coding:utf-8 -*-
#二叉搜索数的特点：左子树的值都小于根结点
#右子树的值都大于根结点
# -*- coding:utf-8 -*-
#运行时间：25ms   占用内存：5728k
#Time:O(n),Space: O(logn)

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        
        length = len(sequence)
        root = sequence[length-1]#最后一位是根结点
        #寻找二叉搜索数的左子树
        for i in range(length):
            if sequence[i] > root:
                break
        for j in range(i,length):
            if sequence[j] < root:
                return False
        left = right = True
        if i:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < length-1 and left:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right#只有都是返回True才是正确
        