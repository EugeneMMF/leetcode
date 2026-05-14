from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = 0
        added = 0
        for rung in rungs:
            diff = rung - prev
            if diff > dist:
                added += (diff - 1) // dist
            prev = rung
        return added
