class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        if k * minLength > n:
            return 0
        prime_digits = set('2357')
        nonprime_digits = set('14689')
        dp_prev = [0] * (n + 1)
        dp_prev[0] = 1
        pref_prime_prev = [0] * (n + 1)
        for i in range(n):
            pref_prime_prev[i + 1] = pref_prime_prev[i]
            if s[i] in prime_digits:
                pref_prime_prev[i + 1] = (pref_prime_prev[i + 1] + dp_prev[i]) % MOD
        for _ in range(1, k + 1):
            dp_curr = [0] * (n + 1)
            pref_prime_curr = [0] * (n + 1)
            for i in range(1, n + 1):
                if s[i - 1] in nonprime_digits:
                    limit = i - minLength
                    if limit >= 0:
                        dp_curr[i] = pref_prime_prev[limit + 1]
            for i in range(n):
                pref_prime_curr[i + 1] = pref_prime_curr[i]
                if s[i] in prime_digits:
                    pref_prime_curr[i + 1] = (pref_prime_curr[i + 1] + dp_curr[i]) % MOD
            dp_prev = dp_curr
            pref_prime_prev = pref_prime_curr
        return dp_prev[n] % MOD