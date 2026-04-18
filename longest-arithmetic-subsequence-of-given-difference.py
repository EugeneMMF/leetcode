class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        best = 0
        for x in arr:
            prev = x - difference
            cur_len = dp.get(prev, 0) + 1
            dp[x] = cur_len
            if cur_len > best:
                best = cur_len
        return best
