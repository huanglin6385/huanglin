#96.59
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_number = 0x7FFFFFFF
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.min_number = min(self.min_number,x)
    def pop(self):
        """
        :rtype: void
        """
        k = self.stack.pop()
        if k == self.min_number:
            self.min_number = min(self.stack+[0x7FFFFFFF])

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_number


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()