class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        half = n // 2
        INF = 10**18
        dp_prev = [[INF] * 3 for _ in range(3)]
        for c1 in range(3):
            for c2 in range(3):
                if c1 == c2:
                    continue
                dp_prev[c1][c2] = cost[0][c1] + cost[n - 1][c2]
        for k in range(1, half):
            dp_cur = [[INF] * 3 for _ in range(3)]
            for pc1 in range(3):
                for pc2 in range(3):
                    prev_val = dp_prev[pc1][pc2]
                    if prev_val == INF:
                        continue
                    for c1 in range(3):
                        if c1 == pc1:
                            continue
                        for c2 in range(3):
                            if c2 == pc2 or c1 == c2:
                                continue
                            val = prev_val + cost[k][c1] + cost[n - 1 - k][c2]
                            if val < dp_cur[c1][c2]:
                                dp_cur[c1][c2] = val
            dp_prev = dp_cur
        ans = INF
        for c1 in range(3):
            for c2 in range(3):
                if dp_prev[c1][c2] < ans:
                    ans = dp_prev[c1][c2]
        return ans