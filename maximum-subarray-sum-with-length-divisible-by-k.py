class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_prefix = [10**20] * k
        min_prefix[0] = 0
        s = 0
        ans = -10**20
        for i in range(1, n + 1):
            s += nums[i - 1]
            r = i % k
            if min_prefix[r] != 10**20:
                cand = s - min_prefix[r]
                if cand > ans:
                    ans = cand
            if s < min_prefix[r]:
                min_prefix[r] = s
        return ans
