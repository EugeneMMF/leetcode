class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [dict() for _ in range(k+1)]
        for x in nums:
            new_dp = [d.copy() for d in dp]
            if 1 > new_dp[0].get(x, 0):
                new_dp[0][x] = 1
            for t in range(k+1):
                for val, length in dp[t].items():
                    if val == x:
                        if length + 1 > new_dp[t].get(x, 0):
                            new_dp[t][x] = length + 1
                    else:
                        if t + 1 <= k:
                            if length + 1 > new_dp[t+1].get(x, 0):
                                new_dp[t+1][x] = length + 1
            dp = new_dp
        ans = 0
        for t in range(k+1):
            for length in dp[t].values():
                if length > ans:
                    ans = length
        return ans
