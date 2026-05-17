class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        from collections import deque
        adj = [[] for _ in range(n)]
        indeg = [0]*n
        for u,v in relations:
            u-=1
            v-=1
            adj[u].append(v)
            indeg[v]+=1
        earliest=[0]*n
        q=deque([i for i in range(n) if indeg[i]==0])
        while q:
            u=q.popleft()
            finish=earliest[u]+time[u]
            for v in adj[u]:
                if finish>earliest[v]:
                    earliest[v]=finish
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)
        return max(earliest[i]+time[i] for i in range(n))
