class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for u, v in edges:
            indeg[v] += 1
        candidates = [i for i, d in enumerate(indeg) if d == 0]
        return candidates[0] if len(candidates) == 1 else -1