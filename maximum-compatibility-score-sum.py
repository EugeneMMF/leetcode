class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        scores = [[sum(a == b for a, b in zip(students[i], mentors[j])) for j in range(n)] for i in range(n)]
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, mask):
            if i == n:
                return 0
            best = 0
            for j in range(n):
                if not (mask >> j) & 1:
                    best = max(best, scores[i][j] + dfs(i + 1, mask | (1 << j)))
            return best
        return dfs(0, 0)
