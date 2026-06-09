class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        if n == 0:
            return 0
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def farthest(start: int):
            stack = [(start, -1, price[start])]
            max_node = start
            max_dist = price[start]
            while stack:
                node, parent, dist = stack.pop()
                if dist > max_dist:
                    max_dist = dist
                    max_node = node
                for nei in adj[node]:
                    if nei == parent:
                        continue
                    stack.append((nei, node, dist + price[nei]))
            return max_node, max_dist
        if n == 1:
            return 0
        u, _ = farthest(0)
        v, _ = farthest(u)
        def distances(start: int):
            dist = [0] * n
            stack = [(start, -1, price[start])]
            while stack:
                node, parent, d = stack.pop()
                dist[node] = d
                for nei in adj[node]:
                    if nei == parent:
                        continue
                    stack.append((nei, node, d + price[nei]))
            return dist
        dist_u = distances(u)
        dist_v = distances(v)
        ans = 0
        for i in range(n):
            max_sum = dist_u[i] if dist_u[i] > dist_v[i] else dist_v[i]
            cost = max_sum - price[i]
            if cost > ans:
                ans = cost
        return ans