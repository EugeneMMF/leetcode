from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        deadlines = [(d - 1) // s for d, s in zip(dist, speed)]
        deadlines.sort()
        count = 0
        for i, d in enumerate(deadlines):
            if d < i:
                break
            count += 1
        return count