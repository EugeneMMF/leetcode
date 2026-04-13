class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            best = s
            n = len(s)
            for i in range(1, n):
                cand = s[i:] + s[:i]
                if cand < best:
                    best = cand
            return best
        return ''.join(sorted(s))
