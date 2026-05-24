class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            digit = pressedKeys[i - 1]
            max_len = 4 if digit in '79' else 3
            for k in range(1, max_len + 1):
                j = i - k
                if j < 0:
                    break
                if pressedKeys[j] != digit:
                    break
                dp[i] = (dp[i] + dp[j]) % MOD
        return dp[n] % MOD
