class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min_row = m
        min_col = n

        for op_ai, op_bi in ops:
            min_row = min(min_row, op_ai)
            min_col = min(min_col, op_bi)
        
        return min_row * min_col
