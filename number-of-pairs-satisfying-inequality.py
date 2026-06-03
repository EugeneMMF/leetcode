class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]
        vals = sorted(set(a))
        size = len(vals)
        bit = [0] * (size + 1)
        def add(idx, val=1):
            i = idx + 1
            while i <= size:
                bit[i] += val
                i += i & -i
        def query(idx):
            i = idx + 1
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s
        ans = 0
        for j in range(n):
            t = a[j] + diff
            idx = bisect_right(vals, t) - 1
            if idx >= 0:
                ans += query(idx)
            pos = bisect_left(vals, a[j])
            add(pos)
        return ans
