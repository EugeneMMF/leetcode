class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        mod1, mod2 = 1000000007, 1000000009
        base = 911382323
        max_len = max(len(p) for p in paths)
        pow1 = [1] * (max_len + 1)
        pow2 = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            pow1[i] = (pow1[i-1] * base) % mod1
            pow2[i] = (pow2[i-1] * base) % mod2
        pref = []
        for p in paths:
            l = len(p)
            h1 = [0] * (l + 1)
            h2 = [0] * (l + 1)
            for i, v in enumerate(p, 1):
                h1[i] = (h1[i-1] * base + v + 1) % mod1
                h2[i] = (h2[i-1] * base + v + 1) % mod2
            pref.append((h1, h2))
        def check(L):
            if L == 0:
                return True
            first_hashes = set()
            h1, h2 = pref[0]
            for i in range(L, len(h1)):
                x1 = (h1[i] - h1[i-L] * pow1[L]) % mod1
                x2 = (h2[i] - h2[i-L] * pow2[L]) % mod2
                first_hashes.add((x1, x2))
            if not first_hashes:
                return False
            for idx in range(1, len(paths)):
                cur_hashes = set()
                h1, h2 = pref[idx]
                for i in range(L, len(h1)):
                    x1 = (h1[i] - h1[i-L] * pow1[L]) % mod1
                    x2 = (h2[i] - h2[i-L] * pow2[L]) % mod2
                    cur_hashes.add((x1, x2))
                first_hashes &= cur_hashes
                if not first_hashes:
                    return False
            return bool(first_hashes)
        lo, hi = 1, min(len(p) for p in paths)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans