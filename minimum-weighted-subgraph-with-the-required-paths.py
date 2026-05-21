import heapq
from typing import List

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        adj=[[] for _ in range(n)]
        rev=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            rev[v].append((u,w))
        def dijkstra(start, graph):
            dist=[float('inf')]*n
            dist[start]=0
            h=[(0,start)]
            while h:
                d,u=heapq.heappop(h)
                if d!=dist[u]: continue
                for v,w in graph[u]:
                    nd=d+w
                    if nd<dist[v]:
                        dist[v]=nd
                        heapq.heappush(h,(nd,v))
            return dist
        dist1=dijkstra(src1,adj)
        dist2=dijkstra(src2,adj)
        distDest=dijkstra(dest,rev)
        ans=float('inf')
        for i in range(n):
            if dist1[i]==float('inf') or dist2[i]==float('inf') or distDest[i]==float('inf'):
                continue
            total=dist1[i]+dist2[i]+distDest[i]
            if total<ans: ans=total
        return ans if ans!=float('inf') else -1