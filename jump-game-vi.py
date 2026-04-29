class Solution:
    def maxResult(self, nums, k):
        from collections import deque
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque()
        dq.append((0, dp[0]))
        for i in range(1, n):
            while dq and dq[0][0] < i - k:
                dq.popleft()
            dp[i] = nums[i] + dq[0][1]
            while dq and dq[-1][1] <= dp[i]:
                dq.pop()
            dq.append((i, dp[i]))
        return dp[-1]
