class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        order = []
        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            order.append((node, parent))
            for nb in g[node]:
                if nb != parent:
                    stack.append((nb, node))
        sub = [[0] * 26 for _ in range(n)]
        ans = [0] * n
        for node, parent in reversed(order):
            idx = ord(labels[node]) - 97
            cnt = sub[node]
            cnt[idx] = 1
            for nb in g[node]:
                if nb != parent:
                    child = sub[nb]
                    for i in range(26):
                        cnt[i] += child[i]
            ans[node] = cnt[idx]
        return ans
