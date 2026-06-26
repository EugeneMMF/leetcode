class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        m = max(freq.values())
        if m > n // 2:
            return 2 * m - n
        return n % 2
