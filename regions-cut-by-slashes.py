class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        parent = list(range(n * n * 4))
        rank = [0] * (n * n * 4)
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
        for i in range(n):
            for j in range(n):
                base = (i * n + j) * 4
                c = grid[i][j]
                if c == ' ':
                    union(base, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)
                elif c == '/':
                    union(base, base + 3)
                    union(base + 1, base + 2)
                else:
                    union(base, base + 1)
                    union(base + 2, base + 3)
                if i + 1 < n:
                    bottom = base + 2
                    down_top = ((i + 1) * n + j) * 4
                    union(bottom, down_top)
                if j + 1 < n:
                    right = base + 1
                    left = ((i) * n + j + 1) * 4 + 3
                    union(right, left)
        regions = sum(1 for i in range(len(parent)) if find(i) == i)
        return regions
