class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        prime_to_index = {}
        for i, val in enumerate(nums):
            x = val
            primes = set()
            while x > 1:
                p = spf[x]
                primes.add(p)
                while x % p == 0:
                    x //= p
            for p in primes:
                if p in prime_to_index:
                    union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i
        sorted_nums = sorted(nums)
        comp = {}
        for i in range(n):
            r = find(i)
            if r not in comp:
                comp[r] = []
            comp[r].append(i)
        for indices in comp.values():
            orig = sorted(nums[i] for i in indices)
            target = sorted(sorted_nums[i] for i in indices)
            if orig != target:
                return False
        return True
