class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        from collections import deque
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        INF=10**9
        ans=INF
        for s in range(n):
            dist=[-1]*n
            parent=[-1]*n
            q=deque([s])
            dist[s]=0
            while q:
                u=q.popleft()
                for v in adj[u]:
                    if dist[v]==-1:
                        dist[v]=dist[u]+1
                        parent[v]=u
                        q.append(v)
                    elif parent[u]!=v:
                        cycle_len=dist[u]+dist[v]+1
                        if cycle_len<ans:
                            ans=cycle_len
        return -1 if ans==INF else ans