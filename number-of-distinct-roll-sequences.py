class Solution:
    def distinctSequences(self, n: int) -> int:
        import math
        mod = 1000000007
        if n == 1:
            return 6
        prev = [[0] * 7 for _ in range(7)]
        for a in range(1, 7):
            prev[a][0] = 1
        for _ in range(2, n + 1):
            cur = [[0] * 7 for _ in range(7)]
            for a in range(1, 7):
                for b in range(7):
                    val = prev[a][b]
                    if not val:
                        continue
                    for c in range(1, 7):
                        if c == a or c == b:
                            continue
                        if math.gcd(a, c) != 1:
                            continue
                        cur[c][a] = (cur[c][a] + val) % mod
            prev = cur
        total = 0
        for a in range(1, 7):
            for b in range(7):
                total = (total + prev[a][b]) % mod
        return total