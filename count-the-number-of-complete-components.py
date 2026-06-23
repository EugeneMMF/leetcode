class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
        for a, b in edges:
            union(a, b)
        comp_edges = {}
        for a, b in edges:
            r = find(a)
            comp_edges[r] = comp_edges.get(r, 0) + 1
        count = 0
        for v in range(n):
            r = find(v)
            if r == v:
                comp_size = size[r]
                needed = comp_size * (comp_size - 1) // 2
                edges_in = comp_edges.get(r, 0)
                if edges_in == needed:
                    count += 1
        return count
