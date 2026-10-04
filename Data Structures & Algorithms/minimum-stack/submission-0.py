# O(1) - time (for each call function). O(n) - space.
class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        minVal = min(val, self.stack[-1][1]) if self.stack else val
        pair = [val, minVal]
        self.stack.append(pair)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
