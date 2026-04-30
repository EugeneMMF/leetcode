from typing import List

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        indexed_queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        indexed_queries.sort(key=lambda x: x[2])
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        res = [False] * len(queries)
        e = 0
        m = len(edgeList)
        for p, q, limit, idx in indexed_queries:
            while e < m and edgeList[e][2] < limit:
                union(edgeList[e][0], edgeList[e][1])
                e += 1
            res[idx] = find(p) == find(q)
        return res
