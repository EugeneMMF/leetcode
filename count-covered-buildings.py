from typing import List
import bisect

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_map = {}
        col_map = {}
        for x, y in buildings:
            row_map.setdefault(x, []).append(y)
            col_map.setdefault(y, []).append(x)
        for lst in row_map.values():
            lst.sort()
        for lst in col_map.values():
            lst.sort()
        count = 0
        for x, y in buildings:
            row_list = row_map[x]
            col_list = col_map[y]
            idx_row = bisect.bisect_left(row_list, y)
            left = idx_row > 0
            right = idx_row < len(row_list) - 1
            idx_col = bisect.bisect_left(col_list, x)
            above = idx_col > 0
            below = idx_col < len(col_list) - 1
            if left and right and above and below:
                count += 1
        return count
