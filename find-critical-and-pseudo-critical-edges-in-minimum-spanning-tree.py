class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, x, y):
                xr, yr = self.find(x), self.find(y)
                if xr == yr:
                    return False
                if self.rank[xr] < self.rank[yr]:
                    self.parent[xr] = yr
                elif self.rank[xr] > self.rank[yr]:
                    self.parent[yr] = xr
                else:
                    self.parent[yr] = xr
                    self.rank[xr] += 1
                return True

        # attach original indices
        indexed_edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[2])

        def kruskal(skip_edge_idx=-1, force_edge_idx=-1):
            dsu = DSU(n)
            total = 0
            used = 0
            # if we force an edge, add it first
            if force_edge_idx != -1:
                u, v, w, idx = indexed_edges[force_edge_idx]
                if dsu.union(u, v):
                    total += w
                    used += 1
            for i, (u, v, w, idx) in enumerate(indexed_edges):
                if i == skip_edge_idx:
                    continue
                if i == force_edge_idx:
                    continue
                if dsu.union(u, v):
                    total += w
                    used += 1
                    if used == n - 1:
                        break
            if used == n - 1:
                return total
            return float('inf')

        # compute original MST weight
        mst_weight = kruskal()

        critical = []
        pseudo = []

        for i in range(len(indexed_edges)):
            # test critical
            w_without = kruskal(skip_edge_idx=i)
            if w_without > mst_weight:
                critical.append(indexed_edges[i][3])
            else:
                # test pseudo-critical
                w_with = kruskal(force_edge_idx=i)
                if w_with == mst_weight:
                    pseudo.append(indexed_edges[i][3])

        return [critical, pseudo]
