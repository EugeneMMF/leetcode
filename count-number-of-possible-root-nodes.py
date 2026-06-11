class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(300000)
        n = len(edges) + 1
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        guess_set = set((u, v) for u, v in guesses)
        parent = [-1] * n
        init_cnt = 0
        def dfs(u):
            nonlocal init_cnt
            for v in g[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                if (u, v) in guess_set:
                    init_cnt += 1
                dfs(v)
        parent[0] = 0
        dfs(0)
        ans = 0
        def dfs2(u, cnt):
            nonlocal ans
            if cnt >= k:
                ans += 1
            for v in g[u]:
                if v == parent[u]:
                    continue
                new_cnt = cnt
                if (u, v) in guess_set:
                    new_cnt -= 1
                if (v, u) in guess_set:
                    new_cnt += 1
                dfs2(v, new_cnt)
        dfs2(0, init_cnt)
        return ans