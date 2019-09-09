#利用两个堆栈，一个叫输入栈，一个叫输出栈。每次从输入栈进，输出栈出。52 ms
#Time: O(1)   Space: O(1)
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                a = self.stack1.pop()#从1出
                self.stack2.append(a)#从2进
        return self.stack2.pop()
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                a = self.stack1.pop()#从1出
                self.stack2.append(a)#从2进
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()