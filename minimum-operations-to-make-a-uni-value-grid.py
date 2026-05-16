from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = [cell for row in grid for cell in row]
        mod = values[0] % x
        for v in values:
            if v % x != mod:
                return -1
        values.sort()
        median = values[len(values)//2]
        ops = sum(abs(v - median)//x for v in values)
        return ops
