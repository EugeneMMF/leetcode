class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        from functools import lru_cache
        n = len(nums1)
        @lru_cache(None)
        def dfs(mask: int) -> int:
            i = mask.bit_count()
            if i == n:
                return 0
            best = 10**9
            for j in range(n):
                if not (mask >> j) & 1:
                    val = (nums1[i] ^ nums2[j]) + dfs(mask | (1 << j))
                    if val < best:
                        best = val
            return best
        return dfs(0)
