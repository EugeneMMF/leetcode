class Solution:
    def minMoves(self, nums, k):
        positions = [i for i, v in enumerate(nums) if v]
        if k <= 1:
            return 0
        adj = [p - idx for idx, p in enumerate(positions)]
        n = len(adj)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + adj[i]
        best = float('inf')
        for l in range(0, n - k + 1):
            r = l + k - 1
            m = l + k // 2
            median = adj[m]
            left = median * (m - l) - (prefix[m] - prefix[l])
            right = (prefix[r + 1] - prefix[m + 1]) - median * (r - m)
            total = left + right
            best = min(best, total)
        return best
