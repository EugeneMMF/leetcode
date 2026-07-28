class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        n = len(conversions) + 1
        mod = 10**9 + 7
        adj = [[] for _ in range(n)]
        for src, tgt, factor in conversions:
            adj[src].append((tgt, factor))
        res = [0] * n
        stack = [(0, 1)]
        while stack:
            node, prod = stack.pop()
            res[node] = prod
            for nxt, f in adj[node]:
                stack.append((nxt, prod * f % mod))
        return res
