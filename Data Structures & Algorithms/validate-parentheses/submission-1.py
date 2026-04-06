class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                last_char = stack.pop()
                if char == "]" and last_char != "[":
                    return False
                if char == "}" and last_char != "{":
                    return False
                if char == ")" and last_char != "(":
                    return False
        return len(stack) == 0