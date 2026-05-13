class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        import bisect
        MOD = 10**9 + 7
        packages.sort()
        n = len(packages)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + packages[i]
        best = None
        max_package = packages[-1]
        for b in boxes:
            b_set = sorted(set(b))
            if b_set[-1] < max_package:
                continue
            waste = 0
            prev = 0
            for size in b_set:
                idx = bisect.bisect_right(packages, size)
                if idx > prev:
                    count = idx - prev
                    waste += size * count - (prefix[idx] - prefix[prev])
                    prev = idx
                if prev == n:
                    break
            if prev == n:
                if best is None or waste < best:
                    best = waste
        return -1 if best is None else best % MOD