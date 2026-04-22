from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()
        for a, b in paths:
            starts.add(a)
        for a, b in paths:
            if b not in starts:
                return b
