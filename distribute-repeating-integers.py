class Solution:
    def canDistribute(self, nums, quantity):
        from collections import Counter
        cnt = list(Counter(nums).values())
        m = len(quantity)
        full = 1 << m
        subset_sum = [0] * full
        for mask in range(1, full):
            lsb = mask & -mask
            idx = (lsb.bit_length() - 1)
            subset_sum[mask] = subset_sum[mask ^ lsb] + quantity[idx]
        cnt.sort(reverse=True)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, mask):
            if mask == 0:
                return True
            if i == len(cnt):
                return False
            sub = mask
            while sub:
                if subset_sum[sub] <= cnt[i]:
                    if dfs(i + 1, mask ^ sub):
                        return True
                sub = (sub - 1) & mask
            return dfs(i + 1, mask)
        return dfs(0, full - 1)
