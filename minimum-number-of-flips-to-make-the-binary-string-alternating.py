class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s
        a = [0] * (2 * n)
        for i, ch in enumerate(t):
            if (i & 1) == 0:
                expected = '0'
            else:
                expected = '1'
            a[i] = 1 if ch != expected else 0
        cur = sum(a[:n])
        best = min(cur, n - cur)
        for i in range(1, n):
            cur += a[i + n - 1] - a[i - 1]
            best = min(best, cur, n - cur)
        return best