class MajorityChecker:
    def __init__(self, arr):
        self.arr = arr
        n = len(arr)
        self.tree = [(-1, 0)] * (4 * n)
        self.pos = {}
        for i, v in enumerate(arr):
            self.pos.setdefault(v, []).append(i)
        def build(idx, l, r):
            if l == r:
                self.tree[idx] = (arr[l], 1)
                return
            m = (l + r) // 2
            build(idx * 2, l, m)
            build(idx * 2 + 1, m + 1, r)
            self.tree[idx] = self._merge(self.tree[idx * 2], self.tree[idx * 2 + 1])
        build(1, 0, n - 1)
    def _merge(self, a, b):
        if a[0] == b[0]:
            return (a[0], a[1] + b[1])
        if a[1] > b[1]:
            return (a[0], a[1] - b[1])
        if b[1] > a[1]:
            return (b[0], b[1] - a[1])
        return (-1, 0)
    def _query(self, idx, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[idx]
        m = (l + r) // 2
        if qr <= m:
            return self._query(idx * 2, l, m, ql, qr)
        if ql > m:
            return self._query(idx * 2 + 1, m + 1, r, ql, qr)
        left = self._query(idx * 2, l, m, ql, qr)
        right = self._query(idx * 2 + 1, m + 1, r, ql, qr)
        return self._merge(left, right)
    def query(self, left, right, threshold):
        cand = self._query(1, 0, len(self.arr) - 1, left, right)[0]
        if cand == -1:
            return -1
        lst = self.pos.get(cand, [])
        import bisect
        cnt = bisect.bisect_right(lst, right) - bisect.bisect_left(lst, left)
        return cand if cnt >= threshold else -1
