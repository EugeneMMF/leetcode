class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        if k == 0:
            return 0
        mask = (1 << t) - 1
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(n):
            dp[0][i] = 1
        for step in range(k):
            next_dp = [0] * n
            for u, v, w in edges:
                shifted = dp[step][u] << w
                shifted &= mask
                next_dp[v] |= shifted
            dp[step + 1] = next_dp
        best = -1
        for node in range(n):
            bits = dp[k][node]
            if bits:
                s = bits.bit_length() - 1
                if s > best:
                    best = s
        return best
