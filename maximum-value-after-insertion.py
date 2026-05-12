class Solution:
    def maxValue(self, n: str, x: int) -> str:
        digit = str(x)
        if n[0] == '-':
            for i, d in enumerate(n[1:]):
                if d > digit:
                    return n[:i+1] + digit + n[i+1:]
            return n + digit
        else:
            for i, d in enumerate(n):
                if d < digit:
                    return n[:i] + digit + n[i:]
            return n + digit
