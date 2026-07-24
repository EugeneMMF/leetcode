class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(300000)
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        def dfs(u, p):
            base0 = 0
            base1 = 0
            deltas = []
            for v, w in adj[u]:
                if v == p: continue
                child0, child1 = dfs(v, u)
                base0 += child0
                base1 += child0
                delta = w + child1 - child0
                deltas.append(delta)
            deltas.sort(reverse=True)
            best0 = base0
            best1 = base1
            cnt = 0
            for d in deltas:
                if cnt < k and d > 0:
                    best0 += d
                    cnt += 1
                else:
                    break
            cnt = 0
            for d in deltas:
                if cnt < k - 1 and d > 0:
                    best1 += d
                    cnt += 1
                else:
                    break
            return best0, best1
        res0, res1 = dfs(0, -1)
        return res0
