class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * n
        for v in nums:
            freq[v] += 1
        ans = 0
        count_lt = 0
        for k in range(n + 1):
            if count_lt == k and (k == n or freq[k] == 0):
                ans += 1
            if k < n:
                count_lt += freq[k]
        return ans