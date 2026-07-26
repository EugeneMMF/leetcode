class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n - k + 1):
            c = s[i]
            if s[i:i + k] == c * k:
                if i == 0 or s[i - 1] != c:
                    if i + k == n or s[i + k] != c:
                        return True
        return False