class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        M = 10**9 + 7
        m = target // 2
        if n <= m:
            return (n * (n + 1) // 2) % M
        sum1 = (m * (m + 1) // 2) % M
        r = n - m
        sum2 = (r * target) % M
        sum2 = (sum2 + (r * (r - 1) // 2) % M) % M
        return (sum1 + sum2) % M
