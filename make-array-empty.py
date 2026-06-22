class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        indexed = [(v, i) for i, v in enumerate(nums)]
        indexed.sort()
        size = n + 1
        bit = [0] * size
        def add(i, delta):
            i += 1
            while i < size:
                bit[i] += delta
                i += i & -i
        def prefix(i):
            i += 1
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        def range_sum(l, r):
            return prefix(r) - (prefix(l - 1) if l > 0 else 0)
        for _, i in enumerate(range(n)):
            add(i, 1)
        front = 0
        ops = 0
        for _, idx in indexed:
            if front <= idx:
                dist = range_sum(front, idx)
            else:
                dist = range_sum(front, n - 1) + range_sum(0, idx)
            ops += dist
            add(idx, -1)
            front = idx + 1
            if front == n:
                front = 0
        return ops