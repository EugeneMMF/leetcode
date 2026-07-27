class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        import sys
        sys.setrecursionlimit(300000)
        adj=[[] for _ in range(n+1)]
        edge_weight={}
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            edge_weight[(u,v)]=w
            edge_weight[(v,u)]=w
        parent=[0]*(n+1)
        dist=[0]*(n+1)
        in_time=[0]*(n+1)
        out_time=[0]*(n+1)
        timer=0
        def dfs(u,p):
            nonlocal timer
            parent[u]=p
            in_time[u]=timer
            timer+=1
            for v,w in adj[u]:
                if v==p: continue
                dist[v]=dist[u]+w
                dfs(v,u)
            out_time[u]=timer-1
        dfs(1,0)
        edge_to_child={}
        for u,v,w in edges:
            if parent[u]==v:
                child=u
            else:
                child=v
            edge_to_child[(min(u,v),max(u,v))]=child
        size=n+5
        bit=[0]*(size)
        def bit_add(i,val):
            i+=1
            while i<size:
                bit[i]+=val
                i+=i&-i
        def bit_sum(i):
            i+=1
            s=0
            while i>0:
                s+=bit[i]
                i-=i&-i
            return s
        def range_add(l,r,val):
            bit_add(l,val)
            bit_add(r+1,-val)
        ans=[]
        for q in queries:
            if q[0]==1:
                _,u,v,wnew=q
                key=(min(u,v),max(u,v))
                child=edge_to_child[key]
                old=edge_weight[key]
                delta=wnew-old
                edge_weight[key]=wnew
                range_add(in_time[child],out_time[child],delta)
            else:
                _,x=q
                res=dist[x]+bit_sum(in_time[x])
                ans.append(res)
        return ans
