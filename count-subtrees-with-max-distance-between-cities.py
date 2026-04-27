class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        from collections import deque
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)
        ans = [0] * (n - 1)
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            first = (mask & -mask).bit_length() - 1
            q = deque([first])
            visited_mask = 0
            visited_mask |= 1 << first
            while q:
                node = q.popleft()
                for nb in adj[node]:
                    if (mask >> nb) & 1 and not (visited_mask >> nb) & 1:
                        visited_mask |= 1 << nb
                        q.append(nb)
            if visited_mask != mask:
                continue
            def bfs(start):
                q = deque([start])
                dist = {start: 0}
                max_node = start
                while q:
                    cur = q.popleft()
                    for nb in adj[cur]:
                        if (mask >> nb) & 1 and nb not in dist:
                            dist[nb] = dist[cur] + 1
                            q.append(nb)
                            if dist[nb] > dist[max_node]:
                                max_node = nb
                return max_node, dist[max_node]
            far, _ = bfs(first)
            _, diam = bfs(far)
            if diam > 0:
                ans[diam - 1] += 1
        return ans
