class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        max_len = 0
        for i in range(n + 1):
            for j in range(i, n + 1):
                sub_s = s[i:j]
                for k in range(m + 1):
                    for l in range(k, m + 1):
                        sub_t = t[k:l]
                        combined = sub_s + sub_t
                        if combined == combined[::-1]:
                            if len(combined) > max_len:
                                max_len = len(combined)
        return max_len