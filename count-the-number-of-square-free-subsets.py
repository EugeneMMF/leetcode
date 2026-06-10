class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mask_counts = []
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
                continue
            m = 0
            ok = True
            tmp = num
            for i, p in enumerate(primes):
                cnt = 0
                while tmp % p == 0:
                    tmp //= p
                    cnt += 1
                if cnt >= 2:
                    ok = False
                    break
                if cnt == 1:
                    m |= 1 << i
            if ok and tmp == 1:
                mask_counts.append(m)
        dp = [0] * (1 << 10)
        dp[0] = 1
        for m in mask_counts:
            for mask in range((1 << 10) - 1, -1, -1):
                if dp[mask] and (mask & m) == 0:
                    dp[mask | m] = (dp[mask | m] + dp[mask]) % mod
        total = sum(dp) % mod
        total = total * pow(2, ones, mod) % mod
        total = (total - 1) % mod
        return total