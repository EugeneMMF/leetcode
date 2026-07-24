class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        L = len(s)
        max_bits = L
        # precompute factorials
        fact = [1] * (max_bits + 1)
        inv_fact = [1] * (max_bits + 1)
        for i in range(1, max_bits + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[max_bits] = pow(fact[max_bits], MOD - 2, MOD)
        for i in range(max_bits, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
        # compute steps to reach 1 via popcount
        max_p = max_bits
        steps = [0] * (max_p + 1)
        steps[0] = 0  # unused
        steps[1] = 0
        for i in range(2, max_p + 1):
            pc = bin(i).count('1')
            steps[i] = 1 + steps[pc]
        # set of popcounts that lead to 1 within k-1 steps
        allowed = set()
        for p in range(1, max_p + 1):
            if steps[p] <= k - 1:
                allowed.add(p)
        total = 0
        ones = 0
        for i, ch in enumerate(s):
            if ch == '1':
                rem = L - i - 1
                for p in allowed:
                    need = p - ones
                    if 0 <= need <= rem:
                        total = (total + comb(rem, need)) % MOD
                ones += 1
        return total % MOD