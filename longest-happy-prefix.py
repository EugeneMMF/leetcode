class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        l = pi[-1]
        return s[:l] if l > 0 else ""
