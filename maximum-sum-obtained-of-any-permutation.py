class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in requests:
            diff[l] += 1
            diff[r + 1] -= 1
        freq = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            freq[i] = cur
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        mod = 10**9 + 7
        ans = 0
        for a, b in zip(nums, freq):
            ans = (ans + a * b) % mod
        return ans
