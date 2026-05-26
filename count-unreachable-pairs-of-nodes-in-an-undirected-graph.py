from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
        for a, b in edges:
            union(a, b)
        comp_sizes = {}
        for i in range(n):
            r = find(i)
            comp_sizes[r] = comp_sizes.get(r, 0) + 1
        total_pairs = n * (n - 1) // 2
        connected_pairs = 0
        for sz in comp_sizes.values():
            connected_pairs += sz * (sz - 1) // 2
        return total_pairs - connected_pairs