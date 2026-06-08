class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        max_sum = vals[0]
        for i in range(n):
            neigh_vals = [vals[j] for j in adj[i]]
            neigh_vals.sort(reverse=True)
            cur = vals[i]
            cnt = 0
            for v in neigh_vals:
                if cnt == k:
                    break
                if v <= 0:
                    break
                cur += v
                cnt += 1
            if cur > max_sum:
                max_sum = cur
        return max_sum
