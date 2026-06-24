class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        max_len = 1
        left = 0
        pair_count = 0
        for right in range(1, n):
            if s[right] == s[right - 1]:
                pair_count += 1
            while pair_count > 1:
                if left + 1 <= right and s[left] == s[left + 1]:
                    pair_count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
