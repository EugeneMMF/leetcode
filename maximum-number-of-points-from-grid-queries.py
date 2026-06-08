class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        total = m * n
        parent = list(range(total))
        sz = [1] * total
        active = [False] * total
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if sz[ra] < sz[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            sz[ra] += sz[rb]
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort(key=lambda x: x[0])
        q_with_idx = sorted([(q, idx) for idx, q in enumerate(queries)])
        res = [0] * len(queries)
        ptr = 0
        for q, idx in q_with_idx:
            while ptr < total and cells[ptr][0] < q:
                val, r, c = cells[ptr]
                id = r * n + c
                active[id] = True
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        nid = nr * n + nc
                        if active[nid]:
                            union(id, nid)
                ptr += 1
            if grid[0][0] < q:
                res[idx] = sz[find(0)]
            else:
                res[idx] = 0
        return res