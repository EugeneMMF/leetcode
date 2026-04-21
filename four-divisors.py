class Solution:
    def sumFourDivisors(self, nums):
        max_n = max(nums)
        spf = list(range(max_n + 1))
        for i in range(2, int(max_n ** 0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, max_n + 1, step):
                    if spf[j] == j:
                        spf[j] = i
        total = 0
        for n in nums:
            x = n
            factors = {}
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                factors[p] = cnt
            if len(factors) == 2 and all(v == 1 for v in factors.values()):
                p, q = factors.keys()
                total += 1 + p + q + p * q
            elif len(factors) == 1:
                p, e = next(iter(factors.items()))
                if e == 3:
                    total += 1 + p + p * p + p * p * p
        return total
