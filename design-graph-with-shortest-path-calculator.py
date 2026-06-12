from typing import List
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.adj=[[] for _ in range(n)]
        for u,v,w in edges:
            self.adj[u].append((v,w))

    def addEdge(self, edge: List[int]) -> None:
        u,v,w=edge
        self.adj[u].append((v,w))

    def shortestPath(self, node1: int, node2: int) -> int:
        import heapq
        dist=[float('inf')]*self.n
        dist[node1]=0
        pq=[(0,node1)]
        while pq:
            d,u=heapq.heappop(pq)
            if d!=dist[u]:
                continue
            if u==node2:
                return d
            for v,w in self.adj[u]:
                nd=d+w
                if nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(pq,(nd,v))
        return -1
