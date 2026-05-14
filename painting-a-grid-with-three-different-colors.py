class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        patterns = []
        def gen(pos, cur):
            if pos == m:
                patterns.append(tuple(cur))
                return
            for color in range(3):
                if pos > 0 and color == cur[-1]:
                    continue
                cur.append(color)
                gen(pos + 1, cur)
                cur.pop()
        gen(0, [])
        pcount = len(patterns)
        comp = [[] for _ in range(pcount)]
        for i, p1 in enumerate(patterns):
            for j, p2 in enumerate(patterns):
                ok = True
                for k in range(m):
                    if p1[k] == p2[k]:
                        ok = False
                        break
                if ok:
                    comp[i].append(j)
        dp = [1] * pcount
        for _ in range(1, n):
            ndp = [0] * pcount
            for i in range(pcount):
                val = dp[i]
                if val == 0:
                    continue
                for j in comp[i]:
                    ndp[j] = (ndp[j] + val) % MOD
            dp = ndp
        return sum(dp) % MOD