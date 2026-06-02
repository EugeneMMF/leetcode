class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n - 1):
            x = n
            digits = []
            while x:
                digits.append(x % b)
                x //= b
            if digits != digits[::-1]:
                return False
        return True