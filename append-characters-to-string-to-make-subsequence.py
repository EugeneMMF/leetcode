class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        lt = len(t)
        for c in s:
            if j < lt and c == t[j]:
                j += 1
        return lt - j