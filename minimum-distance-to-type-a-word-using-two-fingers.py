class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            ra, ca = divmod(ord(a) - 65, 6)
            rb, cb = divmod(ord(b) - 65, 6)
            return abs(ra - rb) + abs(ca - cb)
        n = len(word)
        if n <= 1:
            return 0
        prev = word[0]
        dp = {26: 0}
        INF = 10**9
        for i in range(1, n):
            cur = word[i]
            ndp = {}
            for other, cost in dp.items():
                c1 = cost + dist(prev, cur)
                if c1 < ndp.get(other, INF):
                    ndp[other] = c1
                if other == 26:
                    c2 = cost
                else:
                    c2 = cost + dist(chr(other + 65), cur)
                other2 = ord(prev) - 65
                if c2 < ndp.get(other2, INF):
                    ndp[other2] = c2
            dp = ndp
            prev = cur
        return min(dp.values())
