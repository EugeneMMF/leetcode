class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack
