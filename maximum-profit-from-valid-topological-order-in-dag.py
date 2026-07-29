class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        pred = [0] * n
        for u, v in edges:
            pred[v] |= 1 << u
        size = 1 << n
        dp = [-1] * size
        dp[0] = 0
        for mask in range(size):
            cur = dp[mask]
            if cur < 0:
                continue
            pos = mask.bit_count() + 1
            for v in range(n):
                if mask >> v & 1:
                    continue
                if pred[v] & ~mask:
                    continue
                newmask = mask | (1 << v)
                val = cur + score[v] * pos
                if val > dp[newmask]:
                    dp[newmask] = val
        return dp[size - 1]