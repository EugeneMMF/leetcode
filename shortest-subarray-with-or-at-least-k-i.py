class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = n + 1
        for i in range(n):
            or_val = 0
            for j in range(i, n):
                or_val |= nums[j]
                if or_val >= k:
                    best = min(best, j - i + 1)
                    break
        return best if best <= n else -1