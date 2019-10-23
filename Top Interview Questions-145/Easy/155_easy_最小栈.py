#80ms,开了两个栈，速度会更快，栈的题目都是用列表模仿栈
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.初始化
        """
        self.stack = []   # 数据栈
        self.minVal = []   # 最小值栈
        # self.size = 0

    # 比较当前数据与最小值栈顶数据大小，选择较小的压入最小栈值
    def push(self, x):
        self.stack.append(x)  # push元素
        if len(self.minVal) == 0:
            self.minVal.append(x)
        else:
            if (x > self.minVal[-1]): # 保持数据栈和最小值栈大小相同，这样pop()操作可以保持一致
                x = self.minVal[-1]
            self.minVal.append(x)     #小的直接加，大的改为小的再加
        # self.size += 1

    # 数据栈与最小值栈同时弹出；本函数这里无返回值
    def pop(self):
        self.minVal.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minVal[-1]
        

#88ms
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
 
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]: 
            self.min_stack.append(x)
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
