class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        vals = []
        for i, row in enumerate(grid):
            if i % 2 == 0:
                vals.extend(row)
            else:
                vals.extend(row[::-1])
        return vals[::2]
