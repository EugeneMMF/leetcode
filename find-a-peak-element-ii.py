from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            max_row = 0
            for i in range(1, m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            left_val = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right_val = mat[max_row][mid + 1] if mid + 1 < n else -1
            if left_val > mat[max_row][mid]:
                right = mid - 1
            elif right_val > mat[max_row][mid]:
                left = mid + 1
            else:
                return [max_row, mid]
        return [0, 0]
