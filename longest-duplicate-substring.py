class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - 97 for c in s]
        mod1, mod2 = 1000000007, 1000000009
        base = 256

        def search(L):
            h1 = h2 = 0
            for i in range(L):
                h1 = (h1 * base + nums[i]) % mod1
                h2 = (h2 * base + nums[i]) % mod2
            seen = {(h1, h2): 0}
            baseL1 = pow(base, L, mod1)
            baseL2 = pow(base, L, mod2)
            for start in range(1, n - L + 1):
                h1 = (h1 * base - nums[start - 1] * baseL1 + nums[start + L - 1]) % mod1
                h2 = (h2 * base - nums[start - 1] * baseL2 + nums[start + L - 1]) % mod2
                if (h1, h2) in seen:
                    return start
                seen[(h1, h2)] = start
            return -1

        lo, hi = 1, n
        start = -1
        length = 0
        while lo < hi:
            mid = (lo + hi) // 2
            idx = search(mid)
            if idx != -1:
                lo = mid + 1
                start = idx
                length = mid
            else:
                hi = mid
        if length == 0:
            return ""
        return s[start:start + length]
