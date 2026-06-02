class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        row_masks = []
        for row in matrix:
            mask = 0
            for j, val in enumerate(row):
                if val:
                    mask |= 1 << j
            row_masks.append(mask)
        from itertools import combinations
        best = 0
        cols = range(n)
        for comb in combinations(cols, numSelect):
            subset_mask = 0
            for c in comb:
                subset_mask |= 1 << c
            count = 0
            for rm in row_masks:
                if rm & ~subset_mask == 0:
                    count += 1
            if count > best:
                best = count
        return best
