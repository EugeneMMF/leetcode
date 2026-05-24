class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        occupied = set(map(tuple, guards + walls))
        guarded = set()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for r,c in guards:
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                while 0 <= nr < m and 0 <= nc < n and (nr,nc) not in occupied:
                    guarded.add((nr,nc))
                    nr += dr
                    nc += dc
        total = m*n
        return total - len(occupied) - len(guarded)