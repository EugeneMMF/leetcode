class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        pref = [0] * n
        seen = set()
        for i, ch in enumerate(s):
            seen.add(ch)
            pref[i] = len(seen)
        suf = [0] * n
        seen.clear()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            suf[i] = len(seen)
        ans = 0
        for i in range(n - 1):
            if pref[i] == suf[i + 1]:
                ans += 1
        return ans
