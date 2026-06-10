class Solution:
    def handleQuery(self, nums1, nums2, queries):
        class SegTree:
            def __init__(self, arr):
                self.n = len(arr)
                self.ones = [0] * (4 * self.n)
                self.lazy = [False] * (4 * self.n)
                self.build(1, 0, self.n - 1, arr)
            def build(self, idx, l, r, arr):
                if l == r:
                    self.ones[idx] = arr[l]
                    return
                m = (l + r) // 2
                self.build(idx * 2, l, m, arr)
                self.build(idx * 2 + 1, m + 1, r, arr)
                self.ones[idx] = self.ones[idx * 2] + self.ones[idx * 2 + 1]
            def apply(self, idx, l, r):
                self.ones[idx] = (r - l + 1) - self.ones[idx]
                self.lazy[idx] ^= True
            def push(self, idx, l, r):
                if self.lazy[idx]:
                    m = (l + r) // 2
                    self.apply(idx * 2, l, m)
                    self.apply(idx * 2 + 1, m + 1, r)
                    self.lazy[idx] = False
            def update(self, idx, l, r, ql, qr):
                if ql > r or qr < l:
                    return
                if ql <= l and r <= qr:
                    self.apply(idx, l, r)
                    return
                self.push(idx, l, r)
                m = (l + r) // 2
                self.update(idx * 2, l, m, ql, qr)
                self.update(idx * 2 + 1, m + 1, r, ql, qr)
                self.ones[idx] = self.ones[idx * 2] + self.ones[idx * 2 + 1]
            def flip_range(self, l, r):
                self.update(1, 0, self.n - 1, l, r)
            def count_ones(self):
                return self.ones[1]
        seg = SegTree(nums1)
        total_sum = sum(nums2)
        ans = []
        for q in queries:
            t = q[0]
            if t == 1:
                seg.flip_range(q[1], q[2])
            elif t == 2:
                p = q[1]
                total_sum += p * seg.count_ones()
            else:
                ans.append(total_sum)
        return ans
