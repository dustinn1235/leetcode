# creat another stack that keep track of the current min
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1],val))
        return None

    def pop(self) -> None:
        self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) > 0 else None 

    def getMin(self) -> int:
        return self.minstack[-1] if len(self.minstack) > 0 else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()