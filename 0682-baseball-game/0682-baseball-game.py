class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if stack and op == "C":
                stack.pop()
            elif stack and op == "D":
                stack.append(stack[-1]*2)
            elif stack and op == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))
        
        return sum(stack)