class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        parent = list(range(n + 2))
        rank = [0] * (n + 2)
        top = n
        bottom = n + 1
        land = [False] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            idx = r * col + c
            land[idx] = True
            if r == 0:
                union(idx, top)
            if r == row - 1:
                union(idx, bottom)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    nidx = nr * col + nc
                    if land[nidx]:
                        union(idx, nidx)
            if find(top) == find(bottom):
                return i
        return 0