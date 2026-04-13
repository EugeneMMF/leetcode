class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        s = str(n)
        m = len(s)
        k = len(digits)
        total = 0
        for l in range(1, m):
            total += k ** l
        for i, ch in enumerate(s):
            smaller = 0
            for d in digits:
                if d < ch:
                    smaller += 1
                else:
                    break
            total += smaller * (k ** (m - i - 1))
            if ch not in digits:
                break
        else:
            total += 1
        return total
