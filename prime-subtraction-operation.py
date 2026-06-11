class Solution:
    def primeSubOperation(self, nums):
        n = len(nums)
        max_val = 1000
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_val ** 0.5) + 1):
            if is_prime[i]:
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    is_prime[j] = False
        primes = [i for i, v in enumerate(is_prime) if v]
        prev = -float('inf')
        for num in nums:
            chosen = None
            for p in reversed(primes):
                if p >= num:
                    continue
                val = num - p
                if val > prev:
                    chosen = val
                    break
            if chosen is None:
                if num > prev:
                    chosen = num
                else:
                    return False
            prev = chosen
        return True
