class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1
        degrees.sort()
        total = 0
        for i, d in enumerate(degrees, 1):
            total += i * d
        return total
