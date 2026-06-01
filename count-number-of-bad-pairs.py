class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        cnt = Counter(i - nums[i] for i in range(n))
        good = sum(c * (c - 1) // 2 for c in cnt.values())
        total = n * (n - 1) // 2
        return total - good
