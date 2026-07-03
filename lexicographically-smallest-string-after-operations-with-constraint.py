class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        n = len(s)
        res = []
        for i in range(n):
            orig = s[i]
            for c in map(chr, range(ord('a'), ord('z') + 1)):
                diff = abs(ord(orig) - ord(c))
                cost = min(diff, 26 - diff)
                if cost <= k:
                    res.append(c)
                    k -= cost
                    break
        return ''.join(res)
