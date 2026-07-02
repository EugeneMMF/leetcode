from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        target = sum(apple)
        maxSum = sum(capacity)
        INF = 10**9
        dp = [INF] * (maxSum + 1)
        dp[0] = 0
        for c in capacity:
            for s in range(maxSum - c, -1, -1):
                if dp[s] + 1 < dp[s + c]:
                    dp[s + c] = dp[s] + 1
        ans = INF
        for s in range(target, maxSum + 1):
            if dp[s] < ans:
                ans = dp[s]
        return ans
