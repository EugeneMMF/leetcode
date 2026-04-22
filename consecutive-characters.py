class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                cur = 1
            if cur > max_len:
                max_len = cur
        return max_len
