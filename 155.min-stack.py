import sys


class Solution:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x - self.min)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        if not self.stack:
            return
        tmp = self.stack.pop()
        if tmp < 0:
            self.min -= tmp

    def top(self) -> int:
        if not self.stack:
            return
        tmp = self.stack[-1]
        if tmp < 0:
            return self.min
        else:
            return self.min + tmp

    def getMin(self) -> int:
        return self.min


if __name__ == '__main__':
# Your MinStack object will be instantiated and called as such:
    obj = Solution()
    obj.push(3)
    obj.push(2)
    obj.push(1)
    obj.push(4)
    obj.push(-1)
    obj.push(-2)
    obj.push(-2)
    while obj.stack:
        param_3 = obj.top()
        param_4 = obj.getMin()
        obj.pop()
        print(param_3, param_4)