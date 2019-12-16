#运行时间：41ms   占用内存：5624k

# -*- coding:utf-8 -*-
class Solution:
    def  __init__(self):
        self.count = 0
        
    def movingCount(self, threshold, rows, cols):
        # write code here
        arr = [[1 for i in range(cols)] for j in range(rows)]
        self.findway(arr,0,0,threshold)
        return self.count
        
    def findway(self,arr,i,j,k):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return
        tempi = list(map(int,list(str(i))))
        tempj = list(map(int,list(str(j))))
        if sum(tempi) + sum(tempj) > k or arr[i][j] != 1:
            return
        arr[i][j] = 0
        self.count += 1
        self.findway(arr,i-1,j,k)
        self.findway(arr,i+1,j,k)
        self.findway(arr,i,j-1,k)
        self.findway(arr,i,j+1,k)