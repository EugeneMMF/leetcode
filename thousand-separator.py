class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        parts = []
        while s:
            parts.append(s[-3:])
            s = s[:-3]
        return '.'.join(reversed(parts))
