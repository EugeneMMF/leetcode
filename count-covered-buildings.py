class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_min = {}
        row_max = {}
        col_min = {}
        col_max = {}
        for x, y in buildings:
            if y in row_min:
                if x < row_min[y]:
                    row_min[y] = x
                if x > row_max[y]:
                    row_max[y] = x
            else:
                row_min[y] = row_max[y] = x
            if x in col_min:
                if y < col_min[x]:
                    col_min[x] = y
                if y > col_max[x]:
                    col_max[x] = y
            else:
                col_min[x] = col_max[x] = y
        count = 0
        for x, y in buildings:
            if row_min[y] < x < row_max[y] and col_min[x] < y < col_max[x]:
                count += 1
        return count