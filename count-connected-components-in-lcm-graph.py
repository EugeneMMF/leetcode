class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        from math import gcd
        arr = [x for x in nums if x <= threshold]
        m = len(arr)
        parent = list(range(m))
        rank = [0] * m
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
        buckets = [[] for _ in range(threshold + 1)]
        for idx, val in enumerate(arr):
            for mult in range(val, threshold + 1, val):
                buckets[mult].append(idx)
        for lst in buckets:
            if len(lst) > 1:
                first = lst[0]
                for other in lst[1:]:
                    union(first, other)
        comps = set(find(i) for i in range(m))
        return len(comps) + (len(nums) - m)
