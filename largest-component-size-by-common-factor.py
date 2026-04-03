from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            return True
        return False

class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_val = max(nums)
        dsu = DSU(max_val)

        def get_prime_factors(n):
            factors = set()
            d = 2
            temp = n
            while d * d <= temp:
                if temp % d == 0:
                    factors.add(d)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                factors.add(temp)
            return list(factors)

        for num in nums:
            factors = get_prime_factors(num)
            if factors:
                dsu.union(num, factors[0])
                for i in range(1, len(factors)):
                    dsu.union(factors[0], factors[i])

        component_counts = defaultdict(int)
        for num in nums:
            root = dsu.find(num)
            component_counts[root] += 1
        
        return max(component_counts.values())
