class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.topp = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topp += 1
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        if self.topp > -1:
            # Simply reduce top and slice both stacks accordingly
            self.topp -= 1
            self.stack[:] = self.stack[:self.topp + 1]
            self.minstack[:] = self.minstack[:self.topp + 1]

    def top(self) -> int:
        if self.topp > -1:
            return self.stack[self.topp]

    def getMin(self) -> int:
        if self.topp > -1:
            return self.minstack[self.topp]
