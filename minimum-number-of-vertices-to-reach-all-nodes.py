from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg = [0] * n
        for u, v in edges:
            indeg[v] += 1
        return [i for i in range(n) if indeg[i] == 0]
