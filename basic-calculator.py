
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        num = 0
        sign = 1
        stack = []

        for char in s:
            if '0' <= char <= '9':
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append((result, sign))
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result

        if num != 0:
            result += sign * num

        return result
