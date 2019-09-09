# Time: push: O(n), pop: O(1), top: O(1)
# Space: O(n)
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]#定义空数组

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)#加元素

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()#移除最后一个

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]#返回倒数第一个的值

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack)==0#查看是否为空


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()