class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        from math import inf
        n = len(passingFees)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        dist = [[inf] * (maxTime + 1) for _ in range(n)]
        dist[0][0] = passingFees[0]
        for time in range(maxTime + 1):
            for node in range(n):
                if dist[node][time] == inf:
                    continue
                cur_cost = dist[node][time]
                for nei, t in adj[node]:
                    nt = time + t
                    if nt <= maxTime:
                        nc = cur_cost + passingFees[nei]
                        if nc < dist[nei][nt]:
                            dist[nei][nt] = nc
        ans = min(dist[n-1])
        return -1 if ans == inf else ans
