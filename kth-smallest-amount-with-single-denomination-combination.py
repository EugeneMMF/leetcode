class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        n = len(coins)
        lcms = []
        signs = []
        for mask in range(1, 1 << n):
            l = 1
            bits = 0
            for i in range(n):
                if mask >> i & 1:
                    bits += 1
                    a = coins[i]
                    l = l // gcd(l, a) * a
            lcms.append(l)
            signs.append(1 if bits % 2 else -1)
        def count(x):
            s = 0
            for l, sgn in zip(lcms, signs):
                if l <= x:
                    s += sgn * (x // l)
            return s
        high = max(coins) * k
        low = 1
        while low < high:
            mid = (low + high) // 2
            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low