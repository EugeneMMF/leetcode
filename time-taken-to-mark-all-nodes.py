
from typing import List
import sys
sys.setrecursionlimit(300000)
class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp1 = [0]*n
        best1_val = [0]*n
        best1_child = [-1]*n
        best2_val = [0]*n
        def dfs1(u,p):
            b1 = 0
            b2 = 0
            b1c = -1
            for v in adj[u]:
                if v==p: continue
                dfs1(v,u)
                cand = (1 if (v & 1) else 2) + dp1[v]
                if cand >= b1:
                    b2 = b1
                    b1 = cand
                    b1c = v
                elif cand > b2:
                    b2 = cand
            dp1[u] = b1
            best1_val[u] = b1
            best1_child[u] = b1c
            best2_val[u] = b2
        up = [0]*n
        def dfs2(u,p):
            for v in adj[u]:
                if v==p: continue
                best_other = best1_val[u] if best1_child[u]!=v else best2_val[u]
                up[v] = (1 if (u & 1) else 2) + max(up[u], best_other, 0)
                dfs2(v,u)
        dfs1(0,-1)
        up[0]=0
        dfs2(0,-1)
        res = [0]*n
        for i in range(n):
            res[i] = dp1[i] if dp1[i]>=up[i] else up[i]
        return res
