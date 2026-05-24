class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        last = [-1] * 26
        ans = 0
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            prev = last[idx]
            ans += (i - prev) * (n - i)
            last[idx] = i
        return ans
