# -*- coding:utf-8 -*-
#运行时间：25ms   占用内存：5752k
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:#弹出的下一个恰好为栈顶数字，直接弹出
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True