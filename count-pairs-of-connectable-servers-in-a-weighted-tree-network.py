class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
        res = [0] * n
        for c in range(n):
            counts = {}
            for nb, w in adj[c]:
                stack = [(nb, c, w)]
                cnt = 0
                while stack:
                    node, parent, dist = stack.pop()
                    if dist % signalSpeed == 0:
                        cnt += 1
                    for nxt, wt in adj[node]:
                        if nxt != parent:
                            stack.append((nxt, node, dist + wt))
                counts[nb] = cnt
            total = 0
            subs = list(counts.values())
            for i in range(len(subs)):
                for j in range(i + 1, len(subs)):
                    total += subs[i] * subs[j]
            res[c] = total
        return res
