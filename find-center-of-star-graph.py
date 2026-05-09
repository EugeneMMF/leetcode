from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]
        if c == a or d == a:
            return a
        return b
