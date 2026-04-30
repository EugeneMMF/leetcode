class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = set('aeiouAEIOU')
        m = len(s) // 2
        return sum(c in v for c in s[:m]) == sum(c in v for c in s[m:])
