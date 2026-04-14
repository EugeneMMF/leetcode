class Solution:
    def largestComponentSize(self, nums):
        n = len(nums)
        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i
        parent = list(range(n))
        size = [1] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
        prime_to_index = {}
        for i, num in enumerate(nums):
            x = num
            while x > 1:
                p = spf[x]
                while x % p == 0:
                    x //= p
                if p in prime_to_index:
                    union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i
        ans = 0
        for i in range(n):
            if parent[i] == i and size[i] > ans:
                ans = size[i]
        return ans
