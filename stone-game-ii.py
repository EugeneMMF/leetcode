class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            if i == n:
                return 0
            if (i, m) in memo:
                return memo[(i, m)]

            max_stones = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                remaining_stones = suffix_sum[i + x]
                current_stones = suffix_sum[i] - remaining_stones
                stones_alice_gets = current_stones + (remaining_stones - dp(i + x, max(m, x)))
                max_stones = max(max_stones, stones_alice_gets)

            memo[(i, m)] = max_stones
            return max_stones

        return dp(0, 1)
