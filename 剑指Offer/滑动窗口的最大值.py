#运行时间：28ms   占用内存：5840k
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        queue,res,i = [],[],0
        while size>0 and i<len(num):
            if len(queue)>0 and i-size+1 > queue[0]: #若最大值queue[0]位置过期 则弹出 
                queue.pop(0)
            while len(queue)>0 and num[queue[-1]]<num[i]: #每次弹出所有比num[i]的数字
                queue.pop()
            queue.append(i)
            if i>=size-1:
                res.append(num[queue[0]])
            i += 1
        return res