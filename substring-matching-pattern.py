class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        star = p.index('*')
        prefix = p[:star]
        suffix = p[star+1:]
        lp, ls = len(prefix), len(suffix)
        n = len(s)
        for i in range(n - lp + 1):
            if s[i:i+lp] != prefix:
                continue
            for j in range(n - ls + 1):
                if j < i + lp:
                    continue
                if s[j:j+ls] != suffix:
                    continue
                return True
        return False