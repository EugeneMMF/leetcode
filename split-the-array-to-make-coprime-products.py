class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return -1
        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        def get_primes(x):
            primes = set()
            while x > 1:
                p = spf[x]
                primes.add(p)
                while x % p == 0:
                    x //= p
            return primes
        suffix_counts = {}
        for num in nums:
            for p in get_primes(num):
                suffix_counts[p] = suffix_counts.get(p, 0) + 1
        prefix_set = set()
        for i in range(n - 1):
            primes = get_primes(nums[i])
            for p in primes:
                suffix_counts[p] -= 1
                if suffix_counts[p] == 0:
                    del suffix_counts[p]
            for p in primes:
                prefix_set.add(p)
            if not prefix_set & suffix_counts.keys():
                return i
        return -1