class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        from heapq import heappush, heappop
        node_map = {}
        nodes = []
        def add_node(pt):
            if pt not in node_map:
                node_map[pt] = len(nodes)
                nodes.append(pt)
        add_node(tuple(start))
        add_node(tuple(target))
        for x1, y1, x2, y2, _ in specialRoads:
            add_node((x1, y1))
            add_node((x2, y2))
        n = len(nodes)
        adj = [[] for _ in range(n)]
        for i in range(n):
            xi, yi = nodes[i]
            for j in range(i + 1, n):
                xj, yj = nodes[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        for x1, y1, x2, y2, cost in specialRoads:
            u = node_map[(x1, y1)]
            v = node_map[(x2, y2)]
            adj[u].append((v, cost))
        start_idx = node_map[tuple(start)]
        target_idx = node_map[tuple(target)]
        dist = [10**18] * n
        dist[start_idx] = 0
        heap = [(0, start_idx)]
        while heap:
            d, u = heappop(heap)
            if d != dist[u]:
                continue
            if u == target_idx:
                return d
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(heap, (nd, v))
        return dist[target_idx]