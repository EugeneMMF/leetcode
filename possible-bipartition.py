import collections

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        color = [0] * (n + 1)

        for i in range(1, n + 1):
            if color[i] == 0:
                q = collections.deque()
                q.append(i)
                color[i] = 1

                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if color[v] == 0:
                            color[v] = -color[u]
                            q.append(v)
                        elif color[v] == color[u]:
                            return False
        
        return True
