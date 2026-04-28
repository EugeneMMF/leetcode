class Solution:
    def matrixRankTransform(self, matrix):
        from typing import List
        m=len(matrix); n=len(matrix[0])
        cells=[]
        for i in range(m):
            for j in range(n):
                cells.append((matrix[i][j], i, j))
        cells.sort(key=lambda x:x[0])
        ans=[[0]*n for _ in range(m)]
        row_max=[0]*m
        col_max=[0]*n
        idx=0
        while idx < len(cells):
            val=cells[idx][0]
            same=[]
            while idx < len(cells) and cells[idx][0]==val:
                same.append(cells[idx])
                idx+=1
            parent={}
            rank={}
            def find(x):
                while parent[x]!=x:
                    parent[x]=parent[parent[x]]
                    x=parent[x]
                return x
            def union(x,y):
                rx,ry=find(x),find(y)
                if rx==ry:return
                if rank[rx]<rank[ry]:
                    parent[rx]=ry
                elif rank[rx]>rank[ry]:
                    parent[ry]=rx
                else:
                    parent[ry]=rx
                    rank[rx]+=1
            row_map={}
            col_map={}
            for _,i,j in same:
                id=i*n+j
                parent[id]=id
                rank[id]=0
                if i in row_map:
                    union(id,row_map[i])
                else:
                    row_map[i]=id
                if j in col_map:
                    union(id,col_map[j])
                else:
                    col_map[j]=id
            groups={}
            for _,i,j in same:
                id=i*n+j
                r=find(id)
                groups.setdefault(r,[]).append((i,j))
            for cells_list in groups.values():
                max_rank=0
                for i,j in cells_list:
                    if row_max[i]>max_rank:max_rank=row_max[i]
                    if col_max[j]>max_rank:max_rank=col_max[j]
                new_rank=max_rank+1
                for i,j in cells_list:
                    ans[i][j]=new_rank
                    row_max[i]=new_rank if new_rank>row_max[i] else row_max[i]
                    col_max[j]=new_rank if new_rank>col_max[j] else col_max[j]
        return ans
