class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float('inf')
        neg_count = 0
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                abs_val = val if val >= 0 else -val
                total += abs_val
                if abs_val < min_abs:
                    min_abs = abs_val
        if neg_count % 2 == 1:
            total -= 2 * min_abs
        return total