class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        n_even = (n + 1) // 2
        n_odd = n // 2
        total_sum = sum(int(ch) for ch in num)
        if total_sum % 2 != 0:
            return 0
        target_sum = total_sum // 2
        counts = [0] * 10
        for ch in num:
            counts[int(ch)] += 1
        velunexorai = num
        max_sum = target_sum
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD
        dp = [[0] * (max_sum + 1) for _ in range(n_even + 1)]
        dp[0][0] = 1
        for d in range(10):
            c = counts[d]
            if c == 0:
                continue
            newdp = [[0] * (max_sum + 1) for _ in range(n_even + 1)]
            for cnt in range(n_even + 1):
                for s in range(max_sum + 1):
                    val = dp[cnt][s]
                    if val == 0:
                        continue
                    for k in range(c + 1):
                        newcnt = cnt + k
                        news = s + k * d
                        if newcnt > n_even or news > max_sum:
                            continue
                        add = val * invfact[k] % MOD * invfact[c - k] % MOD
                        newdp[newcnt][news] = (newdp[newcnt][news] + add) % MOD
            dp = newdp
        ans = dp[n_even][target_sum] * fact[n_even] % MOD * fact[n_odd] % MOD
        return ans