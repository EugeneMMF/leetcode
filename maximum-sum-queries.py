import bisect
from typing import List

class SegTree:
    def __init__(self, size):
        self.N = 1
        while self.N < size:
            self.N <<= 1
        self.data = [-1] * (2 * self.N)
    def update(self, pos, val):
        i = pos + self.N
        if val > self.data[i]:
            self.data[i] = val
            i >>= 1
            while i:
                left = self.data[i << 1]
                right = self.data[(i << 1) | 1]
                self.data[i] = left if left > right else right
                i >>= 1
    def query(self, l, r):
        if l > r:
            return -1
        l += self.N
        r += self.N
        res = -1
        while l <= r:
            if l & 1:
                if self.data[l] > res:
                    res = self.data[l]
                l += 1
            if not (r & 1):
                if self.data[r] > res:
                    res = self.data[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        items = [(nums1[i], nums2[i], nums1[i] + nums2[i]) for i in range(n)]
        items.sort(reverse=True)
        qlist = [(queries[i][0], queries[i][1], i) for i in range(len(queries))]
        qlist.sort(reverse=True)
        vals = sorted(set(nums2))
        comp = {v: i for i, v in enumerate(vals)}
        st = SegTree(len(vals))
        ans = [-1] * len(queries)
        idx = 0
        for xi, yi, qi in qlist:
            while idx < n and items[idx][0] >= xi:
                _, y, s = items[idx]
                st.update(comp[y], s)
                idx += 1
            pos = bisect.bisect_left(vals, yi)
            if pos < len(vals):
                ans[qi] = st.query(pos, len(vals) - 1)
        return ans
