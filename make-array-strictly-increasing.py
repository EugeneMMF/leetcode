class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        import bisect
        arr2 = sorted(set(arr2))
        dp = { -1: 0 }
        for a in arr1:
            ndp = {}
            for prev, ops in dp.items():
                if a > prev:
                    if a not in ndp or ops < ndp[a]:
                        ndp[a] = ops
                idx = bisect.bisect_right(arr2, prev)
                if idx < len(arr2):
                    val = arr2[idx]
                    if val not in ndp or ops + 1 < ndp[val]:
                        ndp[val] = ops + 1
            dp = ndp
            if not dp:
                return -1
        return min(dp.values()) if dp else -1
