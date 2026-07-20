class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [dict() for _ in range(k + 1)]
        best1_val = [None] * (k + 1)
        best1_len = [0] * (k + 1)
        best2_len = [0] * (k + 1)
        for x in nums:
            for t in range(k, -1, -1):
                # same value extension
                prev_len = dp[t].get(x, 0)
                new_len = prev_len + 1
                if new_len > prev_len:
                    dp[t][x] = new_len
                    if new_len > best1_len[t]:
                        best2_len[t] = best1_len[t]
                        best1_len[t] = new_len
                        best1_val[t] = x
                    elif new_len > best2_len[t]:
                        best2_len[t] = new_len
                # transition from different value
                if t > 0:
                    bl = best1_len[t - 1]
                    bv = best1_val[t - 1]
                    if bv == x:
                        bl = best2_len[t - 1]
                    if bl > 0:
                        new_len2 = bl + 1
                        if new_len2 > dp[t].get(x, 0):
                            dp[t][x] = new_len2
                            if new_len2 > best1_len[t]:
                                best2_len[t] = best1_len[t]
                                best1_len[t] = new_len2
                                best1_val[t] = x
                            elif new_len2 > best2_len[t]:
                                best2_len[t] = new_len2
        ans = 0
        for t in range(k + 1):
            if dp[t]:
                ans = max(ans, max(dp[t].values()))
        return ans