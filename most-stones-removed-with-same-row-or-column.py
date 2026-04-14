from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent={}
        rank={}
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra==rb:
                return
            if rank[ra]<rank[rb]:
                parent[ra]=rb
            elif rank[ra]>rank[rb]:
                parent[rb]=ra
            else:
                parent[rb]=ra
                rank[ra]+=1
        for x,y in stones:
            row=('r',x)
            col=('c',y)
            if row not in parent:
                parent[row]=row
                rank[row]=0
            if col not in parent:
                parent[col]=col
                rank[col]=0
            union(row,col)
        roots=set()
        for node in parent:
            roots.add(find(node))
        return len(stones)-len(roots)
