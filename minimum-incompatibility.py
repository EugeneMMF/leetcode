class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        group = n // k
        from collections import Counter
        cnt = Counter(nums)
        if any(v > k for v in cnt.values()):
            return -1
        full = (1 << n) - 1
        inc = {}
        for mask in range(1 << n):
            if mask.bit_count() != group:
                continue
            seen = set()
            mn = 10**9
            mx = -10**9
            ok = True
            m = mask
            idx = 0
            while m:
                if m & 1:
                    val = nums[idx]
                    if val in seen:
                        ok = False
                        break
                    seen.add(val)
                    if val < mn:
                        mn = val
                    if val > mx:
                        mx = val
                idx += 1
                m >>= 1
            if ok:
                inc[mask] = mx - mn
        valid = list(inc.keys())
        INF = 10**9
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            for sub in valid:
                if mask & sub:
                    continue
                new = mask | sub
                val = dp[mask] + inc[sub]
                if val < dp[new]:
                    dp[new] = val
        return dp[full] if dp[full] != INF else -1
