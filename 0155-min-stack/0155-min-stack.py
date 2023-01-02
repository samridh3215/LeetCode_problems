class MinStack:

    def __init__(self):
        self.stack = []
        self.m = None
    def push(self, val: int) -> None:
        if(self.stack == []):
            self.m = val
        else:
            if(val<self.m):
                self.m = val
        self.stack.append(val)
        

    def pop(self) -> None:
        a = self.stack.pop()
        if(self.stack!=[]):
            self.m = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()