class Solution:
    def networkBecomesIdle(self, edges, patience):
        from collections import deque
        n = len(patience)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist = [-1] * n
        dist[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        max_time = 0
        for i in range(1, n):
            d = dist[i]
            round_trip = d * 2
            k = (round_trip - 1) // patience[i]
            last_reply = k * patience[i] + round_trip
            if last_reply > max_time:
                max_time = last_reply
        return max_time + 1
