class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        weights = sorted(set(w for _, _, w in edges))
        def can(max_w: int) -> bool:
            rev_adj = [[] for _ in range(n)]
            for a, b, w in edges:
                if w <= max_w:
                    rev_adj[b].append(a)
            seen = [False] * n
            stack = [0]
            seen[0] = True
            while stack:
                v = stack.pop()
                for u in rev_adj[v]:
                    if not seen[u]:
                        seen[u] = True
                        stack.append(u)
            return all(seen)
        lo, hi = 0, len(weights) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(weights[mid]):
                ans = weights[mid]
                hi = mid - 1
            else:
                lo = mid + 1
        return ans