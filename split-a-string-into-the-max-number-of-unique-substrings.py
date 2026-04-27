class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, used):
            if i == n:
                return 0
            used_set = set(used.split(',')) if used else set()
            best = 0
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub not in used_set:
                    new_used = used + (',' + sub if used else sub)
                    best = max(best, 1 + dfs(j, new_used))
            return best

        return dfs(0, '')
