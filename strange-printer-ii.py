class Solution:
    def isPrintable(self, targetGrid):
        m=len(targetGrid); n=len(targetGrid[0])
        max_color=60
        mins=[[m, n] for _ in range(max_color+1)]
        maxs=[[-1, -1] for _ in range(max_color+1)]
        present=set()
        for i in range(m):
            for j in range(n):
                c=targetGrid[i][j]
                present.add(c)
                if i<mins[c][0]: mins[c][0]=i
                if j<mins[c][1]: mins[c][1]=j
                if i>maxs[c][0]: maxs[c][0]=i
                if j>maxs[c][1]: maxs[c][1]=j
        indeg={c:0 for c in present}
        adj={c:set() for c in present}
        for c in present:
            r1,r2=mins[c][0],maxs[c][0]
            c1,c2=mins[c][1],maxs[c][1]
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    d=targetGrid[i][j]
                    if d!=c:
                        if d not in adj[c]:
                            adj[c].add(d)
                            indeg[d]+=1
        from collections import deque
        q=deque([c for c in present if indeg[c]==0])
        cnt=0
        while q:
            cur=q.popleft()
            cnt+=1
            for nb in adj[cur]:
                indeg[nb]-=1
                if indeg[nb]==0:
                    q.append(nb)
        return cnt==len(present)
