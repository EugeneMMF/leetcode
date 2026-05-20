class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        a, b = num1, num2
        steps = 0
        while a and b:
            if a >= b:
                steps += a // b
                a %= b
            else:
                steps += b // a
                b %= a
        return steps
