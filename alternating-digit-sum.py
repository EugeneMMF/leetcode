class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        total = 0
        sign = 1
        for ch in s:
            total += sign * int(ch)
            sign *= -1
        return total
