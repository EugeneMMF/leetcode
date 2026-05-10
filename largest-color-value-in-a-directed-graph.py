class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        from collections import deque
        n = len(colors)
        indeg = [0] * n
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            indeg[b] += 1
        dp = [[0] * 26 for _ in range(n)]
        for i, ch in enumerate(colors):
            dp[i][ord(ch) - 97] = 1
        q = deque([i for i in range(n) if indeg[i] == 0])
        processed = 0
        ans = 0
        while q:
            u = q.popleft()
            processed += 1
            ans = max(ans, max(dp[u]))
            for v in g[u]:
                for c in range(26):
                    val = dp[u][c] + (c == ord(colors[v]) - 97)
                    if val > dp[v][c]:
                        dp[v][c] = val
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if processed != n:
            return -1
        return ans
