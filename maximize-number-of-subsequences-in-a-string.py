class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p0, p1 = pattern[0], pattern[1]
        if p0 == p1:
            cnt = text.count(p0)
            return (cnt + 1) * cnt // 2
        n = len(text)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (text[i] == p0)
        suff = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] + (text[i] == p1)
        orig = 0
        for i in range(n):
            if text[i] == p1:
                orig += pref[i]
        best_add = 0
        for i in range(n + 1):
            best_add = max(best_add, pref[i], suff[i])
        return orig + best_add
