class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        block_counts={}
        for x,y in coordinates:
            for dx in (-1,0):
                for dy in (-1,0):
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<m-1 and 0<=ny<n-1:
                        block_counts[(nx,ny)]=block_counts.get((nx,ny),0)+1
        res=[0]*5
        for cnt in block_counts.values():
            res[cnt]+=1
        total_blocks=(m-1)*(n-1)
        res[0]=total_blocks-sum(res[1:])
        return res