class Solution:
    def numberOfGoodSubsets(self, nums):
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_index = {p: i for i, p in enumerate(primes)}
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        count1 = freq.get(1, 0)
        masks = {}
        for v in range(2, 31):
            if v not in freq:
                continue
            x = v
            mask = 0
            ok = True
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    cnt = 0
                    while x % p == 0:
                        x //= p
                        cnt += 1
                    if cnt > 1:
                        ok = False
                        break
                    mask |= 1 << prime_index[p]
            if not ok:
                continue
            if x > 1:
                if x in prime_index:
                    mask |= 1 << prime_index[x]
                else:
                    ok = False
            if not ok:
                continue
            masks[v] = mask
        dp = [0] * (1 << 10)
        dp[0] = 1
        for v, mask in masks.items():
            c = freq[v]
            for s in range((1 << 10) - 1, -1, -1):
                if s & mask == 0:
                    dp[s | mask] = (dp[s | mask] + dp[s] * c) % MOD
        total = (sum(dp) - 1) % MOD
        total = total * pow(2, count1, MOD) % MOD
        return total
