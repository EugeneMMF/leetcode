class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        M = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        dp[1] = 1
        prefix[1] = 1
        for d in range(2, n + 1):
            left = d - delay
            right = d - forget
            if left >= 1:
                left_sum = prefix[left]
            else:
                left_sum = 0
            if right >= 0:
                right_sum = prefix[right]
            else:
                right_sum = 0
            dp[d] = (left_sum - right_sum) % M
            prefix[d] = (prefix[d - 1] + dp[d]) % M
        start = n - forget + 1
        if start <= 0:
            start = 1
        if start > n:
            return 0
        ans = (prefix[n] - prefix[start - 1]) % M
        return ans