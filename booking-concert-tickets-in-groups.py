class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.next_free = [0] * n
        size = 4 * n
        self.seg_max = [0] * size
        self.seg_sum = [0] * size
        self._build(1, 0, n - 1)

    def _build(self, node: int, l: int, r: int):
        if l == r:
            self.seg_max[node] = self.m
            self.seg_sum[node] = self.m
        else:
            mid = (l + r) // 2
            self._build(node * 2, l, mid)
            self._build(node * 2 + 1, mid + 1, r)
            self.seg_max[node] = max(self.seg_max[node * 2], self.seg_max[node * 2 + 1])
            self.seg_sum[node] = self.seg_sum[node * 2] + self.seg_sum[node * 2 + 1]

    def _update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.seg_max[node] = val
            self.seg_sum[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self._update(node * 2, l, mid, idx, val)
            else:
                self._update(node * 2 + 1, mid + 1, r, idx, val)
            self.seg_max[node] = max(self.seg_max[node * 2], self.seg_max[node * 2 + 1])
            self.seg_sum[node] = self.seg_sum[node * 2] + self.seg_sum[node * 2 + 1]

    def _find_first(self, node: int, l: int, r: int, ql: int, qr: int, k: int):
        if r < ql or l > qr or self.seg_max[node] < k:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        res = self._find_first(node * 2, l, mid, ql, qr, k)
        if res != -1:
            return res
        return self._find_first(node * 2 + 1, mid + 1, r, ql, qr, k)

    def gather(self, k: int, maxRow: int) -> list[int]:
        row = self._find_first(1, 0, self.n - 1, 0, maxRow, k)
        if row == -1:
            return []
        start = self.next_free[row]
        self.next_free[row] += k
        self._update(1, 0, self.n - 1, row, self.m - self.next_free[row])
        return [row, start]

    def scatter(self, k: int, maxRow: int) -> bool:
        def prefix_sum(node, l, r, ql, qr):
            if r < ql or l > qr:
                return 0
            if ql <= l and r <= qr:
                return self.seg_sum[node]
            mid = (l + r) // 2
            return prefix_sum(node * 2, l, mid, ql, qr) + prefix_sum(node * 2 + 1, mid + 1, r, ql, qr)
        total_available = prefix_sum(1, 0, self.n - 1, 0, maxRow)
        if total_available < k:
            return False
        while k > 0:
            row = self._find_first(1, 0, self.n - 1, 0, maxRow, 1)
            if row == -1:
                return False
            avail = self.m - self.next_free[row]
            take = k if k < avail else avail
            self.next_free[row] += take
            self._update(1, 0, self.n - 1, row, self.m - self.next_free[row])
            k -= take
        return True

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
