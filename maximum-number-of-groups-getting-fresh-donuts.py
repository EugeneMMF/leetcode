class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        from functools import lru_cache
        counts = [0] * batchSize
        for g in groups:
            counts[g % batchSize] += 1
        base = counts[0]
        counts[0] = 0
        @lru_cache(None)
        def dfs(state, rem):
            best = 0
            state_list = list(state)
            for r in range(1, batchSize):
                if state_list[r]:
                    state_list[r] -= 1
                    new_rem = (rem + r) % batchSize
                    val = dfs(tuple(state_list), new_rem) + (1 if rem == 0 else 0)
                    if val > best:
                        best = val
                    state_list[r] += 1
            return best
        return base + dfs(tuple(counts), 0)
