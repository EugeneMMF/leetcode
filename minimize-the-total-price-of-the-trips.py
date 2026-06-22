import sys
from typing import List

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1]*n
        depth = [0]*n
        sys.setrecursionlimit(10000)
        def dfs(u,p):
            parent[u]=p
            for v in adj[u]:
                if v==p: continue
                depth[v]=depth[u]+1
                dfs(v,u)
        dfs(0,-1)
        count=[0]*n
        for u,v in trips:
            a,b=u,v
            while a!=b:
                if depth[a]>depth[b]:
                    count[a]+=1
                    a=parent[a]
                elif depth[b]>depth[a]:
                    count[b]+=1
                    b=parent[b]
                else:
                    count[a]+=1
                    count[b]+=1
                    a=parent[a]
                    b=parent[b]
            count[a]+=1
        weight=[count[i]*price[i]//2 for i in range(n)]
        def dp(u):
            inc=weight[u]
            exc=0
            for v in adj[u]:
                if v==parent[u]: continue
                inc_child, exc_child = dp(v)
                inc += exc_child
                exc += max(inc_child, exc_child)
            return inc, exc
        inc_root, exc_root = dp(0)
        total_sum = sum(count[i]*price[i] for i in range(n))
        best = max(inc_root, exc_root)
        return total_sum - best