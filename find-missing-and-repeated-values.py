class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeat = None
        total_sum = 0
        for row in grid:
            for val in row:
                total_sum += val
                if val in seen:
                    repeat = val
                else:
                    seen.add(val)
        all_sum = n * n * (n * n + 1) // 2
        missing = all_sum - (total_sum - repeat)
        return [repeat, missing]
