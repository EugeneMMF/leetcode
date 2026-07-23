class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        pref0 = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref0[i + 1] = pref0[i] + (1 if ch == '0' else 0)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                zeros = pref0[j + 1] - pref0[i]
                ones = (j - i + 1) - zeros
                if zeros <= k or ones <= k:
                    ans += 1
        return ans