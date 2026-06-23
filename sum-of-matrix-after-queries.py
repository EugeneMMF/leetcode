class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_set = [False] * n
        col_set = [False] * n
        remaining_rows = n
        remaining_cols = n
        total = 0
        for typ, idx, val in reversed(queries):
            if typ == 0:
                if not row_set[idx]:
                    total += val * remaining_cols
                    row_set[idx] = True
                    remaining_rows -= 1
            else:
                if not col_set[idx]:
                    total += val * remaining_rows
                    col_set[idx] = True
                    remaining_cols -= 1
        return total