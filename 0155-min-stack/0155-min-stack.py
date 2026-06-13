class MinStack:
    def __init__(self):
        # The stack will hold tuples of (value, min_so_far)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # If stack is empty, the new value is the minimum
            self.stack.append((val, val))
        else:
            # The current min is the smaller of the new value and the previous min
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]