class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        total = s.count('1')
        if total == 0:
            return ((n - 1) * (n - 2) // 2) % MOD
        if total % 3 != 0:
            return 0
        k = total // 3
        ones = [i for i, ch in enumerate(s) if ch == '1']
        first_gap = ones[k] - ones[k - 1] - 1
        second_gap = ones[2 * k] - ones[2 * k - 1] - 1
        return ((first_gap + 1) * (second_gap + 1)) % MOD
