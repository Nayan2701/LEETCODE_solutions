class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop the top element if stack isn't empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the top element, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly closed
        return len(stack) == 0