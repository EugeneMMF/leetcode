class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        self.ans = 1
        import sys
        sys.setrecursionlimit(200000)
        def dfs(u: int) -> int:
            max1 = 0
            max2 = 0
            for v in children[u]:
                child_len = dfs(v)
                if s[v] == s[u]:
                    continue
                if child_len > max1:
                    max2 = max1
                    max1 = child_len
                elif child_len > max2:
                    max2 = child_len
            self.ans = max(self.ans, 1 + max1 + max2)
            return 1 + max1
        dfs(0)
        return self.ans
