class Solution:
    def getSmallestString(self, s: str) -> str:
        best = s
        n = len(s)
        for i in range(n - 1):
            if (int(s[i]) % 2) == (int(s[i + 1]) % 2):
                swapped = s[:i] + s[i + 1] + s[i] + s[i + 2:]
                if swapped < best:
                    best = swapped
        return best