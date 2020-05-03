class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0 or x <= self.mins[-1]:
            self.mins.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.mins):
            return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()